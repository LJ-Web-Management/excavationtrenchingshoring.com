const STRIPE_PUBLISHABLE_KEY = "pk_live_doCHB0jglD5eISjEmB1vB6mb00xIg51noK";
// const STRIPE_PUBLISHABLE_KEY = "pk_test_51KRElxBHssw16TqHLVweh7MZorffCzySrRWdwAeURnEjnjuNZ7tsIfnmcBq1px0qSGWfJ3Kl2bDQRjaCCJpEO27W005Qidmdci" // STAGING
const API_BASE_URL = "https://hazwoper-osha.com/api";

var courses = [
  { id: 415, code: 'safety', name: 'Excavation, Trenching & Shoring Safety Training', price: 59.99 },
  { id: 411, code: 'competent', name: 'Competent Person for Excavation, Trenching & Shoring Training', price: 159.99 },
];

// Bulk pricing tiers (seat-count discount ladder, applied to each course's per-seat price)
var BULK_TIERS = [
  { min: 1, max: 1, discount: 0 },
  { min: 2, max: 10, discount: 0.01 },
  { min: 11, max: 20, discount: 0.02 },
  { min: 21, max: 50, discount: 0.03 },
  { min: 51, max: 100, discount: 0.05 },
  { min: 101, max: 250, discount: 0.07 },
  { min: 251, max: 500, discount: 0.08 },
  { min: 501, max: 1000, discount: 0.10 }
];

function tierForSeats(seats) {
  var match = BULK_TIERS[0];
  for (var i = 0; i < BULK_TIERS.length; i++) {
    if (seats >= BULK_TIERS[i].min) match = BULK_TIERS[i];
  }
  return match;
}

function tierPrice(basePrice, tier) {
  var discount = (tier && typeof tier.discount === 'number') ? tier.discount : 0;
  return Math.round(basePrice * (1 - discount) * 100) / 100;
}

function formatMoney(amount) {
  return Number(amount).toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}

function tierLabel(tier) {
  return tier.min === tier.max ? String(tier.min) : tier.min + '-' + tier.max.toLocaleString('en-US');
}

// Mobile nav toggle (shared by all pages; lets the checkout page run without main.js)
document.addEventListener('DOMContentLoaded', function () {
  var navToggle = document.getElementById('navToggle');
  var mainNav = document.getElementById('mainNav');
  if (navToggle && mainNav && !navToggle.dataset.navWired) {
    navToggle.dataset.navWired = '1';
    navToggle.addEventListener('click', function () {
      var isOpen = mainNav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
    mainNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        mainNav.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }
});
