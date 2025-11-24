# 클래스 (class)
'''
데이터와 기능을 하나로 묶는 구조
개념적(기능적)으로 유사한 관계에 있는 것들을 묶어줌.
'''
'''
#클래스 기분 문법
#클래스의 정의
class ClassName: #파스칼 케이스 형태로 작성
    #생성자(comstructor): 인스턴스(객체)가 생성될 때 호출
    #인스턴스 변수를 초기화, 기본 상태 설정
    #하나의 클래스 에서 하나만 정의 가능
    def __init__ (self, name):
        # 인스턴스 변수
        # self : 인스턴스 자기 자신을 가리킴
        self.name = name #매개변수
        self.age = 0 #임의로 넣은 값

    #(인스턴스) 메서드
    def method_name(self): #메서드는 주로 스네이크 케이스 양식 씀
        print(f"이 인스턴스 이름은 {self.name} 입니다.")
    
#인스턴스 생성
my_instance = ClassName("I1") #name 변수 받기로 했으니, 문자열 입력
print(my_instance.name) #I1
my_instance.method_name() #이 인스턴스 이름은 I1 입니다.

#another_instance = ClassName("I2")
#another_instance.name() 

#실습
# 책 클래스 만들기
class BookClass:
    def __init__(self,title,author,total_pages,current_pages):
        self.title = title
        self.author = author
        self.current_pages = current_pages
        self.total_pages = total_pages

    def read_page(self,page):
       self.current_pages += page #입력한 값(page)을 더해서 할당
       if self.current_pages > self.total_pages:
           self.current_pages = self.total_pages 
           #초과할 시 total과 동일하게 해 넘기지 않도록 한다.
    
    def progress(self): #함수 생성
        percent = (self.current_pages / self.total_pages) * 100 
        #읽은 페이지 나누기 총 페이지에 100 곱한다.        
        print(f"현재 읽은 분량: {percent: .1f}%")
        #소수점 한자리 값까지만 보여준다. (.1f)

book1 = BookClass("넥서스","유발 할라리", 500, 1)
book1.read_page(10) #10 추가하겠다.
book1.progress()

# Rectangle 클래스 구현
class Rectangle_Mathod:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

Rectangle = Rectangle_Mathod(int(input("가로 값: ")),int(input("세로 값: ")))
print(f"사각형의 넓이는 {Rectangle.area()})

#클래스 변수 : 클래스가 가지고 있는 변수
#모든 인스턴스가 공유할 수 있다.

class Dog:
    #클래스 변수
    kind = "강아지"

    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age

dog1 = Dog("포메라니안", "리치", 12)
dog2 = Dog("비숑", "비수", 6)
print("인1", dog1.kind)
print("인2", dog2.kind)
print("클래스", Dog.kind)

#클래스 메서드
#클래스 자체를 대상으로 동작하는 메서드
#클래스 데이터를 조작하는데 사용

class Book_1:
    book_count = 0 #책_카운트 변수는 0으로 시작한다.

    def __init__(self, title, author):
        Book_1.book_count += 1
        self.title = title
        self.author = author
        #제목, 작가 입력될 때마다 book_count가 1씩 올라간단 뜻이다.

    # 클래스 메서드
    @classmethod #데코레이터 (설명해준다 맥락)
    def get_count(cls):
        print(f"현재 {cls.book_count}권의 책을 가지고 있다.")

book1 = Book_1("a1","abc")
book2 = Book_1("a2","def")
print(Book_1.book_count)
Book_1.get_count()

'''

'''
# 정적 메서드
# 클래스나 인스턴스의 데이터를 조작하지 않는 클래스 메서드
# 클래스나 인스턴스의 상태를 의존하지 않는 일반 함수
# 개념적으로는 클래스와 연관이 있으나, 클래스나 인스턴스의 데이터를 조작하지 않음.

class OperationTool:

    @staticmethod #데코레이터
    def add (a, b):
        return a + b
    
print(OperationTool.add(10, 20)) #곧바로 30이란 결과값이 나온다.

#실습 클래스
#User 클래스구현
class User:
    total_users = 0

    def __init__(self,username,points):
        self.username = username
        self.points = points
        User.total_users += 1
        #이름, 점수 입력될 때마다 total 유저 수 1 증가

    #모범 답안
       #def __init__(self,username,points):
       #self.username = username
       #self.points = 0
       #User.total_users += 1
         #이름 입력 될 때마다 유저 수 증가로 설정.

    def add_points(self, amount):
        self.points += amount
        #amount는 self.points 값이 더해지는 값과 같다.

    def get_level(self):
        if 0 <= self.points < 100:
            return "Bronze"
        elif 100 <= self.points < 500:
            return "Silver"
        else: 
            return "Gold"

    @classmethod
    def get_total_users(cls):
        print(f"총 유저 수는 {cls.total_users} 입니다.")

        
User1 = User("a", 200)
User2 = User("b", 500)
print(User1.get_level())
print(User2.get_level())
User.get_total_users()

#User1.add.points(100)
#def add_points(self, amount) 메서드 쓰기 위해서 입력하는 숫자값 맥락.


#접근 제어와 정보 은닉
#데이터 무결성을 보호하기 위함
#코드 안정성을 향상 시키기 위함

class Person2:
    def __init__(self, name, age):
        #public
        self.name = name
        #private : self 언더바(__) 두개 변수 앞에 붙여서 정의
        self.__age = age

    #getter
    def get_age(self):
        return self.__age
    
    #setter
    def set_age(self, value):
        if value > 120 or value < 0:
            print("유효하지 않습니다.")
        else:
            self.__age = value

p1 = Person2("lee", 20)
print(p1.name)
#print(p1.__age)
#AttributeError: 'Person2' object has no attribute '__age' 뜸.
print(p1.get_age())
p1.set_age(-10)
'''
'''
# @property 데코레이터
# 메서드를 속성처럼 보이게 만들어주는 데코레이터

class Ex:
    def __init__(self):
        self.__value = 0
    
    #getter
    @property
    def value(self):
        return self.__value #위의 getter양식과 동일
    
    #setter
    @value.setter
    def value(self, val):
        if val < 0:
            print("유효하지 않은 값입니다.")
        else:
            self.__value = val

ex1 = Ex()
print(ex1.value) #ex1.value() 안해도 0으로 출력
ex1.value = 100
print(ex1.value) #setter 작동함.
ex1.value = -100
print(ex1.value) 
'''

#실습
# UserAccount 클래스 비밀번호 보호

class UserAccount:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def change_password(self, old_pw, new_pw):
        if self.__password != old_pw:
            return "비밀번호 불일치"
        else:
            print("비밀번호 변경되었습니다.")
            return new_pw

    #setter
    def set_check(self, value):
        if value != self.__password:
            return False
        else:
            return True


user1 = UserAccount("asd", 123456)

print(user1.set_check(1234567)) #false
print(user1.set_check(123456)) #ture
print(user1.change_password(123, 123789)) #비밀번호 불일치
print(user1.change_password(123456, 1123)) #비밀번호 변경되었습니다. (변경 번호)
print(user1.set_check(1111)) #false