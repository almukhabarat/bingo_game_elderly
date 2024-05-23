#include "FlaskHttp.h"

FlaskHttp::FlaskHttp(const char* baseAddress, const char* endPoint) : baseAddress(baseAddress), endPoint(endPoint) {}

void FlaskHttp::begin() {
    String url = String(baseAddress) + endPoint;
    httpClient.begin(url);
}

String FlaskHttp::processCommand() {
  uint16_t httpResponseCode = httpClient.GET();
  String payload;
  if (httpResponseCode == 200) {
    payload = httpClient.getString();
  }
  httpClient.end();
  return payload;
}