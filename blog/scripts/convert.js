const fs = require("fs");
const path = require("path");
const mammoth = require("mammoth");
const AdmZip = require("adm-zip");

const ROOT = path.join(__dirname, "..");
const UPLOADS_DIR = path.join(ROOT, "uploads");
const PROCESSED_DIR = path.join(UPLOADS_DIR, "processed");
const POSTS_DIR = path.join(ROOT, "posts");
const POSTS_JSON = path.join(ROOT, "posts.json");
const POST_IMAGES_DIR = path.join(ROOT, "assets", "img", "posts");
const SITE_URL = "https://excavationtrenchingshoring.com";
const BLOG_URL = SITE_URL + "/blog";
const LOGO_URL = SITE_URL + "/images/ets-logo.png";
const GA_ID = "G-4965R39GCF";
const AHREFS_KEY = "6BpOTc7DCKdhopmJKKlYcQ";

const SUPPORTED_EXTENSIONS = [".docx", ".txt", ".zip"];
const DOC_EXTENSIONS = [".docx", ".txt"];
const IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".webp", ".gif"];

// ---------------------------------------------------------------------------
// "Styled text" detection.
//
// Many AI-generated / social-style posts fake bold and headings using the
// Unicode Mathematical Alphanumeric Symbols block (e.g. "𝐎𝐩𝐞𝐧𝐀𝐈") instead of
// real formatting, use a line of box-drawing characters ("━━━━") as a section
// divider, "•" for bullets, and a "Sources" section listing a name followed
// by its URL on the next line. This parser recognises that shape (from a
// .docx OR a plain .txt) and turns it into real HTML headings/lists/links.
// ---------------------------------------------------------------------------

