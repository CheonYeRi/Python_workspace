int BTN = 12; //연결 핀 변수 선언


void setup() {
  Serial.begin(9600);
  pinMode(BTN,INPUT_PULLUP); // 기본 상태가 1(HIGH, 5v), 스위치가 눌렀을때 0 (LOW,0v) 

}

void loop() {
  int BTNState= digitalRead(BTN);
  Serial.println(BTNState);
  delay(500);
}