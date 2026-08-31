"""Page content for the Smartech Technologies static site.
Each function returns the <body>-region HTML for one page.
build() wires them all together and writes files via write().
"""

def build(base, write, wa_link, WA_ICON, EMERGENCY_PHONE, PHONE_DISPLAY):

    # ============================================================
    # HOME — p = ''
    # ============================================================
    home_body = f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <div class="eyebrow" style="color:#dd8f31;">Unified Smart Infrastructure as a Service</div>
      <h1>One team wires, secures,<br>and powers your property.</h1>
      <p class="lede">Most contractors in Kenya specialize in one thing &mdash; solar, or CCTV, or wiring &mdash; and leave you juggling three vendors who blame each other when something breaks. Smartech installs and maintains all of it under one contract, one warranty, and one phone number.</p>
      <div class="hero-ctas">
        <a class="btn btn--amber" href="get-a-quote.html">Get a Free Site Survey</a>
        <a class="btn btn--outline-light" href="solutions/smart-solar-security-hub.html">See the Smart Solar Security Hub</a>
      </div>
      <div class="hero-badges">
        <span>EPRA Licensed</span>
        <span>NCA Registered</span>
        <span>CAK Licensed Contractor</span>
        <span>24/7 Emergency Response</span>
      </div>
    </div>
    <div class="hero-diagram">
      <div class="diagram-title">// Live System Overview</div>
      <div class="diagram-row"><span>Solar &amp; Battery Backup</span><span class="status mono">● online</span></div>
      <div class="diagram-row"><span>AI CCTV &amp; Access Control</span><span class="status mono">● online</span></div>
      <div class="diagram-row"><span>Electrical Distribution</span><span class="status mono">● online</span></div>
      <div class="diagram-row"><span>Structured Cabling</span><span class="status mono">● online</span></div>
      <div class="diagram-row"><span>Compliance &amp; Safety Audit</span><span class="status mono">● current</span></div>
      <p style="margin-top:18px; font-size:0.72rem; color:#9aa3ac;">This is what "unified infrastructure" looks like in practice &mdash; every system installed and monitored by one accountable team.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="eyebrow">What We Connect</div>
    <h2 style="max-width:20ch;">Five systems. One contractor. Zero finger-pointing.</h2>
    <div class="nodes-row">
      <div class="node-item"><div class="node-dot"></div><h3>Solar &amp; Green Energy</h3><p>Hybrid inverters, BESS, solar pumping, EPRA-certified retrofits.</p></div>
      <div class="node-item"><div class="node-dot"></div><h3>Security Systems</h3><p>AI CCTV, biometric access, alarms, IP intercoms.</p></div>
      <div class="node-item"><div class="node-dot"></div><h3>Electrical &amp; Power</h3><p>Wiring, surge protection, backup power, panel boards.</p></div>
      <div class="node-item"><div class="node-dot"></div><h3>Fiber &amp; Cabling</h3><p>Structured LAN, FTTH splicing, data-rack cabling.</p></div>
      <div class="node-item"><div class="node-dot"></div><h3>Safety &amp; Testing</h3><p>Compliance audits, thermal imaging, Earth resistance testing.</p></div>
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="wrap">
    <div class="eyebrow" style="color:#dd8f31;">Flagship Bundle</div>
    <div class="grid" style="grid-template-columns: 1fr 1fr; align-items:center; gap:52px;">
      <div>
        <h2>The Smart Solar Security Hub</h2>
        <p>Solar PV, AI CCTV, smart lighting, and battery backup &mdash; packaged into a single off-grid or hybrid turnkey system. Built for remote properties, farms, and gated homes that need power and security to work as one system, not three separate purchases.</p>
        <a class="btn btn--amber" href="solutions/smart-solar-security-hub.html">Explore the Bundle</a>
      </div>
      <div class="card card--ink">
        <span class="num mono">01 / 04</span>
        <h3>Why bundle instead of buying separately?</h3>
        <p>One site survey instead of three. One warranty instead of three. One team accountable when something needs troubleshooting &mdash; not a dispute over whose system caused the fault.</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="eyebrow">Why Homeowners &amp; Businesses Choose Us</div>
    <h2 style="max-width:24ch;">The questions every Kenyan buyer asks before paying a deposit &mdash; answered up front.</h2>
    <div class="gridline"></div>
    <div class="grid grid--3">
      <div class="card">
        <span class="num mono">Licensing</span>
        <h3>Verified, not just claimed</h3>
        <p>EPRA, NCA, and CAK license numbers are published on our site &mdash; not just badges. You can verify them directly with the regulator.</p>
        <a class="more" href="why-smartech.html">See our credentials &rarr;</a>
      </div>
      <div class="card">
        <span class="num mono">Guarantee</span>
        <h3>A written warranty, not a promise</h3>
        <p>Workmanship warranty and a stated response-time commitment on every job &mdash; in writing, before you pay a deposit.</p>
        <a class="more" href="why-smartech.html">Read our guarantee &rarr;</a>
      </div>
      <div class="card">
        <span class="num mono">Availability</span>
        <h3>Still here after installation</h3>
        <p>Maintenance contracts, 24/7 emergency response, and repair support &mdash; for systems we installed, and systems we didn't.</p>
        <a class="more" href="emergency.html">See emergency response &rarr;</a>
      </div>
    </div>
  </div>
</section>

<section class="section section--dim">
  <div class="wrap">
    <div class="stat-row">
      <div class="stat"><span class="num">5</span><span class="label">Integrated Service Lines</span></div>
      <div class="stat"><span class="num">6</span><span class="label">Counties Served</span></div>
      <div class="stat"><span class="num">24/7</span><span class="label">Emergency Response</span></div>
      <div class="stat"><span class="num">EPRA·NCA·CAK</span><span class="label">Fully Licensed</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap center max-w" style="margin:0 auto;">
    <h2>Ready for a system that doesn't need three vendors to fix?</h2>
    <p>Get a free, no-obligation site survey and itemized quote &mdash; solar, security, electrical, or all three.</p>
    <a class="btn btn--amber" href="get-a-quote.html">Get My Free Quote</a>
  </div>
</section>
"""

    write("index.html", base(
        title="Smartech Technologies | Integrated Solar, CCTV, Electrical &amp; Networking Contractor in Kenya",
        description="Integrated Solar, CCTV, Electrical & Networking Contractor in Kenya. Smartech Technologies provides solar, CCTV, electrical, networking, cabling and security solutions.",
        p="",
        body=home_body,
        canonical="/",
    ))

    # ============================================================
    # WHY SMARTECH — p = ''
    # ============================================================
    why_body = f"""
