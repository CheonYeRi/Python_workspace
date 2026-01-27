#include <SoftwareSerial.h>

SoftwareSerial myESP(2, 3); //D2 = RX(ESP TX) D3=TX(ESP RX)

// 우리가 사용하는 와이파이 모듈은 115200 속도를 지원함
// 115200 속도로 연결한 뒤에 9600으로 다운그레이드 할 예정

// ESP 모듈 속도가 9600으로 바뀌었는지 확인
void setup() {
  Serial.begin(9600);
  myESP.begin(9600);
  Serial.println("=== TEST 9600 ===");

}

void loop() {
  if (myESP.available()){
    Serial.write(myESP.read());
  }
  if (Serial.available()){
    myESP.write(Serial.read());
  }

}
