# 모듈(module)
#여러 기능(함수)의 묶음
#하나의 py파일로 여러 기능을 모아놓은 곳

'''
#모듈 불러오기(1)
import hello

hello.greeting("lee")

#모듈 불러오기(2)
from hello import greeting

greeting("kim")

#모듈 불러오기(3)
from hello import * #전체를 다 불러옴.

introduce("sin",15)

#모듈 불러오기(4)
import hello as h #h로 모듈 약칭하겠다.
h.greeting("kim")
h.introduce("U",10)
'''

'''
#실습
import calc as C
C.add(10,5)
C.subtract(8,2)
C.multiply(7,4)

from calc import divide
divide(9,0)
divide(5,2)

#패키지
#모듈의 묶음
#모듈을 폴더 단위로 묶어놓은 곳

#패키지 폴더 만들어서 py 파일 넣고 모듈 불러와서 쓰면 __pycahe__라는 게 생성된다.

#패키지에서 모듈 불러오기(1)
from my_package import calc as c

#패키지에서 모듈 불러오기(2)
from my_package.calc import add
c.add(10,5)

# 파이썬 표준 라이브러리

#math 모듈: 수학적 연산에 사용되는 모듈
import math as m

#1.올림/내림
#ceil: 올림, 소수점 지정x
m.ceil(3.14)

#floor: 내림, 소수점 저정x
m.floor(3.14)

#round :반올림 - 내장 함수 (math 모듈 아님)
round(3.141492, 2)

#2. 제곱, 제곱근
# pow(x, y) : 제곱 - x^y
m.pow(2,3)

#sqrt(x): 제곱근 반환
m.sqrt(16)

#3. 상수
#pi : 원주율
print(m.pi)

#4. 수학 계산 편의 기능
print(m.factorial(3))

#최대 공약수
print(m.gcd(12,80))

#최소 공배수
print(m.lcm(12,20))

'''
#실습 math모듈 사용
import math as m

x1, y1 = 10, 52
x2, y2 = 4, 30
'''
#모범 답안
x1,y1 = map(int, input("x1, y1을 입력해주세요.: ").split(","))
#int(x1), int(y1)
x2,y2 = map(int, input("x2, y2을 입력해주세요.: ").split(","))
#int(x2), int(y2)
'''
dis = m.sqrt(m.pow(x2 -x1, 2) +m.pow(y2 - x1, 2))
print(f" 거리 값 {round(dis, 2)}")

#최소 공배수, 최대 공약수
s,t= 18,24
print(m.gcd(s,t))
print(m.lcm(s,t))
