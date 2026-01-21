
/*
Serial :시리얼 통신을 담당하는 객체
  시리얼 통신: 글자, 숫자, 데이터를 주고 받는 통신

Serial.begin() : 이 속도로 통신 시작해라.
- 아두이노가 PC와 통신하기 위해 시리얼 통신을 시작하겠다 명시하는 코드
- 매개변수로 넣은 값 속도로 시리얼 통신을 시작함
- 통신속도는 대체로 9600 사용
  -오래전부터 사용해온 안정적이고 에러없는 표준 속도
    - 통신 속도가 너무 빠르면 데이터 손실 생김, 느리면 데이터 전송이 불편
  -거의 모든 장치가 지원하는 속도
-setup() 함수 내에 한번만 작성하면 됨. 


*/


void setup() {
  Serial.begin(9600);
  pinMode(3, OUTPUT);

}

void loop() {
  for (int brightness = 0; brightness < 256 ; brightness++){
    analogWrite(3, brightness);
    delay(10); // 0.01초 마다 밝기 밝아짐.
  }
  Serial.println(brightness); //println은 출력 + 줄바꿈
}
