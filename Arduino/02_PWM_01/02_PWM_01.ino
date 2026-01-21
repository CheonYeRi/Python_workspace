
void setup() {
  pinMode(3, OUTPUT);

}

void loop() {
  analogWrite(3, 255);
  delay(1000);

  for (int brightness = 0; brightness < 256 ; brightness++){
    analogWrite(3, brightness);
    delay(10); // 0.01초 마다 밝기 밝아짐.
  }
}
