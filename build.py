#!/usr/bin/env python3
"""Generates the static Smartech Technologies site from shared templates."""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

WHATSAPP_NUMBER = "254701427045"
PHONE_DISPLAY = "0701 427 045"
EMERGENCY_PHONE = "0701 427 045"

def wa_link(msg="Hi Smartech, I'd like a quote."):
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={msg.replace(' ', '%20')}"

LOGO_SVG = """<svg class="mark" viewBox="0 0 26 26" fill="none" xmlns="http://www.w3.org/2000/svg">
<circle cx="13" cy="13" r="12" stroke="#dd8f31" stroke-width="1.4"/>
<path d="M13 4 L13 12 L18 12 L11 22 L13 14 L8 14 Z" fill="#dd8f31"/>
</svg>"""

WA_ICON = """<svg viewBox="0 0 32 32" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M16.01 3C9.38 3 4 8.36 4 14.97c0 2.2.6 4.27 1.65 6.05L4 29l8.24-1.6a13.1 13.1 0 0 0 3.77.55h.01c6.63 0 12.01-5.36 12.01-11.97C28.03 8.36 22.65 3 16.01 3Zm7 16.9c-.3.83-1.63 1.58-2.26 1.67-.58.09-1.31.13-2.11-.13-.49-.16-1.12-.37-1.93-.72-3.39-1.46-5.6-4.9-5.77-5.13-.17-.23-1.38-1.84-1.38-3.5 0-1.67.87-2.49 1.18-2.83.3-.33.66-.42.88-.42.22 0 .44 0 .63.01.2.01.47-.08.74.56.3.7 1 2.44 1.09 2.61.09.17.15.38.03.61-.12.23-.18.38-.36.58-.18.2-.38.45-.54.6-.18.18-.37.37-.16.73.21.36.93 1.53 2 2.48 1.37 1.22 2.53 1.6 2.9 1.78.36.18.57.15.78-.09.21-.24.9-1.05 1.14-1.41.24-.36.48-.3.8-.18.33.12 2.07.98 2.42 1.16.36.18.6.27.68.42.09.15.09.86-.21 1.7Z"/></svg>"""

NAV_ITEMS = [
    ("Home", "{p}index.html"),
    ("Services", "{p}services/solar.html", [
        ("Solar & Green Energy", "{p}services/solar.html"),
        ("Security Systems", "{p}services/security.html"),
        ("Electrical & Power", "{p}services/electrical.html"),
        ("Fiber & Cabling", "{p}services/cabling.html"),
        ("Industrial Automation & Controls", "{p}services/industrial-automation.html"),
        ("Lift & Machinery Inspection", "{p}services/lift-machinery-inspection.html"),
        ("Safety & Testing", "{p}services/safety-testing.html"),
    ]),
    ("Solutions", "{p}solutions/smart-solar-security-hub.html", [
        ("Smart Solar Security Hub", "{p}solutions/smart-solar-security-hub.html"),
        ("Residential Smart Homes", "{p}solutions/residential.html"),
        ("Commercial & Industrial", "{p}solutions/commercial.html"),
        ("Agriculture & Off-Grid", "{p}solutions/agriculture.html"),
    ]),
    ("Why Smartech", "{p}why-smartech.html"),
    ("Emergency 24/7", "{p}emergency.html"),
    ("Blog", "{p}blog/index.html"),
]

def render_nav(p):
    out = []
    for item in NAV_ITEMS:
        if len(item) == 2:
            label, href = item
            out.append(f'<li><a href="{href.format(p=p)}">{label}</a></li>')
        else:
            label, href, sub = item
            subhtml = "".join(f'<a href="{h.format(p=p)}">{l}</a>' for l, h in sub)
            out.append(
                f'<li class="has-sub"><a href="{href.format(p=p)}">{label}</a>'
                f'<div class="subnav">{subhtml}</div></li>'
            )
    return "\n".join(out)

def base(title, description, p, body, canonical, breadcrumb=None, schema=""):
    """p = relative path prefix to site root, e.g. '' for root pages, '../' for one level deep."""
    crumb_html = ""
    if breadcrumb:
        parts = []
        for i, (label, href) in enumerate(breadcrumb):
            if href:
                parts.append(f'<a href="{href.format(p=p)}">{label}</a>')
            else:
                parts.append(f'<span>{label}</span>')
        crumb_html = f'<div class="crumb wrap">{" / ".join(parts)}</div>'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#10151c">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="https://www.smartechtech.co.ke{canonical}">
<meta property="og:site_name" content="Smartech Technologies">
<meta name="twitter:card" content="summary">
<link rel="canonical" href="https://www.smartechtech.co.ke{canonical}">
<link rel="stylesheet" href="{p}assets/css/style.css">
{schema if schema else """<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"Organization",
  "name":"Smartech Technologies Limited",
  "url":"https://www.smartechtech.co.ke/",
  "areaServed":"Kenya",
  "description":"Integrated Solar, CCTV, Electrical & Networking Contractor in Kenya."
}
</script>"""}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

