const int piezo_pin = 8; 
//const 절대 값이 바뀌지 않는 읽기 타입 선언 > 이후 값 수정 불가
const int melody[] = {
  // 도, 레, 미, 파, 솔, 라, 시, 도
  262, 294, 330, 349, 392, 440, 494, 523
}; //이름[]={} 배열 지정

void setup() {
  tone(piezo_pin, melody[0], 500); 
  delay(500); //500 = 0.5초
  tone(piezo_pin, melody[1], 500); 
  delay(500);
  tone(piezo_pin, melody[2], 500); 
  delay(500);
  tone(piezo_pin, melody[3], 500); 
  delay(500);
  tone(piezo_pin, melody[4], 500); 
  delay(500);
  tone(piezo_pin, melody[5], 500); 
  delay(500);
  tone(piezo_pin, melody[6], 500); 
  delay(500);
  tone(piezo_pin, melody[7], 500) ; 
  delay(500);

  for (int i = 0 ; i < 8; i ++){
    tone(piezo_pin, melody[i],500);
    delay(500;)
  }
}

//for 문으로 개선tone(piezo_pin, melody[0], 500) ; delay(500);
void loop() {

}