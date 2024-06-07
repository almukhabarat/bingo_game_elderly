#include <WiFi.h>
#include <WiFiMulti.h>
#include "FlaskHttp.h"
#include <Stepper.h>


#define SERVER "http://145.92.8.134"
#define GET_END_POINT "/bingobal_api/get"
#define POST_END_POINT "/bingobal_api/post"

// Defines the pinnumber of the relay
#define RELAYPIN 6
// Defines the pinnumber of the custom switch
#define BALLPIN 4

// Defines the number of steps per rotation
const int oneRevolution = 2038;

// Define if wheel is currently rotating
bool rotating = false;

// stepper class wordt ingeladen
// In de steppermotor wordt eerst de stap waarde ingevoerd, met daarop volgend de pinnen van de motor driver in de volgorde IN1-IN3-IN2-IN4
Stepper molenMotor = Stepper(oneRevolution, 8, 10, 9, 11);

WiFiMulti wifiMulti;

FlaskHttp flaskHttp(SERVER, GET_END_POINT, POST_END_POINT);

void setup() {
  // Seriële monitor
  Serial.begin(115200);

  pinMode(RELAYPIN, OUTPUT);
  pinMode(BALLPIN, INPUT_PULLUP);

  // Wifi configuratie
  wifiMulti.addAP("AndroidAP13C5", "rgan6339");
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
  if (wifiMulti.run() == WL_CONNECTED && !rotating) {
    // Stuurt een HTTP GET request naar een flask api op de webserver
    String response = flaskHttp.getCommand();

    if (response == "Draaien pls") {
      Serial.println("response ontvangen: " + response);
      rotating = true;
    }
    if (response == "loslaten pls") {
      Serial.println("response ontvangen: " + response);
      digitalWrite(RELAYPIN, LOW);
    }
    else if (response.isEmpty()) {
      Serial.println("Geen response of foutmelding ontvangen.");
    }
    // update interval
    delay(1000);
  }
  
  if (rotating) {
    // Laat motor roteren met 10 rpm
    molenMotor.setSpeed(10);
    molenMotor.step(10);
    if (digitalRead(BALLPIN) == LOW) {
      rotating = false;
      digitalWrite(RELAYPIN, HIGH);
    }
  }
}
