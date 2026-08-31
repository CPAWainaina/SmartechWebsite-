(function () {
  'use strict';

  const toggle = document.querySelector('.navtoggle');
  const panel = document.getElementById('mobile-menu');

  if (toggle && panel) {
    toggle.addEventListener('click', function () {
      const open = panel.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
      toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    });

    panel.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        panel.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.setAttribute('aria-label', 'Open menu');
      });
    });
  }

  const form = document.getElementById('quote-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      const get = function (id) {
        const el = document.getElementById(id);
        return el ? el.value.trim() : '';
      };
      const status = document.getElementById('form-status');
      const fallback = document.getElementById('form-fallback');
      const name = get('name');
      const phone = get('phone');

      if (!name || !phone) {
        if (status) status.textContent = 'Please enter your full name and phone number.';
        if (!name) document.getElementById('name').focus();
        else document.getElementById('phone').focus();
        return;
      }

      const msg = [
        'Hello Smartech, I would like a free quote.',
        '',
        'Name: ' + name,
        'Phone: ' + phone,
        'Location: ' + get('location'),
        'Service: ' + get('service'),
        'Details: ' + get('details')
      ].join('\n');

      const url = 'https://wa.me/254701427045?text=' + encodeURIComponent(msg);
      const popup = window.open(url, '_blank', 'noopener,noreferrer');

      if (popup) {
        if (status) status.textContent = 'WhatsApp has been opened with your enquiry. Review the message and tap Send.';
        if (fallback) fallback.style.display = 'none';
      } else {
        if (status) status.textContent = 'Your browser blocked the WhatsApp window. Use one of the contact options below.';
        if (fallback) fallback.style.display = 'block';
      }
    });
  }
})();
