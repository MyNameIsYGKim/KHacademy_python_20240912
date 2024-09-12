# 프로그램에서 값을 연산해야 하는 경우 사용
# 산술연산자 : +, -, *, /, //(몫), %(나머지), **(제곱)
i = 10
j = 3
print(i + j)
print(i - j)
print(i * j)
print(i / j)
print(i // j)
print(i % j)
print(i ** j)

# TAX_RATE = 0.10 # 세율
# income = int(input("당신의 수입은 얼마입니까?"))
# print(f"당신이 내야 할 세금은 {income * TAX_RATE}")

# 대입 연산자 : 값을 변수에 대입 =
# 대입 연산자의 종류 : =, +=, -=, *=, /=, %=
num1 = 10
num1 += 2
print(num1)
num1 -= 10
print(num1)

num1 *= 2
print(num1)

# 비교 연산자 : 두 개의 값을 비교해서 참/거짓을 만들어 냄
# ==, >, <, >=, <=
a = 10
b = 20
print(a > b)    # False
print(a < b)    # True
print(a == b)   # False
print(a >= b)   # False
print(a <= b)   # True

# 관계 연산자 : and, or, not
x = 10
y = 20
z = 30
rst1 = (x > 0) and (x > y) # False
rst2 = (x > 0) or (x > y) # True
rst3 = not((x > 0) or (x > y))   # False
print(rst1, rst2, rst3)

# 3항 연산자 : 항 3개인 연산자 : 참과 거짓이 있는 조건문 동일
age = int(input("나이를 임력하세요 : "))
is_adult = age > 19 and "성인" or "미성년자"
print(f"당신은 {is_adult} 입니다.")

if age > 19:
    print(f"당신은 성입입니다.")
else:
    print(f"당신은 미성년자입니다.")

is_adult = age > 19 and print("성인") or print("미성년자")