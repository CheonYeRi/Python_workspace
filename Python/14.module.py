# 모듈(module)
#여러 기능(함수)의 묶음
#하나의 py파일로 여러 기능을 모아놓은 곳

'''
#모듈 불러오기(1)
import hello

hello.greeting("lee")

#모듈 불러오기(2)
from hello import greeting

greeting("kim")

#모듈 불러오기(3)
from hello import * #전체를 다 불러옴.

introduce("sin",15)

#모듈 불러오기(4)
import hello as h #h로 모듈 약칭하겠다.
h.greeting("kim")
h.introduce("U",10)
'''

'''
#실습
import calc as C
C.add(10,5)
C.subtract(8,2)
C.multiply(7,4)

from calc import divide
divide(9,0)
divide(5,2)

#패키지
#모듈의 묶음
#모듈을 폴더 단위로 묶어놓은 곳

#패키지 폴더 만들어서 py 파일 넣고 모듈 불러와서 쓰면 __pycahe__라는 게 생성된다.

#패키지에서 모듈 불러오기(1)
from my_package import calc as c

#패키지에서 모듈 불러오기(2)
from my_package.calc import add
c.add(10,5)

# 파이썬 표준 라이브러리

#math 모듈: 수학적 연산에 사용되는 모듈
import math as m

#1.올림/내림
#ceil: 올림, 소수점 지정x
m.ceil(3.14)

#floor: 내림, 소수점 저정x
m.floor(3.14)

#round :반올림 - 내장 함수 (math 모듈 아님)
round(3.141492, 2)

#2. 제곱, 제곱근
# pow(x, y) : 제곱 - x^y
m.pow(2,3)

#sqrt(x): 제곱근 반환
m.sqrt(16)

#3. 상수
#pi : 원주율
print(m.pi)

#4. 수학 계산 편의 기능
print(m.factorial(3))

#최대 공약수
print(m.gcd(12,80))

#최소 공배수
print(m.lcm(12,20))

'''
#실습 math모듈 사용
import math as m

x1, y1 = 10, 52
x2, y2 = 4, 30
'''
#모범 답안
x1,y1 = map(int, input("x1, y1을 입력해주세요.: ").split(","))
#int(x1), int(y1)
x2,y2 = map(int, input("x2, y2을 입력해주세요.: ").split(","))
#int(x2), int(y2)
'''
'''
dis = m.sqrt(m.pow(x2 -x1, 2) +m.pow(y2 - x1, 2))
print(f" 거리 값 {round(dis, 2)}")

#최소 공배수, 최대 공약수
s,t= 18,24
print(m.gcd(s,t))
print(m.lcm(s,t))
'''
'''
# random 모듈: 랜덤 값(난수) 생성 시 사용
import random

# 1 난수 생성
#random() : 0이상 1미만의 float 난수 반환
print(random.random())

#uniform(a,b) : a이상 b이하의 실수 난수 반환
print(random.uniform(1,10))

#randint(a,b): a이상 b이하의 정수 난수 반환
print(random.randint(5,20))

#randrange(start, stop ,step): 범위 안의 정수 난수 반환, 간격 지정시 
print(random.randrange(0, 100, 5))

# 2 랜덤 선택
fruits = ["apple","banana","watermelon","grape","orange"]

# choice(seq) : 시퀀스에서 임의의 요소 1개 반환
print(random.choice(fruits))

# choices(seq,k): 시퀀스에서 "중복 허용" k개 요소 리스트를 반환
print(random.choices(fruits, k = 2))

# 섞기
#sample(seq,k): 시퀀스에서 "중복 없이" k개 요소 리스트를 반환
print(random.sample(fruits, k = 2))

#shuffle(seq): 시퀀스의 요소를 무작위로 섞음 <- 원본 시퀀스를 변경
number = [1,2,3,4,5]
random.shuffle(number)
print(number)
'''

