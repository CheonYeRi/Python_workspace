void setup() {
  Serial.begin(9600);
  pinMode(8, OUTPUT);
  
}

void loop() {
  int photoresistor = analogRead(A0);
  Serial.println(photoresistor);  

  if(photoresistor > 1000 ) {
    digitalWrite(8, HIGH);
  } else {
    Serial.println("OFF");
    digitalWrite(8,LOW);
  }
  delay(500);
}
