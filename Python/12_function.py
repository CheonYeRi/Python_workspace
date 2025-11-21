'''
함수 (function)
특정 작어을 수행하는 코드 들의 모음
특정한 코드들을 재사용 할 수 있게 함
'''

# 사용자 정의 함수 기본 문법
# 함수의 정의: define의 약자로 def 사용
def 함수이름 (매개변수): #콜론(:), 들여쓰기 중요
    #실행할 코드
    print(매개변수)
    return "반환값"

# 함수의 실행 (호출 call)
result = 함수이름("인자") #인자라는 갓이 def의 매개변수로 들어감.
print(result) #"반환값"으로 출력됨 return 결과물을. 

# 매개 변수(Parameter): 매개 + 변수
# 매개 : 둘 사이를 연결해줌.
#함수가 실행될 때 인자로부터 입력되는 값을 함수의 코드 블록으로 전달하는 역할.
'''
#함수의 필요성 예제
a = 10
b = 20

if a > b:
    print(a - b)
else:
    print(a + b)

c = 30
d = 40

if c > b:
    print(c - d)
else:
    print(c + d)
#... 비슷한 구조로 길어짐

def my_func(a,b):
    if a > b:
        return a - b
    else:
        return a + b

print(my_func(10,20))
print(my_func(30,40))


#실습 1 : 사칙연산 계산기 함수 만들기
def calculate(a,b,operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return float(a / b)
    else:
        print("지원하지 않는 연산입니다.") 

print(calculate(20,5,"?"))


# 키워드 인자
# 예시 1
print("안녕하세요", "반갑습니다.", sep="-", end="/") #공백은 -, 마무리는 /

# 예시 2
def my_func(a, b, c=None, operator=None):
    if operator == "+":
        return a + b
    else:
        return c

print(my_func(10,20,operator="+"))
#a,b만 설정하면 none 뜨고 operator = "+"라고 새인자 지정하면 변경해 적용됨

#기본값 인자
#단, 기본값 매개변수는 뒤쪽에 위치해야 함. 
def greet(name, message="안녕하세요."):
    print(f"{name}님, {message}")

#호출 시 인자 생략 -> 기본값 사용.
greet("luna") #luna님, 안녕하세요.
greet("ff","반갑습니다!") #ff님, 반갑습니다!

#위치 가변 인자
#여러개의 값을 유동적으로 받을 수 있음
#값이 튜플 형태로 받아짐

def add_all(*args):
    return sum(args)

print(add_all(1,2,3,4,5)) #15 출력


#키워드 가변 인자
#여러 키워드 인자를 유동적으로 받을 수 있다.
#딕셔너리 형태로 값이 입력됨. 

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_info(name="luna", age = 15 , city="souel") 
#name : luna / age : 15 /city : souel

'''
'''
#실습 가변인자 연습
def avg(*args):
    return sum(args)/len(args) #sum(iterable) = 모든 요소의 합을 계산

print(avg(1,4,5,2,6))


#def max_log(*args):
    
#    return max(args, key= len)

#print(max_log("as", "asdf"))

#모범 답안
def max_log(*args):
    answer = ""
    for s in args:
        if len(s) > len(answer):
            answer = s
    return answer

print(max_log("asg","qwtsah","01asfssg"))

#모범 답안 2
def max_log(*args):
    #예외처라
     if len(args) == 0:
         return "입력값이 없습니다"
     return max(args, key=len)

max_log()


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_info(name="luna", age = 15 , email="coodingon@gmail.com") 
#헷갈리는 거: name="luna" 입력 시 key = name 이고 value = "luna"로 알아서 적용되는 거다.
# age 정보 넣어도 알아서 반환 되는 거고. 

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} 할인가: {value * 0.9} 정가: {value}")

print_info(item = 12000, item1 = 10000, item2 = 15000)

'''

#전역 변수: 함수 밖에 선언된 변수
#지역 변수: 함수 안에 선언된 변수

#전역 변수
#x = 200

#예제
#def my_func():
    #지역변수
#    x = 10
#    print(x)

#my_func() # 10
#print("함수 밖", x) # 200

