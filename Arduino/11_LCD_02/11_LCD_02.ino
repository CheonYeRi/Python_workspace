#include <LiquidCrystal_I2C.h> //외부 라이브러리 불러오기
#include <Servo.h>


Servo myServo;
LiquidCrystal_I2C myLCD(0x27, 16 ,2); 

int angle = 0;

void setup() {
  myServo.attach(8);
  myLCD.init();
  myLCD.backlight();  


}

void loop() {
  int angleVal = analogRead(A0);
  angle = map(angleVal, 0 ,1023, 0 ,180);
  // map() > 첫번째 매개변수를 네/다섯번째 범위로 1:1 매핑해주는 역할
  // map(매핑하고자 하는 값, 기존값의 최솟값, 기존값의 최댓값, 매핑할 값의 최솟값, 매핑할 값의 최댓값)
  // map(50,50,100,0,100);
    //첫 번째 매개변수 > 50 > 50-100
    // 결과값 > 0 > 0 - 100
  myServo.write(angle);

  myLCD.setCursor(0,0);
  myLCD.print("Servo Angle");
  myLCD.setCursor(0,1);
  myLCD.print(angle);

  delay(500);

  myLCD.clear();
}