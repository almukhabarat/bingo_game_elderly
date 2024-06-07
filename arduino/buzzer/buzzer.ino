#include <WiFi.h>
#include "FlaskHttp.h"
#include "MijnGeheim.h"
#include "Buzzer.h"
#include "BingoButton.h"

#define SERVER "http://145.92.8.134"
#define END_POINT "/send_bingo"

Buzzer buzzer1(15, 0); // Instantiate Buzzer object with pin 15 and channel 0
Buzzer buzzer2(6, 1);  // Instantiate second Buzzer object with pin 6 and channel 1

// buzzer1 en 2 worden in een array gestopt zodat ze makkelijk selecteerbaar zijn
Buzzer buzzers[] = {buzzer1, buzzer2};

BingoButton bingoButton(14); // Instantiate Button object with pin 14

FlaskHttp flaskHttp(SERVER, END_POINT);

void setup() {
  // Seriële monitor
  Serial.begin(115200);

  // Wifi configuratie
  WiFi.begin(H_N, H_A);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Wi-Fi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  flaskHttp.begin();
}

void loop() {
  if (bingoButton.isPressed()) {
    // Geluidspatroon voor 2 buzzers
    for (uint8_t i = 0; i < 2; i++) {
      buzzers[i].playTone(2000, 100);
      delay(100);
      buzzers[i].playTone(1000, 100);
      delay(100);
      buzzers[i].playTone(1500, 100);
      delay(100);
      buzzers[i].playTone(3000, 100);
      delay(100);
      buzzers[i].playTone(500, 100);
      delay(100);
      buzzers[i].stopTone();
    }

    flaskHttp.postCommand("button_pressed");
  }

  // Update buzzers om te controleren of ze de toon moeten stoppen
  for (uint8_t i = 0; i < 2; i++) {
    buzzers[i].update();
  }

  delay(50);
}

