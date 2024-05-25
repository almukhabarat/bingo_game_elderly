#include "BingoButton.h"

BingoButton::BingoButton(uint8_t pin) : pin(pin) {
  pinMode(pin, INPUT_PULLUP);
}

bool BingoButton::isPressed() {
  return digitalRead(pin) == LOW;
}

