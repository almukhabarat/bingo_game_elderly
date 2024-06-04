#ifndef BINGO_BUTTON_H
#define BINGO_BUTTON_H

#include <Arduino.h>

class BingoButton {
  private:
    uint8_t pin;
  public:
    BingoButton(uint8_t pin);
    bool isPressed();
};

#endif