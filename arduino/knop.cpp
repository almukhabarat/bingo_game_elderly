#include <WiFi.h>
#include "kl3z5mgm.h"
#include "FlaskHttp.h"

#define SERVER "http://145.92.8.134"
#define END_POINT "/post_command"

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
      ledcWriteTone(channel, frequency); // Play tone
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

Buzzer buzzer1(15, 0); // Instantiate Buzzer object with pin 15 and channel 0
Buzzer buzzer2(6, 1);  // Instantiate second Buzzer object with pin 6 and channel 1
Button button(14);     // Instantiate Button object with pin 14

FlaskHttp flaskHttp(SERVER, END_POINT);

void setup() {
  // Seriële monitor
  Serial.begin(115200);

  // Wifi configuratie
  WiFi.begin(H_N, H_A);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Wi-Fi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  flaskHttp.begin();
}

void loop() {
  if (button.isPressed()) {
    buzzer1.playTone(2000, 100);
    buzzer2.playTone(2000, 100);
    buzzer1.playTone(1000, 100);
    buzzer2.playTone(1000, 100);
    buzzer1.playTone(1500, 100);
    buzzer2.playTone(1500, 100);
    buzzer1.playTone(3000, 100);
    buzzer2.playTone(3000, 100);
    buzzer1.playTone(500, 100);
    buzzer2.playTone(500, 100);

    flaskHttp.postCommand("button_pressed");
  } else {
    buzzer1.stopTone();
    buzzer2.stopTone();
  }

  delay(50);
}
