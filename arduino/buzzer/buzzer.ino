int buzzerPin = 15;  // GPIO pin connected to the base of the transistor
int buttonPin = 14;  // GPIO pin connected to the button

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  ledcSetup(0, 2000, 8);        // Channel 0, 2kHz frequency, 8-bit resolution
  ledcAttachPin(buzzerPin, 0);  // Attach pin 15 to channel 0
}

void loop() {
  int buttonState = digitalRead(buttonPin);

  if (buttonState == LOW) {  // Button pressed
    ledcWriteTone(0, 2000);  // 2kHz tone
    delay(100);
    ledcWriteTone(0, 1000);  // 2kHz tone
    delay(100);
    ledcWriteTone(0, 1500);  // 2kHz tone
    delay(100);
    ledcWriteTone(0, 3000);  // 2kHz tone
    delay(100);
    ledcWriteTone(0, 500);  // 2kHz tone
    delay(100);

  } else {                // Button not pressed
    ledcWriteTone(0, 0);  // Stop tone
  }

  delay(50);  // Simple debounce
}
