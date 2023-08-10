void setup() {
  Serial.begin(115200);
  Serial.setTimeout(10);
}

void loop() {
}

void serialEvent(){
  String data = Serial.readStringUntil('\n');
  Serial.println(data);
}