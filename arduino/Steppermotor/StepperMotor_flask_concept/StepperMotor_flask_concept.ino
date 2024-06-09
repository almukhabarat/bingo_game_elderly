#include <WiFi.h>
#include <WiFiMulti.h>
#include "FlaskHttp.h"
#include <Stepper.h>

#define SERVER "http://145.92.8.134"
#define GET_END_POINT "/prijsautomaat_api/get"
#define POST_END_POINT "/prijsautomaat_api/post"

// Defines the number of steps per rotation
const int stepsPerRevolution = 2038;

// stepper class wordt ingeladen
// In de steppermotor wordt eerst de stap waarde ingevoerd, met daarop volgend de pinnen van de motor driver in de volgorde IN1-IN3-IN2-IN4
Stepper candyMotor = Stepper(stepsPerRevolution, 12, 10, 11, 9);

WiFiMulti wifiMulti;

FlaskHttp flaskHttp(SERVER, GET_END_POINT, POST_END_POINT);

void setup() {
  // Seriële monitor
  Serial.begin(115200);

  // Wifi configuratie
  wifiMulti.addAP("AndroidAP13C5", "rgan6339");
  wifiMulti.addAP("Pokimane, mijn knuffelmarokkaan!", "i7mgmz3sahu3c7f");
  wifiMulti.addAP("iPhone van Amin", "12345678!?");
  wifiMulti.addAP("iotroam", "c89r5vck5i");
  wifiMulti.addAP("iotroam", "eb8vCLgtTx");
  wifiMulti.addAP("iotroam", "kDBRo0JKGT");

  if (wifiMulti.run() == WL_CONNECTED) {
    Serial.println("Wi-Fi verbonden.");
    Serial.println("IP adres: ");
    Serial.println(WiFi.localIP());
  }
}

void loop() {
  if (wifiMulti.run() == WL_CONNECTED) {
    // Stuurt een HTTP GET request naar een flask api op de webserver
    String response = flaskHttp.getCommand();

    if (response == "geef snoepje ah zahbi") {
      Serial.println("response ontvangen: " + response);
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
