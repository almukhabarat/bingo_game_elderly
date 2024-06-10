#include <WiFi.h>
#include <Adafruit_NeoPixel.h>
#include "FlaskHttp.h"
#include "MijnGeheim.h"

#define SERVER "http://145.92.8.134/"
#define GET_END_POINT "bingobal_api/get"
#define POST_END_POINT "bingobal_api/post"
#define START_BUTTON_PIN 7
#define BINGO_BUTTON_PIN 5

// Onboard RGB LED pin and configuration
#define RGB_LED_PIN 48
#define NUM_LEDS 1

class Buzzer {
public:
  Buzzer(uint8_t pin, uint8_t channel) : _pin(pin), _channel(channel) {
    ledcSetup(_channel, 2000, 8);  // 2 kHz PWM, 8-bit resolution
    ledcAttachPin(_pin, _channel);
  }

  void playTone(uint32_t frequency, uint32_t duration) {
    ledcWriteTone(_channel, frequency);
    delay(duration);
    ledcWriteTone(_channel, 0);
  }

  void stopTone() {
    ledcWriteTone(_channel, 0);
  }

private:
  uint8_t _pin;
  uint8_t _channel;
};

Buzzer buzzer1(15, 0); // Instantiate Buzzer object with pin 15 and channel 0
Buzzer buzzer2(6, 1);  // Instantiate second Buzzer object with pin 6 and channel 1

Buzzer buzzers[] = {buzzer1, buzzer2};

Adafruit_NeoPixel rgbLED(NUM_LEDS, RGB_LED_PIN, NEO_GRB + NEO_KHZ800);

FlaskHttp flaskHttp(SERVER, GET_END_POINT, POST_END_POINT);

void setup() {
  // Serial monitor
  Serial.begin(115200);

  // Initialize the RGB LED
  rgbLED.begin();
  rgbLED.show(); // Initialize all pixels to 'off'

  // Wi-Fi configuration
  WiFi.begin(H_N, H_A);
  while (WiFi.status() != WL_CONNECTED) {
    setLEDColor(255, 0, 0); // Red color
    delay(500);
    Serial.print(".");
  }
  setLEDColor(0, 255, 0); // Green color
  Serial.println("Wi-Fi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

  pinMode(START_BUTTON_PIN, INPUT_PULLUP);
  pinMode(BINGO_BUTTON_PIN, INPUT_PULLUP);
}

void loop() {
  if (WiFi.status() == WL_CONNECTED) {
    setLEDColor(0, 255, 0); // Green color to indicate Wi-Fi is connected
    // Check if the start button is pressed
    if (digitalRead(START_BUTTON_PIN) == LOW) {
      Serial.println("Start button pressed, sending command...");
      int responseCode = flaskHttp.postCommand("start");
      if (responseCode == 200) {
        setLEDColor(253, 115, 255); // Purple color for success
        delay(3000);
      }
      delay(500);
    }

    if (digitalRead(BINGO_BUTTON_PIN) == LOW) {
      Serial.println("Bingo button pressed, sending command...");
      int responseCode = flaskHttp.postCommand("bingo");
      for (uint8_t i = 0; i < 2; i++) {
        buzzers[i].playTone(2000, 100);
        delay(100);
        buzzers[i].playTone(1000, 100);
        delay(100);
        buzzers[i].playTone(1500, 100);
        delay(100);
        buzzers[i].playTone(3000, 100);
        delay(100);
        buzzers[i].playTone(500, 100);
        delay(100);
        buzzers[i].stopTone();
      }
      if (responseCode == 200) {
        setLEDColor(253, 115, 255); // Purple color for success
        delay(3000);
      }
      delay(500); 
    }
  } else {
    setLEDColor(255, 0, 0); // Red color to indicate Wi-Fi is not connected
    Serial.println("Wi-Fi not connected.");
    // Attempt to reconnect
    WiFi.begin(H_N, H_A);
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
    setLEDColor(0, 255, 0); // Green color to indicate Wi-Fi is connected
    Serial.println("Wi-Fi reconnected.");
  }
}

void setLEDColor(uint8_t red, uint8_t green, uint8_t blue) {
  rgbLED.setPixelColor(0, rgbLED.Color(red, green, blue));
  rgbLED.show();
}
