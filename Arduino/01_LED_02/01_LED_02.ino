
int Led_pin = 3; // int(정수) 타입명 변수 선언

void setup() {
  pinMode(Led_pin, OUTPUT); // 디지털 3번 핀을 출력으로 사용한다 정의
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(Led_pin, HIGH);  // 3번 핀을 HIGH(5v)로 출력해 > 빛 켜짐
  delay(1000);                      // 켜진 상태로 1초 중지
  digitalWrite(Led_pin, LOW);   // 3번 핀을 LOW(0V)로 출력해 > LED 꺼짐
  delay(1000);                      // 켜진 상태로 1초 중지
}

//unsigned int = 음수 포함하지 않는 정수 / char = 문자열  