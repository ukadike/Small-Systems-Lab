/*
  Small Systems Lab — Earth Sensor Starter
  Reads soil moisture and light data for visualization or sonification.
*/

const int soilPin = A0;
const int lightPin = A1;
const int buzzerPin = 9;

void setup() {
  Serial.begin(9600);
  pinMode(buzzerPin, OUTPUT);
  Serial.println("soil,light,status");
}

void loop() {
  int soil = analogRead(soilPin);
  int light = analogRead(lightPin);
  String status = "ok";

  if (soil < 350) {
    status = "dry";
    tone(buzzerPin, 440, 120);
  } else {
    noTone(buzzerPin);
  }

  Serial.print(soil);
  Serial.print(",");
  Serial.print(light);
  Serial.print(",");
  Serial.println(status);
  delay(1000);
}
