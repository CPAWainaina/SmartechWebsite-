# Smartech Technologies Website — Guidelines

This package contains a complete, static, ready-to-launch website built from the SEO blueprint: 27 pages covering every service, solution, and conversion page identified in that plan.

## What's in this package

```
site/
├── index.html                          Home
├── why-smartech.html                   Guarantee & certifications
├── emergency.html                      24/7 emergency response
├── financing.html                      Financing & payment plans
├── get-a-quote.html                    Quote request form
├── contact.html                        Contact page
├── services/
│   ├── solar.html
│   ├── security.html
│   ├── electrical.html
│   ├── cabling.html
│   └── safety-testing.html
├── solutions/
│   ├── smart-solar-security-hub.html   Flagship bundle
│   ├── residential.html
│   ├── commercial.html
│   └── agriculture.html
├── repairs/
│   ├── solar-repair.html
│   ├── cctv-repair.html
│   └── backup-power-repair.html
├── service-areas/
│   ├── index.html
│   └── nairobi.html, kiambu.html, machakos.html, kajiado.html, nakuru.html, mombasa.html
├── blog/
│   ├── index.html
│   ├── how-to-choose-a-contractor.html
│   └── cost-of-hybrid-solar-nairobi.html
├── assets/css/style.css                Shared design system
├── build.py / pages.py                 Source generator (see below)
└── GUIDELINES.md                       This file
```

Every page shares one header, navigation, footer, and CSS file, so the whole site stays visually and structurally consistent.

## Design approach

The visual identity is built around one idea: **"the grid line"** — a single connected circuit running through the hero and section dividers, with a node marking each service vertical (solar, security, electrical, cabling, safety). It's a direct visual expression of the company's core pitch: one connected system instead of five separate vendors.

- **Colors:** deep charcoal (`#10151c`) and warm technical paper (`#f1efe7`), with amber (`#dd8f31`, "live current") as the primary accent and teal (`#1f6e68`, "signal") as a secondary.
- **Type:** Space Grotesk for headings, IBM Plex Sans for body text, IBM Plex Mono for labels, data, and certification numbers — giving the site a technical, engineering-firm feel rather than a generic template look.
- Fonts load from Google Fonts via `assets/css/style.css`; an internet connection is required for them to display (they degrade gracefully to system fonts if blocked, as seen in offline previews).

## Before you launch: required edits

Search the codebase for bracketed placeholders — every one needs a real value before publishing:

| Placeholder | Found in | What to do |
|---|---|---|
| `WHATSAPP_NUMBER`, `PHONE_DISPLAY`, `EMERGENCY_PHONE` | Top of `pages.py` | Replace with your real WhatsApp and phone numbers, then re-run `python3 build.py` |
| `[Class A]`, `[Class 1]`, License No. `[XXXXXXX]` | `why-smartech.html`, `emergency.html` | Insert your actual EPRA, NCA, and CAK license classes and numbers |
| `[State term, e.g. 2 years]` / response-time SLAs | `why-smartech.html`, `emergency.html` | Insert your real warranty length and response-time commitment |
| Testimonial placeholders | `why-smartech.html` | Replace with real client quotes, or embed a live Google Reviews widget |
| `[Insert office address here]`, `[Embed Google Map here]` | `contact.html`, `service-areas/*.html` | Add your real address and an embedded Google Map iframe |
| Quote form | `get-a-quote.html` | The form currently submits nowhere — connect it to a form backend (Formspree, a serverless function, your CRM, or email service) before launch |
| `[Local content placeholder]` | `service-areas/*.html` | Add area-specific project photos and a short paragraph per county — this is what makes local SEO pages actually rank |

**How to make edits:** the fastest way to make a global change (like the phone number) is to edit `pages.py`, then re-run:
```
python3 build.py
```
This regenerates every HTML file from the shared templates, so you never have to hand-edit the same header/footer across 27 files.

## Images

No photos are included — the design deliberately uses typography, the grid-line motif, and data-style panels instead of stock photography, since AI-generated "installation photos" would misrepresent your actual work. Before launch, add:
- Real geotagged installation photos to the homepage, service pages, and service-area pages (the plan's local SEO strategy depends on these)
- A logo image if you have one designed, replacing the simple SVG mark in the header

## Deploying the site

This is a plain static site — no build tools or server required to run it. Options:
1. **Simplest:** upload the whole `site/` folder to any static host (Netlify, Vercel, GitHub Pages, or your existing cPanel/hosting via FTP).
2. **Custom domain:** point `smartechtech.co.ke` (or your actual domain) at the host, and update the `canonical` URLs in `pages.py` if your domain differs from the placeholder used (`smartechtech.co.ke`).
3. **Before going live**, run each page through a broken-link checker and confirm the quote form actually delivers submissions somewhere.

## SEO checklist (ties back to the original blueprint)

- [ ] Submit an XML sitemap and `robots.txt` to Google Search Console
- [ ] Set up and verify Google Business Profile, matching the exact business name used sitewide
- [ ] Add `LocalBusiness` and `Service` schema markup (not yet included — add via JSON-LD in each page's `<head>`)
- [ ] Compress and add real alt text to every installation photo once added
- [ ] Register the business on Kenyan directories listed in the original strategy (Yellow Pages Kenya, Business List Kenya, Tuugo Kenya, etc.)
- [ ] Pitch inclusion in existing "Top Solar/CCTV Companies in Nairobi" roundup articles
- [ ] Publish the remaining blog articles from the content calendar (10 more beyond the 2 included here)

## Extending the site

To add a new page (e.g. a new service-area county), open `pages.py`, find the relevant loop or function (e.g. `service_page()`, `repair_page()`, or the `areas` list), add your new entry, and re-run `python3 build.py`. The shared `base()` template in `build.py` automatically adds the header, nav, footer, and WhatsApp button to any new page.
