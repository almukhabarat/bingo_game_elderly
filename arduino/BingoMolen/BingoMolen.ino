#include <WiFi.h>
#include <WiFiMulti.h>
#include "FlaskHttp.h"
#include <Stepper.h>


#define SERVER "http://145.92.8.134"
#define END_POINT "/api/get_command"

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
Stepper myStepper = Stepper(oneRevolution, 8, 10, 9, 11);

FlaskHttp flaskHttp(SERVER, END_POINT);

void setup() {
  // Seriële monitor
  Serial.begin(115200);

  pinMode(RELAYPIN, OUTPUT);
  pinMode(BALLPIN, INPUT_PULLUP);

  // Wifi configuratie
  WiFi.begin("AndroidAP13C5", "rgan6339");

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
  if (WiFi.status() == WL_CONNECTED && !rotating) {
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
    Serial.println("draai nu");
    myStepper.setSpeed(10);
    myStepper.step(10);
    if (digitalRead(BALLPIN) == LOW) {
      Serial.println("Stop draaien");
      rotating = false;
      digitalWrite(RELAYPIN, HIGH);
    }
  }
}
