int BTN = 2; //연결 핀 변수 선언


void setup() {
  Serial.begin(9600);
  pinMode(BTN,INPUT);

}

void loop() {
  int BTNState= digitalRead(BTN);
  Serial.println(BTNState);
  delay(500);
}
