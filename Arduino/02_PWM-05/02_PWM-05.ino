int BTN = 12;
int Light = 4; 

void setup() {
  Serial.begin(9600);
  pinMode(BTN,INPUT_PULLUP);
  pinMode(Light, OUTPUT);

}

void loop() {
  int BTNState= digitalRead(BTN);
  digitalWrite(Light, LOW);

  if(BTNState == LOW){
    Serial.println("BTN:BLUE");
    digitalWrite(Light, HIGH);
  }
  delay(100);
}
