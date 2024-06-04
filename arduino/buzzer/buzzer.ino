#include <WiFi.h>
#include "FlaskHttp.h"
#include "MijnGeheim.h"

#define SERVER "http://145.92.8.134"
#define END_POINT "/api/set_command"
#define bingoButtonPin 14
#define buzzerPin 15
#define startbuttonPin 7


FlaskHttp flaskHttp(SERVER, END_POINT);

void setup() {
  Serial.begin(115200);

  WiFi.begin(H_N, H_A);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Wi-Fi verbonden.");
  Serial.println("IP adres: ");

  Serial.println(WiFi.localIP());

  flaskHttp.begin();

  pinMode(bingoButtonPin, INPUT_PULLUP);
  pinMode(startbuttonPin, INPUT_PULLUP);

  ledcSetup(0, 2000, 8);        // Channel 0, 2kHz frequency, 8-bit resolution
  ledcAttachPin(buzzerPin, 0);  // Attach pin 15 to channel 0
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {

    if (digitalRead(startbuttonPin) == LOW) {
      Serial.println("Start button pressed, sending command...");

      flaskHttp.postCommand("start");

      delay(500);
    }

    if (digitalRead(bingoButtonPin) == LOW) {
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
      ledcWriteTone(0, 0);

      Serial.println("Bingo button pressed, sending command...");

      flaskHttp.postCommand("bingo");

      delay(500);
    }
  } else {

    Serial.println("Wi-Fi niet verbonden.");

    WiFi.begin(H_N, H_A);
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
    Serial.println("Wi-Fi opnieuw verbonden.;");
  }
}