<section class="section--tight">
  <div class="wrap">
    <div class="eyebrow">Trust &amp; Accountability</div>
    <h1>One team, fully licensed,<br>fully accountable.</h1>
    <p class="lede" style="color:var(--text-soft); font-size:1.05rem;">Choosing a contractor for your solar, security, or electrical system means trusting them with your home, your business, and your money. Here's exactly what protects you when you choose Smartech.</p>
  </div>
</section>

<section class="section section--dim">
  <div class="wrap">
    <div class="eyebrow">Certifications</div>
    <h2>Verified, not just claimed</h2>
    <p class="max-w">Buyers and procurement teams increasingly check licensing directly with the regulator before signing a contract. We publish ours so you can too.</p>
    <div class="grid grid--4" style="margin-top:30px;">
      <div class="card"><span class="num mono">EPRA</span><h3>Energy &amp; Solar</h3><p>Publish the current EPRA licence class and number here after verification, so customers can confirm the credential directly with the regulator.</p></div>
      <div class="card"><span class="num mono">NCA</span><h3>Construction Registration</h3><p>Publish the current NCA registration category and number here after verification.</p></div>
      <div class="card"><span class="num mono">CA</span><h3>ICT Infrastructure</h3><p>Publish any applicable Communications Authority credential and licence number here after verification.</p></div>
      <div class="card"><span class="num mono">KRA</span><h3>Tax Compliant</h3><p>Valid Tax Compliance Certificate available on request for procurement and corporate clients.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="eyebrow">Our Written Guarantee</div>
    <h2 style="max-width:26ch;">A guarantee you can hold us to &mdash; not a marketing line.</h2>
    <div class="gridline"></div>
    <div class="grid grid--2">
      <div class="card">
        <h3>Workmanship warranty</h3>
        <p>State the exact workmanship warranty period in every quotation and contract, separately from manufacturer equipment warranties.</p>
      </div>
      <div class="card">
        <h3>Response-time commitment</h3>
        <p>Response commitments should be stated by location and service level in the customer's contract, rather than using an unverified blanket promise.</p>
      </div>
      <div class="card">
        <h3>We service systems we didn't install</h3>
        <p>If another contractor's work is failing, our team will diagnose it honestly and give you a clear repair-or-replace recommendation &mdash; no obligation to switch providers.</p>
      </div>
      <div class="card">
        <h3>One contract, one point of contact</h3>
        <p>If your solar, security, and electrical systems are all Smartech-installed, one call resolves any issue &mdash; instead of three vendors blaming each other.</p>
      </div>
    </div>
  </div>
</section>

<section class="section section--ink">
  <div class="wrap">
    <div class="eyebrow" style="color:#dd8f31;">Client Feedback</div>
    <h2>What our clients say</h2>
    <p class="max-w">[Embed a live Google Reviews widget here once your Google Business Profile has reviews &mdash; showing live, verifiable reviews builds more trust than a static testimonials list.]</p>
    <div class="grid grid--3" style="margin-top:10px;">
      <div class="card card--ink"><p>&ldquo;[Client testimonial placeholder &mdash; replace with a real review, attributed with name and location.]&rdquo;</p></div>
      <div class="card card--ink"><p>&ldquo;[Client testimonial placeholder &mdash; replace with a real review, attributed with name and location.]&rdquo;</p></div>
      <div class="card card--ink"><p>&ldquo;[Client testimonial placeholder &mdash; replace with a real review, attributed with name and location.]&rdquo;</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap center max-w" style="margin:0 auto;">
    <h2>Still deciding?</h2>
    <p>Read our guide: <a href="blog/how-to-choose-a-contractor.html" style="text-decoration:underline;">How to Choose a Solar or Security Contractor in Kenya &mdash; 7 Questions to Ask Before You Pay a Deposit</a></p>
    <div class="hero-ctas" style="justify-content:center;">
      <a class="btn btn--amber" href="get-a-quote.html">Get a Free Site Assessment</a>
      <a class="btn btn--outline" href="{wa_link()}">WhatsApp Us Now</a>
    </div>
  </div>
</section>
"""
    write("why-smartech.html", base(
        title="Our Guarantee &amp; Certifications | Why Choose Smartech Technologies",
        description="See exactly what protects you when you hire Smartech: EPRA, NCA and CAK licensing, a written workmanship warranty, and one accountable team.",
        p="",
        body=why_body,
        canonical="/why-smartech.html",
    ))

    # ============================================================
    # EMERGENCY 24/7 — p = ''
    # ============================================================
    emergency_body = f"""
<section class="section--tight section--ink">
  <div class="wrap">
    <div class="eyebrow" style="color:#dd8f31;">24/7 Emergency Response</div>
    <h1>Power failure or system down?<br>We're on our way.</h1>
    <p class="lede">24/7 emergency response for power outages, electrical faults, and security systems that stop working &mdash; across Nairobi, Kiambu, Machakos, and Kajiado.</p>
    <div class="hero-ctas">
      <a class="btn btn--amber" href="tel:{EMERGENCY_PHONE.replace(' ', '')}">Call Now: {EMERGENCY_PHONE}</a>
      <a class="btn btn--outline-light" href="{wa_link('Emergency - I need help now')}">WhatsApp Us</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="eyebrow">We Respond To</div>
    <h2>Common emergencies we handle</h2>
    <div class="grid grid--3" style="margin-top:20px;">
      <div class="card"><h3>Sudden power failure</h3><p>Affecting your home or business, whether the cause is internal wiring or a suspected grid issue.</p></div>
      <div class="card"><h3>Sparking or exposed wiring</h3><p>Overheating panels, exposed cable, or any electrical fire hazard.</p></div>
      <div class="card"><h3>Backup power not switching over</h3><p>Inverter, battery, or UPS systems that fail to kick in during an outage.</p></div>
      <div class="card"><h3>Security system offline</h3><p>CCTV, alarms, or access control that stop working unexpectedly.</p></div>
      <div class="card"><h3>Water-damaged systems</h3><p>Electrical systems affected by flooding, leaks, or storm damage.</p></div>
      <div class="card"><h3>Solar system fault</h3><p>Sudden drop in output, inverter errors, or a system that has stopped generating entirely.</p></div>
    </div>
  </div>
</section>