'''
# 실습
import random
lotto = []
num = random.randint(1,45)
for n in range(6):
    while num in lotto:
        num = random.randint(1,45)
    lotto.append(num)

print(sorted(lotto))

#모범 답안
result = sorted(random.sample(range(1,46), k= 6))
print(result)

lotto = []
while len(lotto) < 6:
    num = random.randint(1,45)



import random as r

com = ['가위','바위','보']
user = input("가위,바위,보: ")

def game(user):
    com_c =r.choice(com)
    if user == com_c:
        return "무승부"
    elif user == "가위" and com_c == "보":
        return "승"
    elif user == "바위" and com_c == "가위":
        return "승"
    elif user == "보" and com_c == "바위":
        return "승"
    else:
        return "패"

print(game(user))


#모범 답안
RPS = ["가위", "바위", "보"]
win_count = 0

while win_count < 3:
    com_choice = random.choice(RPS)
    user_choice = input("가위, 바위, 보 : ")

    print(f"유저의 선택: {user_choice}")
    print(f"컴퓨터의 선택: {com_choice}")

    if user_choice == com_choice:
        print("무승부")
    elif ((user_choice == "가위" and com_choice == "보") or
          (user_choice == "바위" and com_choice == "가위") or
          (user_choice == "보" and com_choice == "바위")):
        print("이겼습니다")
        win_count += 1
    elif user_choice in RPS:
        print("졌습니다")
    else:
        print("잘못된 입력이에요")

'''
'''
# datetime 모듈
# 날짜와 시간의 생성, 조작, 현실 변환과 같은 시간 관련 기능을 제공
import datetime

# 1 날짜/ 시간 구하기
# 현재 날짜와 시간 구하기
print(datetime.datetime.now())

# 오늘 날짜만 구하기
today = datetime.date.today()
print(today)

# 2. 날짜/ 시간 형식 변환 < 왜 작동을 안 하지...
formatted = now.strftime("%Y/%m/%d %H:%M:%S")
print(formatted)

parsed = datetime.datetime.strptime(formatted, "%Y/%m/%d %H:%M:%S")
print(parsed)

# 3. 날짜/ 시간 연산
dt = datetime.date(2025, 7, 7)
passed_time = today - dt
print(f"{passed_time.days}일이 지났습니다.")

# 4. 요일반환: weekday
# 0: 월요일 ~ 7: 일요일
days = ["월","화","수","목","금","토","일"]
day_num = today.weekday()
print(days[day_num])

# datetime 또는 date 갹체에는 년/월/일 시간 등의 속성으로 들어있음.
print(datetime.datetime.now().year)
'''

