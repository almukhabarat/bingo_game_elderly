#include <WiFi.h>
#include "FlaskHttp.h"
#include "kl3z5mgm.h" 
#include <Stepper.h>

#define SERVER "http://145.92.8.134"
#define END_POINT "/prijsautomaat_api/get"

// Defines the number of steps per rotation
const int stepsPerRevolution = 2048;

// stepper class wordt ingeladen
// In de steppermotor wordt eerst de stap waarde ingevoerd, met daarop volgend de pinnen van de motor driver in de volgorde IN1-IN3-IN2-IN4
Stepper candyMotor = Stepper(stepsPerRevolution, 12, 10, 11, 9);

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

  flaskHttp.begin();
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    // Stuurt een HTTP GET request naar een flask api op de webserver
    String response = flaskHttp.getCommand();

    Serial.println("response ontvangen: " + response);
    if (response == "geef snoepje ah zahbi") {
      // Laat motor roteren met 10 rpm
      candyMotor.setSpeed(10);
      candyMotor.step(-stepsPerRevolution);

    } else if (response.isEmpty()) {
      Serial.println("Geen response of foutmelding ontvangen.");
    }
    // update interval
    delay(1000);
  }
}
