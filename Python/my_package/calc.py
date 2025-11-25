def add(a, b):
    print(f"{a} + {b} = {a + b}")

def subtract(a, b):
    print(f"{a} - {b} = {a - b}")

def multiply(a, b):
    print(f"{a} x {b} = {a * b}")

def divide(a,b):
    if b == 0:
        print("'0'으로 나눌 수 없습니다.")
        return None
    else:
        print(f"{a} % {b} = {a / b}")