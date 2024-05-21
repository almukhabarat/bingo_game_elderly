#include <Stepper.h>

// Defines the number of steps per rotation
const int stepsPerRevolution = 2038;

// Creates an instance of stepper class
Stepper myStepper = Stepper(stepsPerRevolution, 9, 11, 10, 12);

void setup() {
}

void loop() {
  myStepper.setSpeed(20);
  myStepper.step(stepsPerRevolution);
  delay(1000);
}