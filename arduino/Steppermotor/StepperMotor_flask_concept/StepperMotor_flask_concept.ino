#include <WiFi.h>
#include "FlaskHttp.h"
#include <Stepper.h>

const char* ssid = "Pokimane, mijn knuffelmarokkaan!";
const char* pass = "i7mgmz3sahu3c7f";

#define SERVER "http://145.92.8.134"
#define END_POINT "/give_candy"

// Defines the number of steps per rotation
const int stepsPerRevolution = 2048;

// Creates an instance of stepper class
// Pins entered in sequence IN1-IN3-IN2-IN4 for proper step sequence
Stepper candyMotor = Stepper(stepsPerRevolution, 8, 10, 9, 11);

FlaskHttp flaskHttp(SERVER, END_POINT);

void setup() {
  // Seriële monitor
  Serial.begin(115200);

  // Wifi configuratie
  WiFi.begin(ssid, pass);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Wi-Fi verbonden.");
  Serial.println("IP adres: ");
  Serial.println(WiFi.localIP());

  // Laat motor roteren met 10 rpm
  candyMotor.setSpeed(10);
  candyMotor.step(stepsPerRevolution);
}

void loop() {
    // Stuurt een HTTP GET request naar een flask api op de webserver
    String responsePayload = flaskHttp.processCommand();
    if (!responsePayload.isEmpty()) {
      Serial.println("response ontvangen: " + responsePayload);
    }

    // update interval
    delay(1000);
}
