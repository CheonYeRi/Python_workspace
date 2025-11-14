'''
tuple (튜플)
순서가 존재하는 여러 데이터의 모음
불변 (immutable) 자료형
'''

#----튜플 생성-----
#my_tuple = (1,2,3,4)
#print(my_tuple) #(1,2,3,4)로 나옴
#print(type(my_tuple)) #<class 'tuple'>

#my_tuple2 = 5,6,7,8
#print(my_tuple2)

#원소가 하나인 튜플 생성
#single_el_tuple = (100,) #, 인식
# 튜플 생성 함수로 생서
#my_tuple2 = tuple()
#print(my_tuple2) 
#my_tuple2 =tuple('coodingon')
#print(my_tuple2) #단어 한 글자를 쪼개서 요소로 만들어진 게 나옴

#---언패깅----
#시퀸스의 저장된 여러 값을 여러 변수에 나눠서 저장한 것
# 튜플, 리스트, 문자열...
apple, bananan, kiwi = ("apple", "banana", "kiwi")
print(apple, bananan, kiwi)

#----------------------------
#튜플은 불변성이 있다.
# 객체가 생성된 이후 내부 데이터를 변경할 수 없다.
#my_tuple[0] = 100 #'tuple' object does not support item assignment. 튜플은 지원하지 않는다 뜻
#del my_tuple[1] #'tuple' object doesn't support item deletion 타입 에러 나온다.
#튜플 자체는 삭제가 가능하다. but 원소 삭제는 불가함. 
#del my_tuple
#print(my_tuple) #name 'my_tuple' is not defined = 찾을 수 없다 = 삭제 됨

#---튜플 수정
my_tuple = (10,20,30)
print("원래 튜플" , my_tuple) #원래 튜플 (10, 20, 30)
my_tuple2 = (100,) + my_tuple[1:]
print("새로운 튜플", my_tuple2) #새로운 튜플 (100, 20, 30)

#실습+설명 (실습 1-5 중 3만 제외)
#01 user = ("minji", 25, "Seoul")을 ‘eunji’로 수정한 결과를 restored_user에 저장하고 출력
user = ("minji", 25, "Seoul")
restored_use = ("eunji",)+ user[1:]
print("수정된 정보", restored_use)

#02 튜플 restored_user를 언패킹하여 name, age, city 변수에 저장
name, age, city = restored_use
print(name, age, city)

#04 현재 DB보고 "minji" 라는 이름이 몇번 등장하는지 출력
#"soojin"이 처음 등장하는 위치(인덱스)를 출력
users = ("minji", "eunji", "soojin", "minji", "minji")
print(users.count("minji"))
print(users.index("soojin"))

#05 보고서 출력용으로 고객이름을 가나다순으로 정렬
#튜플은 변경불가 이므로 원본은 유지되어야 하며, 정렬 결과는 리스트 형태로 출력
#users 튜플을 정렬한 결과를 sorted_users에 저장하고 출력
sorted_users = list(users)
sorted_users.sort()
print(sorted_users)

print("복원 된 고객 정보:",)