function isStyledChar(ch) {
  const cp = ch.codePointAt(0);
  return cp >= 0x1d400 && cp <= 0x1d7ff;
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function decodeEntities(str) {
  return String(str)
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'");
}

// Normalizes styled Unicode text back to plain characters, wrapping runs
// that were styled in <strong> so the "boldness" survives as real HTML.
function normalizeAndMarkBold(text) {
  const chars = Array.from(text);
  let html = "";
  let i = 0;
  while (i < chars.length) {
    const bold = isStyledChar(chars[i]);
    let j = i;
    while (j < chars.length && isStyledChar(chars[j]) === bold) j++;
    const run = chars.slice(i, j).join("").normalize("NFKC");
    const escaped = escapeHtml(run);
    html += bold ? "<strong>" + escaped + "</strong>" : escaped;
    i = j;
  }
  return html;
}

function plainNormalize(text) {
  return text.normalize("NFKC").trim();
}

function styledRatio(text) {
  const letters = Array.from(text).filter((c) => /[\p{L}\p{N}]/u.test(c));
  if (letters.length === 0) return 0;
  const styled = letters.filter(isStyledChar).length;
  return styled / letters.length;
}

function isMostlyStyled(text) {
  return styledRatio(text) > 0.6;
}

function isDividerLine(text) {
  const t = text.trim();
  if (/^(-{3,}|\*{3,}|_{3,})$/.test(t)) return true;
  if (t.length < 5) return false;
  return /^[─-╿—–\-=_~*]+$/.test(t);
}

function isBulletLine(text) {
  return /^[•‣◦▪●·]\s+/.test(text.trim()) || /^[*-]\s+\S/.test(text.trim());
}

function stripBullet(text) {
  return text.trim().replace(/^[•‣◦▪●·*-]\s+/, "");
}

function isUrlLine(text) {
  return /^https?:\/\/\S+$/i.test(text.trim());
}

function isSourcesHeading(text) {
  return /^(sources?|references?)$/i.test(plainNormalize(text));
}

function linkifyUrls(html) {
  return html.replace(
    /(https?:\/\/[^\s<]+)/g,
    '<a href="$1" target="_blank" rel="noopener noreferrer">$1</a>'
  );
}

// ---------------------------------------------------------------------------
// Manual formatting shortcuts.
//
// Typed directly into the source .docx/.txt, these give the writer control
// over formatting without needing real Word styling:
//   **bold**              -> <strong>
//   *italic*  or _italic_ -> <em>
//   ## Heading            -> <h2>   (### -> <h3>)
//   > quoted text         -> indented pull-quote / blockquote
//   ((small print))       -> smaller caption-style text
//   [space]  (own line)   -> extra vertical gap
//   1. item / 2. item     -> numbered list
// A line of repeated dashes/underscores/box-drawing characters (e.g. "---" or
// "━━━━━━━━━━", already how AI drafts mark section breaks) becomes a real
// horizontal-rule divider instead of being silently discarded.
// ---------------------------------------------------------------------------

function applyMarkdownEmphasis(html) {
  html = html.replace(/\*\*([^\n*]+?)\*\*/g, "<strong>$1</strong>");
  html = html.replace(/\*([^\n*]+?)\*/g, "<em>$1</em>");
  html = html.replace(/(^|[^\w])_([^\n_]+?)_(?!\w)/g, "$1<em>$2</em>");
  return html;
}

function formatInline(text) {
  return linkifyUrls(applyMarkdownEmphasis(normalizeAndMarkBold(text)));
}

function headingShortcutMatch(text) {
  const m = text.trim().match(/^(#{1,3})\s+(\S.*)$/);
  if (!m) return null;
  return { level: m[1].length >= 3 ? 3 : 2, text: m[2].trim() };
}

function isBlockquoteShortcut(text) {
  return /^>\s?\S/.test(text.trim());
}

function stripBlockquote(text) {
  return text.trim().replace(/^>\s?/, "");
}

function isSpacerShortcut(text) {
  return /^\[space\]$/i.test(text.trim());
}

function captionShortcutMatch(text) {
  const m = text.trim().match(/^\(\((.+)\)\)$/);
  return m ? m[1].trim() : null;
}

function isOrderedListLine(text) {
  return /^\d+[.)]\s+\S/.test(text.trim());
}

function stripOrderedMarker(text) {
  return text.trim().replace(/^\d+[.)]\s+/, "");
}

// ---------------------------------------------------------------------------
// Extracting an ordered list of paragraph "blocks" from either a mammoth
// HTML conversion (.docx) or plain text (.txt), so both file types can be
// run through the exact same structural parser below.
// ---------------------------------------------------------------------------

function blocksFromMammothHtml(html) {
  const matches = html.match(/<(h[1-6]|p|ul|ol|table|blockquote)[^>]*>[\s\S]*?<\/\1>/gi) || [];
  return matches.map((block) => {
    const tagMatch = block.match(/^<([a-z0-9]+)/i);
    const tag = tagMatch[1].toLowerCase();
    if (tag === "p") {
      const inner = block.replace(/^<p[^>]*>/i, "").replace(/<\/p>$/i, "");
      if (/<[a-z]/i.test(inner)) {
        // Contains real formatting (bold/italic/link/image) - leave untouched.
        return { type: "raw", html: block };
      }
      return { type: "text", text: decodeEntities(inner) };
    }
    if (tag === "h1" || tag === "h2") {
      const text = decodeEntities(block.replace(/<[^>]+>/g, ""));
      return { type: "heading", tag, text, html: block };
    }
    return { type: "raw", html: block };
  });
}

function blocksFromPlainText(text) {
  return text
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter((line) => line.length > 0)
    .map((line) => ({ type: "text", text: line }));
}

// ---------------------------------------------------------------------------
// Title + body building
// ---------------------------------------------------------------------------

function titleFromFilename(filename) {
  const base = filename.replace(/\.(docx|txt)$/i, "");
  const words = base.replace(/[_-]+/g, " ").trim();
  return words.replace(/\w\S*/g, function (w) {
    return w.charAt(0).toUpperCase() + w.slice(1).toLowerCase();
  });
}

function extractTitle(blocks, fallbackTitle) {
  if (blocks.length === 0) return { title: fallbackTitle, rest: blocks };
  const first = blocks[0];
  if (first.type === "heading") {
    return { title: plainNormalize(first.text) || fallbackTitle, rest: blocks.slice(1) };
  }
  if (first.type === "text" && first.text.trim()) {
    return { title: plainNormalize(first.text) || fallbackTitle, rest: blocks.slice(1) };
  }
  return { title: fallbackTitle, rest: blocks };
}

function buildBodyHtml(blocks) {
  const output = [];
  let bulletBuffer = [];
  let orderedBuffer = [];
  let sourcesMode = false;
  let sourcesBuffer = [];
  let pendingSourceName = null;

  function flushBullets() {
    if (bulletBuffer.length) {
      output.push(
        "<ul>" + bulletBuffer.map((t) => "<li>" + formatInline(t) + "</li>").join("") + "</ul>"
      );
      bulletBuffer = [];
    }
  }

  function flushOrdered() {
    if (orderedBuffer.length) {
      output.push(
        "<ol>" + orderedBuffer.map((t) => "<li>" + formatInline(t) + "</li>").join("") + "</ol>"
      );
      orderedBuffer = [];
    }
  }

  function flushSources() {
    if (sourcesBuffer.length) {
      output.push(
        '<ul class="sources-list">' +
          sourcesBuffer
            .map(
              (s) =>
                '<li><a href="' +
                escapeHtml(s.url) +
                '" target="_blank" rel="noopener noreferrer">' +
                escapeHtml(s.name) +
                "</a></li>"
            )
            .join("") +
          "</ul>"
      );
      sourcesBuffer = [];
    }
    if (pendingSourceName) {
      output.push("<p>" + escapeHtml(pendingSourceName) + "</p>");
      pendingSourceName = null;
    }
  }

  for (const block of blocks) {
    if (block.type === "raw" || block.type === "heading") {
      flushBullets();
      flushOrdered();
      flushSources();
      sourcesMode = false;
      output.push(block.html);
      continue;
    }

    const text = block.text.trim();
    if (!text) continue;

    if (isDividerLine(text)) {
      flushBullets();
      flushOrdered();
      output.push('<hr class="post-divider">');
      continue;
    }

    if (sourcesMode && isUrlLine(text)) {
      sourcesBuffer.push({ name: pendingSourceName || text, url: text.trim() });
      pendingSourceName = null;
      continue;
    }

    if (isSourcesHeading(text)) {
      flushBullets();
      flushOrdered();
      flushSources();
      output.push("<h2>" + escapeHtml(plainNormalize(text)) + "</h2>");
      sourcesMode = true;
      continue;
    }

    const heading = headingShortcutMatch(text);
    if (heading) {
      flushBullets();
      flushOrdered();
      flushSources();
      sourcesMode = false;
      const tag = "h" + heading.level;
      output.push("<" + tag + ">" + formatInline(heading.text) + "</" + tag + ">");
      continue;
    }

    if (isMostlyStyled(text)) {
      flushBullets();
      flushOrdered();
      flushSources();
      sourcesMode = false;
      output.push("<h2>" + escapeHtml(plainNormalize(text)) + "</h2>");
      continue;
    }

    if (sourcesMode) {
      if (pendingSourceName) {
        output.push("<p>" + escapeHtml(pendingSourceName) + "</p>");
      }
      pendingSourceName = plainNormalize(text);
      continue;
    }

    if (isSpacerShortcut(text)) {
      flushBullets();
      flushOrdered();
      output.push('<div class="post-spacer" aria-hidden="true"></div>');
      continue;
    }

    const caption = captionShortcutMatch(text);
    if (caption !== null) {
      flushBullets();
      flushOrdered();
      output.push('<p class="post-caption">' + formatInline(caption) + "</p>");
      continue;
    }

    if (isBlockquoteShortcut(text)) {
      flushBullets();
      flushOrdered();
      output.push("<blockquote><p>" + formatInline(stripBlockquote(text)) + "</p></blockquote>");
      continue;
    }

    if (isOrderedListLine(text)) {
      flushBullets();
      orderedBuffer.push(stripOrderedMarker(text));
      continue;
    }

    if (isBulletLine(text)) {
      flushOrdered();
      bulletBuffer.push(stripBullet(text));
      continue;
    }

    flushBullets();
    flushOrdered();
    output.push("<p>" + formatInline(text) + "</p>");
  }

  flushBullets();
  flushOrdered();
  flushSources();

  return output.join("\n");
}

function excerptFromHtml(html, maxLen) {
  const match = html.match(/<p[^>]*>([\s\S]*?)<\/p>/i);
  const source = match ? match[1] : html;
  const text = decodeEntities(source.replace(/<[^>]+>/g, " "))
    .replace(/\s+/g, " ")
    .trim();
  if (text.length <= maxLen) return text;
  return text.slice(0, maxLen).replace(/\s+\S*$/, "") + "…";
}

// ---------------------------------------------------------------------------
// Page template + post index
// ---------------------------------------------------------------------------

function slugify(text) {
  return (
    text
      .toLowerCase()
      .trim()
      .replace(/[^a-z0-9]+/g, "-")
      .replace(/^-+|-+$/g, "") || "post"
  );
}

function loadPosts() {
  if (!fs.existsSync(POSTS_JSON)) return [];
  const raw = fs.readFileSync(POSTS_JSON, "utf8").trim();
  if (!raw) return [];
  return JSON.parse(raw);
}

function savePosts(posts) {
  fs.writeFileSync(POSTS_JSON, JSON.stringify(posts, null, 2) + "\n");
}

// Keeps the site-root sitemap.xml (built by tools/build.py, which has no
// knowledge of the blog) in sync with posts.json - strips any previously
// written /blog/ entries and re-adds the blog index plus one entry per post.
function updateSitemap(posts) {
  const SITEMAP_PATH = path.join(ROOT, "..", "sitemap.xml");
  if (!fs.existsSync(SITEMAP_PATH)) return;

  const xml = fs.readFileSync(SITEMAP_PATH, "utf8");
  // Each <url>...</url> block is matched individually (the lazy quantifier
  // stops at the nearest </url>, so blocks can't bleed into each other),
  // then any pre-existing /blog/ blocks are dropped and replaced below.
  const urlBlocks = xml.match(/ {2}<url>\n(?:.*\n)*? {2}<\/url>\n/g) || [];
  const nonBlogBlocks = urlBlocks.filter((block) => !block.includes(BLOG_URL));

  const blogBlocks = [
    `  <url>\n    <loc>${BLOG_URL}/</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.7</priority>\n  </url>\n`,
  ];
  for (const post of posts) {
    blogBlocks.push(
      `  <url>\n    <loc>${BLOG_URL}/posts/${post.slug}.html</loc>\n    <lastmod>${post.date}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>\n`
    );
  }

  const newXml =
    '<?xml version="1.0" encoding="UTF-8"?>\n' +
    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    nonBlogBlocks.join("") +
    blogBlocks.join("") +
    "</urlset>\n";

  fs.writeFileSync(SITEMAP_PATH, newXml);
  console.log("updated sitemap.xml with " + posts.length + " blog post(s)");
}

function uniqueSlug(baseSlug, existingSlugs) {
  let slug = baseSlug;
  let n = 2;
  while (existingSlugs.has(slug)) {
    slug = baseSlug + "-" + n;
    n++;
  }
  return slug;
}

// Builds a post page using the site's shared header/footer (matching
// tools/build.py's render_header/render_footer in the main repo), one level
// below /blog/ at /blog/posts/<slug>.html - so site-root assets are "../../"
// and blog-root assets are "../".
function buildPostPage(title, dateDisplay, isoDate, bodyHtml, imagePath, excerpt, slug) {
  const escapedTitle = escapeHtml(title);
  const description = escapeHtml(excerpt ? title + " - " + excerpt : title + " - Excavation, Trenching & Shoring Safety Blog.");
  const canonicalUrl = BLOG_URL + "/posts/" + slug + ".html";
  const shareImageUrl = imagePath ? SITE_URL + "/blog/" + imagePath : LOGO_URL;

  const featuredImageHtml = imagePath
    ? `  <div class="post-featured-image">
    <img src="../${imagePath}" alt="${escapedTitle}" loading="eager">
  </div>
`
    : "";

  return `<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=${GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', '${GA_ID}');
</script>
<script src="https://analytics.ahrefs.com/analytics.js" data-key="${AHREFS_KEY}" async></script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${escapedTitle} | ExcavationTrenchingShoring.com</title>
<meta name="description" content="${description}">
<link rel="canonical" href="${canonicalUrl}">
<link rel="icon" type="image/png" href="../../images/ets-logo.png">
<link rel="apple-touch-icon" href="../../images/ets-logo.png">

<meta property="og:type" content="article">
<meta property="og:site_name" content="ExcavationTrenchingShoring.com">
<meta property="og:title" content="${escapedTitle}">
<meta property="og:description" content="${description}">
<meta property="og:image" content="${shareImageUrl}">
<meta property="og:url" content="${canonicalUrl}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="${escapedTitle}">
<meta name="twitter:description" content="${description}">
<meta name="twitter:image" content="${shareImageUrl}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../css/styles.css">
<link rel="stylesheet" href="../assets/css/blog.css">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": "Home", "item": "${SITE_URL}/" },
        { "@type": "ListItem", "position": 2, "name": "Blog", "item": "${BLOG_URL}/" },
        { "@type": "ListItem", "position": 3, "name": "${escapedTitle}", "item": "${canonicalUrl}" }
      ]
    },
    {
      "@type": "BlogPosting",
      "headline": "${escapedTitle}",
      "image": "${shareImageUrl}",
      "datePublished": "${isoDate}",
      "dateModified": "${isoDate}",
      "author": {
        "@type": "EducationalOrganization",
        "name": "Excavation Trenching Shoring Training",
        "url": "${SITE_URL}/"
      },
      "publisher": {
        "@type": "EducationalOrganization",
        "name": "Excavation Trenching Shoring Training",
        "logo": "${LOGO_URL}"
      },
      "description": "${description}"
    }
  ]
}
</script>
</head>
<body class="blog-page">

<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
  <div class="container header-inner">
    <a href="../../index.html#top" class="logo">
      <img src="../../images/ets-logo.png" alt="ExcavationTrenchingShoring.com" class="logo-icon">
      <span class="logo-text">
        <span class="logo-mark">ExcavationTrenchingShoring.com</span>
        <span class="logo-sub">Excavation Trenching &amp; Shoring Training</span>
      </span>
    </a>

    <nav class="main-nav" id="mainNav">
      <a href="../../index.html#overview">Overview</a>
      <div class="nav-dropdown">
        <a href="../../index.html#courses">Courses</a>
        <div class="nav-dropdown-panel">
          <a href="../../excavation-trenching-shoring-safety-training/">Excavation, Trenching &amp; Shoring Safety Training</a>
          <a href="../../competent-person-excavation-trenching-shoring-training/">Competent Person Training</a>
        </div>
      </div>
      <a href="../../which-excavation-course-do-i-need/">Which Course?</a>
      <div class="nav-dropdown">
        <a href="../../osha-excavation-standards/">Resources</a>
        <div class="nav-dropdown-panel">
          <a href="../../osha-excavation-standards/">OSHA Excavation Standards</a>
          <a href="../../osha-subpart-p-training-guide/">OSHA Subpart P Training Guide</a>
          <a href="../../excavation-protective-systems/">Protective Systems</a>
          <a href="../../soil-classification-training/">Soil Classification</a>
          <a href="../../underground-utility-safety/">Underground Utility Safety</a>
          <a href="../../excavation-emergency-planning/">Emergency Planning</a>
          <a href="../../state-osha-plan-requirements/">State OSHA Plan Requirements</a>
          <a href="../../credential-transparency/">Credential Transparency</a>
        </div>
      </div>
      <div class="nav-dropdown">
        <a href="../../excavation-safety-vs-competent-person-training/">Compare</a>
        <div class="nav-dropdown-panel">
          <a href="../../excavation-safety-vs-competent-person-training/">Safety vs. Competent Person</a>
          <a href="../../trenching-vs-excavation-training/">Trenching vs. Excavation</a>
          <a href="../../sloping-benching-shoring-shielding-explained/">Sloping, Benching, Shoring &amp; Shielding</a>
          <a href="../../excavation-competent-person-requirements/">Competent Person Requirements</a>
          <a href="../../excavation-training-for-utility-crews/">Training for Utility Crews</a>
          <a href="../../excavation-training-for-municipal-crews/">Training for Municipal Crews</a>
        </div>
      </div>
      <a href="../../index.html#accreditations">Accreditations</a>
      <a href="../../about/">About</a>
      <a href="../../instructors-and-training-provider/">Instructors & Provider</a>
      <a href="../../reviews/">Reviews</a>
      <a href="../../index.html#pricing">Pricing</a>
      <a href="../" class="is-active">Blog</a>
      <a href="../../frequently-asked-questions/">FAQ</a>
      <a href="tel:18664296742" class="nav-phone">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        1-866-429-6742
      </a>
      <a href="mailto:info@hazwoper-osha.com" class="nav-phone nav-email">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
        info@hazwoper-osha.com
      </a>
    </nav>

    <div class="header-actions">
      <a href="tel:18664296742" class="header-phone">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        1-866-429-6742
      </a>
      <a href="../../index.html#pricing" class="btn btn-primary btn-sm">Enroll Now</a>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>

<main id="main" class="blog-container">
  <a class="back-link" href="../">&larr; Back to Blog</a>
  <div class="post-header">
    <div class="post-date">${escapeHtml(dateDisplay)}</div>
    <h1>${escapedTitle}</h1>
  </div>
${featuredImageHtml}  <article class="post-content">
${bodyHtml}
  </article>
</main>

<footer class="site-footer">
  <div class="container footer-grid">

    <div class="footer-col footer-col-brand">
      <a href="../../index.html#top" class="logo footer-logo">
        <img src="../../images/ets-logo.png" alt="ExcavationTrenchingShoring.com" class="logo-icon logo-icon-footer">
        <span class="logo-text">
          <span class="logo-mark logo-mark-footer">ExcavationTrenchingShoring.com</span>
          <span class="logo-sub logo-sub-footer">Excavation Trenching &amp; Shoring Training</span>
        </span>
      </a>

      <p class="footer-legal"><strong>Subsidiary Partnership</strong><br>Excavation Trenching Shoring Training is a subsidiary of <a href="https://ictraining.us/" target="_blank" rel="noopener">Industrial Certified Training, LLC</a>, a company specializing in OSHA, EPA, and IACET-accredited training. We partner with <a href="https://hazwoper-osha.com/" target="_blank" rel="noopener">HAZWOPER OSHA Training, LLC</a> to offer comprehensive safety and environmental compliance courses.</p>

      <p class="footer-address">11901 Santa Monica Blvd. Suite # 414<br>Los Angeles, CA 90025</p>
      <div class="footer-badges">
        <a href="https://www.iacet.org/affiliates/accredited-providers-list/accredited-provider-overview/?providerID=131618" target="_blank" rel="noopener" aria-label="IACET Accredited Provider">
          <img src="../../images/badge-iacet.webp" alt="IACET Accredited Provider" loading="lazy" width="200" height="119">
        </a>
        <a href="https://www.bbb.org/us/ca/los-angeles/profile/online-education/hazwoper-osha-training-1216-1424720" target="_blank" rel="noopener" aria-label="BBB A+ Rating">
          <img src="../../images/badge-bbb.webp" alt="BBB A+ Rating" loading="lazy" width="200" height="119">
        </a>
      </div>
    </div>

    <div class="footer-col footer-col-links">
      <h4 class="footer-col-heading">Site</h4>
      <ul class="footer-link-list">
        <li><a href="../../about/">About</a></li>
        <li><a href="../../index.html#courses">Course Catalog</a></li>
        <li><a href="../../index.html#accreditations">Certifications &amp; Accreditations</a></li>
        <li><a href="../../credential-transparency/">Credential Transparency</a></li>
        <li><a href="../../osha-excavation-standards/">OSHA Excavation Standards</a></li>
        <li><a href="../../which-excavation-course-do-i-need/">Which Course Do I Need?</a></li>
        <li><a href="https://hazwoper-osha.com/certificate-verification" target="_blank" rel="noopener">Verify Certificate</a></li>
        <li><a href="../../excavation-protective-systems/">Protective Systems</a></li>
        <li><a href="../../soil-classification-training/">Soil Classification</a></li>
        <li><a href="../../underground-utility-safety/">Underground Utility Safety</a></li>
        <li><a href="../../excavation-emergency-planning/">Emergency Planning</a></li>
        <li><a href="../../state-osha-plan-requirements/">State OSHA Plan Requirements</a></li>
        <li><a href="../../instructors-and-training-provider/">Instructors &amp; Provider</a></li>
        <li><a href="../../reviews/">Reviews</a></li>
        <li><a href="../">Blog</a></li>
        <li><a href="../../frequently-asked-questions/">FAQ</a></li>
      </ul>
    </div>

    <div class="footer-col footer-col-contact">
      <h4 class="footer-col-heading">Contact Us</h4>
      <p class="footer-contact-lead">Get in Touch</p>
      <p class="footer-contact-sub">Have questions? We're here to help. Reach out to us anytime.</p>

      <div class="footer-contact-links">
        <a href="tel:18664296742">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          1-866-429-6742
        </a>
        <a href="mailto:info@hazwoper-osha.com">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          info@hazwoper-osha.com
        </a>
      </div>

      <div class="footer-social">
        <a href="https://www.facebook.com/HazwoperOsha/" target="_blank" rel="noopener" aria-label="Facebook">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
        </a>
        <a href="https://www.instagram.com/hazwoper_osha_training/?hl=en" target="_blank" rel="noopener" aria-label="Instagram">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></svg>
        </a>
        <a href="https://www.youtube.com/@hazwoper-osha" target="_blank" rel="noopener" aria-label="YouTube">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33zM9.75 15.02V8.48l5.75 3.27z"/></svg>
        </a>
        <a href="https://twitter.com/HazwoperOsha" target="_blank" rel="noopener" aria-label="X">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M18.9 2H22l-7.4 8.4L23 22h-6.6l-5.2-6.8L5.1 22H2l7.9-9L1.6 2h6.8l4.7 6.2z"/></svg>
        </a>
        <a href="https://www.linkedin.com/company/hazwoper-osha" target="_blank" rel="noopener" aria-label="LinkedIn">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2zM8.34 18.34V10.1H5.67v8.24zM7.01 8.97a1.55 1.55 0 1 0 0-3.1 1.55 1.55 0 0 0 0 3.1zM18.34 18.34v-4.6c0-2.46-1.31-3.6-3.06-3.6a2.64 2.64 0 0 0-2.39 1.32V10.1H10.2s.04.86 0 8.24h2.68v-4.6c0-.25.02-.5.09-.68a1.5 1.5 0 0 1 1.37-1c.96 0 1.35.73 1.35 1.8v4.48z"/></svg>
        </a>
        <a href="https://www.pinterest.com/hazwoperosha/" target="_blank" rel="noopener" aria-label="Pinterest">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12c0 4.24 2.64 7.86 6.36 9.32-.09-.79-.17-2.01.03-2.88.19-.79 1.22-5.03 1.22-5.03s-.31-.63-.31-1.55c0-1.45.84-2.54 1.89-2.54.89 0 1.32.67 1.32 1.47 0 .89-.57 2.23-.86 3.47-.25 1.03.52 1.88 1.53 1.88 1.84 0 3.07-2.36 3.07-5.15 0-2.12-1.43-3.71-4.02-3.71-2.93 0-4.76 2.19-4.76 4.63 0 .84.25 1.44.63 1.9.18.21.2.3.14.54-.05.18-.16.63-.21.81-.07.26-.28.35-.51.26-1.44-.59-2.11-2.16-2.11-3.93 0-2.92 2.46-6.43 7.34-6.43 3.92 0 6.5 2.84 6.5 5.89 0 4.03-2.24 7.04-5.55 7.04-1.11 0-2.16-.6-2.51-1.28 0 0-.6 2.36-.73 2.82-.22.8-.66 1.6-1.06 2.22.95.29 1.95.45 3 .45 5.52 0 10-4.48 10-10S17.52 2 12 2z"/></svg>
        </a>
      </div>
    </div>

  </div>
  <div class="container footer-grid footer-grid-legal">
    <div class="footer-col">
      <h4 class="footer-col-heading">Policies</h4>
      <ul class="footer-link-list footer-link-list-inline">
        <li><a href="../../privacy-policy/">Privacy Policy</a></li>
        <li><a href="../../refund-policy/">Refund Policy</a></li>
        <li><a href="../../certificate-policy/">Certificate Policy</a></li>
        <li><a href="../../group-training-policy/">Group Training Policy</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container">
      <p>&copy; 2026, Industrial Certified Training, LLC, All Rights Reserved</p>
    </div>
  </div>
</footer>

<script src="../../js/config.js"></script>
<script src="../../js/main.js"></script>

<!--Start of Tawk.to Script-->
<script type="text/javascript">
var Tawk_API=Tawk_API||{}, Tawk_LoadStart=new Date();
Tawk_API.autoStart = false;

setTimeout(function(){
  Tawk_LoadStart = new Date();
  (function(){
    var s1=document.createElement("script"),s0=document.getElementsByTagName("script")[0];
    s1.async=true;
    s1.src='https://embed.tawk.to/6a5a95a2096ab21d402a762c/1jtoth11r';
    s1.charset='UTF-8';
    s1.setAttribute('crossorigin','*');
    s0.parentNode.insertBefore(s1,s0);
  })();

  var attempts = 0;
  var poll = setInterval(function(){
    attempts++;
    if (typeof Tawk_API.showWidget === 'function') {
      Tawk_API.showWidget();
      clearInterval(poll);
    } else if (attempts >= 40) {
      clearInterval(poll);
    }
  }, 250);
}, 2500);
</script>
<!--End of Tawk.to Script-->
</body>
</html>
`;
}

// ---------------------------------------------------------------------------
// Per-file conversion
// ---------------------------------------------------------------------------

// A zip upload may contain OS cruft alongside the real document/image
// (e.g. "__MACOSX/" entries or ".DS_Store" from a Mac zip) - ignore those.
function isJunkEntry(entryName) {
  const base = path.basename(entryName);
  return entryName.startsWith("__MACOSX/") || base === ".DS_Store" || base.startsWith("._");
}

function convertZip(filePath) {
  const zip = new AdmZip(filePath);
  const entries = zip.getEntries().filter((e) => !e.isDirectory && !isJunkEntry(e.entryName));

  const docEntry = entries.find((e) =>
    DOC_EXTENSIONS.includes(path.extname(e.entryName).toLowerCase())
  );
  const imageEntry = entries.find((e) =>
    IMAGE_EXTENSIONS.includes(path.extname(e.entryName).toLowerCase())
  );

  if (!docEntry) {
    return Promise.reject(
      new Error("Zip file does not contain a .docx or .txt document: " + filePath)
    );
  }

  const docExt = path.extname(docEntry.entryName).toLowerCase();
  const docBuffer = docEntry.getData();

  const blocksPromise =
    docExt === ".docx"
      ? mammoth.convertToHtml({ buffer: docBuffer }).then((result) => {
          if (result.messages && result.messages.length) {
            result.messages.forEach((m) => console.log("  [mammoth] " + m.type + ": " + m.message));
          }
          return blocksFromMammothHtml(result.value);
        })
      : Promise.resolve(blocksFromPlainText(docBuffer.toString("utf8")));

  return blocksPromise.then((blocks) => {
    const image = imageEntry
      ? { buffer: imageEntry.getData(), ext: path.extname(imageEntry.entryName).toLowerCase() }
      : null;
    return { blocks, image };
  });
}

function convertFile(filePath, filename) {
  const ext = path.extname(filename).toLowerCase();

  if (ext === ".zip") {
    return convertZip(filePath);
  }

  if (ext === ".docx") {
    return mammoth.convertToHtml({ path: filePath }).then((result) => {
      if (result.messages && result.messages.length) {
        result.messages.forEach((m) => console.log("  [mammoth] " + m.type + ": " + m.message));
      }
      const blocks = blocksFromMammothHtml(result.value);
      return { blocks, image: null };
    });
  }

  if (ext === ".txt") {
    const text = fs.readFileSync(filePath, "utf8");
    return Promise.resolve({ blocks: blocksFromPlainText(text), image: null });
  }

  return Promise.reject(new Error("Unsupported file type: " + ext));
}

function main() {
  if (!fs.existsSync(UPLOADS_DIR)) {
    console.log("No uploads directory found, nothing to do.");
    return;
  }
  fs.mkdirSync(PROCESSED_DIR, { recursive: true });
  fs.mkdirSync(POSTS_DIR, { recursive: true });

  const files = fs
    .readdirSync(UPLOADS_DIR)
    .filter((f) => SUPPORTED_EXTENSIONS.includes(path.extname(f).toLowerCase()));

  if (files.length === 0) {
    console.log("No new documents to convert.");
    return;
  }

  const posts = loadPosts();
  const existingSlugs = new Set(posts.map((p) => p.slug));

  const today = new Date();
  const isoDate = [today.getFullYear(), String(today.getMonth() + 1).padStart(2, "0"), String(today.getDate()).padStart(2, "0")].join("-");
  const dateDisplay = today.toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });

  files
    .reduce((chain, filename) => {
      return chain.then(() => {
        const filePath = path.join(UPLOADS_DIR, filename);
        console.log("Converting " + filename + " ...");
        return convertFile(filePath, filename).then(({ blocks, image }) => {
          const { title, rest } = extractTitle(blocks, titleFromFilename(filename));
          const bodyHtml = buildBodyHtml(rest);

          const baseSlug = slugify(title);
          const slug = uniqueSlug(baseSlug, existingSlugs);
          existingSlugs.add(slug);

          let imagePath = null;
          if (image) {
            fs.mkdirSync(POST_IMAGES_DIR, { recursive: true });
            const imgExt = image.ext === ".jpeg" ? ".jpg" : image.ext;
            imagePath = "assets/img/posts/" + slug + imgExt;
            fs.writeFileSync(path.join(ROOT, imagePath), image.buffer);
          }

          const excerpt = excerptFromHtml(bodyHtml, 160);
          const pageHtml = buildPostPage(title, dateDisplay, isoDate, bodyHtml, imagePath, excerpt, slug);
          fs.writeFileSync(path.join(POSTS_DIR, slug + ".html"), pageHtml);

          posts.push({
            title: title,
            slug: slug,
            image: imagePath,
            date: isoDate,
            dateDisplay: dateDisplay,
            excerpt: excerpt,
          });

          fs.renameSync(filePath, path.join(PROCESSED_DIR, filename));
          console.log("  -> posts/" + slug + ".html");
        });
      });
    }, Promise.resolve())
    .then(() => {
      savePosts(posts);
      updateSitemap(posts);
      console.log("Done. " + files.length + " post(s) published.");
    })
    .catch((err) => {
      console.error(err);
      process.exit(1);
    });
}

if (require.main === module) {
  main();
}

module.exports = { buildPostPage };