<section class="section section--dim">
  <div class="wrap">
    <div class="eyebrow">Our Process</div>
    <h2>What happens when you call</h2>
    <div class="steps" style="margin-top:20px; max-width:760px;">
      <div class="step"><div class="stepnum"></div><div><h3>You call or WhatsApp</h3><p>Describe the issue, your location, and whether anyone is at immediate risk.</p></div></div>
      <div class="step"><div class="stepnum"></div><div><h3>We dispatch the nearest technician</h3><p>Response time depends on location, traffic, severity, and technician availability.</p></div></div>
      <div class="step"><div class="stepnum"></div><div><h3>On-site diagnosis</h3><p>We identify whether the fault is inside your property or a wider grid issue, and give you a clear fix and cost before starting work.</p></div></div>
      <div class="step"><div class="stepnum"></div><div><h3>Repair or safe temporary fix</h3><p>So your home or business is safe and, where possible, back online the same day.</p></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap grid grid--2">
    <div class="card">
      <h3>A note on grid outages</h3>
      <p>Not every power failure is inside your property &mdash; Kenya Power grid outages happen too. If the fault is on the grid side, we'll tell you honestly rather than charge you for work that won't fix the problem, and we can help you plan backup power so the next outage doesn't disrupt you the same way.</p>
      <a class="more" href="repairs/backup-power-repair.html">See backup power options &rarr;</a>
    </div>
    <div class="card">
      <h3>Prefer to prevent this next time?</h3>
      <p>Ask about our Maintenance Contracts (AMAs) &mdash; scheduled inspections that catch faults before they become emergencies.</p>
      <a class="more" href="get-a-quote.html">Ask about maintenance contracts &rarr;</a>
    </div>
  </div>
</section>

<section class="section--tight">
  <div class="wrap trustbar">
    <span><strong>EPRA</strong> [Class A] Licensed</span>
    <span><strong>NCA</strong> [Class 1] Registered</span>
    <span>Serving Nairobi, Kiambu, Machakos, Kajiado &mdash; 24/7</span>
  </div>
</section>
"""
    write("emergency.html", base(
        title="24/7 Emergency Electrical &amp; Power Response Nairobi | Smartech Technologies",
        description="Sudden power failure, sparking wires, or your security system down? Smartech's emergency team responds across Nairobi and surrounding counties, day or night.",
        p="",
        body=emergency_body,
        canonical="/emergency.html",
    ))

    # ============================================================
    # SERVICE PAGE TEMPLATE — used for all 5 service verticals, p = '../'
    # ============================================================
    def service_page(slug, title_short, meta_title, meta_desc, intro, keyword_tag,
                      subservices, audience, faqs, related_repair=None, equipment=None, equipment_note=None):
        sub_html = "".join(
            f'<div class="card"><span class="num mono">0{i+1}</span><h3>{name}</h3><p>{desc}</p></div>'
            for i, (name, desc) in enumerate(subservices)
        )
        faq_html = "".join(
            f'<div class="step"><div class="stepnum" style="visibility:hidden;"></div>'
            f'<div><h3>{q}</h3><p>{a}</p></div></div>'
            for q, a in faqs
        )
        repair_cta = ""
        if related_repair:
            repair_cta = f"""
            <div class="card" style="margin-top:28px;">
              <h3>Already have a {title_short.lower()} system that's failing?</h3>
              <p>We repair and service systems we didn't install too.</p>
              <a class="more" href="../repairs/{related_repair}">See repair &amp; troubleshooting support &rarr;</a>
            </div>"""

        equipment_section = ""
        if equipment:
            eq_cards = "".join(
                f'<div class="card"><span class="num mono">{tag}</span><h3>{brand}</h3><p>{desc}</p></div>'
                for tag, brand, desc in equipment
            )
            equipment_section = f"""
<section class="section section--dim">
  <div class="wrap">
    <div class="eyebrow">Equipment We Work With</div>
    <h2 style="max-width:30ch;">We're not tied to one brand &mdash; we spec the equipment that fits your budget and risk profile.</h2>
    <p class="max-w">{equipment_note or ""}</p>
    <div class="grid grid--3" style="margin-top:24px;">
      {eq_cards}
    </div>
    <p style="margin-top:18px; font-size:0.82rem;">Brand names are the property of their respective manufacturers. Availability and pricing vary &mdash; we'll confirm exact models during your free site survey.</p>
  </div>
</section>"""

        body = f"""
<section class="section--tight">
  <div class="wrap">
    <div class="eyebrow">{keyword_tag}</div>
    <h1>{title_short}</h1>
    <p class="lede" style="color:var(--text-soft); font-size:1.05rem;">{intro}</p>
    <div class="hero-ctas">
      <a class="btn btn--amber" href="../get-a-quote.html">Get a Free Quote</a>
      <a class="btn btn--outline" href="{wa_link()}">WhatsApp Us</a>
    </div>
  </div>
</section>

<section class="section section--dim">
  <div class="wrap trustbar">
    <span><strong>EPRA</strong> Licensed</span>
    <span><strong>NCA</strong> Registered</span>
    <span>Workmanship Warranty on Every Job</span>
    <span>Serving: {audience}</span>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="eyebrow">What's Included</div>
    <h2>Services under this vertical</h2>
    <div class="grid grid--3" style="margin-top:24px;">
      {sub_html}
    </div>
    {repair_cta}
  </div>
</section>
{equipment_section}
<section class="section section--ink">
  <div class="wrap">
    <div class="eyebrow" style="color:#dd8f31;">Why Bundle This With Other Systems?</div>
    <h2 style="max-width:28ch;">This system doesn't have to be your only Smartech install.</h2>
    <p class="max-w">Solar, security, electrical, cabling and safety testing share the same wiring, risers, and plant rooms &mdash; which is exactly why one integrator is more reliable than three separate vendors. See our flagship bundle:</p>
    <a class="btn btn--amber" href="../solutions/smart-solar-security-hub.html">Explore the Smart Solar Security Hub</a>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="eyebrow">Frequently Asked</div>
    <h2>Common questions</h2>
    <div class="steps" style="margin-top:20px; max-width:760px;">
      {faq_html}
    </div>
  </div>
</section>

<section class="section section--dim">
  <div class="wrap center max-w" style="margin:0 auto;">
    <h2>Get an itemized quote for {title_short.lower()}</h2>
    <p>Free site survey. No obligation. Clear pricing before you commit.</p>
    <a class="btn btn--amber" href="../get-a-quote.html">Request My Quote</a>
  </div>
