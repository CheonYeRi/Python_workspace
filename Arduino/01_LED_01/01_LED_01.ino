
void setup() {
  pinMode(3, OUTPUT); // 디지털 3번 핀을 출력으로 사용한다 정의
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(3, HIGH);  // 3번 핀을 HIGH(5v)로 출력해 > 빛 켜짐
  delay(1000);                      // 켜진 상태로 1초 중지
  digitalWrite(3, LOW);   // 3번 핀을 LOW(0V)로 출력해 > LED 꺼짐
  delay(1000);                      // 켜진 상태로 1초 중지
}
