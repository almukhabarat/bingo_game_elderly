#include <WiFi.h>
#include <ArduinoJson.h>
#include <ArduinoJson.hpp>
#include <HTTPClient.h>
#include <Stepper.h>

const char* ssid = "Pokimane, mijn knuffelmarokkaan!";
const char* pass = "i7mgmz3sahu3c7f";
const char* serverUrl = "http://145.92.8.134:5000/instructions"

// Defines the number of steps per rotation
const int stepsPerRevolution = 2048;

// Creates an instance of stepper class
// Pins entered in sequence IN1-IN3-IN2-IN4 for proper step sequence
Stepper candyMotor = Stepper(stepsPerRevolution, 8, 10, 9, 11);

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

  // Laat motor roteren met 10 rpm
  candyMotor.setSpeed(10);
  candyMotor.step(stepsPerRevolution);


}

void loop() {
  // Check if we're connected to Wi-Fi
  if (WiFi.status() == WL_CONNECTED) {
    // Make a GET request to the server
    HTTPClient http;
    http.begin(serverUrl);
    int httpResponseCode = http.GET();

    if (httpResponseCode == HTTP_CODE_OK) {
      // Parse the response
      DynamicJsonDocument doc(1024);
      deserializeJson(doc, http.getString());
      
      // Check if there are instructions
      if (doc.size() > 0) {
        // Process instructions
        for (int i = 0; i < doc.size(); i++) {
          String instruction = doc[i]["instruction"];
          // Implement logic to act based on the received instruction
          if (instruction == "move_motor") {
                myStepper.setSpeed(10);
                myStepper.step(stepsPerRevolution);
                delay(1000);
          // Additional instructions can be added as needed
        }
      }
    } else {
      Serial.print("Error in HTTP request: ");
      Serial.println(httpResponseCode);
    }
    
    http.end();
  }

  // Wait before making the next request
  delay(5000); // Adjust this delay according to your needs
}
