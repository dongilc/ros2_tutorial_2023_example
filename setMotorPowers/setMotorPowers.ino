#include <PRIZM.h>
PRIZM prizm;

void setup() {
  prizm.PrizmBegin();
  prizm.setMotorInvert(1,1);
}

void loop() {
  prizm.setMotorPowers(35,35);
}