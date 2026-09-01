# Page content for build.py. Each entry in PAGES becomes one static HTML file.
# Run `python3 tools/build.py` from the repo root to regenerate.

PAGES = []


def breadcrumb_schema(name, path):
    item = (
        '{"@type":"ListItem","position":2,"name":"%s","item":"https://excavationtrenchingshoring.com%s"}'
        % (name, path)
    )
    home = '{"@type":"ListItem","position":1,"name":"Home","item":"https://excavationtrenchingshoring.com/"}'
    return (
        '<script type="application/ld+json">\n{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[%s,%s]}\n</script>'
        % (home, item)
    )


def hero_solo(eyebrow, title, lead, cta_href="../index.html#pricing", cta_label="Enroll Now"):
    return f"""
  <section class="hero hero-solo" id="top">
    <div class="container hero-inner">
      <div class="hero-copy">
        <p class="eyebrow">{eyebrow}</p>
        <h1>{title}</h1>
        <p class="hero-lead">{lead}</p>
        <div class="hero-cta-row">
          <a href="{cta_href}" class="btn btn-primary btn-lg">{cta_label}</a>
          <a href="../index.html#top" class="btn btn-outline-light btn-lg">Back to Home</a>
        </div>
      </div>
    </div>
  </section>"""


def course_picker_widget(full=False, prefix="../"):
    pricing_href = f"{prefix}index.html#pricing" if prefix else "#pricing"
    extra_row = ""
    if full:
        extra_row = """
        <button type="button" class="course-picker-option" data-answer="inspect">I perform daily inspections</button>
        <button type="button" class="course-picker-option" data-answer="soil">I classify soil on site</button>
        <button type="button" class="course-picker-option" data-answer="systems">I select/evaluate protective systems</button>"""
    return f"""
      <div class="course-picker">
        <p class="course-picker-prompt">What best describes your role on an excavation site?</p>
        <div class="course-picker-options">
          <button type="button" class="course-picker-option active" data-answer="safety">I work in or near trenches/excavations</button>
          <button type="button" class="course-picker-option" data-answer="competent">I supervise excavation work</button>
          <button type="button" class="course-picker-option" data-answer="both">My company needs both crew &amp; supervisor coverage</button>{extra_row}
        </div>

        <div class="course-picker-result" data-result="safety">
          <h3>Recommended: Excavation, Trenching &amp; Shoring Safety Training</h3>
          <p>You work in, near, or around excavations and trenches. This 3-hour course covers hazard recognition, soil and protective system basics, and safe access/egress - the awareness you need to work safely and know when to notify the Competent Person.</p>
          <a href="{prefix}excavation-trenching-shoring-safety-training/" class="btn btn-primary">Course Details</a>
          <a href="{pricing_href}" class="btn btn-outline-light">Enroll - $59.99</a>
        </div>
        <div class="course-picker-result" data-result="competent" hidden>
          <h3>Recommended: Competent Person for Excavation, Trenching &amp; Shoring Training</h3>
          <p>You inspect, classify soil, select protective systems, or supervise excavation work. This 8-hour course covers everything OSHA expects a Competent Person to know - but remember, your employer must formally designate you before you hold that authority on site.</p>
          <a href="{prefix}competent-person-excavation-trenching-shoring-training/" class="btn btn-primary">Course Details</a>
          <a href="{pricing_href}" class="btn btn-outline-light">Enroll - $159.99</a>
        </div>
        <div class="course-picker-result" data-result="both" hidden>
          <h3>Recommended: Both Courses, by Role</h3>
          <p>Enroll your crew, operators, and utility/municipal staff in <strong>Excavation, Trenching &amp; Shoring Safety Training</strong>, and enroll your designated Competent Person(s) - foremen, safety managers, EHS coordinators - in <strong>Competent Person Training</strong>. Most excavation programs need both.</p>
          <a href="{pricing_href}" class="btn btn-primary">See Both Courses &amp; Pricing</a>
        </div>
        <div class="course-picker-result" data-result="inspect" hidden>
          <h3>Recommended: Competent Person for Excavation, Trenching &amp; Shoring Training</h3>
          <p>Daily inspection duties fall to the Competent Person role. This 8-hour course covers required inspection timing, documentation, and how to respond when conditions change.</p>
          <a href="{prefix}competent-person-excavation-trenching-shoring-training/" class="btn btn-primary">Course Details</a>
          <a href="{pricing_href}" class="btn btn-outline-light">Enroll - $159.99</a>
        </div>
        <div class="course-picker-result" data-result="soil" hidden>
          <h3>Recommended: Competent Person for Excavation, Trenching &amp; Shoring Training</h3>
          <p>Soil classification is a Competent Person responsibility under OSHA Appendix A. This course covers visual and manual test methods for Stable Rock, Type A, Type B, and Type C soils. See also our <a href="{prefix}soil-classification-training/">Soil Classification page</a>.</p>
          <a href="{prefix}competent-person-excavation-trenching-shoring-training/" class="btn btn-primary">Course Details</a>
          <a href="{pricing_href}" class="btn btn-outline-light">Enroll - $159.99</a>
        </div>
        <div class="course-picker-result" data-result="systems" hidden>
          <h3>Recommended: Competent Person for Excavation, Trenching &amp; Shoring Training</h3>
          <p>Selecting and evaluating sloping, benching, shielding, and shoring systems is a Competent Person duty. See also our <a href="{prefix}excavation-protective-systems/">Protective Systems page</a> for how tabulated data and engineering requirements fit in.</p>
          <a href="{prefix}competent-person-excavation-trenching-shoring-training/" class="btn btn-primary">Course Details</a>
          <a href="{pricing_href}" class="btn btn-outline-light">Enroll - $159.99</a>
        </div>
      </div>"""


def breadcrumb_nav(name):
    # Visible breadcrumb path removed per request; BreadcrumbList schema
    # (breadcrumb_schema, used separately) still carries this for SEO.
    return ""

# ---------------------------------------------------------------------------
# HOMEPAGE
# ---------------------------------------------------------------------------

HOME_BODY = """
  <!-- HERO -->
  <section class="hero" id="top">
    <div class="container hero-inner">
      <div class="hero-copy">
        <p class="eyebrow">Excavation Compliance &middot; Online Training</p>
        <h1>OSHA Excavation, Trenching <span class="hero-h1-plain">&amp; Shoring Training</span></h1>
        <p class="hero-lead">
          Two online courses covering every role on an excavation job site: <strong>Excavation, Trenching &amp;
          Shoring Safety Training</strong> for the crew working in and around trenches, and <strong>Competent
          Person</strong> training for the individual responsible for daily inspections, protective systems, and
          program oversight. Aligned with 29 CFR 1926 Subpart P.
        </p>
        <div class="hero-cta-row">
          <a href="#courses" class="btn btn-primary btn-lg">See Both Courses</a>
          <a href="#pricing" class="btn btn-outline-light btn-lg">Enroll Now</a>
        </div>
        <ul class="hero-meta">
          <li><strong>2 Courses</strong> one compliance path</li>
          <li><strong>EN / ES</strong> course content</li>
          <li><strong>Instant</strong> certificate</li>
          <li><strong>OSHA</strong> aligned</li>
        </ul>
      </div>

      <div class="hero-card" aria-hidden="false">
        <div class="hero-card-badge">2 Courses, 1 Compliance Path</div>
        <h3>Course Snapshot</h3>
        <ul class="hero-card-courses">
          <li>
            <a class="hero-card-course" href="excavation-trenching-shoring-safety-training/">
              <span>
                <span class="hero-card-course-name">Excavation, Trenching &amp; Shoring Safety</span>
                <span class="hero-card-course-meta">3 hrs &middot; Crew-level hazard awareness &amp; safe work practices</span>
              </span>
              <span class="hero-card-course-price">$59.99</span>
            </a>
          </li>
          <li>
            <a class="hero-card-course" href="competent-person-excavation-trenching-shoring-training/">
              <span>
                <span class="hero-card-course-name">Competent Person</span>
                <span class="hero-card-course-meta">8 hrs &middot; Daily inspections, protective systems &amp; program oversight</span>
              </span>
              <span class="hero-card-course-price">$159.99</span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </section>

  <!-- TRUST STRIP -->
  <section class="trust-strip">
    <div class="container trust-strip-inner">
      <span>Aligned with:</span>
      <div class="trust-badges">
        <span class="badge">OSHA 29 CFR 1926 Subpart P (Excavations)</span>
        <span class="badge">Competent Person Program Requirements</span>
        <span class="badge">SCORM &amp; Virtual Instructor-Led Available</span>
      </div>
    </div>
  </section>

  <!-- CERTIFICATIONS & ACCREDITATIONS -->
  <section class="section accred-section" id="accreditations">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Certifications &amp; Accreditations</p>
        <h2>Who Stands Behind This Training</h2>
        <p class="section-sub">
          Excavation, trenching, and shoring training on this site is provided through
          <strong>HAZWOPER OSHA Training, LLC</strong>. For current training-provider credentials, accreditations,
          continuing-education details, and compliance-related approvals, review HAZWOPER OSHA Training's official
          accreditation profiles below.
        </p>
      </div>

      <div class="accred-grid">
        <a class="accred-card" href="https://www.iacet.org/affiliates/accredited-providers-list/accredited-provider-overview/?providerID=131618" target="_blank" rel="noopener">
          <span class="accred-card-name">IACET Accredited Provider</span>
          <span class="accred-card-detail">Provider ID 131618 &middot; International Association for Continuing Education and Training</span>
          <span class="accred-card-link">View provider profile &rarr;</span>
        </a>
        <a class="accred-card" href="https://www.bbb.org/us/ca/los-angeles/profile/online-education/hazwoper-osha-training-1216-1424720" target="_blank" rel="noopener">
          <span class="accred-card-name">BBB Accredited &middot; A+ Rating</span>
          <span class="accred-card-detail">Better Business Bureau profile for HAZWOPER OSHA Training, LLC</span>
          <span class="accred-card-link">View BBB profile &rarr;</span>
        </a>
        <a class="accred-card" href="https://www.fmcsa.dot.gov/" target="_blank" rel="noopener">
          <span class="accred-card-name">FMCSA Approved Provider</span>
          <span class="accred-card-detail">Federal Motor Carrier Safety Administration</span>
          <span class="accred-card-link">Visit FMCSA.gov &rarr;</span>
        </a>
      </div>

      <div class="accred-cta">
        <a href="https://hazwoper-osha.com/about" target="_blank" rel="noopener" class="btn btn-outline">View Certifications &amp; Accreditations</a>
        <a href="credential-transparency/" class="btn btn-outline">Read Our Credential Transparency Page</a>
      </div>
    </div>
  </section>

  <!-- OVERVIEW -->
  <section class="section" id="overview">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Overview</p>
        <h2>Why Excavation &amp; Trenching Training Matters</h2>
        <p class="section-sub">
          Cave-ins remain one of the deadliest hazards in construction, and unlike most incidents they can happen in
          seconds with almost no warning. A single cubic yard of soil can weigh over a ton, and workers rarely survive
          a full collapse. Proper training for both the crew and the site's Competent Person is what keeps a trench
          job from becoming a fatality statistic.
        </p>
      </div>

      <div class="grid-3 feature-grid">
        <div class="feature-card">
          <div class="feature-icon">&#9935;&#65039;</div>
          <h3>Every Role, Covered Separately</h3>
          <p>A crew-level safety course and a dedicated Competent Person track, so each role gets the depth it actually needs.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">&#128737;&#65039;</div>
          <h3>Reduce Cave-Ins &amp; Violations</h3>
          <p>Understand soil classification, protective systems, and daily inspection duties so your crew and your paperwork hold up if OSHA ever shows up.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">&#128241;</div>
          <h3>Train on Any Schedule</h3>
          <p>Self-paced, mobile-friendly lessons your staff can complete between shifts, on any device.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">&#128483;&#65039;</div>
          <h3>English &amp; Spanish</h3>
          <p>Course content is available in both languages, suited to mixed-language crews and project teams.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">&#128196;</div>
          <h3>Instant Certification</h3>
          <p>A certificate of completion is issued immediately after each course, ready for your compliance files.</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">&#128679;</div>
          <h3>Built for Real Jobsites</h3>
          <p>Scenarios drawn from utility trenches, pipeline work, and foundation excavations, not generic classroom theory.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- COURSES -->
  <section class="section section-alt" id="courses">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Courses</p>
        <h2>Choose the Right Course for Your Role</h2>
        <p class="section-sub">Both courses are self-paced and aligned with OSHA's excavation standard. Many crews enroll their whole team in Safety Training and their designated Competent Person in the advanced course. Not sure which one you need? <a href="which-excavation-course-do-i-need/">Use our course-picker guide &rarr;</a></p>
      </div>

      <div class="course-grid">
        <div class="course-card">
          <span class="course-card-tag">Crew-Level Safety</span>
          <h3>Excavation, Trenching &amp; Shoring Safety Training</h3>
          <p class="course-card-desc">Ideal training for workers involved in excavation and trenching operations at construction sites, covering hazard recognition and safe work practices around open trenches.</p>
          <ul class="course-card-facts">
            <li><strong>3 Hours</strong>Duration</li>
            <li><strong>EN &amp; ES</strong>Languages</li>
            <li><strong>On-Demand</strong>Format</li>
          </ul>
          <ul class="course-card-list">
            <li>Recognize cave-in, atmospheric, and utility strike hazards</li>
            <li>Understand soil classification and protective system basics</li>
            <li>Identify safe access, egress, and spoil pile placement</li>
            <li>Know when to stop work and notify the Competent Person</li>
          </ul>
          <div class="course-card-footer">
            <span class="course-card-price">$59.99 <span>/ seat</span></span>
            <a href="excavation-trenching-shoring-safety-training/" class="btn btn-primary" data-course="safety">Course Details</a>
          </div>
        </div>

        <div class="course-card">
          <span class="course-card-tag">Advanced / Competent Person</span>
          <h3>Competent Person for Excavation, Trenching &amp; Shoring Training</h3>
          <p class="course-card-desc">Advanced training under 29 CFR 1926 Subpart P for the person responsible for a site's daily inspections, protective system selection, and overall excavation program, including large-scale and federally funded projects.</p>
          <ul class="course-card-facts">
            <li><strong>8 Hours</strong>Duration</li>
            <li><strong>EN &amp; ES</strong>Languages</li>
            <li><strong>On-Demand</strong>Format</li>
          </ul>
          <ul class="course-card-list">
            <li>Classify soil and select sloping, benching, or shoring systems</li>
            <li>Conduct required daily excavation inspections</li>
            <li>Evaluate protective system design and installation</li>
            <li>Build a written excavation safety program &amp; emergency plan</li>
          </ul>
          <div class="course-card-footer">
            <span class="course-card-price">$159.99 <span>/ seat</span></span>
            <a href="competent-person-excavation-trenching-shoring-training/" class="btn btn-primary" data-course="competent">Course Details</a>
          </div>
        </div>
      </div>

      <div class="competent-person-note">
        <p><strong>A note on the Competent Person title:</strong> OSHA defines a competent person as someone capable of identifying existing and predictable hazards and authorized to take prompt corrective measures. Training supports this role, but the employer must designate the competent person and ensure they have the knowledge, authority, and site-specific understanding needed for the excavation work being performed. Completing this course is a foundational step, not an automatic designation.</p>
      </div>

      <div class="compare-wrap">
        <table class="compare-table">
          <thead>
            <tr>
              <th>Compare</th>
              <th>Excavation, Trenching &amp; Shoring Safety</th>
              <th>Competent Person</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Primary focus</td>
              <td>Hazard <strong>awareness</strong> &amp; safe work practices for the crew</td>
              <td><strong>Program oversight</strong>, inspections &amp; protective system selection</td>
            </tr>
            <tr>
              <td>Best for</td>
              <td>Excavation crews, equipment operators, laborers, utility &amp; municipal staff</td>
              <td>Safety managers, foremen, EHS coordinators, program owners</td>
            </tr>
            <tr>
              <td>Duration</td>
              <td>3 Hours</td>
              <td>8 Hours</td>
            </tr>
            <tr>
              <td>Price</td>
              <td>$59.99 / seat</td>
              <td>$159.99 / seat</td>
            </tr>
            <tr>
              <td>Certificate validity</td>
              <td>36 months</td>
              <td>24 months</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- WHICH COURSE DO I NEED (interactive teaser) -->
  <section class="section which-course-section" id="which-course">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Not Sure Which One?</p>
        <h2>Which Course Do I Need?</h2>
      </div>
      COURSE_PICKER_TEASER
      <p style="text-align:center;margin-top:24px;"><a href="which-excavation-course-do-i-need/" class="btn btn-outline">Full Decision Guide &amp; Comparison Table</a></p>
    </div>
  </section>

  <!-- CURRICULUM -->
  <section class="section" id="curriculum">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Curriculum</p>
        <h2>What Each Course Covers</h2>
        <p class="section-sub">Focused, practical modules broken out by role.</p>
      </div>

      <div class="curriculum-columns">
        <div>
          <div class="curriculum-col-head">
            <p class="eyebrow">Safety Training</p>
            <h3>Crew-Level Hazard Awareness</h3>
          </div>
          <ol class="curriculum-list">
            <li>
              <span class="curriculum-num">01</span>
              <div>
                <h4>Understanding Excavation Hazards</h4>
                <p>Cave-ins, engulfment, falls, water accumulation, and hazardous atmospheres common to open trenches.</p>
              </div>
            </li>
            <li>
              <span class="curriculum-num">02</span>
              <div>
                <h4>OSHA Subpart P Overview</h4>
                <p>The structure of the excavation standard and where crew-level duties come from.</p>
              </div>
            </li>
            <li>
              <span class="curriculum-num">03</span>
              <div>
                <h4>Soil &amp; Protective Systems Basics</h4>
                <p>How soil type drives the choice between sloping, benching, shielding, and shoring.</p>
              </div>
            </li>
            <li>
              <span class="curriculum-num">04</span>
              <div>
                <h4>Safe Access, Egress &amp; Spoil Placement</h4>
                <p>Ladder and ramp requirements, spoil pile setback, and safe distances from the edge.</p>
              </div>
            </li>
            <li>
              <span class="curriculum-num">05</span>
              <div>
                <h4>Utility Location &amp; Emergency Awareness</h4>
                <p>Call-before-you-dig practices, underground utility hazards, and when to stop work and notify the Competent Person.</p>
              </div>
            </li>
          </ol>
        </div>

        <div>
          <div class="curriculum-col-head">
            <p class="eyebrow">Competent Person</p>
            <h3>Program Oversight Track</h3>
          </div>
          <ol class="curriculum-list">
            <li>
              <span class="curriculum-num">01</span>
              <div>
                <h4>Defining the Competent Person Role</h4>
                <p>Authority and legal responsibility under 29 CFR 1926 Subpart P.</p>
              </div>
            </li>
            <li>
              <span class="curriculum-num">02</span>
              <div>
                <h4>Soil Classification</h4>
                <p>Classifying Stable Rock, Type A, Type B, and Type C soils using visual and manual analysis tests.</p>
              </div>
            </li>
            <li>
              <span class="curriculum-num">03</span>
              <div>
                <h4>Selecting Protective Systems</h4>
                <p>Choosing and sizing sloping, benching, shielding, and shoring systems for site conditions.</p>
              </div>
            </li>
            <li>
              <span class="curriculum-num">04</span>
              <div>
                <h4>Daily Inspection Duties</h4>
                <p>Required inspections before each shift, after rainfall, and whenever conditions change.</p>
              </div>
            </li>
            <li>
              <span class="curriculum-num">05</span>
              <div>
                <h4>Program Development &amp; Emergency Planning</h4>
                <p>Building a written excavation safety program and rescue plan that holds up under inspection.</p>
              </div>
            </li>
          </ol>
        </div>
      </div>
    </div>
  </section>

  <!-- WHO IT'S FOR -->
  <section class="section section-alt" id="audience">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Who It's For</p>
        <h2>Built for Everyone Who Works Around Excavations</h2>
      </div>
      <div class="grid-4 audience-grid">
        <div class="audience-card">Excavation &amp; Trenching Crews</div>
        <div class="audience-card">Equipment Operators</div>
        <div class="audience-card">Competent Persons &amp; Foremen</div>
        <div class="audience-card">EHS Managers &amp; Safety Coordinators</div>
        <div class="audience-card">General Contractors</div>
        <div class="audience-card">Utility &amp; Municipal Crews</div>
        <div class="audience-card">Pipeline &amp; Underground Contractors</div>
        <div class="audience-card">Federal &amp; Public Project Contractors</div>
      </div>
    </div>
  </section>

  <!-- EMPLOYER RESPONSIBILITIES -->
  <section class="section employer-section" id="employer-responsibilities">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Employer Responsibilities</p>
        <h2>Training Is Part of Compliance - Not All of It</h2>
        <p class="section-sub">
          Online training can support OSHA compliance, but employers are responsible for ensuring employees are
          trained for the actual hazards, soil conditions, protective systems, equipment, access and egress points,
          utility hazards, traffic exposure, water conditions, and emergency procedures they will encounter.
          Excavation safety often requires site-specific instruction, daily inspections, documented hazard
          assessments, and employer authorization.
        </p>
      </div>
      <div class="grid-4 audience-grid employer-grid">
        <div class="audience-card">Site-specific hazard assessment</div>
        <div class="audience-card">Competent Person designation</div>
        <div class="audience-card">Daily inspection documentation</div>
        <div class="audience-card">Protective system verification</div>
      </div>
    </div>
  </section>

  <!-- CREDENTIAL TRANSPARENCY TEASER -->
  <section class="section section-alt credential-teaser" id="credential-transparency">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Credential Transparency</p>
        <h2>What Your Certificate Does - and Doesn't - Mean</h2>
        <p class="section-sub">
          Upon successful completion, students receive a certificate of completion for the selected excavation,
          trenching, and shoring training course. This certificate documents completion of training content aligned
          with OSHA 29 CFR 1926 Subpart P. It does not mean OSHA has certified the student, endorsed the course, or
          issued a license. Employers remain responsible for determining whether employees are trained, qualified,
          authorized, and competent for their assigned excavation duties and jobsite conditions.
        </p>
        <a href="credential-transparency/" class="btn btn-outline">Read Full Credential Transparency Page</a>
      </div>
    </div>
  </section>

  <!-- PRICING / ENROLL -->
  <section class="section pricing-section" id="pricing">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Enroll</p>
        <h2>Get Your Team Trained Today</h2>
        <p class="section-sub">Reserve seats in either course, and our team will follow up to complete enrollment.</p>
      </div>

      <div class="pricing-toggle" role="tablist" aria-label="Filter pricing by course">
        <button type="button" class="pricing-toggle-btn active" data-course="safety" role="tab" aria-selected="true">Excavation Safety Training</button>
        <button type="button" class="pricing-toggle-btn" data-course="competent" role="tab" aria-selected="false">Competent Person</button>
      </div>

      <div class="pricing-grid filtered" id="pricingGrid">

        <div class="pricing-card is-visible" data-course="safety">
          <div class="pricing-card-top">
            <h3>Excavation, Trenching &amp; Shoring Safety Training</h3>
            <div class="price">
              <span class="price-original" hidden>$59.99</span>
              <span class="price-current"><span class="price-amount">$59.99</span><span class="price-per">/ seat</span></span>
            </div>
          </div>

          <ul class="pricing-features">
            <li>3 hours of self-paced online training</li>
            <li>Available in English and Spanish</li>
            <li>Mobile-optimized, accessible 24/7</li>
            <li>Certificate of completion issued immediately</li>
            <li>Certificate valid 36 months</li>
            <li>Aligned with 29 CFR 1926 Subpart P</li>
          </ul>

          <form class="enroll-form" id="enrollFormSafety" data-price-per-seat="59.99" data-course-code="safety" data-success-target="formSuccessSafety">
            <div class="form-row">
              <label for="seatsSafety">Number of Seats</label>
              <input type="number" id="seatsSafety" name="seats" min="1" value="1" required>
            </div>

            <div class="bulk-pricing">
              <button type="button" class="bulk-pricing-toggle" aria-expanded="false" aria-controls="bulkPanelSafety">
                <svg class="bulk-pricing-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 20h5v-2a4 4 0 0 0-3-3.87"/><path d="M9 20H4v-2a4 4 0 0 1 3-3.87"/><path d="M9 4.13a4 4 0 0 1 0 7.75"/><circle cx="12" cy="8" r="4"/><path d="M12 20a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4"/></svg>
                <span>Bulk Pricing</span>
                <svg class="bulk-pricing-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="bulk-pricing-panel" id="bulkPanelSafety" hidden>
                <table class="bulk-pricing-table">
                  <thead><tr><th>Seats</th><th>Per Seat</th></tr></thead>
                  <tbody></tbody>
                </table>
              </div>
            </div>

            <div class="form-total">Total: $59.99</div>
            <button type="submit" class="btn btn-primary btn-block btn-lg">Continue to Payment</button>
          </form>

          <p class="format-note">This reserves seats in the <strong>On-Demand Online</strong> course. Need SCORM, Virtual Instructor-Led, or In-Person Group training instead? <a href="https://hazwoper-osha.com/online-courses/osha-excavation-trenching-and-shoring-safety-training" target="_blank" rel="noopener">See other formats on HAZWOPER-OSHA.com &rarr;</a></p>

          <div class="form-success" id="formSuccessSafety" hidden>
            <h4>Seat count received.</h4>
            <p>You'll be taken to secure payment to complete your enrollment.</p>
          </div>
        </div>

        <div class="pricing-card" data-course="competent">
          <div class="pricing-card-top">
            <h3>Competent Person for Excavation, Trenching &amp; Shoring Training</h3>
            <div class="price">
              <span class="price-original" hidden>$159.99</span>
              <span class="price-current"><span class="price-amount">$159.99</span><span class="price-per">/ seat</span></span>
            </div>
          </div>

          <ul class="pricing-features">
            <li>8 hours of self-paced online training</li>
            <li>Available in English and Spanish</li>
            <li>Mobile-optimized, accessible 24/7</li>
            <li>Certificate of completion issued immediately</li>
            <li>Certificate valid 24 months</li>
            <li>Aligned with 29 CFR 1926 Subpart P</li>
          </ul>

          <form class="enroll-form" id="enrollFormCompetent" data-price-per-seat="159.99" data-course-code="competent" data-success-target="formSuccessCompetent">
            <div class="form-row">
              <label for="seatsCompetent">Number of Seats</label>
              <input type="number" id="seatsCompetent" name="seats" min="1" value="1" required>
            </div>

            <div class="bulk-pricing">
              <button type="button" class="bulk-pricing-toggle" aria-expanded="false" aria-controls="bulkPanelCompetent">
                <svg class="bulk-pricing-icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 20h5v-2a4 4 0 0 0-3-3.87"/><path d="M9 20H4v-2a4 4 0 0 1 3-3.87"/><path d="M9 4.13a4 4 0 0 1 0 7.75"/><circle cx="12" cy="8" r="4"/><path d="M12 20a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4"/></svg>
                <span>Bulk Pricing</span>
                <svg class="bulk-pricing-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="6 9 12 15 18 9"/></svg>
              </button>
              <div class="bulk-pricing-panel" id="bulkPanelCompetent" hidden>
                <table class="bulk-pricing-table">
                  <thead><tr><th>Seats</th><th>Per Seat</th></tr></thead>
                  <tbody></tbody>
                </table>
              </div>
            </div>

            <div class="form-total">Total: $159.99</div>
            <button type="submit" class="btn btn-primary btn-block btn-lg">Continue to Payment</button>
          </form>

          <p class="format-note">This reserves seats in the <strong>On-Demand Online</strong> course. Need SCORM, Virtual Instructor-Led, or In-Person Group training instead? <a href="https://hazwoper-osha.com/online-courses/competent-person-for-excavation-trenching-and-shoring" target="_blank" rel="noopener">See other formats on HAZWOPER-OSHA.com &rarr;</a></p>

          <div class="form-success" id="formSuccessCompetent" hidden>
            <h4>Seat count received.</h4>
            <p>You'll be taken to secure payment to complete your enrollment.</p>
          </div>
        </div>

      </div>

      <p class="pricing-accred-note">Questions about who stands behind this training? See <a href="#accreditations">Certifications &amp; Accreditations</a> above, or read our <a href="credential-transparency/">Credential Transparency</a> page.</p>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section" id="faq">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">FAQ</p>
        <h2>Common Questions</h2>
      </div>

      <div class="faq-list">
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">
            Which excavation course do I actually need?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>It depends on your role. Excavation, Trenching &amp; Shoring Safety Training is for anyone working in or around an excavation, including operators and laborers. Competent Person training is for the individual responsible for classifying soil, selecting protective systems, running daily inspections, and owning the site's overall excavation program. Use our <a href="which-excavation-course-do-i-need/">course-picker guide</a> for a role-by-role breakdown.</p>
          </div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">
            Is this training OSHA certified or OSHA approved?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>No. OSHA does not certify, approve, or endorse individual training providers or courses. This training is OSHA-aligned, meaning it's built around OSHA's excavation standard, 29 CFR 1926 Subpart P. See our <a href="credential-transparency/">Credential Transparency</a> page for the full explanation.</p>
          </div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">
            How long does each course take?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Excavation, Trenching &amp; Shoring Safety Training runs about 3 hours, and Competent Person training runs about 8 hours. Both are self-paced.</p>
          </div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">
            Is this training available in Spanish?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Yes. Both courses are available in English and Spanish.</p>
          </div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">
            Do I get a certificate right away?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Yes, a certificate of completion is issued immediately after finishing either course, ready to keep in your compliance files. Safety Training certificates are valid 36 months and Competent Person certificates are valid 24 months before a refresher is recommended.</p>
          </div>
        </div>
        <div class="faq-item">
          <button class="faq-question" aria-expanded="false">
            Does every excavation site need a Competent Person?
            <span class="faq-icon">+</span>
          </button>
          <div class="faq-answer">
            <p>Yes. OSHA requires a designated Competent Person to inspect excavations daily, before each shift, and after any event that could increase hazards, such as rainfall. Training supports this role, but the employer must designate the Competent Person. It's common for the same person to hold both certifications, taking Safety Training first and Competent Person training as they take on more responsibility.</p>
          </div>
        </div>
      </div>

      <div class="faq-view-more">
        <a href="frequently-asked-questions/" class="btn btn-outline">View More Questions</a>
      </div>
    </div>
  </section>

  <!-- FINAL CTA -->
  <section class="final-cta">
    <div class="container final-cta-inner">
      <h2>Keep Your Crew Compliant. Train Every Role.</h2>
      <p>Two courses, online. Certificate on completion. English &amp; Spanish.</p>
      <div class="hero-cta-row">
        <a href="#pricing" class="btn btn-primary btn-lg">Enroll Now</a>
        <a href="tel:18664296742" class="btn btn-outline-light btn-lg">Call 1-866-429-6742</a>
      </div>
    </div>
  </section>
"""

