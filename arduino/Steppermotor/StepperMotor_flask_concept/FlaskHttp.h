#ifndef FLASK_HTTP_H
#define FLASK_HTTP_H

#include <HTTPClient.h>

class FlaskHttp {
  private:
    const char* baseAddress;
    const char* endPoint;
    HTTPClient httpClient;
  public:
    FlaskHttp(const char* baseAddress, const char* endPoint);
    void begin();
    String processCommand();
};

#endif
