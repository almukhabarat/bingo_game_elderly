#include "FlaskHttp.h"

FlaskHttp::FlaskHttp(const char* baseAddress, const char* endPoint) : baseAddress(baseAddress), endPoint(endPoint) {}

void FlaskHttp::begin() {
    String url = String(baseAddress) + endPoint;
    httpClient.begin(url);
}

// haalt JSON op door middel van HTTP GET request en decodeert het bericht, functie geeft een string terug met daarin de instructie voor het aansturen van de snoepautomaat
String FlaskHttp::getCommand() {
  // timeout (voor HTTP long poll)
  httpClient.setTimeout(30000);  // nu ingesteld op 30 seconden, dezelfde timeout als in de flask api

  int httpResponseCode = httpClient.GET();

  String payload; // hierin komt de rauwe http response binnen in JSON
  String decodedString; // hierin komt de string van alleen het stukje na 'command'

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