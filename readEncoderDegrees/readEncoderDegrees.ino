#include <PRIZM.h>
PRIZM prizm;

void setup() {
  prizm.PrizmBegin();
  Serial.begin (115200);
}

void loop() {
  long eCount = prizm. readEncoderDegrees(1);
  Serial.println(eCount);
}