HOME_SCHEMA = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Which excavation course do I actually need?", "acceptedAnswer": {"@type": "Answer", "text": "It depends on your role. Excavation, Trenching & Shoring Safety Training is for anyone working in or around an excavation. Competent Person training is for the individual responsible for classifying soil, selecting protective systems, running daily inspections, and owning the site's overall excavation program."}},
    {"@type": "Question", "name": "Is this training OSHA certified or OSHA approved?", "acceptedAnswer": {"@type": "Answer", "text": "No. OSHA does not certify, approve, or endorse individual training providers or courses. This training is OSHA-aligned, meaning it is built around OSHA's excavation standard, 29 CFR 1926 Subpart P."}},
    {"@type": "Question", "name": "How long does each course take?", "acceptedAnswer": {"@type": "Answer", "text": "Excavation, Trenching & Shoring Safety Training runs about 3 hours, and Competent Person training runs about 8 hours. Both are self-paced."}},
    {"@type": "Question", "name": "Is this training available in Spanish?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. Both courses are available in English and Spanish."}},
    {"@type": "Question", "name": "Do I get a certificate right away?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, a certificate of completion is issued immediately after finishing either course. Safety Training certificates are valid 36 months and Competent Person certificates are valid 24 months before a refresher is recommended."}},
    {"@type": "Question", "name": "Does every excavation site need a Competent Person?", "acceptedAnswer": {"@type": "Answer", "text": "Yes. OSHA requires a designated Competent Person to inspect excavations daily, before each shift, and after any event that could increase hazards. Training supports this role, but the employer must designate the Competent Person."}}
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Excavation, Trenching & Shoring Safety Training",
  "description": "Crew-level hazard-awareness course covering cave-in, atmospheric, and utility-strike hazards, soil classification and protective system basics, and safe access, egress, and spoil pile placement.",
  "provider": {"@type": "Organization", "name": "HAZWOPER OSHA Training, LLC", "sameAs": "https://hazwoper-osha.com/"},
  "url": "https://excavationtrenchingshoring.com/excavation-trenching-shoring-safety-training/",
  "timeRequired": "PT3H",
  "inLanguage": ["en", "es"],
  "educationalCredentialAwarded": "Certificate of Completion",
  "occupationalCategory": "Construction and Extraction Occupations",
  "hasCourseInstance": {
    "@type": "CourseInstance",
    "courseMode": "online",
    "courseWorkload": "PT3H"
  },
  "offers": {"@type": "Offer", "price": 59.99, "priceCurrency": "USD", "url": "https://excavationtrenchingshoring.com/excavation-trenching-shoring-safety-training/"}
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Competent Person for Excavation, Trenching & Shoring Training",
  "description": "Program-oversight course covering the Competent Person role and authority, soil classification, selecting protective systems, daily inspection duties, and building a written excavation safety program.",
  "provider": {"@type": "Organization", "name": "HAZWOPER OSHA Training, LLC", "sameAs": "https://hazwoper-osha.com/"},
  "url": "https://excavationtrenchingshoring.com/competent-person-excavation-trenching-shoring-training/",
  "timeRequired": "PT8H",
  "inLanguage": ["en", "es"],
  "educationalCredentialAwarded": "Certificate of Completion",
  "occupationalCategory": "Construction Managers; Occupational Health and Safety Specialists",
  "hasCourseInstance": {
    "@type": "CourseInstance",
    "courseMode": "online",
    "courseWorkload": "PT8H"
  },
  "offers": {"@type": "Offer", "price": 159.99, "priceCurrency": "USD", "url": "https://excavationtrenchingshoring.com/competent-person-excavation-trenching-shoring-training/"}
}
</script>"""

# ---------------------------------------------------------------------------
# CREDENTIAL TRANSPARENCY
# ---------------------------------------------------------------------------

PAGES.append({
    "slug": "credential-transparency",
    "active": "accreditations",
    "title": "Credential Transparency for Excavation Training",
    "description": "What a certificate of completion means, OSHA-aligned training vs. certification, IACET CEUs, and how this differs from an OSHA Outreach card.",
    "body": breadcrumb_nav("Credential Transparency") + hero_solo(
        "Credential Transparency",
        "What Your Certificate Does - and Doesn't - Mean",
        "A plain-language explanation of certificates of completion, OSHA-aligned training, employer-required documentation, Competent Person designation, IACET CEUs, and how this differs from an OSHA Outreach card.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <div class="callout-box">
        <p>Upon successful completion, students receive a certificate of completion for the selected excavation, trenching, and shoring training course. This certificate documents completion of training content aligned with OSHA 29 CFR 1926 Subpart P. It does not mean OSHA has certified the student, endorsed the course, or issued a license. Employers remain responsible for determining whether employees are trained, qualified, authorized, and competent for their assigned excavation duties and jobsite conditions.</p>
      </div>

      <h2>Certificate of Completion</h2>
      <p>A certificate of completion is a record that a student finished a specific course, on a specific date, for a specific number of training hours. It's issued by the training provider - here, HAZWOPER OSHA Training, LLC - not by OSHA. It's the same kind of document employers use to demonstrate that required training occurred, and it belongs in your compliance files alongside site-specific training records.</p>

      <h2>OSHA-Aligned Training</h2>
      <p>"OSHA-aligned" means the course content is built around a specific OSHA standard - in this case, 29 CFR 1926 Subpart P, Excavations. It means the topics, terminology, and requirements taught in the course match what that standard actually says. It does not mean OSHA reviewed, approved, certified, or endorsed the course. <strong>OSHA does not certify or approve training providers or courses for excavation and trenching.</strong> Any provider claiming an "OSHA certification" for this type of training is describing something OSHA doesn't offer.</p>

      <h2>Employer-Required Training Documentation</h2>
      <p>OSHA's excavation standard requires that workers be trained for the hazards of the work they perform, and that a Competent Person be designated for every excavation site. It does not specify a single approved course or provider. Employers use documentation like this certificate, combined with their own site-specific instruction and records, to demonstrate that required training took place. The certificate is one piece of that documentation, not the whole compliance program.</p>

      <h2>Competent Person Designation</h2>
      <p>Completing Competent Person training is not the same as being designated a Competent Person. OSHA defines a Competent Person as someone capable of identifying existing and predictable hazards and authorized to take prompt corrective measures. The employer designates who holds that authority on a given site. Training builds the knowledge base; the employer grants the authority and confirms the site-specific understanding needed for the work being performed. See our <a href="../which-excavation-course-do-i-need/">course-picker guide</a> for more on how the two courses map to different roles.</p>

      <h2>IACET CEUs</h2>
      <p>HAZWOPER OSHA Training, LLC is an <a href="https://www.iacet.org/affiliates/accredited-providers-list/accredited-provider-overview/?providerID=131618" target="_blank" rel="noopener">IACET Accredited Provider</a> (Provider ID 131618) at the organizational level. That accreditation reflects HAZWOPER OSHA Training's institutional processes for course design and delivery. It is a separate question from whether continuing education units (CEUs) are issued for any individual course. At this time, CEUs are not advertised specifically for the Excavation, Trenching &amp; Shoring Safety Training or Competent Person for Excavation, Trenching &amp; Shoring courses. If your organization requires documented CEUs for a specific course, contact HAZWOPER OSHA Training directly to confirm current CEU availability before enrolling.</p>

      <h2>OSHA Outreach Cards Are a Different Thing</h2>
      <p>OSHA 10-Hour and 30-Hour Outreach cards are issued through OSHA's own Outreach Training Program, delivered by OSHA-authorized trainers using OSHA's curriculum, with cards issued by the OSHA Training Institute (or its designated processing agent). Excavation, trenching, and shoring competent-person training is a separate, standard-specific course - it is not part of the Outreach card program and does not result in an OSHA Outreach card. If your project specifically requires a 10-Hour or 30-Hour Outreach card, that's a different course than the ones offered on this site.</p>

      <div class="disclaimer-box">
        OSHA does not certify or endorse individual training providers for excavation and trenching. OSHA standards require employers to ensure workers receive training appropriate to their assigned duties, hazards, equipment, protective systems, soil conditions, and worksite conditions.
      </div>

      <p>For the provider-level accreditation details referenced above, see <a href="../index.html#accreditations">Certifications &amp; Accreditations</a> or <a href="https://hazwoper-osha.com/about" target="_blank" rel="noopener">HAZWOPER OSHA Training's about page</a>.</p>
    </div>
  </section>

  <section class="final-cta">
    <div class="container final-cta-inner">
      <h2>Ready to Enroll?</h2>
      <p>Know exactly what you're getting, and what still depends on your employer.</p>
      <div class="hero-cta-row">
        <a href="../index.html#pricing" class="btn btn-primary btn-lg">See Course Pricing</a>
        <a href="../which-excavation-course-do-i-need/" class="btn btn-outline-light btn-lg">Which Course Do I Need?</a>
      </div>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Credential Transparency", "/credential-transparency/"),
})

# ---------------------------------------------------------------------------
# OSHA EXCAVATION STANDARDS
# ---------------------------------------------------------------------------

PAGES.append({
    "slug": "osha-excavation-standards",
    "active": "accreditations",
    "title": "OSHA Excavation Standards | 29 CFR 1926 Subpart P Explained",
    "description": "Plain-language summaries and official links to 29 CFR 1926 Subpart P, 1926.650, 1926.651, 1926.652, Appendices A-C, and OSHA's Trenching and Excavation eTool.",
    "body": breadcrumb_nav("OSHA Excavation Standards") + hero_solo(
        "Regulatory Reference",
        "OSHA Excavation Standards: 29 CFR 1926 Subpart P",
        "Plain-language summaries of the federal excavation standard, with direct links to the official OSHA text for every section referenced on this site.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <p>29 CFR 1926 Subpart P is OSHA's construction standard for excavations. The summaries below are for orientation only - always confirm current requirements against OSHA's official published text, linked in each section.</p>

      <h2>Subpart P - Excavations (Overview)</h2>
      <p>The umbrella standard covering all excavation and trenching work in construction, including soil classification, protective systems, access and egress, and inspection duties.</p>
      <p><a href="https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926SubpartP" target="_blank" rel="noopener">Read 29 CFR 1926 Subpart P on osha.gov &rarr;</a></p>

      <h2>1926.650 - Scope, Application, and Definitions</h2>
      <p>Defines the terms used throughout Subpart P - excavation, trench, sloping, benching, shoring, shielding, Competent Person, and more - and states which operations the standard applies to.</p>
      <p><a href="https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.650" target="_blank" rel="noopener">Read 1926.650 on osha.gov &rarr;</a></p>

      <h2>1926.651 - Specific Excavation Requirements</h2>
      <p>Covers surface encumbrances, underground utility location, access and egress, exposure to vehicular traffic, exposure to falling loads, warning systems for mobile equipment, hazardous atmospheres, protection from water accumulation, stability of adjacent structures, protection of employees from loose rock or soil, inspections, and fall protection for walkways.</p>
      <p><a href="https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.651" target="_blank" rel="noopener">Read 1926.651 on osha.gov &rarr;</a></p>

      <h2>1926.652 - Requirements for Protective Systems</h2>
      <p>Requires a protective system for excavations 5 feet or deeper (unless the excavation is entirely in stable rock or a Competent Person determines no hazard exists), and sets the design criteria for sloping, benching, shoring, and shielding systems, including when a registered professional engineer's design is required.</p>
      <p><a href="https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.652" target="_blank" rel="noopener">Read 1926.652 on osha.gov &rarr;</a></p>

      <h2>Appendix A - Soil Classification</h2>
      <p>Defines Stable Rock, Type A, Type B, and Type C soils, and the visual and manual tests used to classify them. See our <a href="../soil-classification-training/">Soil Classification page</a> for a plain-language walkthrough.</p>

      <h2>Appendix B - Sloping and Benching</h2>
      <p>Sets the maximum allowable slopes and bench dimensions for each soil type. See our <a href="../excavation-protective-systems/">Protective Systems page</a> for how this fits alongside shoring and shielding.</p>

      <h2>Appendix C - Timber Shoring for Trenches</h2>
      <p>Tabulated data for timber shoring configurations by soil type and trench depth/width, an alternative to aluminum hydraulic shoring in certain conditions.</p>

      <h2>OSHA Trenching and Excavation eTool</h2>
      <p>OSHA's interactive reference tool covering hazard recognition, soil analysis, protective systems, and the Competent Person's role, with illustrations and scenario walkthroughs.</p>
      <p><a href="https://www.osha.gov/etools/construction/trenching" target="_blank" rel="noopener">Open the OSHA Trenching and Excavation eTool &rarr;</a></p>

      <h2>OSHA Competent Person Guidance</h2>
      <p>OSHA's eTool section specifically on the Competent Person's duties, authority, and required qualifications.</p>
      <p><a href="https://www.osha.gov/etools/construction/trenching/competent-person" target="_blank" rel="noopener">Open OSHA's Competent Person guidance &rarr;</a></p>

      <div class="disclaimer-box">
        This page is a plain-language orientation, not legal advice, and not a substitute for reading the official standard. Regulatory text and enforcement guidance can change; always confirm current requirements directly with OSHA or qualified counsel for your specific site and project. If you're in an OSHA-approved State Plan state, also see our <a href="../state-osha-plan-requirements/">State OSHA Plan Requirements</a> page.
      </div>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("OSHA Excavation Standards", "/osha-excavation-standards/"),
})

# ---------------------------------------------------------------------------
# ABOUT
# ---------------------------------------------------------------------------

PAGES.append({
    "slug": "about",
    "active": None,
    "title": "About ExcavationTrenchingShoring.com",
    "description": "What ExcavationTrenchingShoring.com is, how training is delivered through HAZWOPER OSHA Training, LLC, and how to reach support.",
    "body": breadcrumb_nav("About") + hero_solo(
        "About Us",
        "About ExcavationTrenchingShoring.com",
        "A dedicated excavation, trenching, and shoring safety training resource, with training delivered through HAZWOPER OSHA Training, LLC.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <h2>What This Site Is</h2>
      <p>ExcavationTrenchingShoring.com is a dedicated resource for excavation, trenching, and shoring safety training, built to help construction crews, utility workers, equipment operators, supervisors, and designated Competent Persons find the right course, understand OSHA's excavation standard, and get a certificate of completion they can use for their compliance records.</p>

      <h2>Who Delivers the Training</h2>
      <p>Training courses on this site are provided through <a href="https://hazwoper-osha.com/" target="_blank" rel="noopener">HAZWOPER OSHA Training, LLC</a>, which delivers OSHA, EPA, DOT, hazardous materials, construction safety, and workplace compliance training across online, SCORM, virtual instructor-led, and in-person formats. HAZWOPER OSHA Training is an <a href="https://www.iacet.org/affiliates/accredited-providers-list/accredited-provider-overview/?providerID=131618" target="_blank" rel="noopener">IACET Accredited Provider</a> and a BBB A+ rated business. See <a href="../index.html#accreditations">Certifications &amp; Accreditations</a> for details, and <a href="../credential-transparency/">Credential Transparency</a> for what that accreditation does and doesn't mean for an individual course.</p>

      <h2>Why This Site Exists</h2>
      <p>Excavation and trenching are among the most fatal hazards in construction, and the two roles on a job site - the crew working around a trench and the Competent Person responsible for it - need very different depths of training. This site exists to make that distinction clear, point each role to the right course, and be transparent about what OSHA does and doesn't require, certify, or approve. See our <a href="../which-excavation-course-do-i-need/">course-picker guide</a> to find your role.</p>

      <h2>Training Formats Available</h2>
      <p>Both courses are self-paced, on-demand, and available online in English and Spanish through this site. SCORM packages for company learning management systems, Virtual Instructor-Led sessions, and In-Person Group training are available through HAZWOPER OSHA Training for teams that need those formats - see the course pages for direct links.</p>

      <h2>Contact &amp; Support</h2>
      <p>Questions about enrollment, certificates, group training, or course content can be directed to:</p>
      <ul>
        <li>Phone: <a href="tel:18664296742">1-866-429-6742</a></li>
        <li>Email: <a href="mailto:info@hazwoper-osha.com">info@hazwoper-osha.com</a></li>
        <li>Training provider office: HAZWOPER OSHA Training, LLC, 11901 Santa Monica Blvd. Suite #414, Los Angeles, CA 90025 (by appointment)</li>
      </ul>
      <p>For certificate verification, see <a href="https://hazwoper-osha.com/certificate-verification" target="_blank" rel="noopener">Verify Certificate on hazwoper-osha.com</a>. For refund and policy questions, see our <a href="../refund-policy/">Refund Policy</a> and <a href="../certificate-policy/">Certificate Policy</a>.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("About", "/about/") + """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "HAZWOPER OSHA Training, LLC",
  "description": "Training provider delivering the excavation, trenching, and shoring courses offered on ExcavationTrenchingShoring.com.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "11901 Santa Monica Blvd. Suite #414",
    "addressLocality": "Los Angeles",
    "addressRegion": "CA",
    "postalCode": "90025",
    "addressCountry": "US"
  },
  "telephone": "+1-866-429-6742",
  "email": "info@hazwoper-osha.com",
  "url": "https://hazwoper-osha.com/"
}
</script>""",
})

# ---------------------------------------------------------------------------
# INSTRUCTORS & TRAINING PROVIDER
# ---------------------------------------------------------------------------

PAGES.append({
    "slug": "instructors-and-training-provider",
    "active": None,
    "title": "Instructors & Training Provider | ExcavationTrenchingShoring.com",
    "description": "Meet the training provider and lead instructor behind ExcavationTrenchingShoring.com's excavation, trenching, and shoring courses.",
    "body": breadcrumb_nav("Instructors & Training Provider") + hero_solo(
        "Instructors &amp; Training Provider",
        "Who's Behind This Training",
        "Courses on this site are delivered through HAZWOPER OSHA Training's training platform and instructional team.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <h2>Training Provider</h2>
      <p>Excavation, trenching, and shoring courses on this site are delivered through <a href="https://hazwoper-osha.com/" target="_blank" rel="noopener">HAZWOPER OSHA Training's</a> training platform and instructional team. View current organizational certifications, accreditations, and provider credentials on our <a href="../index.html#accreditations">Certifications &amp; Accreditations</a> section.</p>

      <h2>Lead Instructor</h2>
      <div class="instructor-card">
        <div class="instructor-avatar">MC</div>
        <div>
          <h3>Michael J. Conroy, CSP, CHST</h3>
          <p class="instructor-title">OSHA-Authorized Trainer &middot; Lead Instructor, HAZWOPER OSHA Training</p>
          <p>Michael Conroy is a Certified Safety Professional (CSP) and Construction Health and Safety Technician (CHST), and an OSHA-Authorized Trainer. His background includes service as a paramedic, firefighter-paramedic, and retired battalion chief, during which he supervised battalion-level confined-space, trench-rescue, tunnel, and water-rescue drills - direct, hands-on experience with the same trench and confined-space hazards covered in this site's excavation courses.</p>
          <p><a href="https://hazwoper-osha.com/lead-instructor" target="_blank" rel="noopener">View full bio on hazwoper-osha.com &rarr;</a></p>
        </div>
      </div>

      <p>HAZWOPER OSHA Training's broader instructional team supports course development and delivery across its full catalog of OSHA, EPA, DOT, and workplace safety courses. See <a href="https://hazwoper-osha.com/our-instructors" target="_blank" rel="noopener">hazwoper-osha.com/our-instructors</a> for the wider instructor roster.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Instructors & Training Provider", "/instructors-and-training-provider/"),
})

# NOTE: There is no dedicated /verify-certificate/ page. Certificate
# verification links go straight to hazwoper-osha.com/certificate-verification
# (the actual system of record) with no page in between. See
# HAZWOPER_VERIFY_URL below, used everywhere a "Verify Certificate" link appears.

HAZWOPER_VERIFY_URL = "https://hazwoper-osha.com/certificate-verification"

# ---------------------------------------------------------------------------
# REVIEWS
# ---------------------------------------------------------------------------

REVIEWS_SAFETY = [
    ("Titus Keaton", "Carpenter - Commercial Construction", "Content is thorough and relevant, presented in a manner that employees can comprehend. The platform is extremely user friendly, and the courses can be done at our employees' convenience."),
    ("Drew Caiden", "Human Rights Investigator Trainer", "The course is easy to understand - and have never received a single complaint from my trainees."),
    ("Trey Dallas", "Site Safety Construction Professional", "I can customize the training and even print a certificate for each employee trained. HAZWOPER-OSHA is a trustworthy company. I wouldn't use any other training provider."),
    ("Malik Ahmed", "Maintenance Crew", "Animations used were clear and simple to understand, will use HAZWOPER-OSHA for other construction courses as well."),
    ("Adan Julio", "Construction Inspector", "Different soil classifications and their main properties is explained well in the course."),
]
REVIEWS_COMPETENT = [
    ("Greg Sanders", "Health and Safety Manager", "We used this as baseline training for new site leads. The content is detailed and delivered in a way that's easy to remember and can be applied immediately."),
    ('Thomas "TJ" Garner', "Construction Manager", "The case study scenarios and interactive content were a plus. Operating a medium-scale construction company, it gave me peace of mind knowing we're OSHA-compliant."),
    ("Michelle Harper", "Senior Project Engineer", "As someone moving into a leadership role, this course gave me the in-depth understanding I needed to take on competent person responsibilities. I appreciated that it's not a quick overview, but rather an in-depth learning."),
    ("Elena Cruz", "Field Safety Officer", "I especially found the section on emergency planning useful. This course was worth every dollar!"),
    ("Brian O'Reilly", "Foreman", "This excavation course really is great. Straightforward language, practical examples, and I was able to apply learnings on-site the next day."),
]


def _review_cards(reviews):
    cards = []
    for name, role, quote in reviews:
        cards.append(f"""<div class="testimonial-card">
          <p class="testimonial-quote">&ldquo;{quote}&rdquo;</p>
          <p class="testimonial-name">{name}</p>
          <p class="testimonial-role">{role}</p>
        </div>""")
    return "\n        ".join(cards)


PAGES.append({
    "slug": "reviews",
    "active": None,
    "title": "Reviews | Excavation, Trenching & Shoring Training",
    "description": "Verified student reviews for the Excavation, Trenching & Shoring Safety Training and Competent Person courses, as published by HAZWOPER OSHA Training.",
    "body": breadcrumb_nav("Reviews") + hero_solo(
        "Reviews",
        "What Students Say",
        "Verified reviews for these exact courses, published by HAZWOPER OSHA Training, the platform that delivers this training.",
    ) + f"""
  <section class="section">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Excavation, Trenching &amp; Shoring Safety Training</p>
        <h2>Crew-Level Course Reviews</h2>
      </div>
      <div class="two-col-cards">
        {_review_cards(REVIEWS_SAFETY[:4])}
      </div>
    </div>
  </section>

  <section class="section section-alt">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Competent Person for Excavation, Trenching &amp; Shoring</p>
        <h2>Competent Person Course Reviews</h2>
      </div>
      <div class="two-col-cards">
        {_review_cards(REVIEWS_COMPETENT[:4])}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container content-prose">
      <p class="disclaimer-box">Reviews above are published by HAZWOPER OSHA Training for these exact courses on hazwoper-osha.com and reproduced here with attribution. We do not edit or select reviews to favor a particular outcome. For references, group training questions, or enterprise training needs, contact HAZWOPER OSHA Training support at <a href="tel:18664296742">1-866-429-6742</a> or <a href="mailto:info@hazwoper-osha.com">info@hazwoper-osha.com</a>.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Reviews", "/reviews/"),
})

