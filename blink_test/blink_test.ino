#define LED_PIN 13
int ledState = LOW;

void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, ledState);
}

void loop() {
  if (Serial.available()) {
    String cmd = Serial.readStringUntil('\n');
    cmd.trim();

    if (cmd == "TOGGLE") {
      ledState = !ledState;
      digitalWrite(LED_PIN, ledState);
      Serial.println(String("LED=") + (ledState ? "ON" : "OFF"));
    } else if (cmd == "TEMP") {
      float temp = 45.0;
      Serial.println(String("TEMP=") + temp);
    } else {
      Serial.println("ERR=UNKNOWN_CMD");
    }
  }
}
