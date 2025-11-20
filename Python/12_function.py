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