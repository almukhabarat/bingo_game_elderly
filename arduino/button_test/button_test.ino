#include <WiFi.h>
#include <Adafruit_NeoPixel.h>
#include "FlaskHttp.h"
#include "MijnGeheim.h"

#define SERVER "http://145.92.8.134/"
#define GET_END_POINT "bingobal_api/get"
#define POST_END_POINT "bingobal_api/post"
#define START_BUTTON_PIN 7
#define BINGO_BUTTON_PIN 4

// Onboard RGB LED pin and configuration
#define RGB_LED_PIN 48
#define NUM_LEDS 1

Adafruit_NeoPixel rgbLED(NUM_LEDS, RGB_LED_PIN, NEO_GRB + NEO_KHZ800);

FlaskHttp flaskHttp(SERVER, GET_END_POINT, POST_END_POINT);

void setup() {
  // Seriële monitor
  Serial.begin(115200);

  // Initialize the RGB LED
  rgbLED.begin();
  rgbLED.show(); // Initialize all pixels to 'off'

  // Wi-Fi configuratie
  WiFi.begin(H_N, H_A);
  while (WiFi.status() != WL_CONNECTED) {
    setLEDColor(255, 0, 0); // Red color
    delay(500);
    Serial.print(".");
  }
  setLEDColor(0, 255, 0); // Green color
  Serial.println("Wi-Fi verbonden.");
  Serial.println("IP adres: ");
  Serial.println(WiFi.localIP());

  // Configure the button pins as input
  pinMode(START_BUTTON_PIN, INPUT_PULLUP);
  pinMode(BINGO_BUTTON_PIN, INPUT_PULLUP);
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    setLEDColor(0, 255, 0);
    // Check if the start button is pressed
    if (digitalRead(START_BUTTON_PIN) == HIGH) {
      Serial.println("Start button pressed, sending command...");
      int responseCode = flaskHttp.postCommand("start");
      if (responseCode == 200) {
        setLEDColor(253, 115, 255);
        delay(3000);
      }
      delay(500);
    }

    // Check if the bingo button is pressed
    if (digitalRead(BINGO_BUTTON_PIN) == HIGH) {
      Serial.println("Bingo button pressed, sending command...");
      int responseCode = flaskHttp.postCommand("bingo");
      if (responseCode == 200) {
        setLEDColor(253, 115, 255);
        delay(3000);
      }
      delay(500);
    }
  } else {
    setLEDColor(255, 0, 0);
    Serial.println("Wi-Fi niet verbonden.");
    // Attempt to reconnect
    WiFi.begin(H_N, H_A);
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
    setLEDColor(0, 255, 0);
    Serial.println("Wi-Fi opnieuw verbonden.");
  }
}

void setLEDColor(uint8_t red, uint8_t green, uint8_t blue) {
  rgbLED.setPixelColor(0, rgbLED.Color(red, green, blue));
  rgbLED.show();
}