# ---------------------------------------------------------------------------
# COURSE PAGE HELPERS
# ---------------------------------------------------------------------------

def sample_cert(course_title, hours, org="HAZWOPER OSHA Training, LLC"):
    return f"""
      <div class="cert-sample">
        <span class="cert-sample-watermark">Sample - Not a Real Certificate</span>
        <div class="cert-sample-inner">
          <p class="cert-sample-org">{org}</p>
          <p class="cert-sample-title">Certificate of Completion</p>
          <p class="cert-sample-name">[Student Name Redacted]</p>
          <div class="cert-sample-grid">
            <div><strong>Course</strong>{course_title}</div>
            <div><strong>Training Hours</strong>{hours}</div>
            <div><strong>Completion Date</strong>[Redacted]</div>
            <div><strong>Certificate ID</strong>[XXXXXXX]</div>
            <div><strong>Issuing Provider</strong>{org}</div>
            <div><strong>Standard Referenced</strong>OSHA 29 CFR 1926 Subpart P</div>
          </div>
          <p style="margin:1rem 0 0;font-size:.78rem;color:var(--gray-500);">Verification: <a href="https://hazwoper-osha.com/certificate-verification" target="_blank" rel="noopener">hazwoper-osha.com/certificate-verification</a></p>
        </div>
      </div>"""


def course_meta_table(rows):
    trs = "\n        ".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in rows)
    return f"""<div class="data-table-wrap"><table class="data-table"><tbody>
        {trs}
      </tbody></table></div>"""


# ---------------------------------------------------------------------------
# COURSE PAGE 1: EXCAVATION, TRENCHING & SHORING SAFETY TRAINING
# ---------------------------------------------------------------------------

SAFETY_META = [
    ("Duration", "3 hours, self-paced"),
    ("Price", "$59.99 per seat"),
    ("Format", "On-demand online (SCORM, Virtual Instructor-Led, and In-Person Group available through HAZWOPER OSHA Training)"),
    ("Languages", "English and Spanish"),
    ("Device Compatibility", "Desktop, laptop, tablet, and mobile browsers"),
    ("Certificate Issued", "Certificate of completion, immediately on passing"),
    ("Certificate Validity", "36 months, before a refresher is recommended"),
    ("CEUs", "Not issued per-course. HAZWOPER OSHA Training is IACET Accredited at the organizational level - see <a href=\"../credential-transparency/\">Credential Transparency</a>."),
    ("OSHA Standard Covered", "29 CFR 1926 Subpart P, Excavations"),
]