</section>
"""
        write(f"services/{slug}.html", base(
            title=meta_title,
            description=meta_desc,
            p="../",
            body=body,
            canonical=f"/services/{slug}.html",
            breadcrumb=[("Home", "{p}index.html"), ("Services", None), (title_short, None)],
        ))

    service_page(
        slug="solar",
        title_short="Solar & Green Energy Installation",
        meta_title="Solar Installation Kenya | Hybrid &amp; Off-Grid Systems &ndash; Smartech",
        meta_desc="EPRA-certified hybrid, on-grid and off-grid solar installation in Kenya, including battery storage and solar water pumping. Free site survey.",
        keyword_tag="Solar Installation Company Kenya",
        intro="Hybrid inverter systems with battery storage, solar water pumping, and EPRA-certified commercial retrofits &mdash; sized correctly the first time, with a written performance estimate before you commit.",
        audience="Homeowners, commercial properties, factories, farms and schools",
        subservices=[
            ("Hybrid Inverter + BESS", "Battery Energy Storage Systems paired with hybrid inverters for seamless grid/solar/battery switching."),
            ("On-Grid Solar", "Grid-tied systems sized to offset your Kenya Power bill, with net-metering guidance."),
            ("Off-Grid Solar", "Fully independent systems for remote properties and farms with no reliable grid access."),
            ("Solar Water Pumping", "Agricultural and residential solar pumping systems, sized to your borehole or tank demand."),
        ],
        faqs=[
            ("How much does a hybrid solar system cost in Nairobi?", "Cost depends on your daily consumption, battery capacity, and roof/ground mounting requirements. We provide an itemized quote &mdash; panel count, inverter type, battery capacity, and expected output &mdash; before any deposit."),
            ("Will you disappear after installation?", "No. Every install includes a written workmanship warranty and a maintenance contract option. See our full guarantee on the Why Smartech page."),
            ("Do you service systems installed by another company?", "Yes &mdash; we diagnose and repair solar systems regardless of who installed them."),
        ],
        related_repair="solar-repair.html",
        equipment_note="These are among the most widely deployed hybrid inverter and battery brands in the East African market, known for reliable MPPT charging, app-based monitoring, and strong local parts availability.",
        equipment=[
            ("Inverter", "Deye Hybrid Inverters", "Widely used 48V low-voltage hybrid inverters with strong battery management (BMS) protection and app-based remote monitoring — a common choice for residential and small commercial hybrid systems."),
            ("Inverter", "Growatt Solar Inverters", "Established on-grid and off-grid inverter range with WiFi monitoring, used across a broad range of system sizes from residential to light commercial."),
            ("Battery / Storage", "Felicity Solar", "LiFePO4 battery storage systems with built-in battery management for overvoltage, overload and over-temperature protection, popular in the East African solar market."),
        ],
    )


    service_page(
        slug="security",
        title_short="AI CCTV, Alarm &amp; Security Systems",
        meta_title="CCTV &amp; Alarm System Installation Nairobi | Smartech Technologies",
        meta_desc="AI-powered CCTV, alarm systems, biometric access control and IP intercoms for homes and offices, installed and monitored across Nairobi and Kenya.",
        keyword_tag="Alarm & CCTV Installation Nairobi",
        intro="AI-powered surveillance, alarm systems, biometric access control, and IP video intercoms for homes and offices &mdash; engineered for the layout and risk profile of your specific property.",
        audience="Gated communities, corporate offices, warehouses, high-value residences",
        subservices=[
            ("AI CCTV Surveillance", "Person and vehicle detection, remote viewing, and cloud or local storage options."),
            ("Alarm Systems for Homes &amp; Offices", "Intrusion alarms for doors, windows, and perimeter fencing, plus panic buttons for offices &mdash; monitored 24/7 and linked to your CCTV and access control, with battery backup so they keep working during a power outage."),
            ("Biometric Access Control", "Smart locks, fingerprint and card access for gates, offices, and secure rooms."),
            ("IP Video Intercoms", "Two-way video entry systems integrated with your access control."),
            ("Alarm Monitoring &amp; Dispatch", "Round-the-clock monitoring with rapid-response dispatch when an alarm is triggered."),
        ],
        faqs=[
            ("How many cameras do I need for my property?", "It depends on entry points, blind spots, and whether you need identification-grade footage or general monitoring. A free site survey gives you an exact camera count and placement plan."),
            ("Do you install alarm systems for offices as well as homes?", "Yes &mdash; we design intrusion and panic alarm systems for both residential compounds and commercial offices, including server rooms and stock areas where an office has extra assets to protect."),
            ("Can you integrate CCTV with my existing gate and alarm?", "Yes &mdash; we design around what you already have where it makes sense, rather than requiring a full rip-and-replace."),
            ("What happens if my cameras or alarm go offline?", "Our repair &amp; troubleshooting team responds to security-system faults, including systems installed by other providers."),
        ],
        related_repair="cctv-repair.html",
        equipment_note="Hikvision and Dahua together account for the majority of the global CCTV market and lead on AI analytics; Uniview is a strong professional alternative. We spec the brand and tier based on your budget and how much AI detection your property actually needs.",
        equipment=[
            ("CCTV", "Hikvision", "The world's largest video surveillance manufacturer, with deep-learning AI analytics — real-time human/vehicle detection, facial recognition, and behavior analysis — well suited to higher-security commercial and gated-community deployments."),
            ("CCTV", "Dahua Technology", "A close second globally, known for strong 4K multi-sensor cameras and AI-enabled recorders (NVRs) at competitive pricing, with analytics comparable to Hikvision for most residential and office use cases."),
            ("CCTV", "Uniview", "A professional-grade alternative offering solid AI analytics — including vehicle detection and face recognition — often used where budget or supply considerations favor an alternative to the two market leaders."),
        ],
    )


    service_page(
        slug="electrical",
        title_short="Electrical &amp; Power Installations",
        meta_title="Commercial Electrical Contractor Nairobi | Smartech Technologies",
        meta_desc="Commercial and industrial electrical installation, surge protection, backup power systems and power quality audits across Kenya.",
        keyword_tag="Commercial Electrician Nairobi",
        intro="Commercial and industrial electrical installations, surge protection, backup power systems, and panel board wiring &mdash; built to code, with power quality audits available for facilities that need to prove compliance.",
        audience="Developers, factories, data centers, health facilities, retail centers",
        subservices=[
            ("Commercial &amp; Industrial Wiring", "New installations and upgrades sized to your facility's actual load requirements."),
            ("Surge Protection", "Whole-building surge protection to prevent equipment damage during voltage fluctuations."),
            ("Backup Power Systems", "Generator connections, automatic transfer switches, and UPS integration."),
            ("Panel Board &amp; Switchgear", "Installation, upgrades, and power quality audits on distribution panels."),
        ],
        faqs=[
            ("Do you handle both residential and commercial electrical work?", "Yes &mdash; from single-home wiring upgrades to full commercial and industrial installations."),
            ("Can you connect a generator to my existing system safely?", "Yes, including automatic transfer switches so backup power engages seamlessly during an outage."),
            ("What if I have a live emergency right now?", "Call our 24/7 emergency line &mdash; see the Emergency page for immediate response."),
        ],
        related_repair="backup-power-repair.html",
    )

    service_page(
        slug="cabling",
        title_short="Fiber &amp; Structured Cabling",
        meta_title="Structured Cabling &amp; Fiber Installation Kenya | Smartech Technologies",
        meta_desc="Structured LAN cabling, FTTH fiber splicing and data-center rack cabling for offices, ISPs and business parks across Kenya.",
        keyword_tag="Structured Cabling Installation Kenya",
        intro="Structured LAN cabling, fiber optic splicing and FTTH drop lines, and data center rack cabling &mdash; installed and terminated to support current bandwidth demand and future capacity, not just today's device count.",
        audience="ISPs, office buildings, business parks, tech parks",
        subservices=[
            ("Structured LAN Cabling", "CAT6/CAT6A cabling for offices, designed around current and future device density."),
            ("Fiber Splicing &amp; FTTH", "Fiber-to-the-home drop lines and enterprise backbone splicing."),
            ("Data Center Rack Cabling", "Rack, patch panel, and cable management for server rooms and data closets."),
            ("Network Audits", "Assessment of existing cabling infrastructure against current standards."),
        ],
        faqs=[
            ("Do you work with ISPs on FTTH rollouts?", "Yes &mdash; we support fiber splicing and drop-line installation for ISP partners as well as direct enterprise clients."),
            ("Can you cable a new office before we move in?", "Yes, including full site design so cabling is in place before desks and racks arrive."),
            ("Are you licensed for ICT infrastructure work?", "Yes &mdash; Smartech is a CAK licensed contractor for structured cabling and ICT infrastructure."),
        ],
    )

    service_page(
        slug="safety-testing",
        title_short="Safety &amp; Compliance Testing",
        meta_title="EPRA Electrical Safety Audit &amp; Inspection Kenya | Smartech Technologies",
        meta_desc="Statutory electrical safety compliance audits, thermal imaging and Earth resistance testing for industrial facilities and insurance clients in Kenya.",
        keyword_tag="EPRA Electrical Safety Audit Kenya",
        intro="Statutory electrical safety compliance audits, thermal imaging for switchgears, solar yield inspections, and Earth resistance testing &mdash; documented reports you can hand directly to insurers, regulators, or building management.",
        audience="Industrial facilities, insurance clients, building managers",
        subservices=[
            ("Compliance Audits", "Statutory electrical safety audits with a documented compliance report."),
            ("Thermal Imaging", "Switchgear and panel thermal inspection to catch faults before they cause failures."),
            ("Solar Yield Inspections", "Performance verification for existing solar installations, any installer."),
            ("Earth Resistance Testing", "Grounding system testing required for safety compliance."),
        ],
        faqs=[
            ("What does an EPRA safety audit involve?", "A full inspection of your electrical installation against EPRA safety standards, with a written compliance report you can submit to regulators or insurers."),
            ("How often should a facility be audited?", "Annual audits are standard for most commercial and industrial facilities; higher-risk sites may need more frequent inspection."),
            ("Can you audit a system another contractor installed?", "Yes &mdash; audits are independent of who installed the system."),
        ],
    )

    # ============================================================
    # SOLUTIONS — p = '../'
    # ============================================================
    hub_body = f"""
