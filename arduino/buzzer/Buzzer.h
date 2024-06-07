#ifndef BUZZER_H
#define BUZZER_H

#include <Arduino.h>

class Buzzer {
  public:
    Buzzer(uint8_t pin, uint8_t channel);
    void playTone(uint16_t frequency, uint32_t duration);
    void stopTone();
    void update();

  private:
    uint8_t _pin;
    uint8_t _channel;
    uint32_t _toneEndTime;
};

#endif
