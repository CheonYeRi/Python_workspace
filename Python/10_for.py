#for 문
# 이터너블(순회 가능한) 요소를 하나씩 꺼내서 실행 블록에 전달하는 반복문

'''
#리스트로 생성, 반복
fruits = ['apple','banana','cherry']
for fruit in fruits: #fruit = 리스트 안에 있는 개체 명칭 의미
    print(f"I like {fruit}")

#문자열 반복
my_str = "apple"

for char in my_str:
    print(char)

#튜플 반복+ 변수 값 분해
coords = [(1, 2),(10, 15),(-6, 10)]
#언패킹 (X,Y)구조 (구조 분해 가능)
for x,y in coords:
    print(f"x 좌표 {x} y 좌표 {y}")

#딕셔너리 반복 -key 순회 : dict 파일에서 한번 복습, 이해하기.
person = {
    "name": "kim",
    "age": 15,
    "address": "seoul"
}

# 기본
for key in person:
    print(f"key: {key}, value: {person[key]}")

# value 안 가져오기
for value in person.values():
    print(f"value: {value}")

# items 가져오기
for key, value in person.items():
    print(f"key: {key}, value: {value}")

'''
'''
#set 반복
my_set = {1,2,3,4} #딕셔너리 생성

for key in my_set:
    print(key)
'''

#실습 1
#리스트 값을 두 배로 변환
#numbers = [3, 6, 1, 8, 4]

#for number in numbers:
#    print(number * 2)

#모범 답안
#numbers = [3, 6, 1, 8, 4]
#doubled = [] #새 리스트 생성

#for number in numbers:
#    doubled.append(number * 2) #새 리스트에 바뀐 변수값을 넣겠다는 뜻

#print(doubled) #[6, 12, 2, 16, 8] 출력


'''
numbers[0] = numbers[0]*2
numbers[1] = numbers[1]*2
numbers[2] = numbers[2]*2
numbers[3] = numbers[3]*2
numbers[4] = numbers[4]*2 
할 필요가 줄었다. 이거 짱이다.
'''

#문자열 길이 구해서 새 리스트 만들기
#words = ["apple", "banana", "kiwi", "grape"]

#for word in words:
#    length = len(word) #새로운 리스트를 생성해서 저건 word(변수)의 길이값이다 함.
#    print(length)

# 좌표 튜플에서 x, y 좌표나누기
'''
직접 만든 것.
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
for x_values,y_values in coordinates:
    print(f"x 좌표 {x_values} y 좌표 {y_values}")
'''
#모범답안 해당 리스트 만들어서 추가해 출력 같은 뜻
#coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]
#x_values = []
#y_values = []
#for x, y in coordinates:
#    x_values.append(x)
#    y_values.append(y)
#print(x_values, y_values)

#for 문과 range()
# range 함수 : 지정된 범위의 정수 시퀀스 생성

#기본 문법
#range(start,end,step)
# start: 생략 가능, 기본 0 / end: end -1까지 생성 / step: 생략 가능 기본 값 1

#range(1,5)

#for i in range(1,5):
#    print(i)
'''
동일한 맥락이다.
for i in [1,2,3,4]:
    print(i)
'''
print("--------------")
'''
#start 생략
for i in range(11):
    print(i)

#간격(step) 지정
for i in range(0,11,2):
    print(i)

for i in range(11,0,-2):
    print(i)
'''

#실습 1 입력받은 수의 합 구하기

#num = int(input("수 입력: ")) #먼저 사용자가 입력할 값 구한다.
#num_total = 0
#for n in range(num + 1):
#    num_total += n
#print(num_total)

#구구단 만들기
'''
이건 전체 구구단 만드는 것 (a와 b 범위 지정 곱하기)
for a in range(0,10):
    for b in range (1,10):
        print(a, '*' , b, '=', a*b)
'''

#a = int(input("숫자를 입력하세요: ")) #입력 값 만들기
#for b in range (1,10):
#    print(f"{a}, '*' , {b}, '=', {a*b}")

# 3의 배수의 합 구하기
#total = 0 #현재 총합
#for n in range(1,101,3): #1부터 100까지의 3의 배수를 반복
#    total += n #n에서 3배수로 할당한 값들을 더했다. 
#print(f"합 {total}")

