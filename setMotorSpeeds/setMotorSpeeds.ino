#include <PRIZM.h>
PRIZM prizm;

void setup() {
  prizm.PrizmBegin();
  Serial.begin (115200);
}

void loop() {
  prizm.setMotorSpeeds(50, 50);
}