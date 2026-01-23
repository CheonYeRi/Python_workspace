#include <LiquidCrystal_I2C.h> //외부 라이브러리 불러오기


LiquidCrystal_I2C myLCD(0x27, 16 ,2); 
  // 첫 번째 매개변수: 0x27 > I2C 통신 주소
  // 두 번째 매개변수: 열(가로)
    // 실습에서 사용하는 LCD는 16개 열로 구성(0~15)
  // 세 번째 매개변수: 행(세로)
    // 실습에서 사용하는 LCD는 2개 행으로 구성 (0~1)


void setup() {
  myLCD.init();
  myLCD.backlight();

}

void loop() {
  myLCD.setCursor(0, 0); // home() 도 동일 적용
  myLCD.print("Hello, World");
  delay(1000);

  myLCD.setCursor(0, 1);
  myLCD.print(" I'm Layla");
  delay(1000);

  myLCD.clear();
  delay(1000);
}
