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
  // Send HTTP GET request to start the motor
  if(sendHttpRequest("/start_motor")) {
    Serial.println("Motor started!");
  } else {
    Serial.println("Failed to start motor!");
  }
  
  delay(5000); // Wait for 5 seconds
}

bool sendHttpRequest(String endpoint) {
  HTTPClient http;
  
  // Construct the full URL
  String url = serverAddress + endpoint;
  
  // Send GET request
  http.begin(url);
  int httpCode = http.GET();
  
  if(httpCode > 0) {
    // Check for successful response
    if(httpCode == HTTP_CODE_OK) {
      http.end();
      return true;
    } else {
      Serial.printf("HTTP request failed with error code %d\n", httpCode);
      http.end();
      return false;
    }
  } else {
    Serial.println("HTTP request failed");
    http.end();
    return false;
  }
}