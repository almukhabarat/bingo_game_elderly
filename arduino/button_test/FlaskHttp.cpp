#include "FlaskHttp.h"

FlaskHttp::FlaskHttp(const char* baseAddress, const char* getEndPoint, const char* postEndPoint) 
  : baseAddress(baseAddress), getEndPoint(getEndPoint), postEndPoint(postEndPoint) {}

// haalt JSON op door middel van HTTP GET request en decodeert het bericht, functie geeft een string terug met daarin de instructie voor het aansturen van de snoepautomaat
String FlaskHttp::getCommand() {
  String url = String(baseAddress) + String(getEndPoint);
  httpClient.begin(url);

  // Timeout voor HTTP long poll
  httpClient.setTimeout(30000);  // Nu ingesteld op 30 seconden, dit is de timeout die ook de flask api hanteert

  int httpResponseCode = httpClient.GET();

  String payload; 
  String decodedString; 

  // kijkt of de responscode groter is dan 0 en haalt vervolgens de HTTP request binnen
  // http response code is iets complexer vanwege debugging
  if (httpResponseCode > 0) {
    payload = httpClient.getString();
    Serial.println("Response payload: " + payload);

    // Json parsen
    DynamicJsonDocument doc(1024);
    // kijkt voor fouten bij inkomende JSON pakket
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
    // geeft foutmelding aan 
    Serial.println("Error: HTTP response code " + String(httpResponseCode));
    decodedString = "";
  }
  httpClient.end();

  return decodedString;
}

int FlaskHttp::postCommand(const char* sendMessage) {
  String url = String(baseAddress) + String(postEndPoint);
  httpClient.begin(url);

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
  } else {
    Serial.print("Error on sending POST: ");
    Serial.println(httpResponseCode);
  }
  httpClient.end();
  
  return httpResponseCode; // Return the HTTP response code
}