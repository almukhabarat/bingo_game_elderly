#include <WiFi.h>
#include <HTTPClient.h>
#include <Stepper.h>

const char* ssid = "Pokimane, mijn knuffelmarokkaan!";
const char* pass = "i7mgmz3sahu3c7f";
const char* serverAddress = "http://145.92.8.134";

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
  Serial.println("IP adres: ");
  Serial.println(WiFi.localIP());

  // Laat motor roteren met 10 rpm
  candyMotor.setSpeed(10);
  candyMotor.step(stepsPerRevolution);
}

void loop() {
    if (WiFi.status() == WL_CONNECTED) {
        HTTPClient http;

        // Your Flask API endpoint
        http.begin("http://145.92.8.134/give_candy");

        // Send HTTP GET request
        int httpResponseCode = http.GET();

        if (httpResponseCode > 0) {
            // Print the HTTP response code
            Serial.print("HTTP Response code: ");
            Serial.println(httpResponseCode);

            // Get the response payload
            String payload = http.getString();
            Serial.println("Response payload: ");
            Serial.println(payload);
        }
        else {
            Serial.print("Error code: ");
            Serial.println(httpResponseCode);
        }

        // Free resources
        http.end();
    }
    else {
        Serial.println("WiFi Disconnected");
    }

    // Add a delay before sending the next request
    delay(5000); // 5 seconds
}