<section class="section--tight section--ink">
  <div class="wrap">
    <div class="eyebrow" style="color:#dd8f31;">Flagship Bundle &middot; Low-Competition, High-Intent</div>
    <h1>The Smart Solar Security Hub</h1>
    <p class="lede">Solar PV + AI CCTV + Smart Lighting + Battery Backup, packaged into a single off-grid or hybrid turnkey system. One site survey, one contract, one team accountable for power and security together.</p>
    <div class="hero-ctas">
      <a class="btn btn--amber" href="../get-a-quote.html">Get a Bundle Quote</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="eyebrow">What's Inside the Bundle</div>
    <h2>Four systems, engineered as one</h2>
    <div class="grid grid--4" style="margin-top:24px;">
      <div class="card"><span class="num mono">01</span><h3>Solar PV</h3><p>Sized to your consumption and battery capacity.</p></div>
      <div class="card"><span class="num mono">02</span><h3>AI CCTV</h3><p>Person/vehicle detection, powered by your solar and battery.</p></div>
      <div class="card"><span class="num mono">03</span><h3>Smart Lighting</h3><p>Motion-triggered perimeter and pathway lighting.</p></div>
      <div class="card"><span class="num mono">04</span><h3>Battery Backup</h3><p>Keeps security systems running through outages &mdash; the scenario when you need them most.</p></div>
    </div>
  </div>
</section>

<section class="section section--dim">
  <div class="wrap">
    <div class="eyebrow">Why This, Not Separate Vendors</div>
    <h2 style="max-width:28ch;">Security systems are only as reliable as their power source.</h2>
    <p class="max-w">A CCTV system with no power during an outage isn't protecting anything. Buying solar and security separately means two vendors who've never coordinated on load calculations, wiring runs, or what happens when one system fails. Bundling means we design the power budget and the security coverage together, from day one.</p>
    <div class="grid grid--2" style="margin-top:24px;">
      <div class="card"><h3>Ideal for</h3><p>Remote properties, farms, gated homes, and any site where grid power and security response are both unreliable.</p></div>
      <div class="card"><h3>Delivered as</h3><p>A single turnkey installation with one warranty covering the whole bundle &mdash; not four separate warranty documents.</p></div>
    </div>
  </div>
</section>

<section class="section center max-w" style="margin:0 auto;">
  <h2>See what the bundle costs for your property</h2>
  <p>Free site survey, sized to your actual property and risk profile.</p>
  <a class="btn btn--amber" href="../get-a-quote.html">Request a Bundle Quote</a>
</section>
"""
    write("solutions/smart-solar-security-hub.html", base(
        title="Smart Solar Security Hub | All-in-One Off-Grid Package &ndash; Smartech",
        description="Solar PV, AI CCTV, smart lighting and battery backup bundled into one turnkey off-grid or hybrid system for remote properties, farms and gated homes.",
        p="../",
        body=hub_body,
        canonical="/solutions/smart-solar-security-hub.html",
        breadcrumb=[("Home", "{p}index.html"), ("Solutions", None), ("Smart Solar Security Hub", None)],
    ))

    def solution_page(slug, title, meta_title, meta_desc, intro, points):
        pts = "".join(f'<div class="card"><h3>{h}</h3><p>{d}</p></div>' for h, d in points)
        body = f"""
<section class="section--tight">
  <div class="wrap">
    <div class="eyebrow">Solutions</div>
    <h1>{title}</h1>
    <p class="lede" style="color:var(--text-soft); font-size:1.05rem;">{intro}</p>
    <a class="btn btn--amber" href="../get-a-quote.html">Get a Free Quote</a>
  </div>