'''
이것도 똑같이 작동된다.
for n in range(1,101):
    if n % 3 ==0 #3을 나눴을 때 0이 된 값만, 조건문
        total += n
'''

#짝수이면서 5의 배수인 수 출력
#C = int(input("숫자를 입력하세요: "))
#for c in range(0,C+1,5):
#    print(c)

'''
모범 답안
for c in range(0,C+1):
    if c % 2 == 0 and n % 5 == 0: #짝수이면서 5배수란 조건을 빼먹음
        print(c)
'''
'''
#루프 제어문
# 특정 조건 하에서 작동하도록 구현
#break : 반복문 즉시 중단
for i in range(10):
    if i == 5:
        break
    print(i)
print("반복 종료1")

#continue : 현재 반복을 넘어감
for i in range(5):
    if i == 2:
        print("건너뜀")
        continue

    print(i)
print("반복 종료2")

#pass 
for i in range(10):
    pass

#for - else 구문
for i in range(5): #5면 4까지만 출력한단 뜻
    if i == 2:
        break
    print(i)
else:
    print("반복 종료3")
#이렇게 짜면 2에서 브레이크 걸려 멈춘 거기에 else까지 가지 않는다.

#중첩 for 문
# 하나의 for 문 안에 다른 for 문이 들어있는 구조

#이중 for문
for i in range(5):
    for j in range(5):
        print("i,j", i , j)
    print()
'''

'''
#실습

# 구구단만들기 for문 중첩 활용해서.

for a in range(2,10):
    print(f"{a}단")
    for b in range (1,10):
        print(a, 'x' , b, '=', a*b)
        #또는 print(f"{a} x {b} = {a*b}")

# 중첩 for 문 별 찍기
a = int(input("몇 줄?: "))

#for n in range(0,a):
#    print("*" * (n+1)) #별표를 n+1값 만큼 곱한 걸 출력한다.

for i in range(1,a+1):
    for j in range(i):
        print("*", end ="")

#중앙 정렬
a = int(input("몇 줄?: "))

for n in range(a):
    print(" " * ((a - 1) - n), end = "") #공백의 수를 ((10-1)-1(시작 수)) 만큼 만든다.
    print('*' * (2 * n + 1)) #*을 (a의 시작수+1의 2배) 만큼 곱한다


#역삼각형은?
a = int(input("몇 줄?: "))

for n in range(a):
    print(" " * (a - (n+1)), end="") 
    print('*' * (n+1))
#a값을 지정하고, a=10 - (n+1)=a의 시작점+1 만큼의 여백을 만든다. 
#공백을 줄바꿈으로 정리
'''
'''
for i in range(1,a+1):
    #공백 출력
    for j in range(a-i):
        print(" ", end="")
    for j in range(i):
        print("*",end="")
    print()

#받은 답안 비교용 원본
# 오른쪽 정렬
n = int(input("몇 줄?:"))
for i in range(1, n+1):
  for j in range(n - i):
    print(" ", end="")
  for j in range(i):
    print("*", end="")
  print()
'''



#리스트 컴프리헨션
#for 문을 리스트에 한 줄로 축약하여 새 리스트를 생성하는 문법
#[표현식(리스트의 원소) for 변수 in 반복대상 if 조건문] if 조건문 없어도 ㄱㅊ
# 표현식 : 값을 유도하는 식(표현)

#for문 이용
#squares = []
#for x in range(1,6):
#    squares.append(x ** 2)
#print(squares)

#리스트 컨프리헨션
#squares2 = [x ** 2 for x in range(1,6)]
#print(squares2)
#squares3 = [x ** 2 for x in range(2,6) if = 1 == g] #정수 추가
#print(squares3)

# 실습 
# 1부터1 0까지의숫자에 대해, 각수의제곱값을요소로갖는리스트를리스트컴프리헨션
cphs = [n ** 2 for n in range (1,11)]
print(cphs)

cphs2 = [x for x in range(0,51) if x % 3 == 0] 
#앞의 표현식은 변수값(x)만 두고 없어도 딘다.
# x % 3 == 0 < 3으로 나눴을때 0이 된다 = 3의 배수다.
print(cphs2)

fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]
cphs3 = [f for f in fruits if len(f) >= 5] 
#변수 f만 나오게, fruits 중의 f(변수)가 글자수(len) 5보다 같거나 크게란 뜻
print(cphs3)
#차집합으로 할 수 있을까? <나중에 시도
