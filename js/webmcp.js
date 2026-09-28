/*
 * WebMCP tools for ExcavationTrenchingShoring.com
 *
 * Exposes structured, read-mostly tools to AI agents running in the browser
 * via the WebMCP API (navigator.modelContext). Does nothing in browsers that
 * don't support WebMCP. Agents can look things up and open a pre-filled
 * checkout, but can never submit a payment: the person always clicks Pay.
 *
 * Docs: https://developer.chrome.com/docs/ai/webmcp
 */
(function () {
  'use strict';

  var SITE = {
    "name": "ExcavationTrenchingShoring.com",
    "topic": "excavation and trenching",
    "phone": "1-866-429-6742",
    "languages": [
      "English",
      "Spanish"
    ],
    "format": "Self-paced online, mobile-friendly; certificate of completion issued immediately on finishing",
    "tiers": [
      {
        "min": 1,
        "discount": 0
      },
      {
        "min": 2,
        "discount": 0.01
      },
      {
        "min": 11,
        "discount": 0.02
      },
      {
        "min": 21,
        "discount": 0.03
      },
      {
        "min": 51,
        "discount": 0.05
      },
      {
        "min": 101,
        "discount": 0.07
      },
      {
        "min": 251,
        "discount": 0.08
      },
      {
        "min": 501,
        "discount": 0.1
      }
    ],
    "maxSeats": 1000,
    "bulkNote": "Seat discounts apply automatically: 2-10 seats 1%, 11-20 2%, 21-50 3%, 51-100 5%, 101-250 7%, 251-500 8%, 501-1000 10%.",
    "checkoutPath": "checkout/",
    "decisionGuide": "which-excavation-course-do-i-need/",
    "courses": [
      {
        "code": "safety",
        "name": "Excavation, Trenching & Shoring Safety Training",
        "hours": 3,
        "price": 59.99,
        "audience": "Excavation and trenching crews, equipment operators, and utility/municipal staff.",
        "covers": "Recognizing cave-in, atmospheric, and utility-strike hazards; soil classification and protective system basics; safe access, egress, and spoil pile placement; when to stop work and notify the Competent Person.",
        "details": {
          "osha_standards": "29 CFR 1926 Subpart P",
          "certificate_valid_months": 36
        },
        "page": "excavation-trenching-shoring-safety-training/"
      },
      {
        "code": "competent",
        "name": "Competent Person for Excavation, Trenching & Shoring Training",
        "hours": 8,
        "price": 159.99,
        "audience": "Safety managers, foremen, and EHS coordinators responsible for inspections, soil classification, and protective system selection.",
        "covers": "The Competent Person role and authority; soil classification (Stable Rock, Type A, B, C); selecting protective systems (sloping, benching, shielding, shoring); daily inspection duties; building a written excavation safety program and emergency plan.",
        "details": {
          "osha_standards": "29 CFR 1926 Subpart P",
          "certificate_valid_months": 24
        },
        "page": "competent-person-excavation-trenching-shoring-training/"
      }
    ],
    "roles": {
      "crew_member": {
        "course": "safety",
        "description": "works in or around excavations and trenches (laborer, equipment operator, utility or municipal crew)"
      },
      "competent_person": {
        "course": "competent",
        "description": "foreman, supervisor, or safety manager responsible for daily inspections, soil classification, and choosing protective systems"
      }
    },
    "recommendNote": "Completing the Competent Person course does not by itself make someone the Competent Person: the employer must formally designate them. Employers must also provide site-specific instruction and confirm hands-on competency.",
    "searchScope": "FAQ answers, course curriculum, credential details, policies",
    "searchExample": "\"soil classification\" or \"refund policy\"",
    "verification": {
      "tool": "https://hazwoper-osha.com/certificate-verification",
      "page": "certificate-policy/",
      "need": "The certificate ID printed on the certificate and, if prompted, the student name.",
      "confirms": "Course, completion date, and training hours on record with HAZWOPER OSHA Training, LLC, which issues the certificate."
    }
  };

  var script = document.currentScript;
  var ROOT = script && script.src ? script.src.replace(/js\/webmcp\.js(\?.*)?$/, '') : (location.origin + '/');

  var COURSES = SITE.courses;
  var COURSE_CODES = COURSES.map(function (c) { return c.code; });
  var ROLE_KEYS = Object.keys(SITE.roles);
  var MAX_SEATS = SITE.maxSeats;

  function findCourse(code) {
    for (var i = 0; i < COURSES.length; i++) if (COURSES[i].code === code) return COURSES[i];
    return null;
  }

  function livePrice(course) {
    // Prefer the price from js/config.js when it's loaded on this page
    if (typeof courses !== 'undefined' && Array.isArray(courses)) {
      for (var i = 0; i < courses.length; i++) if (courses[i].code === course.code) return courses[i].price;
    }
    return course.price;
  }

  function perSeatPrice(course, seats) {
    if (SITE.priceTable) {
      // Fixed per-seat price ladder per course (mirrors js/config.js bulkPricing)
      var rows = SITE.priceTable[course.code], price = rows[0].price;
      for (var i = 0; i < rows.length; i++) if (seats >= rows[i].min) price = rows[i].price;
      return price;
    }
    var tier = SITE.tiers[0];
    for (var j = 0; j < SITE.tiers.length; j++) if (seats >= SITE.tiers[j].min) tier = SITE.tiers[j];
    return Math.round(livePrice(course) * (1 - tier.discount) * 100) / 100;
  }

  function quote(course, seats) {
    var perSeat = perSeatPrice(course, seats);
    var base = SITE.priceTable ? SITE.priceTable[course.code][0].price : livePrice(course);
    return {
      course: course.name,
      seats: seats,
      discount_percent: Math.round((1 - perSeat / base) * 1000) / 10,
      price_per_seat_usd: perSeat,
      total_usd: Math.round(perSeat * seats * 100) / 100
    };
  }

  function describe(course) {
    var out = {
      code: course.code,
      name: course.name,
      length_hours: course.hours,
      price_per_seat_usd: SITE.priceTable ? SITE.priceTable[course.code][0].price : livePrice(course),
      who_its_for: course.audience,
      covers: course.covers
    };
    for (var k in course.details) out[k] = course.details[k];
    out.languages = SITE.languages;
    out.format = SITE.format;
    out.url = ROOT + course.page;
    return out;
  }

  function text(obj) {
    return { content: [{ type: 'text', text: typeof obj === 'string' ? obj : JSON.stringify(obj, null, 2) }] };
  }

  function badSeats() {
    return text('Seats must be between 1 and ' + MAX_SEATS + '. For larger orders call ' + SITE.phone + '.');
  }

  var siteText = null;
  function loadSiteText() {
    if (siteText) return Promise.resolve(siteText);
    return fetch(ROOT + 'llms-full.txt')
      .then(function (r) { return r.ok ? r.text() : fetch(ROOT + 'llms.txt').then(function (r2) { return r2.text(); }); })
      .then(function (t) { siteText = t; return t; });
  }

  var TOOLS = [
    {
      name: 'list_courses',
      description: 'List all training courses offered on ' + SITE.name + ' with length, price per seat, audience, topics covered, and page URL.',
      inputSchema: { type: 'object', properties: {} },
      annotations: { readOnlyHint: true },
      execute: function () {
        return text({ courses: COURSES.map(describe), bulk_discounts: SITE.bulkNote });
      }
    },
    {
      name: 'recommend_course',
      description: 'Recommend the right ' + SITE.topic + ' course for a person based on what they do on the job. Use this when someone asks which course they need.',
      inputSchema: {
        type: 'object',
        properties: {
          role: {
            type: 'string',
            enum: ROLE_KEYS,
            description: ROLE_KEYS.map(function (k) { return k + ' = ' + SITE.roles[k].description; }).join('; ') + '.'
          }
        },
        required: ['role']
      },
      annotations: { readOnlyHint: true },
      execute: function (args) {
        var role = SITE.roles[args && args.role];
        if (!role) return text('Unknown role. Use one of: ' + ROLE_KEYS.join(', '));
        return text({
          recommended: describe(findCourse(role.course)),
          note: SITE.recommendNote,
          decision_guide: ROOT + SITE.decisionGuide
        });
      }
    },
    {
      name: 'get_price_quote',
      description: 'Calculate the price for a number of seats in one ' + SITE.name + ' course, including the automatic bulk seat discount.',
      inputSchema: {
        type: 'object',
        properties: {
          course: { type: 'string', enum: COURSE_CODES, description: 'Course code.' },
          seats: { type: 'integer', minimum: 1, maximum: MAX_SEATS, description: 'Number of seats (1-' + MAX_SEATS + ').' }
        },
        required: ['course', 'seats']
      },
      annotations: { readOnlyHint: true },
      execute: function (args) {
        var course = findCourse(args && args.course);
        var seats = Math.floor(Number(args && args.seats));
        if (!course) return text('Unknown course. Use one of: ' + COURSE_CODES.join(', '));
        if (!(seats >= 1 && seats <= MAX_SEATS)) return badSeats();
        return text(quote(course, seats));
      }
    },
    {
      name: 'search_site_content',
      description: 'Search ' + SITE.name + ' content (' + SITE.searchScope + ') and return the most relevant sections.',
      inputSchema: {
        type: 'object',
        properties: { query: { type: 'string', description: 'What to look for, e.g. ' + SITE.searchExample + '.' } },
        required: ['query']
      },
      annotations: { readOnlyHint: true },
      execute: function (args) {
        var terms = String((args && args.query) || '').toLowerCase().split(/\W+/).filter(function (w) { return w.length > 2; });
        return loadSiteText().then(function (t) {
          var sections = t.split(/\n(?=#{2,3} )/);
          var scored = sections.map(function (s) {
            var lower = s.toLowerCase(), score = 0;
            terms.forEach(function (w) { score += lower.split(w).length - 1; });
            return { s: s, score: score };
          }).filter(function (x) { return x.score > 0; })
            .sort(function (a, b) { return b.score - a.score; })
            .slice(0, 3)
            .map(function (x) { return x.s.slice(0, 2500); });
          return text(scored.length ? scored.join('\n\n---\n\n') : 'No matching content. Full site summary: ' + ROOT + 'llms.txt');
        }).catch(function () { return text('Site content is unavailable right now. See ' + ROOT + 'llms.txt'); });
      }
    },
    {
      name: 'get_certificate_verification_info',
      description: 'Explain how an employer can verify a ' + SITE.name + ' certificate of completion, and where to do it.',
      inputSchema: { type: 'object', properties: {} },
      annotations: { readOnlyHint: true },
      execute: function () {
        var v = SITE.verification;
        return text({
          verification_tool: v.tool,
          what_you_need: v.need,
          what_it_confirms: v.confirms,
          more_info: v.page ? ROOT + v.page : undefined
        });
      }
    },
    {
      name: 'start_checkout',
      description: 'Open the ' + SITE.name + ' checkout page with a course and seat count selected. The person must enter their own billing and card details and click Pay; this tool never submits a payment.',
      inputSchema: {
        type: 'object',
        properties: {
          course: { type: 'string', enum: COURSE_CODES, description: 'Course code.' },
          seats: { type: 'integer', minimum: 1, maximum: MAX_SEATS, description: 'Number of seats (default 1).' }
        },
        required: ['course']
      },
      execute: function (args) {
        var course = findCourse(args && args.course);
        if (!course) return text('Unknown course. Use one of: ' + COURSE_CODES.join(', '));
        var seats = Math.min(MAX_SEATS, Math.max(1, Math.floor(Number(args.seats) || 1)));
        var url = ROOT + SITE.checkoutPath + '?course=' + course.code + '&seats=' + seats + '&via=ai-agent';
        setTimeout(function () { location.href = url; }, 300);
        return text({ opening: url, order: quote(course, seats), next_step: 'Ask the person to review the order, fill in their billing details and card, and click Pay themselves.' });
      }
    }
  ];

  // Visible note on checkout when an agent opened it
  function showAgentNotice() {
    if (!/[?&]via=ai-agent\b/.test(location.search)) return;
    var form = document.getElementById('stripeCheckoutForm');
    if (!form || document.getElementById('aiAgentNotice')) return;
    var note = document.createElement('div');
    note.id = 'aiAgentNotice';
    note.setAttribute('role', 'status');
    note.style.cssText = 'margin:0 0 16px;padding:12px 16px;border-radius:12px;border:1px solid rgba(245,158,11,.45);background:rgba(245,158,11,.12);font-size:.92rem;line-height:1.45;';
    note.innerHTML = '<strong>Set up by your AI assistant.</strong> Please check the course and seat count below before paying. Only you can enter your card details and complete the purchase.';
    form.parentNode.insertBefore(note, form);
  }

  function register() {
    var mc = navigator.modelContext;
    if (!mc) return;
    try {
      if (typeof mc.registerTool === 'function') {
        TOOLS.forEach(function (t) { mc.registerTool(t); });
      } else if (typeof mc.provideContext === 'function') {
        mc.provideContext({ tools: TOOLS });
      }
    } catch (e) {
      if (window.console) console.warn('WebMCP registration failed', e);
    }
  }

  // Exposed for testing
  window.WEBMCP_TOOLS = TOOLS;

  register();
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', showAgentNotice);
  else showAgentNotice();
})();
