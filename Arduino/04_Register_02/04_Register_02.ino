void setup() {
  Serial.begin(9600);
  pinMode(3, OUTPUT);

}

void loop() {
  int readValue = analogRead(A0);
  Serial.println(readValue);
  readValue = map(readValue, 0 ,1023, 0 ,255);
  analogWrite(3, readValue);
  delay(10);

}