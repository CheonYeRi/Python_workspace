void setup() {
  Serial.begin(9600);
  pinMode(10, OUTPUT);

}

void loop() {
  int readValue = analogRead(A0);
  Serial.println(readValue);
  readValue = map(readValue, 0 ,1023, 0 ,255);
  // map() > 첫번째 매개변수를 네/다섯번째 범위로 1:1 매핑해주는 역할
  // map(매핑하고자 하는 값, 기존값의 최솟값, 기존값의 최댓값, 매핑할 값의 최솟값, 매핑할 값의 최댓값)
  // map(50,50,100,0,100);
    //첫 번째 매개변수 > 50 > 50-100
    // 결과값 > 0 > 0 - 100
  analogWrite(10, readValue);
  delay(100);

}