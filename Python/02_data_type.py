# 정수형 (integer, int)
# 크기 제한이 없다 (큰 수는 메모리를 더 할당해 씀)

my_int1 =100
my_int2 = 150
print(type(my_int1)) #<class 'int'>으로 출력

#실수형 (float)
# 부동 소수점 방식
my_float = 100.0
print(type(my_float)) #<class 'float'> 로 출력

# 문자열 (string, str)
# 작은 따옴표, 큰 따옴표 표현 써야 할 때 다른 따옴표로 써야 구분할 수 있다
my_str1 = '' #빈문자열
my_str2 = " " #공백 문자열
mt_str3 = "안녕하세요"

#문자열 여러줄로 만들기
multi_str = """코딩을 하는
처음 배우는
파이썬 언어
"""
print(multi_str)
print(type(my_str1)) #<class 'str'> 출력

#따옴표 속에 따옴표 쓰기
print("'python' 코딩언어") #'python' 코딩언어 로 출력됨. 
#print (""에러"")

# 불리언형 = 논리형 (boolean, bool)
# 참과 거짓을 표현하는 자료형
print(True)
print(False)
print(type(True)) #<class 'bool'>

# 형 변환 (type casting)
# 명시적 형 변환 vs 암시적 형 변환

# 정수로 변환 int() 
'''
실수 -> 정수
문자열로 표현된 숫자 -> 정수
논리형 -> 정수
'''

#가능 예제
print(int(3.14)) #3
print(int("100")) #100
print(int(True)) #1
print(int(False)) #0

# print(int("3.14")) 
#ValueError: invalid literal for int() with base 10: '3.14'
#문자열 안에 정수가 아닌 것을 넣었다고 에러 남.
# "abc"같이 문자열만 있는 것도 안된다.

# 실수로 변환 float()
'''
정수 > 실수
문자열로 표현된 실수 > 실수
문자열로 표현된 정수 > 실수
논리형 > 실수
'''

#가능 예제
print(float(7)) #7.0
print(float('3.14')) #3.14
print(float('100')) #100.0
print(float(True),float(False)) #1.0, 0.0
# print(float("abc")) 이것도 "abc"같이 문자열만 있는 것도 안된다.

#str() - 모든 타입을 문자열로 변환

#암시적 형변환
# 정수와 실수의 연산에서 자동으로 실행되는 연산
print(10+5.2) #15.2 자동 연산

#논리형으로 변환 : bool()
print(bool(1)) #True 출력

#------------------------
#문자열 포맷팅 (f-string)
# 문자열 안에 변수를 쓸 수 있도록 해주는 기능

name = "Luna"
age = 20
print("내 이름은", name, "이고, 나이는", age, "입니다.")
print(f"내 이름은 {name}이고, 나이는 {age}입니다.")

#실습1 영화 정보 출력하기
영화이름 = "Suspiria"
감독 = "Luca Guadagnino"
개봉연도 = "2019"
장르 = "horror/fantasy"
print(f"Title: {영화이름} Director: {감독} Year: {개봉연도} Gener: {장르}")
#변수값 입력시 영화이름, 감독 = "제목", "이름" 식으로 코드 간략화 해보기. (개인 피드백)

#실습2 자기소개 하기
이름 = "천예리"
나이 = "28"
MBTI = "ISTJ"
print(f"""안녕하세요. 
제 이름은 {이름}입니다. 
{나이}살 입니다. 
제 MBTI는 {MBTI}에요.""")