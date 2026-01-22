#define TRIG 10
#define ECHO 8
#define LED 5
#define PIEZO 11


void setup() {
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(5, OUTPUT);
  pinMode(11,OUTPUT);
}

void loop() {
  digitalWrite(TRIG, HIGH);
  delay(10);
  digitalWrite(TRIG, LOW);
  digitalWrite(LED,LOW);
  digitalWrite(PIEZO,LOW);

  float duration = pulseIn(ECHO, HIGH);
  float distance = ((34000*duration)/10000000)/2;
  Serial.print(distance);
  Serial.println("cm");
  delay(100);
  if(distance < 10){
    Serial.println("물체 가까움!");
    digitalWrite(LED, HIGH);
    digitalWrite(PIEZO, HIGH);
  } else {
    return;
  }
  delay(500);
  //평소, 기본 상태를 if문 기준으로 삼으면 실행은 LOW/ else는 HIGH로 하면 된다. 
}