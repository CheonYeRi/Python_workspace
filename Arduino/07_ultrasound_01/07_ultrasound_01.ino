#define TRIG 10
#define ECHO 8

void setup() {
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

}

void loop() {
  digitalWrite(TRIG, HIGH);
  delay(10); //Microsecondes 
  digitalWrite(TRIG, LOW);

  float duration = pulseIn(ECHO, HIGH);
  float distance = ((34000*duration)/10000000)/2;
  //편도 거리로 바꾸기 위해 마지막에 /2 붙는다. (측정 거리가 왕복이기 때문에)
  Serial.println(distance);
  Serial.println("cm");
  delay(100);
}
