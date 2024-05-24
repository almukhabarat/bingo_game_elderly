#include "FlaskHttp.h"

FlaskHttp::FlaskHttp(const char* baseAddress, const char* endPoint) : baseAddress(baseAddress), endPoint(endPoint) {}

void FlaskHttp::begin() {
    String url = String(baseAddress) + String(endPoint);
    httpClient.begin(url);
}

// haalt JSON op door middel van HTTP GET request en decodeert het bericht, functie geeft een string terug met daarin de instructie voor het aansturen van de snoepautomaat
String FlaskHttp::getCommand() {
  String url = String(baseAddress) + String(endPoint);
  httpClient.begin(url);

  // Set timeout (for HTTP long poll)
  httpClient.setTimeout(30000);  // Set to 30 seconds, same as in the Flask API

  int httpResponseCode = httpClient.GET();

  String payload; 
  String decodedString; 

  if (httpResponseCode > 0) {
    payload = httpClient.getString();
    Serial.println("Response payload: " + payload);

    // Json parsen
    DynamicJsonDocument doc(1024);
    // kijkt voor fouten en print deze
    DeserializationError error = deserializeJson(doc, payload);
    if (error) {
        Serial.print(F("deserializeJson() failed: "));
        Serial.println(error.c_str());
        decodedString = "";
    } else {
      // parst JSON
      const char* command = doc["command"];
      decodedString = String(command);
    }
  } else {
    Serial.println("Error: HTTP response code " + String(httpResponseCode));
    decodedString = "";
  }
  httpClient.end();

  return decodedString;
}

void FlaskHttp::postCommand(const char* sendMessage) {

  httpClient.addHeader("Content-Type", "application/json");

  // String wordt in JSON verpakt
  DynamicJsonDocument doc(1024);
  // String wordt verstuurd onder het "command" object (dus je krijgt: {"command": "dit is het bericht"})
  doc["command"] = sendMessage;
  String requestBody;
  serializeJson(doc, requestBody);

  // Verstuurt HTTP POST request
  int httpResponseCode = httpClient.POST(requestBody);

  if (httpResponseCode > 0) {
    Serial.print("HTTP Response code: ");
    Serial.println(httpResponseCode);

  }
  httpClient.end();
}