'''
#지역 변수
x = 200

#예제
def my_func2():
    #지역변수
    x = 20
    x += 5
    print("지역변수", x)

my_func2() # 25 x가 20으로 바뀌고, 5가 더해졌단 뜻.
print("전역변수", x) #200

#예제2: UnboundLocalError, x를 지역변수로 인지함.
#def my_func2():
#    #x = 20
#    x += 5
#    print("지역변수", x)

#my_func2()
#print("전역변수", x)

#global 키워드 쓰면 전역 변수라고 지정할 수 있지만.
#어디서 선언 했는지 파악하기 어렵고, 의도 따라 달리 익히기 때문에.
#권장하지 않는다.

#nonlocal :내부 함수가 외부 함수를 쓰려고 할 때 씀. 

#예제3
x = 10

def my_func3():
    global x #전역변수 사용 선언
    x += 5 
    print("지역", x) #15 지역이 전역으로 바뀌었다.

my_func3()
print("전역", x) #15

#권장되는 패턴
#부수효가(side effect)을 발생시키지 않는 함수를 위주로 프로그래밍
x = 10

def my_func4(n): #변수명칭(n)이 함수 내부에서 일치해 사용하면 된다.
    n += 5 
    return n

x = my_func4(x)

print("전역", x )
'''
'''
#실습
current_user = ""

#로그인, 로그아웃 함수식 만들기
def login(name): #name = 매게 위치 login(A) 쓰면 name = a다.
    global current_user #전역변수로 사용.

    if current_user == "":
        current_user = name
        print(f"{name}님 로그인 성공!")
    else:
        print("이미 로그인 되어 있습니다.")

def logout():
    global current_user

    if not current_user:
        print("로그인 상태 없습니다.")
    else:
        current_user = ""
        print("로그아웃 되었습니다.")


login("ian")
login("coodingOwl")
logout()
login("coodinOwl")
print(current_user)
'''
'''
#모법 답안
current_user = ""
login_count = 0

def login(name):
    global current_user
    global login_count

    if current_user == None:
        current_user = name
        print(f"{name}님 로그인 성공!")
    else:
        print("이미 로그인 되어있습니다.")
        login_count += 1
        if login_count > 4:
            print("더이상 로그인 할 수 없습니다.")

def logout():
    global current_user
    global login_count

    if current_user == None:
        print("로그인 상태가 아닙니다.")
    else:
        print("로그아웃 되었습니다.")
        current_user = None
        login_count = 0

logout()
login("kim")
login("coodingOwl")
logout()
login("coodinOwl")
print(current_user)
'''
'''
#재귀함수
#1 자기 자신을 호출하는 함수
#2 반드시 기본 조건 (종료 조건)이 있어야 함.
# - 큰 문제를 작은 문제로 나누었을 때 일정한 패턴이 있어야 함.
import time

def recursive_func(n):
    #기본조건
    if n == 0:
        return
    
    recursive_func(n-1)
    print("재귀 호출" , n)
    time.sleep(1)

recursive_func(5) #1,2,3,4,5 순으로 나옴.

#실습4
#거듭제곱. a**b = a*(a*b-1) 함수 <이해가 안 간다. 
def func_c (a,b):
    if (b == 0): # a 의 b(0승) = 1이란 뜻 
        return 1 
    return a * func_c(a, b-1) 
    # a가 b개 만큼 곱해야 한다. a * a * a*... 1 (=> b = 1)
        
print("재귀함수", func_c(2,3)) 
#2의 3승 2*2*2*1 b= 3이면 3,2,1,0이 되는 순간까지 포함 총 4개의 곱
#그래서 0 되는 걸 1로 조건 거는 것 if (b == 0): 1 

'''
'''
#실습, 팩토리얼
#팩토리얼 : 1부터 지정된 수 까지 모든 수의 곱 수학 기호로 "!" 숫자 뒤에 붙여 표시
# 3! = 3의 계승 1 2 3  =6 

N = int(input("팩토리얼 할 숫자: "))
Result = 1
for n in range(1, N+1):
    Result *= n

print(Result)
# 1부터 N+1의 값을 반복 생성한다.
# Result은 1에서 시작하고 지정한 값만큼 곱해진다.
# 1 사이클 1*1 / 2사이클 +1*2/ 3사이클 + 1*3 =6 

#모범답안
def fact_f(n):
    #예외 처리
    if n < 0 :
        return "음수의 팩토리얼은 정의되지 않습니다."
    if n == 0 or n == 1:
        return 1
    
    return n * fact_f(n-1)

def m_func(N):
    if (N == 0):
        return 1
    return N * m_func(N-1)
    
print(m_func(N))
#1*1 + 1*2 + 1*3 = 6
#리턴을 한다. 3이면 3(N)에 2(n-1)호출, 2에서는 1(n-1)호출, 1은 0이되니 1로.
#사이클 도는 것처럼 역순으로 더해져서 3 * 2* 1* 1로 =6이다.

'''
'''
#실습, 피보나치 수열
#피보나치 수열은? N의 수가 N-1와 N-2를 더한 값.
#프로그램 작성 시, 규칙을 찾아서 공통된 코드로 만든다. 

def fibonacci_f(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(n-1):
        a,b = b , a+b
        # 0 1 <= 1 1
        # 1 1 <= 1 2
        # 1 2 <= 2 3
    return b

print(fibonacci_f(5))    
#모범 답안인데 안 되어서 코드 비교하거나 질문하기. 


def fibonacci_R(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_R(n-1) + fibonacci_R(n-2)

print(fibonacci_R(6))
'''
'''
#람다(lambda) 함수 : 익명 함수
# 간단한 함수를 한줄로 표현 할 때 사용
#기본 문법
# lambda 매개변수 : 표현식
#표현식: 값이 반환이 되는 식

#일반 함수
def add(x,y):
    return x+y
#람다 함수
add_func = lambda x, y: x + y
print(add_func(3, 5))

#람다로 값을 반환하고 사용을 끝내는 경우
print((lambda x: x**2)(10)) #100 뜸

#람다 함수의 활용
# 1 map 에서 활용
my_list = [1,2,3,4]

#일반 함수
def square_func(x):
    return x ** 2

#함수를 인자로 받는 함수
print(list(map(square_func, my_list))) #[1, 4, 9, 16]

#람다 함수 
print(list(map(lambda x: x ** 2,my_list))) #[1, 4, 9, 16]

#2. filter 에서 활용

my_list2 = [1,2,3,4,5,6,7,8,9,10]

#일반 함수
def is_even(x):
    return x % 2 == 0

print(list(filter(is_even, my_list2))) #[2, 4, 6, 8, 10]

#람다 함수
print(list(filter(lambda x: x % 2 == 0, my_list2))) #return x % 2 == 0의 계산식 넣음. 

#3. sorted 에서 활용
my_list3 = ["apple", "banana", "watermelon", "grape"]
print(sorted(my_list3, key= lambda word: len(word)))
#['apple', 'grape', 'banana', 'watermelon'] 글자 수 적은 순으로 출력
'''

