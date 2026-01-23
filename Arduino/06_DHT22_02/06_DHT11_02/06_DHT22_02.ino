#include <DHT.h>
#include <DHT_U.h>

#include <DHT.h> //매크로이기 때문에 ; 마무리 안 해도 된다.

#define DHTPIN 2
#define DHTTYPE DHT22 //실제 쓰는 도구 명칭 선언

DHT myDHT(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  myDHT.begin(); //한번 신호 주는 걸 선언
  
}

void loop() {
  delay(2000);
  float h = myDHT.readHumidity(); //습도 읽을 감
  float c = myDHT.readTemperature(); //섭씨 온도 값 읽어옴.
  float f = myDHT.readTemperature(true); //화씨 온도 값 읽어옴.
  Serial.println("습도,  ");

if(isnan(h) || isnan(c) || isnan(f)) {
    Serial.println("값을 읽어보지 못했습니다.");
    return;
  } // 아래 코드를 실행시키지 않기 위해 loop 함수 자체나감
  
  //정상 측정이 되었을 때 실행되는 코드
  Serial.print("습도,  ");
  Serial.println(h);
  Serial.print("섭씨,  ");
  Serial.println(c);
  Serial.print("화씨,  ");
  Serial.println(f);  
}