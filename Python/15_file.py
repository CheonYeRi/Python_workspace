# 파일 입출력
# 저장 장치에 저장된 파일을 읽어오거나 저장하는 작업

#파일 열기와 닫기
# open() : 파일 열기
# open("파일 경로", mode = "r", encoding="원하는 인코딩 - utf8")
# open으로 파일을 읽으면 '파일 객체'를 반환
'''
f = open("example.txt", "w", encoding="utf-8")

f.write("파이썬 파일 입출력 예제\n")
f.write("파이썬 공부")

#close(): 파일 닫기
# 열린 파일을 닫아 시스템 자원을 해제함.
f.close()

#파일 읽기
#read(): 전체 내용을 한번에 읽기.
f = open("example.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()

#readlin() :한줄 씩 순차적으로 읽기
f = open("example.txt", "r", encoding="utf-8")
line1 = f.readline()
line2 = f.readline()

print("첫번 째 줄", line1)
print("두번 째 줄", line2)
f.close() #close로 계속 닫아주는 중.

#for문으로 읽기
f = open("example.txt", "r", encoding="utf-8")
for line in f:
    print(line.strip())
f.close()

# readlines() 모든 줄을 한번에 리스트로 읽기.

f = open("example.txt", "r", encoding="utf-8")
contents = f.readlines()
print(contents)
f.close()

# tell () 현재 읽고 있는 위치(바이트)를 반환

f = open("example.txt", "r", encoding="utf-8")
print("처음 위치", f.tell())
f.read(5)
print("바이트 5 미만 후 읽은 위치", f.tell)
f.close()

# seek() : 파일 포인터 위치로 이동

f = open("example.txt", "r", encoding="utf-8")
print(f.read(10)) #10바이트를 읽기
f.seek(0)#10 바이트 읽기ㅡ 맨 처음으로 가기
print(f.read())
f.close()

# a 모드 : 추가 쓰기
f = open("example.txt", "a", encoding="utf-8")
f.write("\n추가한 내용입니다.")
f.close()

# 파일 쓰기
with open("with_example.txt", "w", encoding="utf-8") as f1:
    f1.write("with문으로 작성한 파일이에요\n")
    f1.write("파일 입출력 완료")


# 예제 1. 파일에서 랜덤 추출
import random

with open("words.txt", "w", encoding="utf-8") as f1:
    words = [
        "apple", "banana", "orange", "grape", "lemon",
        "peach", "melon", "cherry", "plum", "pear",
        "school", "friend", "family", "flower", "garden",
        "window", "bottle", "pencil", "summer", "winter",
        "happy", "future", "travel", "animal", "market",
        "doctor", "planet", "energy", "nature", "memory"
    ]
    for i in words:
        f1.write(i + "\n")


with open("words.txt", "r", encoding="utf-8") as f1:
    data = f1.readlines()
    for i in range(5):
        word = random.choice(data).strip()
        print(word)


# 예제2. 입력 받아 파일 쓰기
with open("with_example.txt", "a", encoding="utf-8") as f1:
    while True:
        text = input("저장할 내용을 입력해주세요(종료 : z)")
        if text == "Z" or text == "z":
            break
        f1.write(text + "\n")
'''

'''
# 실습
# 회원 명부 작성하기

user = []
with open("member.txt", "a", encoding="utf-8") as f2:
    for m in range(3):
        user_name = input(f"{m + 1} 회원명 입력해주세요: ")
        user_pass = input(f"{m + 1} 비밀번호 6자 입력해주세요: ")
        f2.write(f"회원 {user_name} 번호 {user_pass} \n")
        user.append((user_name, user_pass))


with open("member.txt", "r", encoding="utf-8") as f2:
    members = f2.readlines()
    print(members)


#회원 명부를 통해 로그인 기능 구현
#근데 이거 파일 입출력 어떻게 정보 고정시키냐...
with open("words.txt", "r", encoding="utf-8") as f2:
    user_count = 0
    for line in f2:
        line = line.strip()
        user_name, user_pass = line.split(":")
        user_name = user_name.strip()
        user_pass = user_pass.strip()

    while user_count < 3 :
        id_input = input("이름을 입력하세요.: ")
        pw_input = input("비밀번호를 입력하세요.: ")

        if id_input == user_name and pw_input == user_pass:
            print("로그인 성공")
            user_count += 1
        else:
            print("로그인 실패")

    if user_count == 3:
        print("전원 로그인 됐습니다.")

#로그인 성공시 추가 정보 입력

'''

