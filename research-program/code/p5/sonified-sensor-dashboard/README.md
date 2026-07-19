# Sonified Sensor Dashboard

A standalone p5.js demo pairing a visual bar-chart readout with a sonified tone for
simulated soil-moisture and light sensor readings, built to accompany
`research-program/code/arduino/earth-sensor-starter/`.

## Run it

Open `index.html` in a browser (or serve the folder with any static file server) and
click "Simulate Sensor Reading."

## Dependencies

`vendor/p5.min.js` and `vendor/p5.sound.min.js` (p5.js 1.9.4, LGPL-2.1, from the
[p5 npm package](https://www.npmjs.com/package/p5)) are vendored locally rather than
loaded from a CDN, so the dashboard runs offline and does not depend on third-party
availability.

## Accessibility

Sensor values are mirrored into an `aria-live` region and a definition list so
screen-reader users get the same data as the canvas visualization; the tone gives a
non-visual cue when soil moisture is low.
