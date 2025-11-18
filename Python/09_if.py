'''
조건문
조건에 따라서 프로그램의 실행 흐름을 분기시키는 제어문
조건: 참/거짓 구분할 수 있는 문장
'''

#조건문 기초 문법
#if + 조건 > 조건이 참이면 실행

'''
a = int(input())
if a > 10:
    print("a는 10보다 커요")
print("조건문 종료")
'''

#들여쓰기 오류
#if a > 10:
#   print("a는 10보다 커요") #IndentationError 뜸 
# 알아볼 수 있을 정도의 공백도 돌아가나, tab 공백이면 전부 tab공백으로 일관성 있는 게 좋다.

#조건문에 실행할 코드를 작성하지 않았을 때
#pass 로 해당 조건문을 넘길 수 있다.
#if a > 100:
#    pass 
#IndentationError 떠서 pass 붙이면 안 뜸.

#실습1
#날씨 = input("오늘의 날씨를 입력하세요.(비/맑음): ")
#if 날씨 == "비":
#    print("우산을 챙기세요!") #명령어에서 언어는 "" 표시를 해야 인식되는 듯 하다.
#if 날씨 == "맑음":
#    print("선크림을 바르세요!")

#if + else 문
#조건이 참일 때는 if 문, 조건이 거짓일 때는 else문을 실행
#else > ~아니라면 의 의미라서 조건 필요 X 대신 if문과 같이 나와야 한다.
#a = int(input())
#if a > 10:
#    print("a는 10보다 커요.")
#else:
#    print("a는 10보다 작아요.")
    
#실습2
#정수 = int(input("정수를 입력해주세요.: "))
#계산 = 정수 % 2
#if 계산 == 0:
#    print("짝수입니다.")
#else:
#    print("홀수입니다.")

#if - elif - else 구문
#elif: else if의 약자
#elif 에서 조건을 반드시 기록
#if 가 있어야 사용 가능

'''
score = int(input())
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
'''

#실습3: 사용자의 나이를 입력받아 관람 가능한 등급을 출력하는 프로그램

'''
사용자_나이 = int(input())
if 사용자_나이 >= 19:
    print("청소년 관람불가 가능")
elif 사용자_나이 >= 16:
    print("15세 이상 관람가")
elif 사용자_나이 >= 13:
    print("12세 이상 관람가")
else:
    print("전체 관람가")
'''

#실습4: 초를 입력하면 시, 분, 초로 나누어 알려주는 프로그램
#구조를 통해 명령어 만들 요령을 모르겠어서 설명 듣고 싶어진다.
#이 실습 4문제 해설 듣기.
'''
hour, minute, second = 0, 0, 0
time = int(input())
#60s = 1m, 60m =1h
minute = time // 60 #60으로 나누고 남은 몫
second = time % 60 #나누고 남은 나머지
hour = minute // 60 #분에서 60으로 나누고 나온 몫
minute %= 60 #60나누고 나머지 값

if hour > 0:
    print(f"{hour}시간{minute}분 {second}초")
elif minute > 0:
    print(f"{minute}분 {second}초")
else:
    print(f"{second}초")
'''

#중첩 조건문
#하나의 if문 안에 또다른 if문을 작성하는 것
'''
username = input("관리자 아이디를 입력하세요.: ")
password = input("비밀번호를 입력하세요.: ")

if username == "admin":
    if password == "abcd":
        print("관리자 로그인 성공")
    else:
        print("비밀번호가 틀렸습니다.")
else:
    print("존재하지 않는 사용자입니다.")
'''


#실습5 <직접 풀지 못해 정해진 과정 메모.
#상수로 정보 기입할 때 보통 대문자를 쓴다. 값이 변하지 않는 정보라는 의미로.
#먼저 금액을 입력 받습니다.
'''
김밥 = "김밥"
삼김 = "삼각김밥"
도시락 = "도시락"
a_price, b_price, c_price = 2500, 1500, 4000
#사용자가 어떤 식의 입력을 할 지 모르니 오류, 중복을 줄이고자 가독성 신경 써서 짠다고 함.

주문 = input("무엇을 주문하겠습니까?(김밥/ 삼각김밥/도시락): ")
금액 = int(input("금액을 입력하세요.: "))

if 주문 == 김밥:
    if 금액 >= a_price:
        print(f"{김밥}을 구매했습니다.")
    else:
        print("금액이 부족합니다.")
elif 주문 == 삼김:
    if 금액 >= b_price:
        print(f"{삼각김밥}을 구매했습니다.")
    else:
        print("금액이 부족합니다.")
elif 주문 == 도시락:
    if 금액 >= c_price:
        print(f"{도시락}을 구매했습니다.")
    else:
        print("금액이 부족합니다.")
else:
    print("입력이 잘못됐습니다.")
'''
#윗 조건이 결정되면(주문) 아랫 조건도 결정된다.(금액)
#딕셔너리가 짝을 이루는 값이니, 저 형태를 딕셔너리 형태로 묶어도 된다. 
# 2) 딕셔너리 활용한 코드.
가격 = {
    "김밥" : 2500,
    "삼각김밥" : 1500,
    "도시락": 4000
}
주문 = input("무엇을 주문하겠습니까?(김밥/ 삼각김밥/도시락): ")
금액 = int(input("금액을 입력하세요.: "))
#딕셔너리에 밸류에 접근하는 방법 N.get 또는 [딕셔너리]

if 주문 in 가격:
    if 금액 >= 가격[주문]:
        print(f"{주문}을 구매했습니다.")
    else:
        print("금액이 부족합니다.")
else:
    print("입력이 잘못됐습니다.")