</section>
<section class="section section--dim">
  <div class="wrap grid grid--3">
    {pts}
  </div>
</section>
"""
        write(f"solutions/{slug}.html", base(
            title=meta_title, description=meta_desc, p="../", body=body,
            canonical=f"/solutions/{slug}.html",
            breadcrumb=[("Home", "{p}index.html"), ("Solutions", None), (title, None)],
        ))

    solution_page(
        slug="residential",
        title="Residential Smart Homes",
        meta_title="Smart Home Solar, Security &amp; Alarm Systems Kenya | Smartech Technologies",
        meta_desc="Solar, CCTV, alarm systems, smart access and backup power packages designed for Kenyan homes and gated residences.",
        intro="Solar, security, and backup power designed around how a household actually runs &mdash; not a generic package.",
        points=[
            ("Solar sized to your home", "Panels and battery sized to your real daily consumption, not a one-size estimate."),
            ("Security that fits your layout", "Camera and access placement based on your compound's actual entry points."),
            ("Home alarm systems", "Intrusion alarms for doors, windows, and perimeter fencing, monitored and linked to your CCTV and gate access &mdash; with a battery backup so they still work during an outage."),
            ("One maintenance contract", "A single annual agreement covering every system in the home."),
        ],
    )
    solution_page(
        slug="commercial",
        title="Commercial &amp; Industrial",
        meta_title="Commercial Solar, Security &amp; Alarm Systems Kenya | Smartech Technologies",
        meta_desc="Integrated solar, security, alarm systems, electrical and safety compliance solutions for commercial and industrial facilities in Kenya.",
        intro="For facilities where downtime has a direct cost &mdash; power, security, and compliance engineered together.",
        points=[
            ("Load-matched power systems", "Solar, backup power, and surge protection sized to your operational load."),
            ("Office alarm systems", "Intrusion and panic alarms across entry points, server rooms, and stock areas, integrated with access control and monitored around the clock."),
            ("Compliance built in", "Safety audits and documentation ready for insurers and regulators."),
            ("Maintenance agreements (AMAs)", "Bundled inspection and maintenance across every system we install."),
        ],
    )
    solution_page(
        slug="agriculture",
        title="Agriculture &amp; Off-Grid",
        meta_title="Off-Grid Solar &amp; Security for Farms Kenya | Smartech Technologies",
        meta_desc="Off-grid solar power, solar water pumping and remote-property security for farms and agricultural sites across Kenya.",
        intro="Reliable power and security for sites where grid connection isn't an option &mdash; and where a failure isn't just inconvenient, it's costly.",
        points=[
            ("Solar water pumping", "Sized to your borehole yield and irrigation demand."),
            ("Off-grid power systems", "Fully independent solar and battery systems for remote sites."),
            ("Remote-site security", "Camera and alarm systems built for properties without permanent staff on-site."),
        ],
    )

    # ============================================================
    # REPAIRS & TROUBLESHOOTING — p = '../'
    # ============================================================
    def repair_page(slug, title, meta_title, meta_desc, symptoms, keyword):
        sym_html = "".join(f'<li>{s}</li>' for s in symptoms)
        body = f"""
<section class="section--tight">
  <div class="wrap">
    <div class="eyebrow">{keyword}</div>
    <h1>{title}</h1>
    <p class="lede" style="color:var(--text-soft); font-size:1.05rem;">We repair and troubleshoot systems &mdash; whether we installed them or not. Fast diagnosis, honest recommendation, clear pricing before any work starts.</p>
    <div class="hero-ctas">
      <a class="btn btn--amber" href="tel:{EMERGENCY_PHONE.replace(' ', '')}">Call {EMERGENCY_PHONE}</a>
      <a class="btn btn--outline" href="{wa_link()}">WhatsApp Us</a>
    </div>
  </div>
</section>
<section class="section section--dim">
  <div class="wrap">
    <h2>Common issues we fix</h2>
    <ul class="checklist" style="margin-top:20px; max-width:640px;">{sym_html}</ul>
  </div>
</section>
<section class="section">
  <div class="wrap center max-w" style="margin:0 auto;">
    <h2>Not an emergency, just needs fixing?</h2>
    <p>Book a diagnostic visit and we'll give you a clear repair quote before starting work.</p>
    <a class="btn btn--amber" href="../get-a-quote.html">Book a Diagnostic Visit</a>
  </div>
</section>
"""
        write(f"repairs/{slug}.html", base(
            title=meta_title, description=meta_desc, p="../", body=body,
            canonical=f"/repairs/{slug}.html",
            breadcrumb=[("Home", "{p}index.html"), ("Repairs &amp; Troubleshooting", None), (title, None)],
        ))

    repair_page(
        slug="solar-repair",
        title="Solar System Repair &amp; Troubleshooting",
        meta_title="Solar System Repair Nairobi | We Fix Any Brand &ndash; Smartech",
        meta_desc="Solar system stopped working? Smartech diagnoses and repairs solar installations across Kenya, regardless of who installed it.",
        keyword="Solar System Not Working",
        symptoms=[
            "Solar output has suddenly dropped or stopped entirely",
            "Inverter is showing an error code or fault light",
            "Battery isn't holding charge or isn't switching over during outages",
            "System was installed by another company and they're no longer responsive",
        ],
    )
    repair_page(
        slug="cctv-repair",
        title="CCTV &amp; Security System Repair",
        meta_title="CCTV Repair Nairobi | Camera &amp; Alarm Troubleshooting &ndash; Smartech",
        meta_desc="CCTV not working? Smartech diagnoses and repairs security camera, alarm and access control systems across Kenya.",
        keyword="CCTV Not Working Fix",
        symptoms=[
            "Cameras have gone offline or show a blank/frozen feed",
            "Remote viewing app has stopped connecting",
            "Alarm system is triggering false alerts or not triggering at all",
            "Access control (biometric/smart lock) is malfunctioning",
        ],
    )
    repair_page(
        slug="backup-power-repair",
        title="Backup Power &amp; Generator Repair",
        meta_title="Backup Power Repair Nairobi | Generator &amp; UPS Troubleshooting &ndash; Smartech",
        meta_desc="Backup power not switching over during outages? Smartech diagnoses and repairs generator connections, UPS and transfer switches across Kenya.",
        keyword="Backup Power Not Working",
        symptoms=[
            "Generator isn't starting or isn't connecting automatically during an outage",
            "UPS is not holding charge or shutting down critical equipment unexpectedly",
            "Automatic transfer switch is not switching between grid and backup power",
            "Backup system is undersized for your current load",
        ],
    )

    # ============================================================
    # FINANCING — p = ''
    # ============================================================
    financing_body = f"""
