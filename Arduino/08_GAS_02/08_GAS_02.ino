#define GAS_AO A0  
#define GAS_DO 8
#define LED 5
#define PIEZO 11


void setup() {
  Serial.begin(9600);
  pinMode(GAS_AO, INPUT);
  pinMode(GAS_DO, INPUT);
  Serial.println("히터 가열 시작");
  delay(1000);
  Serial.println("히터 가열 종료 동작 시작");

  pinMode(5, OUTPUT);
  pinMode(11,OUTPUT);
}

void loop() {
  float sensorValue = analogRead(GAS_AO);
  int sensorDValue = digitalRead(GAS_DO);
  digitalWrite(LED,LOW);
  digitalWrite(PIEZO,LOW);

  Serial.print("아날로그 센서 입력:");
  Serial.println(sensorValue);

  Serial.print("|");
  Serial.print("디지털 센서 입력:");
  Serial.println(sensorDValue); 

  if(sensorValue > 100) {
    Serial.println("|");
    Serial.println("!! 연기 감지 !!");
    digitalWrite(LED, HIGH);
    digitalWrite(PIEZO, HIGH);
  }

  delay(1000);
}