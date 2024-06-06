#ifndef FLASK_HTTP_H
#define FLASK_HTTP_H

#include <HTTPClient.h>
#include <ArduinoJson.h>

class FlaskHttp {
  private:
    const char* baseAddress;
    const char* getEndPoint;
    const char* postEndPoint;
    HTTPClient httpClient;
  public:
    FlaskHttp(const char* baseAddress, const char* getEndPoint, const char* postEndPoint);
    String getCommand();
    int postCommand(const char* sendMessage); // Changed return type to int
};

#endif