SAFETY_BODY = breadcrumb_nav("Excavation, Trenching &amp; Shoring Safety Training") + hero_solo(
    "Crew-Level Safety Course",
    "Excavation, Trenching &amp; Shoring Safety Training",
    "A 3-hour, OSHA-aligned course for anyone who works in or around excavations and trenches - hazard recognition, soil and protective system basics, and safe work practices.",
    cta_href="#enroll",
) + f"""
  <section class="section">
    <div class="container content-prose">
      {course_meta_table(SAFETY_META)}

      <h2>Role &amp; Purpose</h2>
      <p>This course builds hazard awareness for anyone whose job puts them in or around an open excavation or trench. It covers what makes trenching dangerous, how soil type and protective systems reduce that danger, and what to do - and who to notify - when something looks wrong. It is not a Competent Person course; it does not cover soil classification testing, protective system design, or daily inspection duties in depth. For that, see <a href="../competent-person-excavation-trenching-shoring-training/">Competent Person for Excavation, Trenching &amp; Shoring Training</a>.</p>

      <h2>Who Should Take This Course</h2>
      <ul>
        <li>Excavation and trenching crew members</li>
        <li>Equipment operators working near open trenches</li>
        <li>Utility and municipal crews performing ground disturbance work</li>
        <li>Pipeline and underground contractors</li>
        <li>Laborers and general contractors on projects with excavation work</li>
        <li>Anyone entering, working around, or supervising entry-level work near a trench</li>
      </ul>

      <h2>Who Should Not Rely on This Course Alone</h2>
      <ul>
        <li>Anyone being designated the site's Competent Person - take <a href="../competent-person-excavation-trenching-shoring-training/">Competent Person training</a> instead</li>
        <li>Anyone responsible for soil classification, protective system selection, or daily excavation inspections</li>
        <li>Anyone expecting this course to satisfy a requirement for an OSHA 10-Hour or 30-Hour Outreach card - those are separate programs; see <a href="../credential-transparency/">Credential Transparency</a></li>
      </ul>

      <h2>Learning Objectives</h2>
      <ul>
        <li>Recognize cave-in, engulfment, fall, water accumulation, and hazardous atmosphere risks around excavations</li>
        <li>Describe the structure of OSHA's excavation standard, 29 CFR 1926 Subpart P</li>
        <li>Explain the basics of soil classification and how it drives protective system choice</li>
        <li>Identify safe access, egress, and spoil pile placement requirements</li>
        <li>Understand call-before-you-dig practices and underground utility hazards</li>
        <li>Know when to stop work and notify the Competent Person</li>
      </ul>

      <h2>Full Curriculum</h2>
      <ol class="step-list">
        <li><strong>Understanding Excavation Hazards</strong> - cave-ins, engulfment, falls, water accumulation, and hazardous atmospheres common to open trenches.</li>
        <li><strong>OSHA Subpart P Overview</strong> - the structure of the excavation standard and where crew-level duties come from.</li>
        <li><strong>Soil &amp; Protective Systems Basics</strong> - how soil type drives the choice between sloping, benching, shielding, and shoring.</li>
        <li><strong>Safe Access, Egress &amp; Spoil Placement</strong> - ladder and ramp requirements, spoil pile setback, and safe distances from the edge.</li>
        <li><strong>Utility Location &amp; Emergency Awareness</strong> - call-before-you-dig practices, underground utility hazards, and when to stop work and notify the Competent Person.</li>
      </ol>

      <h2>Knowledge Check &amp; Exam Details</h2>
      <p>The course includes knowledge checks throughout and a final assessment. A passing score is required to receive a certificate of completion. If a student does not pass on the first attempt, a retake is available; contact HAZWOPER OSHA Training support at <a href="tel:18664296742">1-866-429-6742</a> for the current passing-score threshold and retake process for your enrollment.</p>

      <h2>Sample Certificate</h2>
      <p>Below is a redacted sample. It illustrates the certificate format only - it is not a real certificate and does not represent OSHA issuance.</p>
      {sample_cert("Excavation, Trenching &amp; Shoring Safety Training", "3 Hours")}

      <h2>Employer Responsibility</h2>
      <div class="callout-box">
        <p>This course supports OSHA compliance but does not replace it. Employers remain responsible for site-specific hazard assessment, protective system selection, daily inspections, and ensuring each worker is trained, qualified, authorized, and competent for the excavation duties and jobsite conditions they'll actually encounter.</p>
      </div>

      <h2>Policies</h2>
      <p>See our <a href="../refund-policy/">Refund Policy</a> and <a href="../certificate-policy/">Certificate Policy</a> for cancellation terms and certificate handling.</p>

      <h2>Also Available Through HAZWOPER OSHA Training</h2>
      <p>SCORM packages for company LMS platforms, Virtual Instructor-Led sessions, and In-Person Group training for this course are available directly through HAZWOPER OSHA Training. See <a href="../index.html#accreditations">Certifications &amp; Accreditations</a> for provider credentials.</p>
      <p><a href="https://hazwoper-osha.com/online-courses/osha-excavation-trenching-and-shoring-safety-training" target="_blank" rel="noopener" class="btn btn-outline">View This Course on HAZWOPER-OSHA.com &rarr;</a></p>
    </div>
  </section>

  <section class="section pricing-section" id="enroll">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Enroll</p>
        <h2>Excavation, Trenching &amp; Shoring Safety Training</h2>
      </div>
      <div class="pricing-grid" style="max-width:520px;">
        <div class="pricing-card is-visible">
          <div class="pricing-card-top">
            <h3>Excavation, Trenching &amp; Shoring Safety Training</h3>
            <div class="price"><span class="price-current"><span class="price-amount">$59.99</span><span class="price-per">/ seat</span></span></div>
          </div>
          <ul class="pricing-features">
            <li>3 hours of self-paced online training</li>
            <li>Available in English and Spanish</li>
            <li>Certificate of completion, valid 36 months</li>
            <li>Aligned with 29 CFR 1926 Subpart P</li>
          </ul>
          <a href="../index.html#pricing" class="btn btn-primary btn-block btn-lg">Enroll Now</a>
        </div>
      </div>
    </div>
  </section>"""

SAFETY_SCHEMA = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Excavation, Trenching & Shoring Safety Training",
  "description": "Crew-level hazard-awareness course covering cave-in, atmospheric, and utility-strike hazards, soil classification and protective system basics, and safe access, egress, and spoil pile placement, aligned with OSHA 29 CFR 1926 Subpart P.",
  "provider": {"@type": "Organization", "name": "HAZWOPER OSHA Training, LLC", "sameAs": "https://hazwoper-osha.com/"},
  "url": "https://excavationtrenchingshoring.com/excavation-trenching-shoring-safety-training/",
  "timeRequired": "PT3H",
  "inLanguage": ["en", "es"],
  "educationalCredentialAwarded": "Certificate of Completion",
  "teaches": "Excavation and trenching hazard recognition, soil and protective system basics, safe access/egress, and underground utility awareness",
  "occupationalCategory": "Construction and Extraction Occupations",
  "hasCourseInstance": {
    "@type": "CourseInstance",
    "courseMode": "online",
    "courseWorkload": "PT3H"
  },
  "offers": {"@type": "Offer", "price": 59.99, "priceCurrency": "USD", "url": "https://excavationtrenchingshoring.com/excavation-trenching-shoring-safety-training/"}
}
</script>""" + breadcrumb_schema("Excavation, Trenching & Shoring Safety Training", "/excavation-trenching-shoring-safety-training/")

PAGES.append({
    "slug": "excavation-trenching-shoring-safety-training",
    "active": "courses",
    "title": "Excavation, Trenching & Shoring Safety Training | 3-Hour Online Course",
    "description": "3-hour, OSHA-aligned crew-level excavation safety course. Certificate of completion, English & Spanish, $59.99/seat.",
    "body": SAFETY_BODY,
    "extra_schema": SAFETY_SCHEMA,
})

# ---------------------------------------------------------------------------
# COURSE PAGE 2: COMPETENT PERSON FOR EXCAVATION, TRENCHING & SHORING
# ---------------------------------------------------------------------------

COMPETENT_META = [
    ("Duration", "8 hours, self-paced"),
    ("Price", "$159.99 per seat"),
    ("Format", "On-demand online (SCORM, Virtual Instructor-Led, and In-Person Group available through HAZWOPER OSHA Training)"),
    ("Languages", "English and Spanish"),
    ("Device Compatibility", "Desktop, laptop, tablet, and mobile browsers"),
    ("Certificate Issued", "Certificate of completion, immediately on passing"),
    ("Certificate Validity", "24 months, before a refresher is recommended"),
    ("CEUs", "Not issued per-course. HAZWOPER OSHA Training is IACET Accredited at the organizational level - see <a href=\"../credential-transparency/\">Credential Transparency</a>."),
    ("OSHA Standard Covered", "29 CFR 1926 Subpart P, Excavations"),
]

COMPETENT_BODY = breadcrumb_nav("Competent Person for Excavation, Trenching &amp; Shoring Training") + hero_solo(
    "Advanced / Program Oversight",
    "Competent Person for Excavation, Trenching &amp; Shoring Training",
    "An 8-hour, OSHA-aligned course for the person responsible for soil classification, protective system selection, daily inspections, and overall excavation program oversight.",
    cta_href="#enroll",
) + f"""
  <section class="section">
    <div class="container content-prose">
      <div class="callout-box">
        <p>OSHA defines a competent person as someone capable of identifying existing and predictable hazards and authorized to take prompt corrective measures. Training supports this role, but the employer must designate the competent person and ensure they have the knowledge, authority, and site-specific understanding needed for the excavation work being performed. Completing this course is a foundational step, not an automatic designation.</p>
      </div>

      {course_meta_table(COMPETENT_META)}

      <h2>Role &amp; Purpose</h2>
      <p>This course prepares the individual an employer intends to designate as a site's excavation Competent Person: classifying soil, selecting and verifying protective systems, running daily inspections, and building the site's written excavation safety program. If your role is limited to working in or around a trench without these oversight duties, see <a href="../excavation-trenching-shoring-safety-training/">Excavation, Trenching &amp; Shoring Safety Training</a> instead.</p>

      <h2>Who Should Take This Course</h2>
      <ul>
        <li>Individuals an employer intends to designate as Competent Person for excavation work</li>
        <li>Safety managers, foremen, and site supervisors overseeing daily trench inspections</li>
        <li>EHS coordinators and compliance staff assessing excavation risk</li>
        <li>Construction engineers and project managers overseeing protective system installation</li>
        <li>Contractors and subcontractors on projects involving excavation, trenching, utility installation, shoring, or site preparation</li>
      </ul>

      <h2>Who Should Not Rely on This Course Alone</h2>
      <ul>
        <li>Workers who only need crew-level hazard awareness - see <a href="../excavation-trenching-shoring-safety-training/">Excavation, Trenching &amp; Shoring Safety Training</a> (lower cost, shorter, matched to that role)</li>
        <li>Anyone expecting this course alone to satisfy engineering-design requirements for excavations 20 feet or deeper, which require a registered professional engineer - see <a href="../excavation-protective-systems/">Protective Systems</a></li>
        <li>Anyone whose employer has not yet formally designated them as Competent Person - training builds knowledge, but designation and site-specific authority come from the employer</li>
      </ul>

      <h2>Learning Objectives</h2>
      <ul>
        <li>Define the Competent Person's authority and responsibility under 29 CFR 1926 Subpart P</li>
        <li>Classify Stable Rock, Type A, Type B, and Type C soils using visual and manual analysis tests</li>
        <li>Select and size sloping, benching, shielding, and shoring systems for site conditions</li>
        <li>Conduct required daily inspections and document findings</li>
        <li>Build a written excavation safety program and emergency/rescue plan</li>
        <li>Recognize when tabulated data is sufficient and when a registered professional engineer is required</li>
      </ul>

      <h2>Full Curriculum</h2>
      <ol class="step-list">
        <li><strong>Defining the Competent Person Role</strong> - authority and legal responsibility under 29 CFR 1926 Subpart P.</li>
        <li><strong>Soil Classification</strong> - classifying Stable Rock, Type A, Type B, and Type C soils using visual and manual analysis tests.</li>
        <li><strong>Selecting Protective Systems</strong> - choosing and sizing sloping, benching, shielding, and shoring systems for site conditions.</li>
        <li><strong>Daily Inspection Duties</strong> - required inspections before each shift, after rainfall, and whenever conditions change.</li>
        <li><strong>Program Development &amp; Emergency Planning</strong> - building a written excavation safety program and rescue plan that holds up under inspection.</li>
      </ol>

      <h2>Knowledge Check &amp; Exam Details</h2>
      <p>The course includes module knowledge checks and a final assessment covering soil classification, protective system selection, and inspection duties. A passing score is required to receive a certificate of completion. If a student does not pass on the first attempt, a retake is available; contact HAZWOPER OSHA Training support at <a href="tel:18664296742">1-866-429-6742</a> for the current passing-score threshold and retake process for your enrollment.</p>

      <h2>Sample Certificate</h2>
      <p>Below is a redacted sample. It illustrates the certificate format only - it is not a real certificate and does not represent OSHA issuance.</p>
      {sample_cert("Competent Person for Excavation, Trenching &amp; Shoring Training", "8 Hours")}

      <h2>Employer Responsibility</h2>
      <div class="callout-box">
        <p>This course supports OSHA compliance but does not replace it. The employer must designate who serves as Competent Person on each site, confirm that person has the authority to stop work, and ensure site-specific conditions - soil, water, utilities, equipment, and access - are actually evaluated in the field, not assumed from training alone.</p>
      </div>

      <h2>Policies</h2>
      <p>See our <a href="../refund-policy/">Refund Policy</a> and <a href="../certificate-policy/">Certificate Policy</a> for cancellation terms and certificate handling.</p>

      <h2>Also Available Through HAZWOPER OSHA Training</h2>
      <p>SCORM packages for company LMS platforms, Virtual Instructor-Led sessions, and In-Person Group training for this course are available directly through HAZWOPER OSHA Training. See <a href="../index.html#accreditations">Certifications &amp; Accreditations</a> for provider credentials.</p>
      <p><a href="https://hazwoper-osha.com/online-courses/competent-person-for-excavation-trenching-and-shoring" target="_blank" rel="noopener" class="btn btn-outline">View This Course on HAZWOPER-OSHA.com &rarr;</a></p>
    </div>
  </section>

  <section class="section pricing-section" id="enroll">
    <div class="container">
      <div class="section-head">
        <p class="eyebrow">Enroll</p>
        <h2>Competent Person for Excavation, Trenching &amp; Shoring Training</h2>
      </div>
      <div class="pricing-grid" style="max-width:520px;">
        <div class="pricing-card is-visible">
          <div class="pricing-card-top">
            <h3>Competent Person Training</h3>
            <div class="price"><span class="price-current"><span class="price-amount">$159.99</span><span class="price-per">/ seat</span></span></div>
          </div>
          <ul class="pricing-features">
            <li>8 hours of self-paced online training</li>
            <li>Available in English and Spanish</li>
            <li>Certificate of completion, valid 24 months</li>
            <li>Aligned with 29 CFR 1926 Subpart P</li>
          </ul>
          <a href="../index.html#pricing" class="btn btn-primary btn-block btn-lg">Enroll Now</a>
        </div>
      </div>
    </div>
  </section>"""

COMPETENT_SCHEMA = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Competent Person for Excavation, Trenching & Shoring Training",
  "description": "Program-oversight course covering the Competent Person role and authority, soil classification, selecting protective systems, daily inspection duties, and building a written excavation safety program, aligned with OSHA 29 CFR 1926 Subpart P.",
  "provider": {"@type": "Organization", "name": "HAZWOPER OSHA Training, LLC", "sameAs": "https://hazwoper-osha.com/"},
  "url": "https://excavationtrenchingshoring.com/competent-person-excavation-trenching-shoring-training/",
  "timeRequired": "PT8H",
  "inLanguage": ["en", "es"],
  "educationalCredentialAwarded": "Certificate of Completion",
  "teaches": "Soil classification, protective system selection, daily inspection duties, and excavation safety program development",
  "occupationalCategory": "Construction Managers; Occupational Health and Safety Specialists",
  "hasCourseInstance": {
    "@type": "CourseInstance",
    "courseMode": "online",
    "courseWorkload": "PT8H"
  },
  "offers": {"@type": "Offer", "price": 159.99, "priceCurrency": "USD", "url": "https://excavationtrenchingshoring.com/competent-person-excavation-trenching-shoring-training/"}
}
</script>""" + breadcrumb_schema("Competent Person for Excavation, Trenching & Shoring Training", "/competent-person-excavation-trenching-shoring-training/")

PAGES.append({
    "slug": "competent-person-excavation-trenching-shoring-training",
    "active": "courses",
    "title": "Competent Person Excavation Training | 8-Hour Course",
    "description": "8-hour, OSHA-aligned Competent Person course: soil classification, protective systems, daily inspections. $159.99/seat, English & Spanish.",
    "body": COMPETENT_BODY,
    "extra_schema": COMPETENT_SCHEMA,
})

# ---------------------------------------------------------------------------
# WHICH COURSE DO I NEED
# ---------------------------------------------------------------------------

DECISION_ROWS = [
    ("Excavation crew member / laborer", "Digs, works in/around open trenches, handles materials near the excavation", "Excavation, Trenching &amp; Shoring Safety Training", "Hazard recognition, safe access/egress, spoil placement", "Still needs site-specific instruction from the Competent Person"),
    ("Equipment operator", "Operates excavators, backhoes, or trenchers near or over open excavations", "Excavation, Trenching &amp; Shoring Safety Training", "Cave-in hazards, spoil pile placement, utility strikes", "Employer must also cover equipment-specific operating procedures"),
    ("Utility / municipal crew", "Installs or repairs underground utility lines, works in trenches routinely", "Excavation, Trenching &amp; Shoring Safety Training", "Utility location, call-before-you-dig, safe access/egress", "See also our <a href=\"../underground-utility-safety/\">Underground Utility Safety</a> page"),
    ("Foreman / site supervisor", "Oversees daily excavation work, often performs inspections", "Competent Person for Excavation, Trenching &amp; Shoring", "Daily inspections, soil classification, protective systems", "Employer must formally designate supervisor as Competent Person"),
    ("Safety manager / EHS coordinator", "Owns the excavation safety program across sites", "Competent Person for Excavation, Trenching &amp; Shoring", "Program development, protective system selection, emergency planning", "May need to train multiple designated Competent Persons"),
    ("Soil classification personnel", "Performs visual/manual soil tests before protective system selection", "Competent Person for Excavation, Trenching &amp; Shoring", "Stable Rock/Type A/B/C classification, testing methods", "See also our <a href=\"../soil-classification-training/\">Soil Classification</a> page"),
    ("Protective system selector / evaluator", "Chooses sloping, benching, shoring, or shielding for site conditions", "Competent Person for Excavation, Trenching &amp; Shoring", "Tabulated data, sloping/benching limits, shoring/shielding", "Engineering-designed systems (20 ft+) still require a Registered PE"),
    ("Contractor with mixed crews", "Needs both hands-on crew and designated program oversight", "Both courses, by role", "Full Subpart P coverage across the team", "Enroll crew in Safety Training, supervisors in Competent Person"),
]

def decision_table():
    trs = "\n        ".join(
        f'<tr><td>{role}</td><td>{duties}</td><td class="rec">{course}</td><td>{topics}</td><td>{notes}</td></tr>'
        for role, duties, course, topics, notes in DECISION_ROWS
    )
    return f"""<div class="data-table-wrap"><table class="data-table decision-table">
      <thead><tr><th>Job Role</th><th>Typical Duties</th><th>Recommended Course</th><th>OSHA Topics Covered</th><th>Employer Notes</th></tr></thead>
      <tbody>
        {trs}
      </tbody>
    </table></div>"""