#실습
#특정 조건 만족하는 튜플만 추출
students = [
    ("Alice", [80, 90]),
    ("Bob", [60, 65]),
    ("Charlie", [70, 70])
    ]

'''
x = ()
total = 0

def average_70(x):
    global students
    global total
    for name, score in students:
        total = sum(students)/len(students)
        if total >= 70:
            x.append()

    return
'''
print(list(filter(lambda a: sum(a[1] )/ len(a[1]) >= 70 , students)))
#튜플 키워드 a의 v 값을 더하고, v의 개체 수(len)만큼 나누겠다.
#튜플을 리스트로 변환하고, [1]인덱스 값을 쓰겠다.(튜플의 각 요소 2번째 값)

# 키워드 추출 리스트 만들기: 맨 앞단어만 출력
sentences = [
    "Python is fun",
    "Lambda functions are powerful",
    "Coding is creative"
]
print(list(map(lambda s: s.split()[0],sentences)))
#공백을 기준으로 나누고 리스트의 첫번째 요소만 나열하겠다.
#마지막 위치는 넣어야 할 리스트,튜플 등의 정보
#리스트 변환, 지정값, 계산식, 넣을 정보 흐름.


#튜플 리스트 정렬 (나이를 기준으로 오름차순)
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

print(sorted(people, key= lambda age : age[1]))

#key 사용해 리스트를 정렬함.
#튜플의 1인덱스를 기준으로 나열하겠다.
#print(sorted(my_list3, key= lambda word: len(word)))