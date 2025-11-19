'''
while문
조건이 true 인 동안 코드 반복하는 반복문
조건이 false가 되면 반복을 멈춤
반복 힛수가 정해지지 않았을 때 사용
'''

#while 기본 분법
#조건 : 참/거짓으로 구분할 수 있는 문장
#while 조건:
    #반복할 코드


#무한 루프
#사용시 주의, 반드시 종료 조건이 있어야 한다. #ctrl + c 누르면 실행 멈춤.

#while True:
#    print("반복 중")
'''
#예제1
light = "green"

while light == "green":
    print("계속 가세요")
    light = input("신호등의 신호를 입력하세요.(green/yellow/red): ")

print("중지!")
#green 제외한 답 나올 때까지 계속 물어봄.
'''

'''
#예제 2. 별도의 반복 변수를 정의
i = 0
while i < 5:
    print(i,"반복")
    i += 1
print("반복 종료")
'''
'''
secret_code = "coodingonre3"
code = input("비밀 코드를 입력하세요.: ")
while code != secret_code:
    print("비밀 코드가 틀렸습니다.")
    code = input("비밀 코드를 입력하세요.: ")
print("입장이 허용되었습니다!")

#축약 버전
while code != secret_code:
    code = input("비밀 코드를 입력하세요.: ")
print("입장이 허용되었습니다!")
'''
'''
#답안 듣기 전에 다른 분들 코드와 서치 통해 손 본 것.
N = int(input("숫자를 정합니다.(1~100): "))
try_count = 0

while True: 
    A = int(input("답을 정합니다.(1~100): "))
    try_count += 1

    if A == N:
        print(f"{try_count}만에 정답을 맞췄습니다.")
        break
    elif A < N:
        print("입력한 숫자보다는 작아요.")
    elif A > N:
        print("입력한 숫자보다 커요.")
#if 에서 true가 될 때를 상정하고 elif는 조건 벗어났을때(false)를 작성하는게 맞는 듯
# true는 왜 붙이는 거지. 

'''

'''
#모범 답안
N = int(input("숫자를 정합니다.(1~100): ")) 
#import random 코드 쓸 수 있다. 
# N = random.randint(1,100)
#print(N)
A = 0 #사용자 입력 변수
try_count = 0 #횟수 변수

while A != N:
    A = int(input("1-100 사이의 수를 정합니다.: "))
    try_count += 1

    if A > N:
        print("입력한 숫자보다는 커요.")
    elif A < N:
        print("입력한 숫자보다 작아요.")

print(f"{try_count}만에 정답을 맞췄습니다.")
'''

'''
#루프 제어문
running = True
while running:
    if 조건1:
        running = False

    if 조건2:
        running = False

#break문
while running:
    if 조건1:
        break
'''

'''
#예제1
i = 0

while True:
    print(i, "실행")
    my_select = input("메뉴를 골라주세요.: ")

    if my_select == "종료":
        break

    i += 1

print("반복문 종료")

#continue
i = 0
while i < 5:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
print("반복 종료")
'''
'''
#실습
#비밀 코드 입력
secret_code = "coodingonre3"
while True:
    code = input("비밀 코드를 입력하세요.: ")

    if code == secret_code:
        print("입장 완료!환영합니다.")
        break
    else:
        print("비밀 코드가 틀렸습니다. 다시 시도하세요.")
    
print("반복 종료")

#유효한 나이만 평균 내기
times = 0
sum_age = 0


while True:
    age = int(input("나이를 입력하세요: "))

    if age <= 0 or age >= 120:
        continue
    
    times += 1
    sum_age += age

    if times == 5:
        break

avg = sum_age / times
print(f"총 나이 합계는 {sum_age}, 평균은 {avg} 입니다.") 


#모범 답안
while times < 5:
    age = int(input("나이를 입력하세요: "))
    #나이가 0이하 또는 120 초과면 건너 뜀.
    if age <= 0 or age >= 120:
        continue
    # 정상 입력 시 코드.
    times += 1
    sum_age += age

print(f"총 나이 합계는 {sum_age}, 평균은 {int(sum_age / times)} 입니다.") 
'''
'''
# 중첩 while문
#예제

dan = 2
while dan <= 9:
    num = 1
    print(f"[ {dan}단 ]")

    while num <= 9:
        num += 1
        if num % 2 != 0:
            continue #면 짝수 곱하기로 나오고 break 하면 해당 수만 하고 멈춤.
        else:
            print(f"{dan} X {num} = {dan * num}")
    num += 1

    print()
    dan += 1
#실습

ID = "Re3_1234"
Pass_word = "56789"

while True: 
    id = input("아이디를 입력하세요: ")
    if id == ID:
        while True:
            password = input("비밀번호를 입력하세요.: ")
            
            if password != Pass_word:
                print("비밀번호가 틀렸습니다.")

            else:
                print("로그인 성공")
                break
    else:
        print("ID가 존재하지 않습니다.")
    break
    
'''

#추가 실습3
ID = "abc123"
PW = "7789"

while True: 
    print ("===로그인 화면===", sep="")
    In = input("1. 로그인 2. 종료 (1/2) 선택: ")

    while In == "1":
        id = input("아이디를 입력하세요: ")
        pw = input("비밀번호를 입력하세요.: ")

        if id == ID and pw == PW:
            print('로그인 성공')
            break
        else:
            print("로그인 실패! 다시 시도해주세요.")

    print("종료합니다.")
    break


while True: 
    print ("===로그인 화면===", sep="")
    In = input("1. 로그인 2. 종료 (1/2) 선택: ")

    while In == "1":
        id = input("아이디를 입력하세요: ")
        pw = input("비밀번호를 입력하세요.: ")

        if id == ID and pw == PW:
            print('로그인 성공')
            break
        else:
            print("로그인 실패! 다시 시도해주세요.")

    print("종료합니다.")
    break