<div class="topbar">
  <div class="wrap">
    <span>EPRA &amp; NCA Licensed &middot; Serving Nairobi, Kiambu, Machakos, Kajiado &amp; Nakuru</span>
    <span><a href="tel:{EMERGENCY_PHONE.replace(' ', '')}">24/7 Emergency: {EMERGENCY_PHONE}</a></span>
  </div>
</div>

<header class="site">
  <nav class="wrap nav">
    <a class="logo" href="{p}index.html">
      {LOGO_SVG}
      <span>Smartech Technologies<small>Integrated Solar, CCTV, Electrical &amp; Networking Contractor in Kenya</small></span>
    </a>
    <ul class="navlinks">
      {render_nav(p)}
    </ul>
    <div class="navcta">
      <a class="btn btn--outline btn--sm" href="{p}contact.html">Contact</a>
      <a class="btn btn--amber btn--sm" href="{p}get-a-quote.html">Get a Free Quote</a>
    </div>
    <button class="navtoggle" type="button" aria-expanded="false" aria-controls="mobile-menu" aria-label="Open menu">
      <span></span><span></span><span></span>
    </button>
  </nav>
  <div class="mobile-panel" id="mobile-menu">
    <a href="{p}index.html">Home</a>
    <div class="mobile-group">Services</div>
    <a href="{p}services/solar.html">Solar &amp; Green Energy</a>
    <a href="{p}services/security.html">Security Systems</a>
    <a href="{p}services/electrical.html">Electrical &amp; Power</a>
    <a href="{p}services/cabling.html">Fiber &amp; Cabling</a>
    <a href="{p}services/safety-testing.html">Safety &amp; Testing</a>
    <div class="mobile-group">Solutions</div>
    <a href="{p}solutions/smart-solar-security-hub.html">Smart Solar Security Hub</a>
    <a href="{p}solutions/residential.html">Residential Smart Homes</a>
    <a href="{p}solutions/commercial.html">Commercial &amp; Industrial</a>
    <a href="{p}solutions/agriculture.html">Agriculture &amp; Off-Grid</a>
    <a href="{p}why-smartech.html">Why Smartech</a>
    <a href="{p}emergency.html">Emergency 24/7</a>
    <a href="{p}blog/index.html">Blog</a>
    <a class="btn btn--amber" style="margin:14px 24px;" href="{p}get-a-quote.html">Get a Free Quote</a>
  </div>
</header>

{crumb_html}

<main id="main">
{body}
</main>

<footer class="site">
  <div class="wrap footgrid">
    <div>
      <a class="logo" href="{p}index.html" style="margin-bottom:14px;">{LOGO_SVG}<span>Smartech Technologies</span></a>
      <p>Kenya's single-source integrator for solar, security, electrical, cabling and safety systems &mdash; one team, one contract, fully accountable.</p>
      <p class="mono" style="font-size:0.78rem;">EPRA Licensed &middot; NCA Registered &middot; CAK Licensed Contractor</p>
    </div>
    <div>
      <h4>Services</h4>
      <ul>
        <li><a href="{p}services/solar.html">Solar &amp; Green Energy</a></li>
        <li><a href="{p}services/security.html">Security Systems</a></li>
        <li><a href="{p}services/electrical.html">Electrical &amp; Power</a></li>
        <li><a href="{p}services/cabling.html">Fiber &amp; Cabling</a></li>
        <li><a href="{p}services/safety-testing.html">Safety &amp; Testing</a></li>
      </ul>
    </div>
    <div>
      <h4>Company</h4>
      <ul>
        <li><a href="{p}why-smartech.html">Why Smartech</a></li>
        <li><a href="{p}emergency.html">Emergency 24/7</a></li>
        <li><a href="{p}financing.html">Financing</a></li>
        <li><a href="{p}service-areas/index.html">Service Areas</a></li>
        <li><a href="{p}blog/index.html">Blog</a></li>
      </ul>
    </div>
    <div>
      <h4>Get In Touch</h4>
      <ul>
        <li><a href="tel:{PHONE_DISPLAY.replace(' ', '')}">{PHONE_DISPLAY}</a></li>
        <li><a href="{wa_link()}">WhatsApp Us</a></li>
        <li><a href="mailto:info@smartechtech.co.ke">info@smartechtech.co.ke</a></li>
        <li><a href="{p}get-a-quote.html">Request a Free Site Survey</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap footbottom">
    <span>&copy; Smartech Technologies Limited. All rights reserved.</span>
    <span>Nairobi, Kenya</span>
  </div>
</footer>

<script src="{p}assets/js/site.js" defer></script>
<a class="wa-float" href="{wa_link()}" aria-label="Chat on WhatsApp">{WA_ICON}</a>

</body>
</html>"""

def write(relpath, html):
    full = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(html)
    print("wrote", relpath)

# ============================================================
# Import page content modules
# ============================================================
import pages
pages.build(base, write, wa_link, WA_ICON, EMERGENCY_PHONE, PHONE_DISPLAY)

print("\nDone. Open site/index.html in a browser to preview.")

# V5 search-first pages are generated by upgrade_v5.py after the core site build.
