"""
딕셔너리
키-값 쌍으로 묶어 데이터를 저장하는 자료형
키는 유일해야 함. 값은 중복 가능함.
변경 가능한 자료형
순서가 보장되지 않았다가 버전 업글을 통해 순서가 보장됨.
"""

#dict 만들기
d1 = {} #빈 dict
#print(d1, type(d1)) #{}, <class 'dict'>

person = {"name": "홍길동", "age": 25}
#print(person)

#dict 함수로 생성
d2 = dict()
#print(d2, type(d2)) #{} <class 'dict'>

#키가 문자열일 때 가능한 수
movie = dict(title = "int", director= "nolan")
#print(movie, movie["director"]) #{'title': 'int', 'director': 'nolan'} nolan

# 리스트나 튜플로 만들기
pairs = [("name", "luna"),("age",10),("job","dev")]
person2 = dict(pairs)
#print(person2)

#zip 함수 활용
key = ["title", "director","year"]
valus = ["기생충", "봉준호", "2019"]
movie2 = dict(zip(key,valus))
#print(movie2)

#키는 사용할 수 없는 자료형
#키는 불변 자료형캍 사용
di1= {(3,2,1): (1,2,3,)} #튜플 가능함
di2 = {1:10} #숫자 가능
#di3 = {[1,2,3] : "리스트 값은 같은 걸로?"} 
#cannot use 'list' as a dict key (unhashable type: 'list')
#print(d3)

#dict 데이터 조회
#print(person2["name"])
#print(person2["age"])
#TypeError: cannot use 'list' as a dict key (unhashable type: 'list'

#get 매서드 활용한 조회
#print(person2.get("name"))
#print(person2.get("email")) #None 뜸

# get 사용 예제 *추가 적으로 묻기 < ,로 구별하지 못해 잘못된 문법 나옴.
user_data = {
    "username" : "luna",
    "email" : "luna@spreatics.com",
    "password" : "1234"
}

#key = input("조회할 정보를 입력하세요.(username, email, password): ")
#result = user_data.get(key, "존재하지 않는 데이터입니다.")
#print(result)

# 데이터 추가 및 수정
# 1) 기본적인 추가, 수정 방법
user_data["phone"] = "010-1234-3456"
user_data["username"] = "lunaaaaa"
#print(user_data)

# 2) update 매서드 사용
user_data.update({"nickname" : "luna"})

#print(user_data)

# 3) 키가 문자열일 경우
user_data.update(phone= "010-2345-6788")
#print(user_data) #교체됨

# 다른 딕셔너리 추가
extra_data = {"city" : "seoul"}
user_data.update(extra_data)

#print(user_data)

#데이터 삭제
del user_data["city"] #없는 값을 지우려 하면 에러가 뜸.
#print(user_data)

# 키로 제거
nickname = user_data.pop("nickname")
#print("pop >>", user_data, nickname, sep=" /// ")
#pop >> /// {'username': 'lunaaaaa', 'email': 'luna@spreatics.com', 'password': '1234', 'phone': '010-2345-6788'} /// luna

#가장 마지막 요소 제거
phone = user_data.popitem() #가장 맨 뒤를 지움
#print(user_data, phone, sep= " /// ")

#dict 비우기
user_data.clear()
#print(user_data) #{} 로 뜸

# dict 삭제
del user_data 
#print(user_data) #name 'user_data' is not defined. 사라졌기 때문에 에러가 뜸

#실습
#빈 딕셔너리 생성: user라는 이름의 빈딕셔너리를 생성
user = {}
#사용자 기본 정보 추가
user.update({"username": "skywalker", "email": "sky@example.com", "level": 5})
#print(user)

#값 읽기
email_value = user["email"]
#print(email_value)

#값 수정
user["level"] = "6"
#print(user)

# 안전하게 키 조회
#key_1 = input("조회할 정보를 입력하세요.(username, email, level): ")
#result_1 = user.get(key_1, "미입력.") #get은 정보 없어도 오류라고 안 한다. 
#print(result_1)

#항목 추가 및 삭제
user.update({"nickname": "sky"})
del user["email"] # user.pop("email") 가능
#user.update({"singup_date": "2025-07-10"})
#print(user)
#print(user.setdefault("singup_date","2025-07-10"))
user.setdefault("singup_date","2025-07-10") #정석 답
#print(user)

#실습2
students = {}
students.update({"Alice": 85, "Bob": 90, "Charlie": 95})
students.update({"David": 80})
students["Alice"] = 88
del students["Bob"] #students.pop("Bob")
#print(students)

#매서드
user_data = {
    "username" : "luna",
    "email" : "luna@spreatics.com",
    "password" : "1234"
}

#keys : 모든 키를 반환
print("키", list(user_data.keys())) #키 ['username', 'email', 'password']

#valuse :모든 값을 반환
print("값", list(user_data.values())) #값 ['luna', 'luna@spreatics.com', '1234']

#items : 모든 쌍을 반환
print("items", list(user_data.items()))
#items [('username', 'luna'), ('email', 'luna@spreatics.com'), ('password', '1234')]