#실습
#사용자로부터 생일 입력 받고, 오늘 날짜를 기준으로 올해 또는 내년 생일까지 남은 날짜(일 수) 계산 출력
import datetime
'''
my_birth = input("생일 입력하세요.: ")
today = datetime.date.today()
if my_birth < today:
    dday = datetime.date(today.year +1, month, day)
else:
    dday = my_birth - today


print(f"{dday.days}일 남았습니다.")
#작성 못해서 봉인함...
'''
'''
#모범 답안
#사용자로부터 생일 입력 받음
birth_month, birth_day = map(int,input("생일을 입력하세요.(예 03-14): ").split("-"))
today = datetime.date.today()
# 올해 생일은 date 객체로 변환
birthday_this_year = datetime.date(today.year, birth_month, birth_day)
#오늘 날짜와 올해의 생일을 비교
if today > birthday_this_year:
    #올해 생일이 지났으면 내년으로 설정
    birthday_naxt = datetime.date(today.year + 1, birth_month, birth_day)
else:
    #올해로 설정
    birthday_naxt = birthday_this_year

#남은 일수 계산
day_left = (birthday_naxt - today).days

print(f"다음 생일까지 {day_left}일이 남았어요.")
'''
'''
# calender 모듈
# 날짜와 달력 관련 기능을 제공

import calendar

# 1. 달력 조회
print(calendar.prmonth(2025,9))
print(calendar.prcal(2025))

#텍스트로 값을 반환
print(calendar.month(2025, 11))

#요일 반환
print(calendar.weekday(2025,11,26))

'''
'''
#time 모듈
# 시간의 측정, 지연, 변환가 같은 시간 관련 기능 제공

import time

#1. 시간 반환
#time()
#Unix 타임 스탬프로 반환 (1920.1.1부터 경과 초)
print(time.time())

#ctime(): 현재 시간을 문자열로 반환
print(time.ctime())
print(time.ctime(0)) #기준 시로 반환 Thu Jan  1 09:00:00 1970 나옴.

#strptime(): 원하는 포켓의 문자열로 시간 객체 변환
lt = time.localtime()
formatted = time.strftime("%Y-%m-%d %H:%M:%S", lt)
print(formatted) #2025-11-26 12:37:35 형식으로 나옴.

#strptime(): 문자열을 struct_time 객체로 변환
parsed = time.strptime(formatted,"%Y-%m-%d %H:%M:%S")
print(parsed)

#2. 시간 지연
# sleep(seconds): 지정한 초만큼 프로그램이 일시 정지
time.sleep(1)
print("time sleep") #지연 후에 다음 코드 실행

#시간 측정하기
start = time.time()

for i in range(5):
    print(i)
    time.sleep(1)

end = time.time()
print(f"수행시간 : {end - start: .2f}초")

'''

'''
#실습
#타자 연습 게임 만들기

import random
import time

words = ["apple", "banana", "orange", "grape", "lemon",
    "peach", "melon", "cherry", "plum", "pear",
    "school", "friend", "family", "flower", "garden",
    "window", "bottle", "pencil", "summer", "winter",
    "happy", "future", "travel", "animal", "market",
    "doctor", "planet", "energy", "nature", "memory"
    ]

input("[타자 게임] 준비되면 엔터 ")
start = time.time()
n = 1
while n <= 10:
    q = random.choice(words)
    print(f"문제 {n} : {q}")
    x = input()
    if x == q:
        print("통과!")
        n += 1
    else:
        print("다시 입력!")
        continue
        
    
end = time.time()
#et = end - start
#et = format(et, ".2f")
#print(f"총 걸린 시간{et}초")
print(f"총 걸린 시간{end - start:.2f}")

#모범 답안
input("[타자 게임] 준비되면 엔터 ")
start = time.time()

while n < 11:
    print(f"{n}번 문제")
    q = random.choice(words)
    print(q)
    while True: #문제가 계속 바뀌지 않고 고정하기 위한 방법 
        answer = input()

        if answer == q:
            print("통과!")
            n += 1
            break
        else:
            print("다시 도전!")

end = time.time()
play_time = end - start
print(f"총 소요시간: {play_time:.2f}초")
'''

#sys 모듈
# 파이썬 인터프리터와 관련된 다양한 기능 제공

import sys

#파이썬 버전 정보
print(sys.version) #3.14.0

#운영 체제 정보
print(sys.platform) #win32

#프로그램 종료
#sys.exit() #강제 종료
print("실행되지 않는 코드") #위 코드로 인해 그 아래 코드들이 출력되지 않는다.


#os 모듈
# 운영체제와 상호작용 할 수 있도록 도와주는 기능 제공

import os

# getcwd(): 현재 작업 디렉토리 반환
print(os.getcwd())

#lisrdir(): 현재 폴더 내 파일, 디렉토리 목록 반환
print(os.listdir())

#폴더 생성
folder_name = "sample_folder"
if not os.path.exists(folder_name): #서치했을 때 이 명칭이 존재하지 않다면- 양식
    os.mkdir(folder_name)
else:
    print(f"{folder_name} 폴더가 이미 있습니다.")

print(os.listdir())