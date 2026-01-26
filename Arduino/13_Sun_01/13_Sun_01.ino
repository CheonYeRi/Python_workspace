const int PANLE = A0; // 태양광 패널 입력
const int SW_PIN = 2; // 판매 버튼(INPUT_PULLUP)

long energy = 0; // 가상 에너지 저장소
// const로 변수 고정할 수 없으니 long 선언 (누적 합산될테니까)

const long SELL_UNIT = 100; //판매 단위 (원하는 만큼 설정 가능)

const int MAX_CHARGE_RATE = 50; //충전 스케일 조정 (밝을수록 더 빠르게 charging)
//전압이 5v일 때 50+ 적립

void setup(){
  Serial.begin(9600);
  pinMode(SW_PIN, INPUT_PULLUP);
}


void loop() {
  // 1 태양광 패널 전압 읽기 (0-5V)
  int raw = analogRead(PANLE); // raw 변수값 지정
  float voltage = (raw * 5.0) / 1023.0;

  // 2 전압 기반 충전 공식
  //gain = (전압비율) x (최대충전량)
  int gain = (voltage / 5.0) * MAX_CHARGE_RATE; //위에 선언한 voltage 값을 활용해 gain 변수 선언
  
  //햇빛이 없어서 충전이 되지 않을 때의 예외 처리
  if (gain > 0 ) {
    energy += gain;
  }

  // 판매 버튼 눌림 감지
  // 논리형 선언해서 이전 상태를 기준으로 설정
  bool prev = HIGH; // INPUT_PULL 선언 기준으로 해서.
  bool curr = digitalRead(SW_PIN);

  if (prev == HIGH && curr == LOW) {
    // && 그리고. curr 버튼이 눌렸다면 기준.
    Serial.println("== 판매 요청 발생 ==");

    if(energy >= SELL_UNIT){
      //에너지가 판매하는 양보다 많다면
      energy -= SELL_UNIT; //판매하기 위해 빼기 산술
      Serial.print("판매 성공| 판매량: ");
      Serial.print(SELL_UNIT);
      Serial.print("| 남은 에너지: ");
      Serial.println(energy);
    } else {
      Serial.print("저장된 에너지가 없어 판매할 수 없습니다. | 현재 에너지: ");
      Serial.println(energy);
    }
  }
  prev = curr; //재 할당

  //현재 상태 출력
  Serial.print("전압: ");
  Serial.print(voltage);
  Serial.print("v| 적립량: ");
  Serial.print(gain);
  Serial.print("| 현재 저장된 에너지량");
  Serial.print(energy);

  delay(500);
}

