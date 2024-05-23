class Buzzer {
  private:
    int pin;
    int channel;

  public:
    Buzzer(int pin, int channel) : pin(pin), channel(channel) {
      pinMode(pin, OUTPUT);
      ledcSetup(channel, 2000, 8); // Channel 0, 2kHz frequency, 8-bit resolution
      ledcAttachPin(pin, channel); // Attach pin to the channel
    }

    void playTone(int frequency, int duration) {
      ledcWriteTone(channel, frequency);  // Play tone
      delay(duration);
      ledcWriteTone(channel, 0); // Stop tone
    }

    void stopTone() {
      ledcWriteTone(channel, 0); // Stop tone
    }
};

class Button {
  private:
    int pin;

  public:
    Button(int pin) : pin(pin) {
      pinMode(pin, INPUT_PULLUP);
    }

    bool isPressed() {
      return digitalRead(pin) == LOW;
    }
};

Buzzer buzzer(15, 0); // Instantiate Buzzer object with pin 15 and channel 0
Button button(14);    // Instantiate Button object with pin 14

void setup() {
}

void loop() {
  if (button.isPressed()) {
    buzzer.playTone(2000, 100);
    buzzer.playTone(1000, 100);
    buzzer.playTone(1500, 100);
    buzzer.playTone(3000, 100);
    buzzer.playTone(500, 100);
  } else {
    buzzer.stopTone();
  }

  delay(50);
}