<section class="section--tight">
  <div class="wrap">
    <div class="eyebrow">Financing &amp; Payment Plans</div>
    <h1>Solar and security financing options in Kenya</h1>
    <p class="lede" style="color:var(--text-soft); font-size:1.05rem;">Going solar or upgrading security shouldn't require paying the full cost upfront. We work with financing partners to offer flexible payment terms.</p>
  </div>
</section>
<section class="section section--dim">
  <div class="wrap grid grid--3">
    <div class="card"><span class="num mono">Option 01</span><h3>Pay-As-You-Go</h3><p>Spread the cost of your solar or security system over manageable monthly installments.</p></div>
    <div class="card"><span class="num mono">Option 02</span><h3>SACCO Financing</h3><p>We work with SACCO partners so members can finance installations through their existing SACCO.</p></div>
    <div class="card"><span class="num mono">Option 03</span><h3>Bank Loan Support</h3><p>We provide the documentation your bank needs to process an asset finance or personal loan application.</p></div>
  </div>
</section>
<section class="section">
  <div class="wrap center max-w" style="margin:0 auto;">
    <h2>Talk to us about what fits your budget</h2>
    <p>Every property is different &mdash; we'll walk through what a monthly payment could look like for your specific system.</p>
    <a class="btn btn--amber" href="get-a-quote.html">Get a Quote With Financing Options</a>
  </div>
</section>
"""
    write("financing.html", base(
        title="Solar &amp; Security Financing Options Kenya | Smartech Technologies",
        description="Pay-as-you-go, SACCO financing, and bank loan support for solar and security installations in Kenya.",
        p="", body=financing_body, canonical="/financing.html",
    ))

    # ============================================================
    # GET A QUOTE — p = ''
    # ============================================================
    quote_body = f"""
<section class="section--tight">
  <div class="wrap">
    <div class="eyebrow">Free, No-Obligation Quote</div>
    <h1>Get an itemized quote in one visit</h1>
    <p class="lede" style="color:var(--text-soft); font-size:1.05rem;">Tell us what you need and we'll schedule a free site survey. You'll get an itemized proposal &mdash; specific equipment, capacity, and cost &mdash; before you decide anything.</p>
  </div>
</section>
<section class="section section--dim">
  <div class="wrap" style="max-width:760px;">
    <form class="formcard" id="quote-form">
      <div class="formrow">
        <div><label for="name">Full Name</label><input id="name" type="text" required></div>
        <div><label for="phone">Phone Number</label><input id="phone" type="tel" required></div>
      </div>
      <div class="formrow">
        <div><label for="location">Location / County</label><input id="location" type="text" placeholder="e.g. Kiambu"></div>
        <div><label for="service">Service Needed</label>
          <select id="service">
            <option>Solar &amp; Green Energy</option>
            <option>Security Systems</option>
            <option>Electrical &amp; Power</option>
            <option>Fiber &amp; Cabling</option>
            <option>Safety &amp; Testing</option>
            <option>Smart Solar Security Hub (Bundle)</option>
            <option>Not sure &mdash; need advice</option>
          </select>
        </div>
      </div>
      <div style="margin-bottom:16px;">
        <label for="details">Tell us about your property</label>
        <textarea id="details" rows="4" placeholder="Property type, approximate size, and what you're trying to solve"></textarea>
      </div>
      <button class="btn btn--amber" type="submit" style="border:none; width:100%; justify-content:center;">Request My Free Quote</button>
      <p id="form-status" class="small-note" role="status" aria-live="polite" style="margin-top:12px;"></p>
      <p style="margin-top:14px; font-size:0.82rem;">Prefer to talk now? <a href="{wa_link()}" style="text-decoration:underline;">WhatsApp us</a> or call <a href="tel:{PHONE_DISPLAY.replace(' ', '')}" style="text-decoration:underline;">{PHONE_DISPLAY}</a>.</p>
    </form>
    <p style="margin-top:24px; font-size:0.8rem;">Your enquiry opens in WhatsApp so you can review the message before sending it. Replace the WhatsApp number in <span class="mono">build.py</span> before launch.</p>

  </div>
</section>
"""
    write("get-a-quote.html", base(
        title="Free Quote Calculator | Solar &amp; Security Kenya &ndash; Smartech",
        description="Request a free, no-obligation site survey and itemized quote for solar, security, electrical, cabling or safety testing in Kenya.",
        p="", body=quote_body, canonical="/get-a-quote.html",
    ))

    # ============================================================
    # CONTACT — p = ''
    # ============================================================
    contact_body = f"""
<section class="section--tight">
  <div class="wrap">
    <div class="eyebrow">Contact</div>
    <h1>Talk to Smartech</h1>
    <p class="lede" style="color:var(--text-soft); font-size:1.05rem;">For quotes, project questions, or emergencies &mdash; reach us directly.</p>
  </div>
</section>
<section class="section section--dim">
  <div class="wrap grid grid--3">
    <div class="card"><h3>Call or WhatsApp</h3><p><a href="tel:{PHONE_DISPLAY.replace(' ', '')}">{PHONE_DISPLAY}</a><br><a href="{wa_link()}">WhatsApp Us</a></p></div>
    <div class="card"><h3>Emergency Line (24/7)</h3><p><a href="tel:{EMERGENCY_PHONE.replace(' ', '')}">{EMERGENCY_PHONE}</a></p></div>
    <div class="card"><h3>Email</h3><p><a href="mailto:info@smartechtech.co.ke">info@smartechtech.co.ke</a></p></div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <h2>Our Office</h2>
    <p>[Insert office address here]</p>
    <div style="border:1px solid var(--line); height:320px; display:flex; align-items:center; justify-content:center; font-family:'IBM Plex Mono',monospace; color:var(--text-soft); font-size:0.8rem;">[Embed Google Map here]</div>
  </div>
</section>
"""
    write("contact.html", base(
        title="Contact Smartech Technologies | Nairobi, Kenya",
        description="Contact Smartech Technologies for quotes, project inquiries, or 24/7 emergency electrical and security support in Kenya.",
        p="", body=contact_body, canonical="/contact.html",
    ))

    # ============================================================
    # SERVICE AREAS — p = ''
    # ============================================================
    areas = ["Nairobi", "Kiambu", "Machakos", "Kajiado", "Nakuru", "Mombasa"]
    area_cards = "".join(
        f'<div class="card"><h3>{a}</h3><p>Solar, security, electrical, cabling and safety testing services in {a} County.</p>'
        f'<a class="more" href="{a.lower()}.html">View {a} page &rarr;</a></div>' for a in areas
    )
    areas_index_body = f"""
