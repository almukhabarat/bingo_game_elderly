#include <WiFi.h>
#include "FlaskHttp.h"
#include "MijnGeheim.h"

#define SERVER "http://145.92.8.134/"
#define END_POINT "bingoknop_api/post"
#define START_BUTTON_PIN 7
#define BINGO_BUTTON_PIN 4

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
  Serial.println("Wi-Fi verbonden.");
  Serial.println("IP adres: ");
  Serial.println(WiFi.localIP());

  // Configure the button pins as input
  pinMode(START_BUTTON_PIN, INPUT_PULLUP);
  pinMode(BINGO_BUTTON_PIN, INPUT_PULLUP);
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    // Check if the start button is pressed
    if (digitalRead(START_BUTTON_PIN) == HIGH) {
      Serial.println("Start button pressed, sending command...");
      flaskHttp.postCommand("start");
      // Debounce delay to avoid multiple triggers
      delay(500);
    }

    // Check if the bingo button is pressed
    if (digitalRead(BINGO_BUTTON_PIN) == HIGH) {
      Serial.println("Bingo button pressed, sending command...");
      flaskHttp.postCommand("bingo");
      // Debounce delay to avoid multiple triggers
      delay(500);
    }
  } else {
    Serial.println("Wi-Fi niet verbonden.");
    // Attempt to reconnect
    WiFi.begin(H_N, H_A);
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
    Serial.println("Wi-Fi opnieuw verbonden.");
  }
}