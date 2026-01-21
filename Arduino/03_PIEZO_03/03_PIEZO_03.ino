
const int BTN = 10;
const int piezo_pin = 8; 
const int melody[] = {
  262, 294, 330, 349, 392, 440, 494, 523
}; 


void setup() {
  Serial.begin(9600);
  pinMode(BTN,INPUT_PULLUP);
  pinMode(piezo_pin, OUTPUT);
}

void loop() {
  int BTNstate= digitalRead(BTN);
  digitalWrite(piezo_pin,LOW); //디버깅 코드

  if(BTNstate == LOW){
    Serial.println("부저 ON");
    // digitalWrite(piezo_pin, HIGH);
    tone(piezo_pin, melody[3], 500); // tone 하나는 한 개만 인식한다. 여러개 써야 멜로디 연주 가능하다.
  } else {
    Serial.println("부저 OFF");
  }
  delay(100);
}
