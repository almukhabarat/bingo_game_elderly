#ifndef BUZZER_H
#define BUZZER_H

class Buzzer {
  private:
    uint8_t pin
    uint8_t channel
  public:
    Buzzer(uint8_t pin, uint8_t channel);
    void playTone();
    void stopTone();
}

#endif