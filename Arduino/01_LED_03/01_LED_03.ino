/*
Ctrl + N 아두이노 새 스케치 열기

새로운 스케치를 열면 새로운 창이 열림

아두이노 IDE에서는 탭 방식이 아닌 여러 창을 사용하는 방식이기 때문

스케치 = 하나의 폴더
폴더 = 하나의 독립 프로젝트
그래서 .ino 파일은 새로운 폴더 안에 생김

아두이노는 폴더 이름과 동일한 .ino 파일을 "메인 파일"로 간주
같은 폴더 안의 .ino 파일은 하나의 코드처럼 합쳐서 컴파일

즉, 하나의 스케치 폴더 안에는 .ino 파일이 여러개 있다면 하나의 큰 코드로 인식

하나의 스케치 폴더 안에는 setup(), loop()가 단 하나씩만 존재해야 함.
*/

int Red_p = 12;
int Green_p = 11;
int Blue_p = 10;


void setup() {
  pinMode(Red_p, OUTPUT);
  pinMode(Green_p, OUTPUT);
  pinMode(Blue_p, OUTPUT);
}

//버전 1 0.5초마다 하나씩 켜지고, 하나씩 꺼지는 코드
void loop() {
  digitalWrite(Red_p, HIGH);
  delay(500);
  digitalWrite(Green_p, HIGH);
  delay(500);
  digitalWrite(Blue_p, HIGH);
  delay(500);
  digitalWrite(Red_p, LOW);
  delay(500);
  digitalWrite(Green_p, LOW);
  delay(500);
  digitalWrite(Blue_p, LOW);
  delay(500);
}
