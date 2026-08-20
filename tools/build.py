#!/usr/bin/env python3
"""
Local static-site assembler for excavationtrenchingshoring.com.

Not part of the deployed site. Run `python3 tools/build.py` from the repo
root any time a page in PAGES changes, and it writes plain static HTML files
into place (e.g. PAGES entry slug="about" -> about/index.html). Hosting stays
100% static -- this script just keeps the header/nav/footer markup from being
hand-duplicated across ~25 pages.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GA_TAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-4965R39GCF"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-4965R39GCF');
</script>"""

TAWK_SCRIPT = """<!--Start of Tawk.to Script-->
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

  // Tawk_API.onLoad isn't reliably invoked by this widget build, so poll
  // for Tawk_API.showWidget to become available instead, then reveal just
  // the launcher bubble (never auto-opens the chat window).
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
<!--End of Tawk.to Script-->"""


def org_schema():
    return """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "EducationalOrganization",
  "name": "Excavation Trenching Shoring Training",
  "alternateName": "ExcavationTrenchingShoring.com",
  "legalName": "Industrial Certified Training, LLC",
  "url": "https://excavationtrenchingshoring.com/",
  "logo": "https://excavationtrenchingshoring.com/images/ets-logo.png",
  "image": "https://excavationtrenchingshoring.com/images/ets-logo.png",
  "email": "info@hazwoper-osha.com",
  "telephone": "+1-866-429-6742",
  "sameAs": [
    "https://www.facebook.com/HazwoperOsha/",
    "https://www.instagram.com/hazwoper_osha_training/?hl=en",
    "https://twitter.com/HazwoperOsha",
    "https://www.linkedin.com/company/hazwoper-osha",
    "https://www.pinterest.com/hazwoperosha/",
    "https://www.youtube.com/@hazwoper-osha"
  ],
  "parentOrganization": {
    "@type": "Organization",
    "name": "Industrial Certified Training, LLC",
    "url": "https://ictraining.us/"
  }
}
</script>"""


def breadcrumb_schema(name, path):
    """path like '/about/' -> Home > name breadcrumb schema."""
    items = [
        '{"@type":"ListItem","position":1,"name":"Home","item":"https://excavationtrenchingshoring.com/"}'
    ]
    if path:
        items.append(
            '{"@type":"ListItem","position":2,"name":"%s","item":"https://excavationtrenchingshoring.com%s"}'
            % (name, path)
        )
    return (
        '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[%s]}\n</script>'
        % ",".join(items)
    )


def render_head(*, prefix, title, description, canonical_path, extra_schema="", og_title=None, og_description=None):
    og_title = og_title or title
    og_description = og_description or description
    icon = f'{prefix}images/ets-logo.png'
    css = f'{prefix}css/styles.css'
    canonical = f"https://excavationtrenchingshoring.com{canonical_path}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
{GA_TAG}
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<link rel="icon" type="image/png" href="{icon}">
<link rel="apple-touch-icon" href="{icon}">

