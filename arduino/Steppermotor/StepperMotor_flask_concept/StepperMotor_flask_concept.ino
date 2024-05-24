#include <WiFi.h>
#include "FlaskHttp.h"
#include <Stepper.h>

const char* ssid = "Pokimane, mijn knuffelmarokkaan!";
const char* pass = "i7mgmz3sahu3c7f";

#define SERVER "http://145.92.8.134"
#define END_POINT "/get_command"

// Defines the number of steps per rotation
const int stepsPerRevolution = 2048;

// Creates an instance of stepper class
// Pins entered in sequence IN1-IN3-IN2-IN4 for proper step sequence
Stepper candyMotor = Stepper(stepsPerRevolution, 12, 10, 11, 9);

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

  flaskHttp.begin();
}

void loop() {
    // Stuurt een HTTP GET request naar een flask api op de webserver
    String response = flaskHttp.getCommand();

    if (response.isEmpty()) {
      Serial.println("Geen response of foutmelding ontvangen.");
      
    } else if (response == "geef snoepje ah zahbi") {
      Serial.println("response ontvangen: " + response);
      // Laat motor roteren met 10 rpm
      candyMotor.setSpeed(10);
      candyMotor.step(-stepsPerRevolution);
    }

    // update interval
    delay(1000);
}
