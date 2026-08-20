# Excavation, Trenching & Shoring Training - Landing Page

Standalone marketing landing page for the 2 excavation courses on
[HAZWOPER-OSHA.com](https://hazwoper-osha.com/): Excavation, Trenching & Shoring Safety Training, and
Competent Person for Excavation, Trenching & Shoring.

Pure HTML/CSS/JS, no build step, no dependencies. Meant to be tested/previewed on GitHub (e.g. GitHub Pages) before any backend work is wired up.

## Structure

```
index.html                          - main landing page (hero, courses, curriculum, pricing, FAQ teaser)
frequently-asked-questions/index.html - standalone FAQ resource page
css/styles.css                      - all styling
js/main.js                          - mobile nav toggle, FAQ accordion, pricing toggle, enroll form UX
images/ets-logo.png                 - site logo (navy/gold, transparent background)
```

## Current state

- Static, self-contained landing page only.
- The enroll forms are **front-end only** - they don't submit anywhere or charge anyone. Submitting just swaps in a confirmation message (see `js/main.js`).
- No Stripe, no course-platform API, no auth, no database.
- Course details (titles, prices, durations) were sourced from the live listings on hazwoper-osha.com as of 2026-07-20; confirm against the source pages before launch in case pricing changes.

## Planned next steps (not yet implemented)

1. Connect the enroll forms to the HAZWOPER-OSHA course/enrollment API.
2. Add Stripe Checkout (or Stripe Elements) for real payment.
3. Point the `excavationtrenchingshoring.com` domain at this page once hosting is set up.

## Local preview

Just open `index.html` in a browser, or serve the folder with any static server, e.g.:

```
npx serve .
```
