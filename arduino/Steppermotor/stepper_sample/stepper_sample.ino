//Includes the Arduino Stepper Library
#include <Stepper.h>

// Defines the number of steps per rotation
const int stepsPerRevolution = 2048;

// Creates an instance of stepper class
// Pins entered in sequence IN1-IN3-IN2-IN4 for proper step sequence
Stepper candyMotor = Stepper(stepsPerRevolution, 12, 10, 11, 9);

void setup() {
    Serial.begin(115200);
}

void loop() {
    Serial.println("Looping...");
    // Rotate CW slowly at 5 RPM
    candyMotor.setSpeed(10);
    candyMotor.step(-stepsPerRevolution);
    delay(1000);
    
    // // Rotate CCW quickly at 10 RPM
    // candyMotor.setSpeed(10);
    // candyMotor.step(-stepsPerRevolution);
    // delay(1000);
}