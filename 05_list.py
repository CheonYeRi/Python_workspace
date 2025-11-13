'''
리스트(list)
여러 값들을 순서대로 저장할 수 있는 자료형
인덱스(index) 각 값에 부여된 순서(0부터 시작)
가변 자료형(muetable) : 원소 추가/수정/삭제 가능
'''

#리스트 만들기
#list1 = [] #빈 리스트
#list2 = ["안녕하세요","반갑습니다"]
#list3 = [10, "good", 3.14, list2,[1,2,3]]
#print(list1, list2, list3)

#list4 = list()
#list5 = list("CodingOn")
#print(list4, list5) #한 글자씩 나눠져서 나온다. 

#인덱싱과 슬라이싱
#my_list = [1,2,3,4,5]
#print(my_list[0]) #1
#print(my_list[-1]) #5
#my_list[3] = -1 
#print(my_list) #1,2,3,-1,5로 수정됨

#number = input("네 자릿수 정수를 입력하세요.: ")
#천 = number[0]
#백 = number[1]
#십 = number[2]
#일 = number[3]
#print(천, 백, 십, 일)

#------
#슬라이싱
#my_numbers = [10,20,30,40,50,60,70,80,90,100]
#print(my_numbers[1:4]) #20 30 40
#print(my_numbers[3:]) #40 - 100까지 나옴
#print(my_numbers[:4]) #10 20 30 40
#my_numbers[2:4] = [300,400] #값[위치] =(대입) [입력값]
#print(my_numbers)

#문자열, 리스트는 슬라이싱 되지만 리스트만 슬라이싱+ 대입(수정) 가능하다


#실습
#nums = [10,20,30,40,50] #처음과 마지막 요소 출력
#print(nums[:1])
#print(nums[-1:])

#nums = [100,200,300,400,500,600,700] 
#가운데 3개의 요소만 슬라이싱하여 새 리스트로 만들어 출력
#nums[2:5] = [350,410,555]
#print(nums)

nums = [1,2,3,4,5] #모든 원소를 두 배로 만들기
nums[0] = nums[0] * 2
nums[1] = nums[1] * 2
nums[2] = nums[2] * 2
nums[3] = nums[3] * 2
nums[4] = nums[4] * 2
print(nums)

#items = ["a","b","c","d","e"] #리스트를 역순으로 슬라이싱하여 출력
#print(items[::-1])

#data = ["zero","one","two","three","four","five"]
 #짝수 인덱스의 요소만 출력
#print(data[::2])
#2칸 간격으로 나옴.

#movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"] 
#"어벤져스", "라라랜드" → "매트릭스", "타이타닉“ 으로바꾸기
#movies[2:4] = ["매트릭스","타이타닉"] #값[위치] =(대입) [입력값]
#print(movies)

#subjects = ["국어", "수학", "영어", "물리", "화학", "생물", "역사", "지구과학", "윤리"]
#"물리", "생물", "지구과학"만 순서대로 추출하여 새 리스트
#특정 규칙에 따라 요소 추출
#print(subjects[3:8:2])
#시작 지점(3)넣고 끝나는 지점(8)지정하고 2칸(2)간격으로 뜻

#data = ["A", "B", "C", "D", "E", "F", "G", "H"]
#[1~3번째요소] + [4~6번째요소] + [7~9번째요소] 순서로 세구간 나누고
#각 구간을 역순으로 따로 출력 한 줄에 다 들어가게.
#print(data[0:3][::-1], end = " ") #end = " " :공백 지우기 
#print(data[3:6][::-1], end = " ")
#print(data[6:9][::-1])
#해당 범위 지정해 역순 [::-1] 넣고 end = " "로 줄 간격 지워버림)

#인덱싱, 슬라이싱 주의 사항
#my_list = [1,2,3,4]
#my_list[5] #IndexError: list index out of range 리스트 초과하는 인덱스 기입 안된다.

#my_list = [1,2,3,4,5]
#print(my_list[4:1:2]) #[]
#print(my_list[1:3:-1]) #[]
#슬라이싱 시 방향 주의

# ----------------------
# 리스트 연산 -del 
#my_list = [10,20,30,40,50]
#del my_list[2] # 2번 리스트 지워줘 명령어 형식 (특정 요소)
#print(my_list) 
#del my_list[1:3] #슬라이스 범위 삭제
#del my_list #해당 리스트 삭제

#리스트 연결 (+)
#리스트1 + 리스트 2 명령어 양식
#list1 = ["가","나","다"]
#list2 = ["라","마","바"]
#new_list = list1 + list2
#print(list1, list2, new_list, sep="/") #sep는 리스트 사이에 / 넣으란 명령어

#리스트 반복(*)
#medal = ["금","은","동"]
#new_list = medal * 3
#print(new_list)

#포함 여부 (in, not in) True /False 로 판정
#fruite = ["토마토","사과","포도"]
#print("포도" in fruite)
#print("참외" in fruite)


#실습
#특정 요소 삭제 + 앞/뒤 리스트 연결해 새 리스트 result를 출력
fruits = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]
del fruits[1:4]
result = fruits[:1] + fruits[1:] #fruits 의 범위 A, B를 합친 값이 result란 뜻 
#ㄴ 오답노트 표기 
print(result)

letters = ["A", "B"]
new_letters = letters * 3
del new_letters[2]
print(new_letters)
#리스트를 3번 반복한 후, 전체 결과에서 중간에 있는 "A"만 삭제 출력

#주요 메서드 : 내장된 함수. 
#len(리스트 명칭) : 리스트 안 요소 갯수를 세줌.
number = [1,2,3,4]
print("길이 값", len(number), len("Coding")) #len(삽입할 내용) 해도 바로 출력됨

#삽입
number.append (5)
number.append (6)
number.append (7)
print("append 연습", number)

number.insert(2,2.5) #(인덱스위치, 값)
number.insert(4,3.5)
print("insert 실행", number)

number.extend([8,9]) #여러개 삽입 명령어
print("extend 실행",number)

#삭제
number.remove(2.5) #리스트에 있는 값 지정해 삭제
number.remove(3.5)
print("remove 실행",number)

a = number.pop(4) #4 인덱스에 삭제한 요소 (5)
print("pop 실행, 삭제한 요소 값", a)
print(number)
b = number.pop() #공백일 시 맨 뒷 요소 삭제 됨
print("pop 실행, 삭제한 요소 값", b)
print(number) 

#list.sort() : (리스트명칭).sort 원본 리스트를 정렬
#sorted(list) : 정렬된 새로운 리스트 반환
#오름차순 기본, .sort(reverse=True) 옵션을 주면 내림차순으로 정렬
number = [3,2,1,5,4]
number.sort()
print("sort 실행",number)
number.sort(reverse=True)
print("sort reverse=true 실행",number)

number1 = [10,20,40,50,30]
new_number = sorted(number1)
new_number_desc = sorted(number1, reverse=True)
print("sorted 실행", number1, new_number, new_number_desc)

#리스트.reverse() 리스트 뒤집기 (원본 변경)