#모범 답안
import os
#os 모듈 갖고 온다. 운영 체제와 상호 작용하는 기능 제공
#파일 및 디렉토리 관리하기 목적으로.

if os.path.exists("member.txt"): #경로의 존재 확인 명령어.
    print("member.txt가 이미 존재합니다. 회원 등록을 건너뜁니다.\n")
else: #파일 없을 시 생성해서 추가하기 위한 과정
    with open("member.txt", "w", encoding="utf-8") as f:
        for i in range(3):
            name = input(f"{i+1}번째 회원의 이름: ")
            password = input(f"{i+1}번째 회원의 비밀번호: ")
            f.write(f"{name},{password}\n")
        
print("\n[회원 명부 저장 완료]\n")

with open("member.txt", "r", encoding="utf-8") as f:
    members = f.readlines()
    print(members)

# 로그인 과정
input_name = input("로그인 - 이름을 입력하세요: ")
input_password = input("로그인 - 비밀번호를 입력하세요: ")

login = False #로그인은 '거짓'으로 정의한다.
#텍스트 파일의 정보를 할당해야 함.
#로그인 성공하면 반복문을 탈출한다.(break 사용)
with open("member.txt", "r", encoding="utf-8") as f:
    for line in f: #한줄 씩 갖고와서 비교하고자 for문 사용.
        name, password = line.strip().split(",") #,를 기준으로 리스트로 반환해서 출력.
        print(line.strip().split(",")) #리스트 형태로 반환되어 나옴. ['QWER','001234']
        if input_name == name and input_password == password:
            login = True
            break

#로그인 성공시 전화번호 등록/ 수정
if login:
    print("\n로그인 성공!")

    #기존 전화번호 데이터 로드
    phone_data = {} #딕셔너리 자료형 생성, 빈 걸로 만듬.

    if os.path.exists("member_tel.txt"): #파일 존재 유무 확인
        with open("member_tel.txt", "r", encoding="utf-8") as f: #존재가 있을 경우에 실행
            for line in f:
                name, phone = line.strip().split(",")
                phone_data[name] = phone #name 키값 폰이 밸류 값 딕셔너리
    print(phone_data)
    #파일이 있어서 정보를 확인하고, 그걸 딕셔너리에 할당. 그렇기에 phone_data를 출력하면 정보가 나온다.

    #전화번호 입력, if 바깥이므로 상관 없이 실행.
    new_phone = input(f"{input_name}님의 전화번호를 입력하세요: ")

    #전화번호를 딕셔너리로 추가한 것이라 파일 닫으면 사라지므로
    #파일 불러와서 작성해야 데이터 저장이 된다. (파일 갱신)
    # 추가 또는 수정
    if input_name in phone_data: #입력한 값과 기존 정보와 비교.
        print("기존 전화번호 수정")
    else:
        print("전화번호 새로 추가")
    
    phone_data[input_name] = new_phone
    #딕셔너리는 해당 키값이 있으면 밸류를 수정. 없으면 추가.
    
    # 전화번호 파일 갱신
    with open("member_tel.txt", "w", encoding="utf-8") as f:
        for name, phone in phone_data.items():
            f.write(f"{name},{phone}\n")
            
    print("전화번호 저장 완료!")
else:
    print("\n로그인 실패!")