<section class="section--tight">
  <div class="wrap">
    <div class="eyebrow">Service Areas</div>
    <h1>Where we work</h1>
    <p class="lede" style="color:var(--text-soft); font-size:1.05rem;">Smartech serves homeowners and businesses across these counties, with 24/7 emergency response in Nairobi and Kiambu.</p>
  </div>
</section>
<section class="section section--dim">
  <div class="wrap grid grid--3">{area_cards}</div>
</section>
"""
    write("service-areas/index.html", base(
        title="Service Areas | Solar &amp; Security Installation Across Kenya &ndash; Smartech",
        description="Smartech Technologies serves Nairobi, Kiambu, Machakos, Kajiado, Nakuru and Mombasa with solar, security, electrical and cabling services.",
        p="../", body=areas_index_body, canonical="/service-areas/",
        breadcrumb=[("Home", "{p}index.html"), ("Service Areas", None)],
    ))

    for a in areas:
        body = f"""
<section class="section--tight">
  <div class="wrap">
    <div class="eyebrow">Service Area</div>
    <h1>Solar &amp; Security Installation in {a}</h1>
    <p class="lede" style="color:var(--text-soft); font-size:1.05rem;">Smartech installs and maintains solar, security, electrical, cabling and safety systems for homes and businesses across {a} County.</p>
    <a class="btn btn--amber" href="../get-a-quote.html">Get a Free Quote in {a}</a>
  </div>
</section>
<section class="section section--dim">
  <div class="wrap">
    <h2>[Local content placeholder]</h2>
    <p>Add {a}-specific project photos, local landmarks, and a short paragraph on common power/security needs in this area to strengthen local SEO relevance.</p>
    <div style="border:1px solid var(--line); height:260px; display:flex; align-items:center; justify-content:center; font-family:'IBM Plex Mono',monospace; color:var(--text-soft); font-size:0.8rem;">[Embed map centered on {a}]</div>
  </div>
</section>
"""
        write(f"service-areas/{a.lower()}.html", base(
            title=f"Solar &amp; Security Installation in {a} | Smartech Technologies",
            description=f"Solar, security, electrical, cabling and safety testing services in {a}, Kenya. Free quote, EPRA &amp; NCA licensed.",
            p="../", body=body, canonical=f"/service-areas/{a.lower()}.html",
            breadcrumb=[("Home", "{p}index.html"), ("Service Areas", "{p}service-areas/index.html"), (a, None)],
        ))

    # ============================================================
    # BLOG — p = '../' for posts, '' handled via blog/index.html at p='../'... use p='../' consistently since blog/ is one level deep
    # ============================================================
    posts = [
        ("how-to-choose-a-contractor", "How to Choose a Solar or Security Contractor in Kenya (7 Questions to Ask Before You Pay a Deposit)",
         "The single biggest risk in buying solar or security in Kenya isn't the technology &mdash; it's ending up with a contractor who disappears after the deposit clears.",
         ["Ask for an itemized proposal, not a lump sum &mdash; panel count, inverter type, battery capacity, and expected performance should all be listed separately.",
          "Verify their EPRA, NCA, or CAK license number directly with the regulator, not just the badge on their website.",
          "Ask what happens if the system underperforms &mdash; get the warranty terms in writing before you pay anything.",
          "Check for a stated response-time commitment for after-sales support, not just a promise of 'good service.'",
          "Ask whether they'll service equipment they didn't install &mdash; this tells you whether they see you as a customer or a one-time sale.",
          "Look for structured after-sales support: maintenance plans, not just an installation date.",
          "Read recent reviews, not just testimonials on their own site &mdash; check their Google Business Profile."]),
        ("cost-of-hybrid-solar-nairobi", "Cost of Installing a Hybrid Solar System in Nairobi",
         "A realistic breakdown of what affects hybrid solar pricing in Nairobi &mdash; and the questions to ask so your quote is comparing like with like.",
         ["System cost depends primarily on your daily consumption and desired battery backup duration, not just panel count.",
          "Battery capacity is usually the single biggest cost driver in a hybrid system.",
          "Get quotes itemized by component so you can compare inverter brand, battery chemistry, and panel wattage across providers.",
          "Ask whether installation labour and workmanship warranty are included in the quoted price or billed separately.",
          "Financing options like pay-as-you-go or SACCO financing can make a larger, better-sized system more accessible than a smaller undersized one."]),
    ]
    post_cards = "".join(
        f'<div class="card"><h3><a href="{slug}.html" style="text-decoration:none;">{title}</a></h3><p>{excerpt}</p>'
        f'<a class="more" href="{slug}.html">Read article &rarr;</a></div>'
        for slug, title, excerpt, _ in posts
    )
    blog_index_body = f"""
<section class="section--tight">
  <div class="wrap">
    <div class="eyebrow">Blog / Insights</div>
    <h1>Local guides for Kenyan buyers</h1>
    <p class="lede" style="color:var(--text-soft); font-size:1.05rem;">Straight answers to the questions people search before buying solar, security, or electrical work in Kenya.</p>
  </div>
</section>
<section class="section section--dim">
  <div class="wrap grid grid--2">{post_cards}</div>
</section>
"""
    write("blog/index.html", base(
        title="Blog &amp; Local Guides | Smartech Technologies Kenya",
        description="Guides on solar cost, EPRA compliance, choosing a contractor, and more for Kenyan homeowners and businesses.",
        p="../", body=blog_index_body, canonical="/blog/",
        breadcrumb=[("Home", "{p}index.html"), ("Blog", None)],
    ))

    for slug, title, excerpt, points in posts:
        li = "".join(f"<li>{p}</li>" for p in points)
        body = f"""
<article class="section--tight">
  <div class="wrap max-w" style="max-width:760px;">
    <div class="eyebrow">Blog</div>
    <h1>{title}</h1>
    <p class="lede" style="color:var(--text-soft); font-size:1.05rem;">{excerpt}</p>
    <ul class="checklist" style="margin-top:26px;">{li}</ul>
    <div class="gridline"></div>
    <p>Want this handled for you instead of researched from scratch? Get a free site survey and an itemized quote &mdash; no obligation.</p>
    <a class="btn btn--amber" href="../get-a-quote.html">Get My Free Quote</a>
  </div>
</article>
"""
        write(f"blog/{slug}.html", base(
            title=f"{title} | Smartech Technologies Blog",
            description=excerpt.replace("&mdash;", "-"),
            p="../", body=body, canonical=f"/blog/{slug}.html",
            breadcrumb=[("Home", "{p}index.html"), ("Blog", "{p}blog/index.html"), (title[:40] + "...", None)],
        ))