PAGES.append({
    "slug": "which-excavation-course-do-i-need",
    "active": "which-course",
    "title": "Which Excavation Course Do I Need? | Course Decision Guide",
    "description": "Not sure which excavation course you need? Answer one question or use our role-by-role comparison table to find out.",
    "body": breadcrumb_nav("Which Course Do I Need?") + hero_solo(
        "Decision Guide",
        "Which Excavation Course Do I Need?",
        "Answer one question below, or use the full role-by-role comparison table to match your job to the right course.",
        cta_href="#comparison",
        cta_label="Jump to Comparison Table",
    ) + f"""
  <section class="section">
    <div class="container">
      {course_picker_widget(full=True)}
    </div>
  </section>

  <section class="section section-alt" id="comparison">
    <div class="container content-prose">
      <h2>Full Role-by-Role Comparison</h2>
      <p>Use the table below if your role isn't a clean fit for the quick picker above, or if you're planning training for a mixed team.</p>
      {decision_table()}

      <h2>Decision Logic, Summarized</h2>
      <ul>
        <li>If the worker operates near trenches or excavations: <strong>Excavation, Trenching &amp; Shoring Safety Training</strong></li>
        <li>If the worker enters or works around trenches: <strong>Excavation, Trenching &amp; Shoring Safety Training</strong></li>
        <li>If the person performs daily inspections: <strong>Competent Person Training</strong></li>
        <li>If the person classifies soil: <strong>Competent Person Training</strong></li>
        <li>If the person selects or evaluates protective systems: <strong>Competent Person Training</strong></li>
        <li>If the person supervises excavation work: <strong>Competent Person Training</strong></li>
        <li>If the company needs both crew and supervisor coverage: <strong>enroll each role in its matching course</strong></li>
      </ul>

      <div class="disclaimer-box">
        This guide is a starting point, not a substitute for the employer's own hazard assessment. OSHA requires training appropriate to each worker's assigned duties; when in doubt, the more advanced course is the safer choice. See <a href="../credential-transparency/">Credential Transparency</a> for what a completed course does and does not establish about Competent Person authority.
      </div>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Which Course Do I Need?", "/which-excavation-course-do-i-need/"),
})

# ---------------------------------------------------------------------------
# PROTECTIVE SYSTEMS
# ---------------------------------------------------------------------------

PAGES.append({
    "slug": "excavation-protective-systems",
    "active": None,
    "title": "Excavation Protective Systems Explained",
    "description": "Plain-language guide to sloping, benching, shoring, shielding, trench boxes, tabulated data, and when a Registered Professional Engineer is required.",
    "body": breadcrumb_nav("Protective Systems") + hero_solo(
        "Protective Systems",
        "Excavation Protective Systems Explained",
        "Sloping, benching, shoring, shielding, tabulated data, and when a Registered Professional Engineer's design is required - and where online training's role ends.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <p>OSHA's excavation standard requires a protective system for excavations 5 feet or deeper, unless the excavation is entirely in stable rock or a Competent Person determines no hazard exists. There are two broad approaches: reshaping the excavation itself (sloping, benching) or adding a support/containment structure (shoring, shielding).</p>

      <h2>Sloping</h2>
      <p>Cutting the trench wall back at an angle away from the excavation instead of keeping it vertical. The maximum allowable slope depends on soil type - Type A soil allows a steeper slope than Type C. Sloping needs enough lateral space on site, which many urban or congested jobs don't have.</p>

      <h2>Benching</h2>
      <p>Cutting the wall into a series of horizontal steps rather than one continuous slope. Allowable bench dimensions depend on soil type, and benching is not permitted in Type C soil.</p>

      <h2>Shoring</h2>
      <p>A support system installed to prevent trench walls from collapsing.</p>
      <div class="two-col-cards">
        <div class="mini-card">
          <h3>Aluminum Hydraulic Shoring</h3>
          <p>Aluminum or steel supports under hydraulic pressure. The most common modern method - fast to install and typically doesn't require workers to enter the trench to place it.</p>
        </div>
        <div class="mini-card">
          <h3>Timber Shoring</h3>
          <p>Wood supports, still used in certain conditions, particularly deep or irregular excavations. See OSHA Appendix C for tabulated timber shoring configurations.</p>
        </div>
      </div>

      <h2>Shielding &amp; Trench Boxes</h2>
      <p>A trench shield (trench box) doesn't prevent a cave-in the way shoring does - it protects workers by containing the collapse if one occurs. Shields are typically steel or aluminum structures workers perform their work inside of, and unlike shoring, they can often be pulled along the trench as work progresses.</p>

      <h2>Manufacturer Tabulated Data</h2>
      <p>Most protective systems are designed using tabulated data supplied by the manufacturer of the shoring or shielding equipment, spelling out safe configurations for given soil types and depths. This is the standard approach for the vast majority of trenches.</p>

      <h2>When a Registered Professional Engineer Is Required</h2>
      <div class="callout-box callout-warning">
        <p>A protective system designed by a registered professional engineer is required for excavations 20 feet or deeper, or for non-standard conditions that manufacturer tabulated data doesn't cover. This is a hard line in the standard - tabulated data and training knowledge are not substitutes for an engineer's design once that threshold applies.</p>
      </div>

      <h2>The Limits of Online Training for Protective System Design</h2>
      <div class="disclaimer-box">
        Online training does not replace site-specific engineering review, manufacturer instructions, tabulated data, or Registered Professional Engineer design where required by OSHA. Our Competent Person course teaches how to select and size standard protective systems from tabulated data - it does not qualify a student as a Registered Professional Engineer, and it cannot account for every site-specific condition an actual excavation will present.
      </div>

      <p>See also: <a href="../soil-classification-training/">Soil Classification</a>, which determines which protective systems and slope angles are allowed, and <a href="../osha-excavation-standards/">OSHA Excavation Standards</a> for the official 1926.652 text and Appendices B and C.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Protective Systems", "/excavation-protective-systems/"),
})

# ---------------------------------------------------------------------------
# SOIL CLASSIFICATION
# ---------------------------------------------------------------------------

PAGES.append({
    "slug": "soil-classification-training",
    "active": None,
    "title": "Soil Classification Training for Excavations",
    "description": "How OSHA's soil classification system works: Stable Rock, Types A-C, visual and manual tests, and water/vibration effects on stability.",
    "body": breadcrumb_nav("Soil Classification") + hero_solo(
        "Soil Classification",
        "Soil Classification for Excavations",
        "How OSHA's four-category soil classification system works, and how a Competent Person determines which one applies on site.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <p>Soil classification is the foundation of excavation safety planning - it determines which protective systems are allowed and at what slope angles. OSHA classifies soil into four categories, from most to least stable.</p>

      <div class="data-table-wrap">
        <table class="data-table">
          <thead><tr><th>Classification</th><th>Description</th></tr></thead>
          <tbody>
            <tr><td><strong>Stable Rock</strong></td><td>Solid mineral material that can be excavated with vertical sides and remain intact while exposed.</td></tr>
            <tr><td><strong>Type A</strong></td><td>The most stable soil type, such as clay, silty clay, or clay loam, with an unconfined compressive strength of 1.5 tons per square foot (tsf) or greater. Never classified as Type A if fissured, previously disturbed, subject to vibration, or if water is seeping through it.</td></tr>
            <tr><td><strong>Type B</strong></td><td>Moderately stable soil, such as silt, sandy loam, or unstable dry rock, with an unconfined compressive strength between 0.5 and 1.5 tsf.</td></tr>
            <tr><td><strong>Type C</strong></td><td>The least stable soil, including granular soils (gravel, sand, loamy sand), submerged soil, soil with seeping water, or previously disturbed soil, with an unconfined compressive strength of 0.5 tsf or less.</td></tr>
          </tbody>
        </table>
      </div>

      <h2>Visual Tests</h2>
      <p>Observing the soil and excavation for signs of instability: fissures, layered soil types, water seepage, previously disturbed ground, spoil pile placement, and vibration sources nearby (traffic, equipment).</p>

      <h2>Manual Tests</h2>
      <p>At least one manual analysis test is required, such as a plasticity (thread) test, dry strength test, thumb penetration test, or pocket penetrometer reading, to confirm the soil's unconfined compressive strength.</p>

      <h2>Water &amp; Vibration Impacts</h2>
      <p>Water seepage and vibration (from traffic, equipment, or nearby construction) both reduce soil stability and can downgrade a classification - soil that would otherwise test as Type A cannot be classified that way if water is seeping through it or it's subject to vibration.</p>

      <h2>Layered Soil Systems</h2>
      <p>Where a trench exposes more than one soil type in layers, OSHA requires the excavation to be classified based on the least stable layer present, unless each layer is classified and protected individually.</p>

      <h2>Competent Person Responsibility</h2>
      <div class="callout-box">
        <p>Soil classification must be performed by a competent person based on actual site conditions. Training provides the knowledge framework, but field conditions must be evaluated on site - classroom or online instruction cannot substitute for physically testing the soil in the trench being dug.</p>
      </div>

      <p>Official reference: <a href="https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.652" target="_blank" rel="noopener">OSHA 1926.652, Appendix A - Soil Classification &rarr;</a></p>
      <p>See also: <a href="../excavation-protective-systems/">Protective Systems</a>, which explains how classification determines which sloping, benching, or shoring options are allowed.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Soil Classification", "/soil-classification-training/"),
})

# ---------------------------------------------------------------------------
# UNDERGROUND UTILITY SAFETY
# ---------------------------------------------------------------------------

PAGES.append({
    "slug": "underground-utility-safety",
    "active": None,
    "title": "Underground Utility Safety & Call-Before-You-Dig | Excavation Training",
    "description": "811 / call-before-you-dig practices, utility line hazards, employer coordination duties, and OSHA 1926.651(b) requirements.",
    "body": breadcrumb_nav("Underground Utility Safety") + hero_solo(
        "Underground Utilities",
        "Underground Utility Safety &amp; Call-Before-You-Dig",
        "Utility locating, 811 practices, and the OSHA requirements that make locating a legal obligation, not just a good idea.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <h2>811 / Call-Before-You-Dig</h2>
      <p>Calling 811 (or a local one-call utility locate service) before digging is a nationwide practice that notifies utility owners to mark buried lines before excavation begins. It's required in every state, typically several business days before work starts. It is a separate obligation from OSHA's excavation safety requirements around soil classification, protective systems, and daily inspections - both are required; one doesn't substitute for the other.</p>

      <h2>Utility Types &amp; Their Hazards</h2>
      <div class="two-col-cards">
        <div class="mini-card"><h3>Electric</h3><p>Contact or arc-flash risk from energized lines; requires de-energization or safe clearance distances before digging nearby.</p></div>
        <div class="mini-card"><h3>Gas</h3><p>Strike risk creates fire/explosion hazard and can release hazardous atmospheres into the excavation.</p></div>
        <div class="mini-card"><h3>Water</h3><p>Strikes can flood the excavation rapidly, destabilizing soil and creating engulfment/drowning risk.</p></div>
        <div class="mini-card"><h3>Sewer</h3><p>Strikes create hazardous atmosphere exposure (H2S, methane) and contamination risk.</p></div>
        <div class="mini-card"><h3>Telecom</h3><p>Lower direct injury risk but strikes cause costly outages and site disruption.</p></div>
        <div class="mini-card"><h3>Fuel Lines</h3><p>Fire/explosion risk similar to gas; requires the same locate-and-clear-distance discipline.</p></div>
      </div>

      <h2>Employer Coordination Duties</h2>
      <p>Employers are responsible for coordinating utility locate requests with the timeline of the actual dig, confirming markings are current before work begins, using safe excavation practices (hand digging or vacuum excavation) within utility tolerance zones, and re-verifying locates if work is delayed past the marking's validity window.</p>

      <h2>OSHA 1926.651(b) Requirements</h2>
      <p>OSHA 1926.651(b) requires employers to determine the estimated location of utility installations before opening an excavation, contact utility companies or owners to establish exact locations, and (when excavation approaches the estimated location) determine the exact location by safe means, such as hand digging, while the excavation is open.</p>
      <p><a href="https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.651" target="_blank" rel="noopener">Read 1926.651 on osha.gov &rarr;</a></p>

      <h2>Stop-Work Authority</h2>
      <div class="callout-box callout-warning">
        <p>Any worker who strikes, exposes, or suspects an undocumented utility line should stop work immediately and notify the Competent Person, regardless of role or seniority. Continuing to dig near a suspected strike - especially gas, electric, or fuel lines - is one of the most dangerous decisions on an excavation site.</p>
      </div>

      <p>This topic is covered at the awareness level in <a href="../excavation-trenching-shoring-safety-training/">Excavation, Trenching &amp; Shoring Safety Training</a> and at the program-oversight level in <a href="../competent-person-excavation-trenching-shoring-training/">Competent Person Training</a>.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Underground Utility Safety", "/underground-utility-safety/"),
})

# ---------------------------------------------------------------------------
# EMERGENCY PLANNING
# ---------------------------------------------------------------------------

PAGES.append({
    "slug": "excavation-emergency-planning",
    "active": None,
    "title": "Excavation Emergency & Rescue Planning | Cave-In Response",
    "description": "Cave-in response, rescue planning, water accumulation, and hazardous atmospheres. Why online training alone doesn't make a rescue specialist.",
    "body": breadcrumb_nav("Emergency Planning") + hero_solo(
        "Emergency Planning",
        "Excavation Emergency &amp; Rescue Planning",
        "What a site needs to be ready for a cave-in, water accumulation, or hazardous atmosphere - and why training alone isn't readiness.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <h2>Cave-In Response</h2>
      <p>A cave-in can bury a worker in seconds, and a cubic yard of soil can weigh well over a ton. If a cave-in occurs, the immediate priorities are: call 911 and site emergency services, do not enter the trench, shut down nearby equipment and vibration sources to prevent a secondary collapse, and account for all workers who were in or near the excavation.</p>

      <div class="callout-box callout-warning">
        <p><strong>Why workers should not rush into an unprotected trench:</strong> A second cave-in during a rescue attempt is a leading cause of multiple-fatality excavation incidents. An untrained, unequipped rescuer entering a collapsed or unstable trench is at the same risk the first worker faced - and now there are two victims instead of one.</p>
      </div>

      <h2>Rescue Planning</h2>
      <p>An excavation rescue plan should be established before work begins, not improvised during an emergency. It typically includes: designated emergency contacts and notification procedures, on-site or on-call trench rescue resources, shoring/shielding equipment available for a controlled rescue approach, and a clear chain of authority for who calls the rescue versus who calls off unsafe rescue attempts.</p>

      <h2>Water Accumulation</h2>
      <p>Workers should not be permitted to work in an excavation with accumulating water unless precautions have been taken - special support systems, water removal to control the level, or a safety harness and lifeline. Water dramatically increases cave-in risk by destabilizing surrounding soil, and can also create rapid engulfment or drowning hazards.</p>

      <h2>Hazardous Atmospheres</h2>
      <p>Excavations deeper than 4 feet, near landfills, sewers, or areas with known gas sources require atmospheric testing whenever there's a reasonable possibility of oxygen deficiency or a hazardous atmosphere. The Competent Person must test and provide ventilation or respiratory protection as needed before entry, and some trenches also meet the definition of a confined space, requiring both sets of precautions.</p>

      <h2>Emergency Access</h2>
      <p>Emergency responders need a clear, marked path to the excavation, free of parked equipment, spoil piles, or material staging. Access requirements (ladders, ramps, stairways) that serve routine work also need to support emergency evacuation without becoming a bottleneck.</p>

      <h2>Rescue Limitations &amp; Employer Responsibilities</h2>
      <div class="disclaimer-box">
        Completing online training does not by itself qualify a worker as an excavation rescue specialist. Emergency readiness depends on employer procedures, equipment, coordination, practice, and site-specific hazards. Confined space and trench rescue typically require specialized hands-on training, dedicated equipment (tripods, harnesses, atmospheric monitors, shoring for rescue access), and practiced drills - none of which an online course can provide on its own.
      </div>

      <p>See also: <a href="../underground-utility-safety/">Underground Utility Safety</a> for utility-strike emergency response, and <a href="../excavation-protective-systems/">Protective Systems</a> for the systems that prevent the collapse in the first place.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Emergency Planning", "/excavation-emergency-planning/"),
})

# ---------------------------------------------------------------------------
# STATE OSHA PLAN REQUIREMENTS
# ---------------------------------------------------------------------------

PAGES.append({
    "slug": "state-osha-plan-requirements",
    "active": None,
    "title": "State OSHA Plan Requirements for Excavation & Trenching",
    "description": "Federal OSHA vs. OSHA-approved State Plans for excavation and trenching requirements, and where this training is designed around.",
    "body": breadcrumb_nav("State OSHA Plan Requirements") + hero_solo(
        "State Plans",
        "State OSHA Plan Requirements",
        "Federal OSHA covers most states directly, but OSHA-approved State Plans can add requirements on top. Here's how to tell which applies to you.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <h2>Federal OSHA Applies in Most States</h2>
      <p>Federal OSHA enforces 29 CFR 1926 Subpart P directly in most states. This site's excavation and Competent Person courses are designed around these federal standards unless otherwise stated.</p>

      <h2>OSHA-Approved State Plans May Differ</h2>
      <p>Roughly half the states, plus a few territories, operate their own OSHA-approved State Plan, run by a state agency instead of federal OSHA. State Plans are required to be at least as effective as federal OSHA standards, and many add requirements on top - different training documentation, additional protective-system rules, or state-specific reporting.</p>

      <h2>What Employers Should Check</h2>
      <ul>
        <li>Whether your state operates its own OSHA-approved State Plan or falls under federal OSHA</li>
        <li>Whether your state plan has excavation-specific requirements beyond 29 CFR 1926 Subpart P</li>
        <li>Whether your state plan requires additional documentation, permits, or state-specific training elements</li>
        <li>Your state's occupational safety agency contact for confirming current requirements</li>
      </ul>

      <div class="callout-box">
        <p>This course is designed around federal OSHA standards unless otherwise stated. If you're in an OSHA-approved State Plan state, confirm any additional or different requirements with your state's occupational safety agency before relying on this training as your sole compliance documentation.</p>
      </div>

      <p>Official reference: <a href="https://www.osha.gov/stateplans" target="_blank" rel="noopener">OSHA State Plans directory &rarr;</a> - find your state's plan (if any) and its administering agency.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("State OSHA Plan Requirements", "/state-osha-plan-requirements/"),
})

# ---------------------------------------------------------------------------
# COMPARISON / SEO LANDING PAGES
# ---------------------------------------------------------------------------

PAGES.append({
    "slug": "excavation-safety-vs-competent-person-training",
    "active": None,
    "title": "Excavation Safety vs. Competent Person Training",
    "description": "How Excavation Safety Training differs from Competent Person training: scope, audience, duration, cost, and what each authorizes.",
    "body": breadcrumb_nav("Safety vs. Competent Person Training") + hero_solo(
        "Course Comparison",
        "Excavation Safety Training vs. Competent Person Training",
        "Two courses, two different jobs. Here's exactly how they differ, and why one doesn't substitute for the other.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <p>These two courses are often confused because they cover the same standard - OSHA 29 CFR 1926 Subpart P - but they're built for different jobs, and neither substitutes for the other.</p>

      <div class="data-table-wrap">
        <table class="data-table">
          <thead><tr><th></th><th>Excavation, Trenching &amp; Shoring Safety Training</th><th>Competent Person Training</th></tr></thead>
          <tbody>
            <tr><td>Scope</td><td>Hazard awareness &amp; safe work practices</td><td>Program oversight, inspections &amp; protective system selection</td></tr>
            <tr><td>Duration</td><td>3 hours</td><td>8 hours</td></tr>
            <tr><td>Price</td><td>$59.99</td><td>$159.99</td></tr>
            <tr><td>Soil classification</td><td>Basics only</td><td>Full visual/manual test methods</td></tr>
            <tr><td>Protective system selection</td><td>Not covered</td><td>Sloping, benching, shoring, shielding selection</td></tr>
            <tr><td>Daily inspections</td><td>Not covered</td><td>Full inspection duties &amp; documentation</td></tr>
            <tr><td>Authorizes Competent Person designation?</td><td>No</td><td>No - supports it, but the employer must designate</td></tr>
            <tr><td>Certificate validity</td><td>36 months</td><td>24 months</td></tr>
          </tbody>
        </table>
      </div>

      <h2>The Core Difference</h2>
      <p>Safety Training answers "how do I work safely around this trench?" Competent Person Training answers "how do I decide whether this trench is safe, and what do I do if it isn't?" A crew member who only needs the first question answered doesn't need the depth - or the price - of the second course.</p>

      <h2>Neither Course Alone Makes Someone a Competent Person</h2>
      <p>OSHA defines a Competent Person as someone capable of identifying existing and predictable hazards and authorized to take prompt corrective measures. That authorization comes from the employer, not from finishing a course. See <a href="../credential-transparency/">Credential Transparency</a> for the full explanation.</p>

      <p>Still not sure which one fits your team? Use our <a href="../which-excavation-course-do-i-need/">full decision guide</a>.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Safety vs. Competent Person Training", "/excavation-safety-vs-competent-person-training/"),
})

PAGES.append({
    "slug": "trenching-vs-excavation-training",
    "active": None,
    "title": "Trenching vs. Excavation Training | What's the Difference?",
    "description": "Every trench is an excavation, but not every excavation is a trench. Here's the OSHA distinction and why it matters for training.",
    "body": breadcrumb_nav("Trenching vs. Excavation") + hero_solo(
        "Terminology Guide",
        "Trenching vs. Excavation: What's the Difference?",
        "Every trench is an excavation, but not every excavation is a trench - and the distinction matters more than it sounds.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <h2>The OSHA Definitions</h2>
      <p>OSHA defines an <strong>excavation</strong> as any man-made cut, cavity, trench, or depression in the earth's surface formed by removing soil. A <strong>trench</strong> is a specific type of excavation: narrow in relation to its depth, generally no wider than 15 feet at the bottom, with depth usually greater than width.</p>
      <p>In other words, every trench is an excavation, but broader excavations - building foundations, basements, large utility vaults - follow the same 29 CFR 1926 Subpart P standard without technically being "trenches."</p>

      <h2>Why the Distinction Matters</h2>
      <p>Trenches concentrate cave-in risk differently than wide excavations because of their narrow geometry - a worker inside has less room to escape a collapsing wall, and the walls themselves are often less self-supporting relative to their height. That's part of why trenching is consistently one of OSHA's most-cited and most fatal construction hazards. Training content, protective system selection, and access/egress requirements all apply to both, but trenching scenarios get particular emphasis because of that elevated risk profile.</p>

      <h2>Both Courses on This Site Cover Both</h2>
      <p>Excavation, Trenching &amp; Shoring Safety Training and Competent Person for Excavation, Trenching &amp; Shoring Training both use "excavation" and "trenching" in their titles deliberately - the curriculum covers the full Subpart P standard, with trenching-specific hazards (like the 15-foot width threshold and narrow-space cave-in dynamics) called out explicitly.</p>

      <p>See our <a href="../osha-excavation-standards/">OSHA Excavation Standards</a> page for the official definitions in 1926.650, or our <a href="../which-excavation-course-do-i-need/">course decision guide</a> to find the right training for your role.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Trenching vs. Excavation", "/trenching-vs-excavation-training/"),
})

PAGES.append({
    "slug": "sloping-benching-shoring-shielding-explained",
    "active": None,
    "title": "Sloping vs. Benching vs. Shoring vs. Shielding",
    "description": "The four main excavation protective system approaches, side by side, with when each is used and its main limitations.",
    "body": breadcrumb_nav("Sloping, Benching, Shoring & Shielding") + hero_solo(
        "Protective Systems Comparison",
        "Sloping vs. Benching vs. Shoring vs. Shielding",
        "Four different ways to protect workers from a cave-in, side by side.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <div class="data-table-wrap">
        <table class="data-table">
          <thead><tr><th>System</th><th>How It Works</th><th>Best For</th><th>Main Limitation</th></tr></thead>
          <tbody>
            <tr><td><strong>Sloping</strong></td><td>Cuts the wall back at an angle</td><td>Sites with room to expand the excavation footprint</td><td>Needs lateral space many urban sites don't have</td></tr>
            <tr><td><strong>Benching</strong></td><td>Cuts the wall into horizontal steps</td><td>Similar to sloping, more compact footprint</td><td>Not permitted in Type C soil</td></tr>
            <tr><td><strong>Shoring</strong></td><td>Support structure (hydraulic or timber) holds the wall in place</td><td>Confined sites without room to slope or bench</td><td>Requires correct tabulated data for soil/depth</td></tr>
            <tr><td><strong>Shielding (trench box)</strong></td><td>Protects workers by containing a collapse, doesn't prevent it</td><td>Utility work where the box can be pulled along the trench</td><td>Doesn't stabilize the surrounding soil itself</td></tr>
          </tbody>
        </table>
      </div>

      <h2>They're Not Interchangeable</h2>
      <p>Soil type, trench depth, available space, and the nature of the work all determine which system (or combination) is appropriate. A Competent Person makes this call using tabulated data for standard conditions, or a registered professional engineer's design for excavations 20 feet or deeper or non-standard conditions.</p>

      <p>For the full breakdown, including OSHA Appendix B and C references, see our <a href="../excavation-protective-systems/">Protective Systems page</a>. For how soil type drives this decision, see <a href="../soil-classification-training/">Soil Classification</a>.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Sloping, Benching, Shoring & Shielding", "/sloping-benching-shoring-shielding-explained/"),
})

PAGES.append({
    "slug": "osha-subpart-p-training-guide",
    "active": None,
    "title": "OSHA Subpart P Training Guide | 29 CFR 1926 Subpart P for Employers",
    "description": "A practical guide to training your workforce to OSHA 29 CFR 1926 Subpart P: what the standard requires, who needs what training, and how to document it.",
    "body": breadcrumb_nav("Subpart P Training Guide") + hero_solo(
        "Employer Guide",
        "OSHA Subpart P Training Guide",
        "A practical, employer-focused walkthrough of what 29 CFR 1926 Subpart P requires and how training fits into meeting it.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <h2>What Subpart P Requires, in Practice</h2>
      <ol class="step-list">
        <li><strong>Designate a Competent Person</strong> for every excavation site - someone capable of identifying hazards and authorized to take corrective action, including stopping work.</li>
        <li><strong>Classify the soil</strong> using visual and manual tests before selecting a protective system.</li>
        <li><strong>Select a protective system</strong> (sloping, benching, shoring, or shielding) appropriate to the soil type and depth, using tabulated data or, for 20+ foot excavations, a registered professional engineer's design.</li>
        <li><strong>Provide safe access and egress</strong> for excavations 4 feet or deeper, and keep spoil piles and equipment at least 2 feet from the edge.</li>
        <li><strong>Test for hazardous atmospheres</strong> where there's a reasonable possibility of oxygen deficiency or hazardous gas.</li>
        <li><strong>Inspect daily</strong> - before each shift, after rainfall, and whenever conditions change - and document findings.</li>
        <li><strong>Train workers</strong> for the hazards of the work they'll actually perform.</li>
      </ol>

      <h2>Matching Training to Duties</h2>
      <p>Subpart P doesn't mandate one specific course, but it does require training "appropriate to their assigned duties." In practice, that means two different depths of training for two different roles:</p>
      <ul>
        <li>Crew members working in or around excavations need hazard-awareness training - see <a href="../excavation-trenching-shoring-safety-training/">Excavation, Trenching &amp; Shoring Safety Training</a>.</li>
        <li>The designated Competent Person needs full program-oversight training - see <a href="../competent-person-excavation-trenching-shoring-training/">Competent Person Training</a>.</li>
      </ul>

      <h2>Documenting Compliance</h2>
      <p>A complete training record typically includes: the certificate of completion for each worker, the employer's own site-specific orientation records, daily inspection logs signed by the Competent Person, and documentation of the protective system selected for each excavation. Certificates from this site cover the first item; the rest is the employer's responsibility. See <a href="../credential-transparency/">Credential Transparency</a> for more on what a certificate does and doesn't establish.</p>

      <p>Full standard text: <a href="../osha-excavation-standards/">OSHA Excavation Standards</a> reference page.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Subpart P Training Guide", "/osha-subpart-p-training-guide/"),
})

PAGES.append({
    "slug": "excavation-competent-person-requirements",
    "active": None,
    "title": "Excavation Competent Person Requirements",
    "description": "OSHA's Competent Person requirements for excavation work: definition, authority, typical duties, and who can be designated.",
    "body": breadcrumb_nav("Competent Person Requirements") + hero_solo(
        "Competent Person",
        "Excavation Competent Person Requirements",
        "What OSHA actually requires of a Competent Person, and who an employer can designate for the role.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <h2>OSHA's Definition</h2>
      <div class="callout-box">
        <p>A Competent Person is someone capable of identifying existing and predictable hazards in the surroundings or working conditions, and who has authorization to take prompt corrective measures to eliminate them.</p>
      </div>

      <h2>Who Can Be Designated</h2>
      <p>OSHA does not require a specific certificate, license, or third-party credential to become a Competent Person - there's no such thing as an "OSHA Competent Person certification" issued by OSHA itself. The employer designates the individual, based on that person's knowledge, experience, and demonstrated ability to identify hazards and act on them. Training like our <a href="../competent-person-excavation-trenching-shoring-training/">Competent Person course</a> builds the knowledge base; the employer's designation grants the authority.</p>

      <h2>Typical Duties</h2>
      <ul>
        <li>Classifying soil using visual and manual tests</li>
        <li>Selecting and verifying protective systems</li>
        <li>Conducting daily inspections before each shift, after rainfall, and whenever conditions change</li>
        <li>Stopping work and removing workers from a hazardous area when needed</li>
        <li>Overseeing the site's written excavation safety program</li>
      </ul>

      <h2>Multiple Sites</h2>
      <p>OSHA doesn't set a fixed limit on how many sites one Competent Person can cover, but they must actually be able to perform the required daily inspections and respond to hazards at each site. Spreading one person too thin to inspect adequately doesn't meet the standard's intent.</p>

      <h2>Training Supports, Doesn't Substitute For, Designation</h2>
      <div class="disclaimer-box">
        Completing Competent Person training is a strong foundation, not an automatic qualification. The employer must still formally designate the individual and confirm they have the site-specific understanding needed for the excavation work being performed. See <a href="../credential-transparency/">Credential Transparency</a> for the full explanation of what a certificate does and doesn't establish.
      </div>

      <p>Official reference: <a href="https://www.osha.gov/etools/construction/trenching/competent-person" target="_blank" rel="noopener">OSHA's Competent Person eTool guidance &rarr;</a></p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Competent Person Requirements", "/excavation-competent-person-requirements/"),
})

PAGES.append({
    "slug": "excavation-training-for-utility-crews",
    "active": None,
    "title": "Excavation Training for Utility Crews",
    "description": "How OSHA excavation and trenching requirements apply to utility crews installing or repairing underground electric, gas, water, sewer, and telecom lines.",
    "body": breadcrumb_nav("Utility Crew Training") + hero_solo(
        "Utility Crews",
        "Excavation Training for Utility Crews",
        "Utility work means trenching every day, near live electric, gas, water, sewer, and telecom infrastructure. Here's how Subpart P applies.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <h2>Why Utility Work Is Different</h2>
      <p>Utility crews don't just work near excavations occasionally - trenching is often the job itself, repeated across many locations, often in existing rights-of-way already crowded with other buried infrastructure. That combination of routine trenching plus utility-strike risk makes 811/call-before-you-dig coordination and daily inspection discipline especially important. See our <a href="../underground-utility-safety/">Underground Utility Safety</a> page for the full breakdown.</p>

      <h2>What Applies</h2>
      <ul>
        <li>Every trench dug for utility installation or repair, regardless of how routine, falls under 29 CFR 1926 Subpart P once it reaches 5 feet (or shallower, if the Competent Person identifies a hazard).</li>
        <li>Locate requests (811) are a separate, additional requirement, not a substitute for soil classification, protective systems, or daily inspection.</li>
        <li>Trench boxes/shields are common on utility jobs because they can be pulled along the trench as work progresses - well suited to the linear nature of utility installation.</li>
        <li>Crews working around energized electric lines or pressurized gas lines carry hazards beyond cave-in risk; strike protocols and clearance distances still apply even with excavation protective systems in place.</li>
      </ul>

      <h2>Recommended Training</h2>
      <p>Utility crew members performing the digging and installation work need <a href="../excavation-trenching-shoring-safety-training/">Excavation, Trenching &amp; Shoring Safety Training</a>. Foremen and crew leads responsible for daily inspections and protective system selection across multiple dig sites need <a href="../competent-person-excavation-trenching-shoring-training/">Competent Person Training</a>. Many utility contractors train their whole field crew in Safety Training and designate one or more Competent Persons per crew or region.</p>

      <p>See our <a href="../which-excavation-course-do-i-need/">decision guide</a> for a full role-by-role breakdown.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Utility Crew Training", "/excavation-training-for-utility-crews/"),
})

PAGES.append({
    "slug": "excavation-training-for-municipal-crews",
    "active": None,
    "title": "Excavation Training for Municipal Crews",
    "description": "How OSHA excavation and trenching requirements apply to municipal public works crews doing water main, sewer, and street utility work.",
    "body": breadcrumb_nav("Municipal Crew Training") + hero_solo(
        "Municipal Crews",
        "Excavation Training for Municipal Crews",
        "Public works, water/sewer, and street departments dig trenches as routine work - often under public and budget scrutiny that adds pressure to cut corners. Here's what still applies.",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <h2>Municipal Excavation Work Is Still Construction Work</h2>
      <p>Water main breaks, sewer repairs, and street utility work performed by a city or county public works crew are covered by the same 29 CFR 1926 Subpart P requirements as any private contractor's excavation - OSHA's construction standards don't have a carve-out for government crews performing construction-type work. Emergency repair conditions (a burst water main flooding a street) create real time pressure, but they don't remove the requirement for soil classification, protective systems, and a designated Competent Person.</p>

      <h2>Common Municipal Scenarios</h2>
      <ul>
        <li><strong>Emergency water/sewer repairs</strong> - often in already-disturbed soil (previous utility cuts), which typically classifies as Type C and needs more conservative protective systems, not less.</li>
        <li><strong>Street and sidewalk excavation</strong> - adds traffic control and pedestrian safety on top of the standard excavation requirements.</li>
        <li><strong>Multi-crew, multi-site operations</strong> - a public works department may run several excavation crews across a city at once, raising the question of how many sites one Competent Person can realistically cover.</li>
      </ul>

      <h2>Recommended Training</h2>
      <p>Field crew performing the digging and repair work need <a href="../excavation-trenching-shoring-safety-training/">Excavation, Trenching &amp; Shoring Safety Training</a>. Crew leads, foremen, and public works safety coordinators responsible for daily inspections and protective system decisions - including under time pressure during emergency repairs - need <a href="../competent-person-excavation-trenching-shoring-training/">Competent Person Training</a>. Departments running multiple simultaneous dig sites should plan for enough trained Competent Persons to actually cover each active site, not just one for the whole department.</p>

      <p>See our <a href="../which-excavation-course-do-i-need/">decision guide</a> for a full role-by-role breakdown, or <a href="../state-osha-plan-requirements/">State OSHA Plan Requirements</a> if your municipality operates under a state plan rather than federal OSHA.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Municipal Crew Training", "/excavation-training-for-municipal-crews/"),
})

# ---------------------------------------------------------------------------
# POLICY PAGES
# ---------------------------------------------------------------------------

PAGES.append({
    "slug": "refund-policy",
    "active": None,
    "title": "Refund Policy | ExcavationTrenchingShoring.com",
    "description": "30-day full refund, money-back guarantee, and refund exclusions for excavation, trenching, and shoring training courses.",
    "body": breadcrumb_nav("Refund Policy") + hero_solo(
        "Policy",
        "Refund Policy",
        "This policy mirrors the refund terms used across HAZWOPER OSHA Training's course catalog, since courses on this site are delivered and billed through that platform.",
        cta_href="../index.html#pricing",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <h2>30-Day Full Refund</h2>
      <p>Not sure whether you or your employees will be able to complete a purchased course? You can cancel a course for up to 30 days after purchase and receive a full refund. If you decide to cancel a course after 30 days of purchase, we will give you a credit for the full value paid, which can be used to enroll in a different course of equal or lesser value. You can also choose the "Pay by Invoice" option at registration to make it easier to finalize your plans later.</p>
      <p>You must provide notice of cancellation to receive a refund, credit your account, or cancel an invoice. Call 1-866-429-6742 between 6:00 AM and 5:00 PM PST to notify us.</p>

      <h2>100% Money-Back Guarantee</h2>
      <p>Your purchase is 100% risk-free. In the rare event you're unsatisfied with the value of the training after completing a course, notify us in writing at info@hazwoper-osha.com with a valid reason and we'll promptly refund your payment. Most refunds are returned via the original payment method. Certain restrictions may apply, and some purchases may only be eligible for credit refunds.</p>

      <h2>No Refund or Credit Will Be Issued For</h2>
      <ul>
        <li><strong>Course Completion:</strong> if 65% or more of the course material has been completed.</li>
        <li><strong>Certificate Issuance:</strong> once the certificate of completion has been issued.</li>
        <li><strong>Assessment Failure:</strong> if you fail to pass quizzes, final exams, or other in-course assessments within the specified number of attempts.</li>
        <li><strong>Identity Validation:</strong> if you fail to pass identity validation requirements outlined in the course guidelines.</li>
        <li><strong>Time Limit:</strong> refund requests must be made within 30 days of the purchase date.</li>
        <li>Expedited processing or mailing of certificates, once that expedited service has been fulfilled as promised.</li>
      </ul>
      <p>Approved refunds may take up to 10 business days to reflect in your account, and are issued only to the original payment method.</p>

      <h2>International Customers</h2>
      <p>This guarantee does not apply to international or overseas registrations. Payment for international and overseas students must be made prior to the start of the course, in U.S. dollars, and all course fees are non-refundable. Student substitutions can be made freely at any time prior to the start of the course.</p>

      <div class="disclaimer-box">
        Courses on this site are delivered and billed through HAZWOPER OSHA Training, LLC's enrollment platform. For refund status or an active request, contact HAZWOPER OSHA Training support directly at <a href="tel:18664296742">1-866-429-6742</a> or <a href="mailto:info@hazwoper-osha.com">info@hazwoper-osha.com</a>.
      </div>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Refund Policy", "/refund-policy/"),
})

PAGES.append({
    "slug": "privacy-policy",
    "active": None,
    "title": "Privacy Policy | ExcavationTrenchingShoring.com",
    "description": "How personal information is collected, used, shared, and protected for excavationtrenchingshoring.com and its HAZWOPER OSHA Training-delivered courses.",
    "body": breadcrumb_nav("Privacy Policy") + hero_solo(
        "Policy",
        "Privacy Policy",
        "This site's data practices follow HAZWOPER OSHA Training, LLC's Privacy Policy, since course enrollment, delivery, and certificate issuance are handled through that platform.",
        cta_href="../index.html#pricing",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <div class="disclaimer-box">This version mirrors HAZWOPER OSHA Training, LLC's Privacy Policy (Version 5.146, effective November 10, 2023) as of the date this page was published, adapted to reference excavationtrenchingshoring.com. Course registration, payment, and certificate data collected through this site is processed under HAZWOPER OSHA Training's systems and practices described below.</div>

      <h2>Overview</h2>
      <p>This Privacy Policy (the "Policy") discloses the privacy practices that apply to excavationtrenchingshoring.com and the training delivered through HAZWOPER OSHA Training, LLC ("HAZWOPER OSHA," referred to collectively as "we," "us," "our"). This Policy governs how we use and protect personal information collected when you visit this website, enroll in a course, or otherwise engage with us.</p>

      <h2>About Us</h2>
      <p>HAZWOPER OSHA Training, LLC is a limited liability company registered in California, with a principal office located at 11901 Santa Monica Blvd. Suite #414, Los Angeles, CA 90025, United States of America. ExcavationTrenchingShoring.com is a subsidiary of Industrial Certified Training, LLC, and training displayed on this site is delivered through HAZWOPER OSHA Training's platform.</p>

      <h2>Questions or Concerns: Contact Us</h2>
      <p>If you have questions or complaints about our privacy practices, contact: Data Protection Officer, HAZWOPER OSHA Training, LLC, 11901 Santa Monica Blvd. Suite #414, Los Angeles, CA 90025, USA. Email: <a href="mailto:info@hazwoper-osha.com">info@hazwoper-osha.com</a>.</p>

      <h2>Information We Collect</h2>
      <p><strong>Information you provide directly</strong> - when you purchase a course, subscribe to communications, fill in forms, make an inquiry, register for or update an account, or contact us. This may include identity and contact data (name, address, email, phone), account profile data, financial data (billing address, payment details), and any other information you choose to share with us.</p>
      <p><strong>Information collected through technology</strong> - cookies, beacons, tags, and similar technologies used to navigate the site, manage content, analyze trends, and gather demographic information about our user base. Cookies allow us to monitor use of the site and simplify your experience.</p>
      <p><strong>Information from other sources</strong> - in certain circumstances we receive information about you from third parties, including service providers (payment processors, IT support, cloud hosting), commercial contact lists, and publicly available sources.</p>

      <h2>Using Personal Information</h2>
      <p>We use your information to: provide and personalize access to the website; register and maintain your account; process and fulfill course orders and payments; provide customer service and support; communicate about changes to our terms or this Policy; conduct data analytics to improve the website and services; carry out marketing communications where permitted; and protect, investigate, and deter fraudulent or unlawful activity. We rely on your consent (where requested), performance of our contract with you, compliance with legal obligations, or our legitimate business interests as the basis for this processing.</p>

      <h2>How We Share and Disclose Personal Information</h2>
      <p>We do not sell your personal information to third parties. We may share it with: service providers who assist with administrative, payment, or IT functions; wholly owned subsidiaries and affiliated companies, including Industrial Certified Training, LLC and HAZWOPER OSHA Training, LLC; regulators and governmental bodies where required; and other third parties where necessary to enforce our legal rights or protect the rights, property, or safety of our employees, or as required by law.</p>

      <h2>How We Protect Your Information &amp; How Long We Keep It</h2>
      <p>We use administrative, technical, and physical safeguards - including SSL encryption for sensitive data such as payment details, access limits, and a data protection policy - to protect personal information against loss, misuse, and unauthorized access. We retain information for as long as necessary to provide the services requested or as required for our lawful business purposes.</p>

      <h2>International Transfers</h2>
      <p>HAZWOPER OSHA is based in the United States. If you reside outside the U.S., your information may be processed in the United States. We take steps to ensure information transferred internationally is protected consistent with this Policy.</p>

      <h2>Your Rights</h2>
      <p>Depending on your jurisdiction, you may have the right to: be informed how we use your information; request access to information we hold about you; request correction of inaccurate information; withdraw consent where we rely on it; object to processing based on legitimate interests; request a copy of your information in a portable format; and request that we limit, cease processing, or erase your information. Exercise these rights by contacting us using the details above.</p>

      <h2>Children's Privacy</h2>
      <p>This website is not intended for children. We do not knowingly collect personal information from children under 13 (or under 16 in some jurisdictions). If we learn we've collected such information, we will take steps to delete it.</p>

      <h2>Sharing Data with Third Parties</h2>
      <p>This site may link to third-party websites, including hazwoper-osha.com for enrollment and course delivery. We are not responsible for the privacy practices of third-party sites; please review their policies directly.</p>

      <h2>For California Residents</h2>
      <p>We share your personal information only with your consent. California law requires disclosure of our Do Not Track (DNT) practices: we do not currently respond to DNT browser signals.</p>

      <h2>Changes to This Policy</h2>
      <p>This Policy may change from time to time. We will not reduce your rights under this Policy without your consent, and we will notify you of material changes by posting a notice on this website prior to the change taking effect.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Privacy Policy", "/privacy-policy/"),
})

PAGES.append({
    "slug": "certificate-policy",
    "active": None,
    "title": "Certificate Policy | ExcavationTrenchingShoring.com",
    "description": "How certificates of completion are issued, what they mean, validity periods, and how to request verification or a reissue.",
    "body": breadcrumb_nav("Certificate Policy") + hero_solo(
        "Policy",
        "Certificate Policy",
        "How certificates of completion are issued, what they mean, and how long they're valid.",
        cta_href="../index.html#pricing",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <h2>Issuance</h2>
      <p>A certificate of completion is issued immediately after a student passes the required knowledge assessment for a course. Certificates include the student's name, course name, training hours, completion date, a unique certificate ID, and the issuing provider, HAZWOPER OSHA Training, LLC.</p>

      <h2>What the Certificate Means</h2>
      <p>A certificate of completion documents that the named student completed and passed the identified course. It is not an OSHA certification, approval, license, or endorsement. See <a href="../credential-transparency/">Credential Transparency</a> for the full explanation.</p>

      <h2>Validity Periods</h2>
      <div class="data-table-wrap">
        <table class="data-table">
          <thead><tr><th>Course</th><th>Certificate Validity</th></tr></thead>
          <tbody>
            <tr><td>Excavation, Trenching &amp; Shoring Safety Training</td><td>36 months</td></tr>
            <tr><td>Competent Person for Excavation, Trenching &amp; Shoring Training</td><td>24 months</td></tr>
          </tbody>
        </table>
      </div>
      <p>OSHA does not set a fixed renewal interval for this type of training; these validity periods are recommended refresher intervals, not a federal mandate. Retraining is also required whenever job duties change, a new hazard is introduced, or a performance evaluation indicates it's needed.</p>

      <h2>Requesting Verification</h2>
      <p>Employers, contractors, and compliance teams can verify a certificate directly through HAZWOPER OSHA Training's <a href="https://hazwoper-osha.com/certificate-verification" target="_blank" rel="noopener">certificate verification form</a>.</p>

      <h2>Lost or Reissued Certificates</h2>
      <p>If you've lost access to your certificate, contact HAZWOPER OSHA Training support at <a href="tel:18664296742">1-866-429-6742</a> or <a href="mailto:info@hazwoper-osha.com">info@hazwoper-osha.com</a> with your name and course details. Expedited reissue or mailing services, where offered, are non-refundable once fulfilled - see our <a href="../refund-policy/">Refund Policy</a>.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Certificate Policy", "/certificate-policy/"),
})

PAGES.append({
    "slug": "group-training-policy",
    "active": None,
    "title": "Group Training Policy | ExcavationTrenchingShoring.com",
    "description": "How bulk/group enrollment, pricing tiers, and team training work for excavation, trenching, and shoring courses.",
    "body": breadcrumb_nav("Group Training Policy") + hero_solo(
        "Policy",
        "Group Training Policy",
        "How bulk enrollment, seat pricing, and team training work for construction crews and safety departments.",
        cta_href="../index.html#pricing",
    ) + """
  <section class="section">
    <div class="container content-prose">
      <h2>Bulk Seat Pricing</h2>
      <p>Per-seat pricing decreases as seat count increases, applied automatically at checkout based on the number of seats entered. See the "Bulk Pricing" table on either course's enrollment card at <a href="../index.html#pricing">Pricing</a> for current tier discounts.</p>

      <h2>Mixed-Course Group Enrollment</h2>
      <p>Many employers enroll their crew in Excavation, Trenching &amp; Shoring Safety Training and their designated Competent Person(s) in the advanced course as a combined order. Contact us to coordinate a combined invoice across both courses.</p>

      <h2>Pay by Invoice</h2>
      <p>Groups can choose the "Pay by Invoice" option at registration to finalize payment after enrollment details are confirmed, consistent with our <a href="../refund-policy/">Refund Policy</a>'s 30-day cancellation window.</p>

      <h2>Progress Tracking &amp; Reporting</h2>
      <p>For teams needing centralized completion tracking or a company LMS integration, SCORM packages are available through HAZWOPER OSHA Training - see the "Also Available Through HAZWOPER OSHA Training" section on each course page, or contact support to discuss reporting needs for larger groups.</p>

      <h2>Substitutions</h2>
      <p>Seat substitutions (swapping one enrolled student for another before course access begins) can generally be made by contacting support before the substitute student has started the course.</p>

      <h2>Contact for Group Training</h2>
      <p>For enterprise, multi-site, or recurring group training needs, contact HAZWOPER OSHA Training support at <a href="tel:18664296742">1-866-429-6742</a> or <a href="mailto:info@hazwoper-osha.com">info@hazwoper-osha.com</a>.</p>
    </div>
  </section>""",
    "extra_schema": breadcrumb_schema("Group Training Policy", "/group-training-policy/"),
})

# ---------------------------------------------------------------------------
# FAQ (migrated into the build system + new categories appended)
# ---------------------------------------------------------------------------

FAQ_BODY = """
  <section class="hero hero-solo" id="top">
    <div class="container hero-inner">
      <div class="hero-copy">
        <p class="eyebrow">FAQ &amp; Resource Library</p>
        <h1>Excavation, Trenching &amp; Shoring <span>FAQ</span></h1>
        <p class="hero-lead">
          45+ answers on OSHA excavation requirements, cave-in hazards, soil classification, protective systems,
          Competent Person duties, certificates, and which of our two courses fits your job.
        </p>
        <div class="hero-cta-row">
          <a href="#basics" class="btn btn-primary btn-lg">Browse Questions</a>
          <a href="../index.html#pricing" class="btn btn-outline-light btn-lg">Enroll Now</a>
        </div>
      </div>
    </div>
  </section>

  <nav class="faq-jumpnav" aria-label="FAQ categories">
    <a href="#basics">Excavation Basics</a>
    <a href="#regulations">Regulations &amp; Legal Requirements</a>
    <a href="#protective-systems">Soil &amp; Protective Systems</a>
    <a href="#site-safety">Site Safety Practices</a>
    <a href="#competent-person">Competent Person Duties</a>
    <a href="#certifications">Certifications &amp; Course Formats</a>
    <a href="#credentials">Credentials &amp; Verification</a>
    <a href="#formats">Training Formats &amp; Requirements</a>
  </nav>

  <section class="section" id="basics">
    <div class="container">
      <div class="section-head"><p class="eyebrow">Category</p><h2>Excavation Basics</h2></div>
      <div class="faq-page-list">
        <div class="faq-item"><button class="faq-question" aria-expanded="false">What counts as an excavation under OSHA rules?<span class="faq-icon">+</span></button><div class="faq-answer"><p>OSHA defines an excavation as any man-made cut, cavity, trench, or depression in the earth's surface formed by removing soil. A trench is a specific type of excavation that is narrow in relation to its depth, generally no wider than 15 feet at the bottom.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">How deep does a trench have to be before OSHA rules apply?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Most protective-system requirements apply once an excavation reaches 5 feet in depth, unless a Competent Person determines the soil is stable rock. Excavations less than 5 feet deep can still require protection if the Competent Person identifies a hazard, and excavations 20 feet or deeper require a protective system designed by a registered professional engineer.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">What is the difference between an excavation and a trench?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Every trench is an excavation, but not every excavation is a trench. A trench is a narrow excavation, generally less than 15 feet wide at the bottom, made below the surface of the ground; the depth is usually greater than the width. Broader excavations, like building foundations or basements, follow the same Subpart P standard but aren't technically trenches. See our <a href="../trenching-vs-excavation-training/">Trenching vs. Excavation</a> page.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Why are trenches considered so dangerous?<span class="faq-icon">+</span></button><div class="faq-answer"><p>A cubic yard of soil can weigh well over a ton, and a trench wall can collapse in seconds with little or no warning. Workers caught in a cave-in are rarely able to escape unaided, and the weight and speed of a collapse make trench-related fatalities disproportionately high compared to many other construction hazards.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Is a trench considered a confined space?<span class="faq-icon">+</span></button><div class="faq-answer"><p>It depends on the configuration and hazards present. Trenches are regulated separately under 29 CFR 1926 Subpart P, but a trench can also meet the confined space definition if entry and exit are restricted, in which case both trenching and confined space precautions may be required at once.</p></div></div>
      </div>
    </div>
  </section>

  <section class="section section-alt" id="regulations">
    <div class="container">
      <div class="section-head"><p class="eyebrow">Category</p><h2>Regulations &amp; Legal Requirements</h2></div>
      <div class="faq-page-list">
        <div class="faq-item"><button class="faq-question" aria-expanded="false">What does 29 CFR 1926 Subpart P cover?<span class="faq-icon">+</span></button><div class="faq-answer"><p>29 CFR 1926 Subpart P is OSHA's excavation standard for construction. It sets requirements for soil classification, protective systems (sloping, benching, shoring, and shielding), safe access and egress, spoil placement, and the daily inspection duties of the Competent Person. See our <a href="../osha-excavation-standards/">OSHA Excavation Standards</a> page for official links.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Is excavation and trenching training legally required?<span class="faq-icon">+</span></button><div class="faq-answer"><p>OSHA requires that only trained and authorized personnel design protective systems and that a Competent Person, capable of identifying hazards and authorized to take corrective action, be designated for every excavation site. Employers are responsible for training workers on the hazards of the work they perform. Our <a href="../index.html#courses">Safety Training and Competent Person courses</a> map directly to these requirements.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">What happens if a site is found out of compliance with excavation rules?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Non-compliance can result in significant OSHA fines per violation, stop-work orders, and in serious cases criminal referral if a fatality results from a willful violation. Trenching is consistently one of OSHA's most-cited and most fatal construction hazards, and enforcement has intensified in recent years.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Who enforces excavation regulations, and can state rules differ from federal OSHA?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Federal OSHA enforces 29 CFR 1926 Subpart P in most states, but roughly half the states run their own OSHA-approved state plans, which must be at least as protective as the federal rules and sometimes add requirements on top. See our <a href="../state-osha-plan-requirements/">State OSHA Plan Requirements</a> page.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Does every excavation need a permit like a confined space entry?<span class="faq-icon">+</span></button><div class="faq-answer"><p>No. Unlike confined space entry, OSHA's excavation standard doesn't require a written permit for each dig. Instead it requires a Competent Person to evaluate soil and site conditions, select an appropriate protective system, and conduct daily inspections before and during the work.</p></div></div>
      </div>
    </div>
  </section>

  <section class="section section-alt" id="protective-systems">
    <div class="container">
      <div class="section-head"><p class="eyebrow">Category</p><h2>Soil &amp; Protective Systems</h2></div>
      <div class="faq-page-list">
        <div class="faq-item"><button class="faq-question" aria-expanded="false">What are the four soil types under OSHA's classification system?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Stable Rock, Type A, Type B, and Type C, in order from most to least stable. See our <a href="../soil-classification-training/">Soil Classification</a> page for the full breakdown.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Who is qualified to classify soil on an excavation site?<span class="faq-icon">+</span></button><div class="faq-answer"><p>The designated Competent Person, using at least one visual test and one manual analysis test (such as a plasticity or dry strength test), classifies the soil type present. Our <a href="../competent-person-excavation-trenching-shoring-training/">Competent Person course</a> covers both test methods in detail.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">What is sloping, and when can it be used instead of shoring?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Sloping cuts back the trench wall at an angle away from the excavation. The maximum allowable slope depends on soil type. See our <a href="../sloping-benching-shoring-shielding-explained/">Sloping vs. Benching vs. Shoring vs. Shielding</a> comparison.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">What is benching, and how is it different from sloping?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Benching cuts the trench wall into a series of horizontal steps rather than one continuous slope. Benching is not permitted in Type C soil.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">What is shoring, and what are the common types?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Shoring is a support system, typically hydraulic or timber, installed to prevent trench walls from collapsing. See our <a href="../excavation-protective-systems/">Protective Systems</a> page.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">What is the difference between shoring and shielding?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Shoring actively supports the trench wall to prevent a collapse; shielding (a trench box) doesn't prevent a cave-in, it protects workers by containing the collapse if one occurs. See our <a href="../sloping-benching-shoring-shielding-explained/">Sloping, Benching, Shoring &amp; Shielding Explained</a> page.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Can a manufacturer's tabulated data be used instead of engineering calculations for a protective system?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Yes, for most standard configurations. A registered professional engineer's design is required for excavations 20 feet or deeper, or for non-standard conditions tabulated data doesn't cover.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">When is a protective system required?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Whenever an excavation is 5 feet or deeper, unless it's entirely in stable rock or a Competent Person determines no hazard exists. A Competent Person can also require protection in shallower excavations if a hazard is identified.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">When is a registered professional engineer required?<span class="faq-icon">+</span></button><div class="faq-answer"><p>For excavations 20 feet or deeper, or for protective system designs that fall outside standard manufacturer tabulated data. See our <a href="../excavation-protective-systems/">Protective Systems</a> page.</p></div></div>
      </div>
    </div>
  </section>

  <section class="section" id="site-safety">
    <div class="container">
      <div class="section-head"><p class="eyebrow">Category</p><h2>Site Safety Practices</h2></div>
      <div class="faq-page-list">
        <div class="faq-item"><button class="faq-question" aria-expanded="false">How close can spoil piles and equipment be to the edge of an excavation?<span class="faq-icon">+</span></button><div class="faq-answer"><p>OSHA requires spoil piles, excavated materials, and equipment to be kept at least 2 feet back from the edge of an excavation, or otherwise retained by a barrier.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">What are the requirements for safe access and egress from a trench?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Excavations 4 feet or deeper require a stairway, ladder, ramp, or other safe means of exit, located so that no worker has to travel more than 25 feet laterally to reach it.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Does a trench need to be tested for hazardous atmospheres?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Yes, whenever there's a reasonable possibility of an oxygen deficiency or hazardous atmosphere. See our <a href="../excavation-emergency-planning/">Emergency Planning</a> page.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">What should be done if water is accumulating in an excavation?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Workers should not be permitted to work in an excavation with accumulating water unless precautions have been taken, such as special support systems, water removal, or a safety harness and lifeline.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Does call-before-you-dig / 811 satisfy OSHA's excavation requirements?<span class="faq-icon">+</span></button><div class="faq-answer"><p>No. Calling 811 identifies underground utilities, but it's a separate obligation from OSHA's excavation safety requirements. See our <a href="../underground-utility-safety/">Underground Utility Safety</a> page.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Does the course cover underground utilities?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Yes. Both courses cover call-before-you-dig practices and underground utility hazard awareness; see our dedicated <a href="../underground-utility-safety/">Underground Utility Safety</a> page for the full topic.</p></div></div>
      </div>
    </div>
  </section>

  <section class="section section-alt" id="competent-person">
    <div class="container">
      <div class="section-head"><p class="eyebrow">Category</p><h2>Competent Person Duties</h2></div>
      <div class="faq-page-list">
        <div class="faq-item"><button class="faq-question" aria-expanded="false">What must a Competent Person inspect, and how often?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Daily before work begins, after every rainstorm or hazard-increasing event, and whenever there's an indication of a possible cave-in or other hazardous condition.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">What is a Competent Person responsible for on an excavation site?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Classifying soil, selecting and verifying protective systems, conducting daily inspections, and overseeing the site's written excavation safety program. See our <a href="../excavation-competent-person-requirements/">Competent Person Requirements</a> page.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Does completing this course make me a Competent Person?<span class="faq-icon">+</span></button><div class="faq-answer"><p>No. Training builds the knowledge base, but the employer must formally designate the Competent Person and confirm they have the authority and site-specific understanding needed. See <a href="../credential-transparency/">Credential Transparency</a>.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Who can designate a Competent Person?<span class="faq-icon">+</span></button><div class="faq-answer"><p>The employer. OSHA doesn't require a specific third-party certification - the employer designates someone based on their knowledge, experience, and demonstrated ability to identify and correct hazards.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Can one person serve as Competent Person for multiple excavation sites at once?<span class="faq-icon">+</span></button><div class="faq-answer"><p>OSHA doesn't set a fixed limit, but the Competent Person must actually be able to perform required daily inspections and respond to hazards at each site they're responsible for.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Who pays for excavation training, the employer or the worker?<span class="faq-icon">+</span></button><div class="faq-answer"><p>The employer. OSHA requires legally mandated safety training to be provided at no cost to employees.</p></div></div>
      </div>
    </div>
  </section>

  <section class="section" id="certifications">
    <div class="container">
      <div class="section-head"><p class="eyebrow">Category</p><h2>Certifications &amp; Course Formats</h2></div>
      <div class="faq-page-list">
        <div class="faq-item"><button class="faq-question" aria-expanded="false">How long does each excavation course take?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Excavation, Trenching &amp; Shoring Safety Training runs about 3 hours, and Competent Person training runs about 8 hours. Both are self-paced online courses.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">How much does excavation training cost?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Excavation, Trenching &amp; Shoring Safety Training is $59.99 per seat, and Competent Person training is $159.99 per seat. Volume discounts are available; see <a href="../index.html#pricing">Pricing</a>.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Is excavation training available online, or does it require in-person attendance?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Both courses are on-demand online by default. SCORM packages, Virtual Instructor-Led sessions, and In-Person Group training are available through HAZWOPER OSHA Training for teams that need those formats.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Is online excavation training accepted for OSHA compliance?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Yes, for the classroom and knowledge portion. Employers must also confirm hands-on competency wherever the standard requires it. See "Is online excavation training enough?" below.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">How often should excavation training be refreshed?<span class="faq-icon">+</span></button><div class="faq-answer"><p>OSHA doesn't set a fixed renewal interval, but our certificates carry recommended validity periods: 36 months for Safety Training, 24 months for Competent Person training.</p></div></div>
      </div>
    </div>
  </section>

  <section class="section section-alt" id="credentials">
    <div class="container">
      <div class="section-head"><p class="eyebrow">Category</p><h2>Credentials &amp; Verification</h2></div>
      <div class="faq-page-list">
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Is excavationtrenchingshoring.com training OSHA certified?<span class="faq-icon">+</span></button><div class="faq-answer"><p>No. OSHA does not certify training providers or courses. This training is OSHA-aligned - built around 29 CFR 1926 Subpart P. See <a href="../credential-transparency/">Credential Transparency</a>.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Does OSHA approve this course?<span class="faq-icon">+</span></button><div class="faq-answer"><p>No. OSHA does not approve or endorse individual excavation training courses or providers. Any language on this site describing the course as "OSHA-aligned" refers to content alignment with the standard, not OSHA approval.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">What certificate do I receive?<span class="faq-icon">+</span></button><div class="faq-answer"><p>A certificate of completion showing your name, the course, training hours, completion date, a certificate ID, and the issuing provider, HAZWOPER OSHA Training, LLC. See our <a href="../certificate-policy/">Certificate Policy</a> and each course page's sample certificate.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Can employers verify certificates?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Yes, directly through <a href="https://hazwoper-osha.com/certificate-verification" target="_blank" rel="noopener">HAZWOPER OSHA Training's certificate verification form</a>.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Do state OSHA plans have different requirements?<span class="faq-icon">+</span></button><div class="faq-answer"><p>They can. Roughly half the states run their own OSHA-approved State Plan, which may add requirements beyond federal OSHA. See our <a href="../state-osha-plan-requirements/">State OSHA Plan Requirements</a> page.</p></div></div>
      </div>
    </div>
  </section>

  <section class="section" id="formats">
    <div class="container">
      <div class="section-head"><p class="eyebrow">Category</p><h2>Training Formats &amp; Requirements</h2></div>
      <div class="faq-page-list">
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Which course do excavation workers need?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Excavation, Trenching &amp; Shoring Safety Training, for crew-level hazard awareness. See our <a href="../which-excavation-course-do-i-need/">course decision guide</a>.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Which course do foremen or supervisors need?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Competent Person for Excavation, Trenching &amp; Shoring Training, for those responsible for inspections, soil classification, and protective system selection.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Is online excavation training enough?<span class="faq-icon">+</span></button><div class="faq-answer"><p>It covers the knowledge portion, but OSHA compliance typically also requires site-specific instruction, hands-on competency confirmation, and daily inspection practice that online training alone can't provide. See "Employer Responsibilities" on the homepage.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Do I need hands-on training too?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Often, yes - particularly for Competent Person duties like soil testing and protective system installation, and for rescue/emergency response. See our <a href="../excavation-emergency-planning/">Emergency Planning</a> page.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Does the course cover soil classification?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Competent Person training covers full soil classification methods. Safety Training covers the basics only. See our <a href="../soil-classification-training/">Soil Classification</a> page.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Is the course available in Spanish?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Yes, both courses are available in English and Spanish.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Do you offer SCORM for company LMS systems?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Yes, through HAZWOPER OSHA Training. See the "Also Available Through HAZWOPER OSHA Training" section on each course page.</p></div></div>
        <div class="faq-item"><button class="faq-question" aria-expanded="false">Do you offer virtual instructor-led or in-person training?<span class="faq-icon">+</span></button><div class="faq-answer"><p>Yes, both are available through HAZWOPER OSHA Training for teams that need those formats. Links are on each course page.</p></div></div>
      </div>

      <div class="faq-cta-box">
        <p><strong>Which course fits your role? &rarr;</strong> Working in or around excavations? Start with <strong>Excavation, Trenching &amp; Shoring Safety Training</strong>. Responsible for soil classification, protective systems, and daily inspections? Take <strong>Competent Person</strong> training. Use our <a href="../which-excavation-course-do-i-need/">full decision guide</a> or call 1-866-429-6742 to sign up.</p>
      </div>

      <p class="faq-page-disclaimer">This FAQ is provided for general guidance and staff training purposes and is not legal advice. Regulatory details and enforcement practices change over time and can vary by jurisdiction. Confirm current requirements for your specific site and project with qualified counsel or OSHA before relying on them.</p>
    </div>
  </section>

  <section class="final-cta">
    <div class="container final-cta-inner">
      <h2>Keep Your Crew Compliant. Train Every Role.</h2>
      <p>Two courses, online. Certificate on completion. English &amp; Spanish.</p>
      <div class="hero-cta-row">
        <a href="../index.html#pricing" class="btn btn-primary btn-lg">Enroll Now</a>
        <a href="tel:18664296742" class="btn btn-outline-light btn-lg">Call 1-866-429-6742</a>
      </div>
    </div>
  </section>"""

PAGES.append({
    "slug": "frequently-asked-questions",
    "active": "faq",
    "title": "Excavation, Trenching & Shoring Training FAQ",
    "description": "45+ answers on OSHA excavation requirements, cave-in hazards, soil classification, protective systems, and Competent Person duties.",
    "body": FAQ_BODY,
    "extra_schema": breadcrumb_schema("FAQ", "/frequently-asked-questions/"),
})

# ---------------------------------------------------------------------------
# CHECKOUT (Stripe + HAZWOPER OSHA order API)
# ---------------------------------------------------------------------------

CHECKOUT_HEAD_EXTRA = """<meta name="robots" content="noindex, follow">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/css/intlTelInput.css">
<link rel="stylesheet" href="../css/checkout.css">
<script src="https://js.stripe.com/v3/"></script>
<script src="https://cdn.jsdelivr.net/npm/intl-tel-input@18.2.1/build/js/intlTelInput.min.js"></script>"""

CHECKOUT_STATE_OPTIONS = """<option value="">Select a State</option>
                  <option value="AL">Alabama</option>
                  <option value="AK">Alaska</option>
                  <option value="AZ">Arizona</option>
                  <option value="AR">Arkansas</option>
                  <option value="CA">California</option>
                  <option value="CO">Colorado</option>
                  <option value="CT">Connecticut</option>
                  <option value="DE">Delaware</option>
                  <option value="FL">Florida</option>
                  <option value="GA">Georgia</option>
                  <option value="HI">Hawaii</option>
                  <option value="ID">Idaho</option>
                  <option value="IL">Illinois</option>
                  <option value="IN">Indiana</option>
                  <option value="IA">Iowa</option>
                  <option value="KS">Kansas</option>
                  <option value="KY">Kentucky</option>
                  <option value="LA">Louisiana</option>
                  <option value="ME">Maine</option>
                  <option value="MD">Maryland</option>
                  <option value="MA">Massachusetts</option>
                  <option value="MI">Michigan</option>
                  <option value="MN">Minnesota</option>
                  <option value="MS">Mississippi</option>
                  <option value="MO">Missouri</option>
                  <option value="MT">Montana</option>
                  <option value="NE">Nebraska</option>
                  <option value="NV">Nevada</option>
                  <option value="NH">New Hampshire</option>
                  <option value="NJ">New Jersey</option>
                  <option value="NM">New Mexico</option>
                  <option value="NY">New York</option>
                  <option value="NC">North Carolina</option>
                  <option value="ND">North Dakota</option>
                  <option value="OH">Ohio</option>
                  <option value="OK">Oklahoma</option>
                  <option value="OR">Oregon</option>
                  <option value="PA">Pennsylvania</option>
                  <option value="RI">Rhode Island</option>
                  <option value="SC">South Carolina</option>
                  <option value="SD">South Dakota</option>
                  <option value="TN">Tennessee</option>
                  <option value="TX">Texas</option>
                  <option value="UT">Utah</option>
                  <option value="VT">Vermont</option>
                  <option value="VA">Virginia</option>
                  <option value="WA">Washington</option>
                  <option value="WV">West Virginia</option>
                  <option value="WI">Wisconsin</option>
                  <option value="WY">Wyoming</option>"""

CHECKOUT_BODY = """
  <section class="section checkout-page-section">
    <div class="container">

      <div class="checkout-page-header">
        <h1>Checkout</h1>
        <p class="checkout-subtitle">Complete the checkout below to enroll in your excavation training course.</p>
      </div>

      <!-- SUCCESS CONFIRMATION VIEW (Shown after successful payment) -->
      <div id="checkoutSuccessView" class="success-view-card" hidden>
        <div class="success-icon-wrapper">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        </div>
        <h2>Order Confirmed!</h2>
        <p class="success-lead">Thank you for your purchase. Your payment has been processed successfully.</p>
        <div class="success-details-card">
          <div class="success-detail-row">
            <span>Order Reference:</span>
            <strong id="successOrderId">#---</strong>
          </div>
          <div class="success-detail-row">
            <span>Confirmation Email Sent To:</span>
            <strong id="successUserEmail">---</strong>
          </div>
        </div>
        <div class="account-notice-callout success-callout">
          <p>Check your email inbox for your receipt and LMS account login details to start your course training immediately.</p>
        </div>
        <a href="../index.html" class="btn btn-primary btn-lg">Return to Home</a>
      </div>

      <!-- MAIN CHECKOUT FORM (2-COLUMN LAYOUT) -->
      <form id="stripeCheckoutForm" class="checkout-grid">
        <!-- Left Column: Billing Information & Payment -->
        <div class="checkout-main">
          <div class="checkout-section">
            <h3>Billing Information</h3>
            <div class="form-row-group">
              <div class="form-group">
                <label for="billingFirstName">First Name <span class="required">*</span></label>
                <input type="text" id="billingFirstName" name="firstName" class="form-control" required placeholder="First Name">
              </div>
              <div class="form-group">
                <label for="billingLastName">Last Name <span class="required">*</span></label>
                <input type="text" id="billingLastName" name="lastName" class="form-control" required placeholder="Last Name">
              </div>
            </div>

            <div class="form-group">
              <label for="billingCompany">Company Name</label>
              <input type="text" id="billingCompany" name="company" class="form-control" placeholder="Company Name">
            </div>

            <div class="form-row-group">
              <div class="form-group">
                <label for="billingPhone">Phone <span class="required">*</span></label>
                <input type="tel" id="billingPhone" name="phone" class="form-control" required placeholder="(555) 000-0000">
                <div id="phone-error" class="payment-error-alert" style="margin-top:6px;font-size:.82rem;" hidden></div>
              </div>
              <div class="form-group">
                <label for="billingEmail">Email Address <span class="required">*</span></label>
                <input type="email" id="billingEmail" name="email" class="form-control" required placeholder="you@example.com">
              </div>
            </div>

            <div class="form-row-group">
              <div class="form-group">
                <label for="billingAddress">Street Address <span class="required">*</span></label>
                <input type="text" id="billingAddress" name="address" class="form-control" required placeholder="Street address">
              </div>
              <div class="form-group">
                <label for="billingAddress2">Suite, Apt, Building</label>
                <input type="text" id="billingAddress2" name="address2" class="form-control" placeholder="Apt, Suite, Unit, etc.">
              </div>
            </div>

            <div class="form-row-group">
              <div class="form-group">
                <label for="billingCity">City <span class="required">*</span></label>
                <input type="text" id="billingCity" name="city" class="form-control" required placeholder="City">
              </div>
              <div class="form-group">
                <label for="billingState">State <span class="required">*</span></label>
                <select id="billingState" name="state" class="form-control" required>
                  """ + CHECKOUT_STATE_OPTIONS + """
                </select>
              </div>
            </div>

            <div class="form-row-group">
              <div class="form-group">
                <label for="billingZip">Zip / Postal Code <span class="required">*</span></label>
                <input type="text" id="billingZip" name="zip" class="form-control" required placeholder="Zip Code">
              </div>
              <div class="form-group">
                <label for="billingCountry">Country <span class="required">*</span></label>
                <select id="billingCountry" name="country" class="form-control" required>
                  <option value="US" selected>United States</option>
                  <option value="CA">Canada</option>
                </select>
              </div>
            </div>
          </div>

          <div class="checkout-section">
            <h3>Payment</h3>

            <div class="stripe-card-wrapper">
              <div id="payment-element">
                <!-- Stripe Payment Element dynamically mounts here -->
              </div>
              <div id="payment-error" class="payment-error-alert" hidden></div>
            </div>

            <button type="submit" id="submitPaymentBtn" class="btn btn-primary btn-block btn-lg btn-pay">
              <span class="btn-text">Place Order</span>
              <span class="btn-spinner" hidden></span>
            </button>
          </div>
        </div>

        <!-- Right Column: Order Summary -->
        <div class="checkout-sidebar">
          <div class="order-summary-card">
            <div class="order-summary-header">
              <h3>Order Summary</h3>
            </div>
            <div class="order-summary-body">
              <div class="summary-line-item">
                <div class="summary-course-info">
                  <span class="summary-course-name" id="summaryCourseName">Excavation, Trenching &amp; Shoring Safety Training</span>
                  <span class="summary-qty" id="summaryCourseQty">Qty: 1</span>
                </div>
                <span class="summary-amount" id="summaryCourseAmount">$59.99</span>
              </div>
              <hr class="summary-divider">
              <div class="summary-row">
                <span>Subtotal</span>
                <span id="summarySubtotal">$59.99</span>
              </div>
              <div class="summary-row summary-total">
                <span>Total</span>
                <span id="summaryTotal">$59.99</span>
              </div>
            </div>

            <div class="account-notice-callout">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><polyline points="9 12 11 14 15 10"/></svg>
              <p>An account will be automatically created at checkout. Login details will be emailed to you.</p>
            </div>
          </div>
        </div>
      </form>

    </div>
  </section>"""

PAGES.append({
    "slug": "checkout",
    "active": None,
    "title": "Checkout | Excavation, Trenching & Shoring Training",
    "description": "Complete your purchase of OSHA-aligned excavation, trenching, and shoring training. Secure checkout, instant access, and certificates included.",
    "body": CHECKOUT_BODY,
    "extra_head_raw": CHECKOUT_HEAD_EXTRA,
    "extra_body_scripts": '<script src="../js/checkout.js"></script>',
    "main_class": "checkout-page-main",
    "include_main_js": False,
    "noindex": True,
})

PAGES.append({
    "slug": "",
    "is_home": True,
    "active": "overview",
    "title": "OSHA Excavation, Trenching & Shoring Training Courses",
    "description": "OSHA-aligned excavation training: Safety Training and Competent Person courses. Self-paced, English & Spanish, instant certificate. 29 CFR 1926 Subpart P.",
    "body": HOME_BODY.replace("COURSE_PICKER_TEASER", course_picker_widget(prefix="")),
    "extra_schema": HOME_SCHEMA,
})