<meta property="og:type" content="website">
<meta property="og:site_name" content="ExcavationTrenchingShoring.com">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{og_description}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{og_description}">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}">
{org_schema()}
{extra_schema}
</head>"""


def render_header(*, prefix, active=None):
    home = f"{prefix}index.html" if prefix else "#top"
    def a(href, label, key=None):
        cls = ' class="is-active"' if key and key == active else ""
        return f'<a href="{href}"{cls}>{label}</a>'
    return f"""<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
  <div class="container header-inner">
    <a href="{prefix}index.html#top" class="logo">
      <img src="{prefix}images/ets-logo.png" alt="ExcavationTrenchingShoring.com" class="logo-icon">
      <span class="logo-text">
        <span class="logo-mark">ExcavationTrenchingShoring.com</span>
        <span class="logo-sub">Excavation Trenching &amp; Shoring Training</span>
      </span>
    </a>

    <nav class="main-nav" id="mainNav">
      {a(prefix + 'index.html#overview', 'Overview', 'overview')}
      <div class="nav-dropdown">
        {a(prefix + 'index.html#courses', 'Courses', 'courses')}
        <div class="nav-dropdown-panel">
          <a href="{prefix}excavation-trenching-shoring-safety-training/">Excavation, Trenching &amp; Shoring Safety Training</a>
          <a href="{prefix}competent-person-excavation-trenching-shoring-training/">Competent Person Training</a>
        </div>
      </div>
      {a(prefix + 'which-excavation-course-do-i-need/', 'Which Course?', 'which-course')}
      <div class="nav-dropdown">
        <a href="{prefix}osha-excavation-standards/">Resources</a>
        <div class="nav-dropdown-panel">
          <a href="{prefix}osha-excavation-standards/">OSHA Excavation Standards</a>
          <a href="{prefix}osha-subpart-p-training-guide/">OSHA Subpart P Training Guide</a>
          <a href="{prefix}excavation-protective-systems/">Protective Systems</a>
          <a href="{prefix}soil-classification-training/">Soil Classification</a>
          <a href="{prefix}underground-utility-safety/">Underground Utility Safety</a>
          <a href="{prefix}excavation-emergency-planning/">Emergency Planning</a>
          <a href="{prefix}state-osha-plan-requirements/">State OSHA Plan Requirements</a>
          <a href="{prefix}credential-transparency/">Credential Transparency</a>
        </div>
      </div>
      <div class="nav-dropdown">
        <a href="{prefix}excavation-safety-vs-competent-person-training/">Compare</a>
        <div class="nav-dropdown-panel">
          <a href="{prefix}excavation-safety-vs-competent-person-training/">Safety vs. Competent Person</a>
          <a href="{prefix}trenching-vs-excavation-training/">Trenching vs. Excavation</a>
          <a href="{prefix}sloping-benching-shoring-shielding-explained/">Sloping, Benching, Shoring &amp; Shielding</a>
          <a href="{prefix}excavation-competent-person-requirements/">Competent Person Requirements</a>
          <a href="{prefix}excavation-training-for-utility-crews/">Training for Utility Crews</a>
          <a href="{prefix}excavation-training-for-municipal-crews/">Training for Municipal Crews</a>
        </div>
      </div>
      {a(prefix + 'index.html#accreditations', 'Accreditations', 'accreditations')}
      {a(prefix + 'about/', 'About')}
      {a(prefix + 'instructors-and-training-provider/', 'Instructors & Provider')}
      {a(prefix + 'reviews/', 'Reviews')}
      {a(prefix + 'index.html#pricing', 'Pricing', 'pricing')}
      {a(prefix + 'frequently-asked-questions/', 'FAQ', 'faq')}
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
      <a href="{prefix}index.html#pricing" class="btn btn-primary btn-sm">Enroll Now</a>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>"""


def render_footer(*, prefix):
    p = prefix
    return f"""<footer class="site-footer">
  <div class="container footer-grid">

    <div class="footer-col footer-col-brand">
      <a href="{p}index.html#top" class="logo footer-logo">
        <img src="{p}images/ets-logo.png" alt="ExcavationTrenchingShoring.com" class="logo-icon logo-icon-footer">
        <span class="logo-text">
          <span class="logo-mark logo-mark-footer">ExcavationTrenchingShoring.com</span>
          <span class="logo-sub logo-sub-footer">Excavation Trenching &amp; Shoring Training</span>
        </span>
      </a>

      <p class="footer-legal"><strong>Subsidiary Partnership</strong><br>Excavation Trenching Shoring Training is a subsidiary of <a href="https://ictraining.us/" target="_blank" rel="noopener">Industrial Certified Training, LLC</a>, a company specializing in OSHA, EPA, and IACET-accredited training. We partner with <a href="https://hazwoper-osha.com/" target="_blank" rel="noopener">HAZWOPER OSHA Training, LLC</a> to offer comprehensive safety and environmental compliance courses.</p>

      <p class="footer-address">11901 Santa Monica Blvd. Suite # 414<br>Los Angeles, CA 90025</p>
      <div class="footer-badges">
        <a href="https://www.iacet.org/affiliates/accredited-providers-list/accredited-provider-overview/?providerID=131618" target="_blank" rel="noopener" aria-label="IACET Accredited Provider">
          <img src="https://media.hazwoper-osha.com/wp-content/uploads/2023/11/1698821020/IACET-small.webp" alt="IACET Accredited Provider" loading="lazy">
        </a>
        <a href="https://www.bbb.org/us/ca/los-angeles/profile/online-education/hazwoper-osha-training-1216-1424720" target="_blank" rel="noopener" aria-label="BBB A+ Rating">
          <img src="https://media.hazwoper-osha.com/wp-content/uploads/2026/07/1784291935/bbb.webp" alt="BBB A+ Rating" loading="lazy">
        </a>
        <a href="https://www.fmcsa.dot.gov/" target="_blank" rel="noopener" aria-label="FMCSA Approved Provider">
          <img src="https://media.hazwoper-osha.com/wp-content/uploads/2024/06/1718276545/fmcsa.webp" alt="FMCSA Approved Provider" loading="lazy">
        </a>
      </div>
    </div>

    <div class="footer-col footer-col-links">
      <h4 class="footer-col-heading">Site</h4>
      <ul class="footer-link-list">
        <li><a href="{p}about/">About</a></li>
        <li><a href="{p}index.html#courses">Course Catalog</a></li>
        <li><a href="{p}index.html#accreditations">Certifications &amp; Accreditations</a></li>
        <li><a href="{p}credential-transparency/">Credential Transparency</a></li>
        <li><a href="{p}osha-excavation-standards/">OSHA Excavation Standards</a></li>
        <li><a href="{p}which-excavation-course-do-i-need/">Which Course Do I Need?</a></li>
        <li><a href="https://hazwoper-osha.com/certificate-verification" target="_blank" rel="noopener">Verify Certificate</a></li>
        <li><a href="{p}excavation-protective-systems/">Protective Systems</a></li>
        <li><a href="{p}soil-classification-training/">Soil Classification</a></li>
        <li><a href="{p}underground-utility-safety/">Underground Utility Safety</a></li>
        <li><a href="{p}excavation-emergency-planning/">Emergency Planning</a></li>
        <li><a href="{p}state-osha-plan-requirements/">State OSHA Plan Requirements</a></li>
        <li><a href="{p}instructors-and-training-provider/">Instructors &amp; Provider</a></li>
        <li><a href="{p}reviews/">Reviews</a></li>
        <li><a href="{p}frequently-asked-questions/">FAQ</a></li>
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
        <li><a href="{p}privacy-policy/">Privacy Policy</a></li>
        <li><a href="{p}refund-policy/">Refund Policy</a></li>
        <li><a href="{p}certificate-policy/">Certificate Policy</a></li>
        <li><a href="{p}group-training-policy/">Group Training Policy</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <div class="container">
      <p>&copy; 2026, Industrial Certified Training, LLC, All Rights Reserved</p>
    </div>
  </div>
