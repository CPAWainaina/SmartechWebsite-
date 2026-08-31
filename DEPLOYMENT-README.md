# Smartech Technologies — Final Deployment Build

This build is production-hardened from V14.

## Completed
- Internal HTML link/anchor paths preserved and rechecked.
- Sitemap regenerated from indexable HTML pages.
- Project JPEGs optimized in place without changing public URLs.
- Project/gallery images use native lazy-loading below the first image and intrinsic dimensions where available.
- Twitter/X social metadata standardized.
- Long meta descriptions condensed to concise search snippets.
- Overlong title suffixes trimmed where safe.
- Quote form validates required fields and provides WhatsApp, email and phone fallbacks.
- Removed internal build/development note from the customer-facing quote page.
- JavaScript kept lightweight and dependency-free.

## Before/at launch
1. Upload the contents of `smartech_v5/` to the web root.
2. Confirm HTTPS and redirect HTTP to HTTPS.
3. Confirm the preferred host is `https://www.smartechtech.co.ke/`.
4. Enable Brotli/Gzip and long-lived caching for immutable assets.
5. Submit `https://www.smartechtech.co.ke/sitemap.xml` in Google Search Console and Bing Webmaster Tools.
6. Run representative URLs through Google Rich Results Test and PageSpeed Insights.
7. Verify WhatsApp, phone and email conversion paths on desktop and mobile.
8. Test 404 handling, mobile navigation, forms, keyboard focus and HTTPS redirects.


## V17 deployment notes
- Nationwide Kenya service-area hub and all 47 county pages are included.
- South Sudan/Juba remains project-based; do not create a local office claim unless verified.
- Sitemap includes all indexable HTML pages except 404.html.
- Google Fonts external dependencies have been removed; CSS uses local system fallbacks.

## V20 brand refresh
V20 applies the supplied Smartech Technologies Limited logo, logo-derived navy/blue/green colour palette, Poppins headings, Inter body text and IBM Plex Mono technical labels. Upload the complete V20 folder contents with `index.html` at the deployment root.
