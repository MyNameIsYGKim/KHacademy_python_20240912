# 비트 연산자 : 각 비트끼리 연산
# 2진법을 이해해야 한다.
# ff0000 000000 ffffff
a = 10
b = 12

# bit and
print(a & b)    # 00001000 => 8
# bit or : 둘 중 하나만 1이면
print(a | b)    # 14
# xor : 두개의 값이 다른 경우 1
print(a ^ b)   # 6
# 비트 반전 : ~
print(~a)   # -11
# 쉬프트 연산자
print(a << 1)   # *2랑 같음