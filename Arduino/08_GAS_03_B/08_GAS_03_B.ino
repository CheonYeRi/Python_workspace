#define GAS_AO A0  
#define GAS_DO 8
#define LED_R 5
#define LED_B 4
#define LED_G 6
#define PIEZO 11

#include <DHT.h>
#include <DHT_U.h>

#define DHTPIN 2
#define DHTTYPE DHT22 

DHT myDHT(DHTPIN, DHTTYPE);


void setup() {
  Serial.begin(9600);
  pinMode(GAS_AO, INPUT);
  pinMode(GAS_DO, INPUT);
  Serial.println("히터 가열 시작");
  delay(1000);
  Serial.println("히터 가열 종료 동작 시작");

  pinMode(5, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(11,OUTPUT);
  myDHT.begin();
}

void loop() {
  delay(2000);
  float sensorValue = analogRead(GAS_AO);
  int sensorDValue = digitalRead(GAS_DO);
  digitalWrite(LED_R,LOW);
  digitalWrite(LED_B,LOW);
  digitalWrite(LED_G,LOW);
  digitalWrite(PIEZO,LOW);
 /*
  float h = myDHT.readHumidity(); //습도 읽을 감
  float c = myDHT.readTemperature(); //섭씨 온도 값 읽어옴.
  float f = myDHT.readTemperature(true); //화씨 온도 값 읽어옴.
*/
  Serial.print("디지털 센서 입력:");
  Serial.println(sensorDValue); 

  if(sensorValue < 20) {
    Serial.print("아날로그 센서 상태: 안전 ");
    Serial.println(sensorValue);
    digitalWrite(LED_G, HIGH);
    delay(1000);

  } else if (sensorValue > 50) {
    Serial.print("아날로그 센서 상태: 보통");
    Serial.print(sensorValue);
    digitalWrite(LED_B, HIGH);
  } else if (sensorValue > 100){
    Serial.println("|");
    Serial.println("!! 연기 감지 !!");
    digitalWrite(LED_R, HIGH);
    digitalWrite(PIEZO, HIGH);
  }
  
  delay(1000);

}
