let soil = 500;
let lightValue = 600;
let statusText = "ok";
let osc;

function setup() {
  const canvas = createCanvas(640, 240);
  canvas.parent("canvas-holder");
  textSize(18);
  osc = new p5.Oscillator("sine");
  osc.amp(0);

  document.getElementById("simulate").addEventListener("click", () => {
    soil = Math.floor(random(200, 900));
    lightValue = Math.floor(random(100, 900));
    statusText = soil < 350 ? "dry" : "ok";
    updateDom();
    sonify();
  });

  updateDom();
}

function draw() {
  background(255);
  fill(0);
  text("Soil moisture", 30, 40);
  rect(30, 55, map(soil, 0, 1023, 0, 560), 40);
  text("Light", 30, 140);
  rect(30, 155, map(lightValue, 0, 1023, 0, 560), 40);
}

function updateDom() {
  document.getElementById("soil").textContent = soil;
  document.getElementById("light").textContent = lightValue;
  document.getElementById("status").textContent = statusText;
  document.getElementById("summary").textContent =
    `Soil is ${soil}. Light is ${lightValue}. Status is ${statusText}.`;
}

function sonify() {
  userStartAudio();
  const freq = map(soil, 0, 1023, 220, 880);
  osc.freq(freq);
  osc.start();
  osc.amp(0.2, 0.05);
  setTimeout(() => osc.amp(0, 0.2), 300);
}
