#ifndef FLASK_HTTP_H
#define FLASK_HTTP_H

#include <HTTPClient.h>
#include <ArduinoJson.h>

class FlaskHttp {
  private:
    const char* baseAddress;
    const char* endPoint;
    HTTPClient httpClient;
  public:
    FlaskHttp(const char* baseAddress, const char* endPoint); // Constructor
    void begin(); // Methode
    String getCommand(); // Methode
    void postCommand(const char* sendMessage); // Methode
};

#endif