</footer>

<script src="{p}js/main.js"></script>

{TAWK_SCRIPT}"""


def render_page(*, slug, title, description, body, extra_schema="", og_title=None, og_description=None, active=None, is_home=False):
    prefix = "" if is_home else "../"
    canonical_path = "/" if is_home else f"/{slug}/"
    head = render_head(
        prefix=prefix,
        title=title,
        description=description,
        canonical_path=canonical_path,
        extra_schema=extra_schema,
        og_title=og_title,
        og_description=og_description,
    )
    header = render_header(prefix=prefix, active=active)
    footer = render_footer(prefix=prefix)
    return f"""{head}
<body>

{header}

<main id="main">
{body}
</main>

{footer}
</body>
</html>
"""


def write_page(slug, html, is_home=False):
    if is_home:
        out_path = os.path.join(ROOT, "index.html")
    else:
        out_dir = os.path.join(ROOT, slug)
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", os.path.relpath(out_path, ROOT))


def write_sitemap(pages):
    urls = []
    for page in pages:
        path = "/" if page.get("is_home") else f"/{page['slug']}/"
        priority = "1.0" if page.get("is_home") else ("0.8" if page.get("active") else "0.6")
        urls.append(
            f"  <url>\n    <loc>https://excavationtrenchingshoring.com{path}</loc>\n    <changefreq>monthly</changefreq>\n    <priority>{priority}</priority>\n  </url>"
        )
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    out_path = os.path.join(ROOT, "sitemap.xml")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(xml)
    print("wrote sitemap.xml")


def write_robots():
    content = (
        "User-agent: *\n"
        "Allow: /\n\n"
        "Sitemap: https://excavationtrenchingshoring.com/sitemap.xml\n"
    )
    out_path = os.path.join(ROOT, "robots.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote robots.txt")


if __name__ == "__main__":
    from pages import PAGES  # noqa

    for page in PAGES:
        is_home = page.get("is_home", False)
        html = render_page(
            slug=page["slug"],
            title=page["title"],
            description=page["description"],
            body=page["body"],
            extra_schema=page.get("extra_schema", ""),
            og_title=page.get("og_title"),
            og_description=page.get("og_description"),
            active=page.get("active"),
            is_home=is_home,
        )
        write_page(page["slug"], html, is_home=is_home)

    write_sitemap(PAGES)
    write_robots()
    print(f"\nBuilt {len(PAGES)} pages.")
