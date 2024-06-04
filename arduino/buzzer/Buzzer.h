#ifndef BUZZER_H
#define BUZZER_H

#include <Arduino.h>

class Buzzer {
  private:
    const uint8_t pin;
    const uint8_t channel;
  public:
    Buzzer(const uint8_t pin, const uint8_t channel);
    void playTone(uint16_t frequency, uint16_t duration);
    void stopTone();
};

#endif