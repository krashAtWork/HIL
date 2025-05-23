void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);  
  Serial.println("READY");
  
}

void loop() {
  if (Serial.available()) {
    String command = Serial.readStringUntil('\n');

    if (command == "TOGGLE_LED") {  
      
      int ledState = digitalRead(13);
      
      if (ledState == 0) {
        digitalWrite(13, HIGH);
        Serial.println(digitalRead(13));
        
        
      } else {
        digitalWrite(13, 0);
        Serial.println(digitalRead(13));
      }
       delay(50);    
      // Serial.println(digitalRead(13));
    }
    // Add a short delay to avoid multiple toggles on a single press
        
    if (command == "READ_TEMP") {
      float fakeTemp = 25.4;  // Replace with sensor read later
      Serial.println(fakeTemp);
    }
  }
}

