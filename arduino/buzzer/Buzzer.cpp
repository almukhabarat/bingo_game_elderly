#include "Buzzer.h"

Buzzer::Buzzer(const uint8_t pin, const uint8_t channel) :pin(pin), channel(channel) {
  pinMode(pin, OUTPUT);
  ledcSetup(channel, 2000, 8); // Channel 0, 2kHz frequency, 8-bit resolution
  ledcAttachPin(pin, channel); // Attach pin to the channel
}

void Buzzer::playTone(uint16_t frequency, uint16_t duration) {
  ledcWriteTone(channel, frequency); // Play tone
  delay(duration);
  ledcWriteTone(channel, 0); // Stop tone
}

void Buzzer::stopTone() {
  ledcWriteTone(channel, 0); // Stop tone
}