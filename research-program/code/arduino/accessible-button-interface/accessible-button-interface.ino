/*
  Small Systems Lab — Accessible Button Interface
  Demonstrates large-button / adaptive-switch input with LED and haptic output.
*/

const int switchPin = 2;
const int ledPin = 13;
const int hapticPin = 9;
int lastState = HIGH;

void setup() {
  pinMode(switchPin, INPUT_PULLUP);
  pinMode(ledPin, OUTPUT);
  pinMode(hapticPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int currentState = digitalRead(switchPin);

  if (currentState == LOW && lastState == HIGH) {
    digitalWrite(ledPin, HIGH);
    analogWrite(hapticPin, 180);
    Serial.println("activated");
    delay(250);
  } else if (currentState == HIGH) {
    digitalWrite(ledPin, LOW);
    analogWrite(hapticPin, 0);
  }

  lastState = currentState;
}
