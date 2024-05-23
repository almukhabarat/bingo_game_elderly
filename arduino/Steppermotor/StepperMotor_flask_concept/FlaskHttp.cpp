#include "FlaskHttp.h"

FlaskHttp::FlaskHttp(const char* baseAddress, const char* endPoint) : baseAddress(baseAddress), endPoint(endPoint) {}

void FlaskHttp::begin() {
    String url = String(baseAddress) + endPoint;
    httpClient.begin(url);
}

String FlaskHttp::processCommand() {
  // Optional: Set a custom timeout
  httpClient.setTimeout(30000);  // Set timeout to 30 seconds

  int httpResponseCode = httpClient.GET();

  String payload;
  String decodedString;

  if (httpResponseCode > 0) {
    payload = httpClient.getString();

    // Json parsen
    DynamicJsonDocument doc(1024);
    const char* command = doc["command"];
    decodedString = String(command);

  } else {
    Serial.println("Error: HTTP response code " + String(httpResponseCode));
  }
  httpClient.end();

  return decodedString;
}