'''
원소의 중복을 허용하지 않는 여러 데이터의 모음
순서가 없는 컬렉션 자료형
'''
#s1 = {1,2,3} # 형태로 사용
#print(s1, type(s1)) #{1, 2, 3} <class 'set'>

#s2 = {1,1,1,2,2,2,3,3,3,4,4,4}
#print(s2) #{1, 2, 3, 4} 출력, 중복 무시

#빈 set 만들기
# {} 안에 원소를 넣지 않고 만들면 빈 dict로 인식함
#s3 = {}
#print(type(s3)) #<class 'dict'>

#set 함수로 생성
#s4 = set()
#print(s4, type(s4)) #set() <class 'set'>

# set 함수의 활용: 원소의 중복 제거
#my_list1 = [1,1,1,2,2,2,3,3,3,4,4,4]
#s5 = set(my_list1)
#print(s5) #{1, 2, 3, 4}

#인덱싱 X
#s1[1] # 'set' object is not subscriptable 오류 나옴.

#자료형 제한
#set에 요소가 추가/삭제 될 수 있지만 가변 자료형은 원소로 사용할 수 없다.
#s = {1,2,(3,4)} < 숫자, 문자열, 튜플 가능함
#s = {[1,2]} #리스트,딕셔너리는 내부 요소 바꿀 수 있는 객체= 해씨너리가 바뀜. 이라 X
#cannot use 'list' as a set element (unhashable type: 'list') 오류

# set 연산
# 집합의 연산 : 합집합, 교집합, 차집합, 대칭차집합
#a = {1,2,3}
#b = {3,4,5}

#합집합 (쉬프트+\ .union)
#s_union1 = a | b
#s_union2 = a.union(b)
#print("합집합1", s_union1)
#print("합집합2", s_union2)

#교집합 (&, .intersection)
#s_inter1 = a & b
#s_inter2 = a.intersection(b)
#print("교집합1", s_inter1)
#print("교집합2", s_inter2)

#차집합 (-, .difference)
#a_diff1 = a - b
#a_diff2 = a.difference(b)
#print("차집합", a_diff1)
#print("차집합", a_diff2)
#print(b-a)

#대칭차집합 (^, .symmetric_difference)
#s_symm1 = a ^ b
#s_symm2 = a.symmetric_difference(b)
#print("대칭차집합", s_symm1)
#print("대칭차집합", s_symm2)

#실습 1
#중복을 제거한 후, 총 몇 명이 제출했는지 출력하는 프로그램을 작성
submissions = [' kim', 'lee', ' kim', 'park', 'choi', 'lee', 'lee']
명단 = set(submissions)
#print("제출한 학생 수:", len(명단))
#print("제출자 명단:", 명단)

#02 두 사용자의 공통 관심 장르, 서로 다른 장르, 모든 장르 목록을 출력
user1 = {'SF', 'Action', 'Drama'}
user2 = {'Drama', 'Romance', 'Action'}
#print("공통 관심 장르:", user1 & user2)
#print("서로 다른 장르:", user1 ^ user2)
#print("전체 장르:", user1 | user2)

#Set 매서드
s1 = {1,2,3}

#원소 추가
s1.add(4)
#print("원소추가", s1)

#여러 원소 추가
s1.update((5,6,7))
#print("여러 원소 추가", s1)

#원소 체거
s1.remove(4)
#print("원소 제거", s1)
#s1.remove(100) # 없는 걸 제거할 시 에러 나옴

s1.discard(6)
s1.discard(100)
#print("원소 제거2", s1) #discard 는 없는 원소 무시해 적용함

deleted = s1.pop() #임의의 값 하나 제거 
#print("원소 제거3", s1 , deleted)

#부분 집합 (subset) 관련 매서드
a = {10,20,30,40,50} #상위 집합
b = {20,30,40} #부분 집합
c = {10, 200,300,400,500}

#부분집합 여부 판단
print(b.issubset(a)) #True
print(a.issubset(b)) #False

#상위집합 여부 판단
print(a.issuperset(b)) #True
print(b.issuperset(a)) #False

#공통 원소가 없는 지 여부 판단
print(a.isdisjoint(b)) #False
print(a.isdisjoint(c)) #False
print(b.isdisjoint(c)) #True

#실습
#03 이 사용자가 지원 자격을 갖추었는지 확인
# 유저가 가지고 있는 자격증 목록 / 특정 직무에 필요한 자격증 목록
my_certificates = {'SQL', 'Python', 'Linux'}
job_required = {'SQL', 'Python'}
print("지원 자격 충족 여부:",job_required.issubset(my_certificates)) 
#job이 my의 부분집합인지 판단

