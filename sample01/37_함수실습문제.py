# 입력 받은 수 미만의 소수의 합 구하기
# 입력 : 12 (2 + 3 + 5 + 7 + 11) = 28

# def prime_func(n):
#     result = 0  # 소수의 합
#     for e in range(2, n):   # 2부터 n-1 까지 반복
#         cnt = 0     # 소수인지 판별
#         for f in range(2, e):
#             if e % f == 0: cnt += 1     # 소수가 아니면 cnt + 1
#         if cnt == 0: result += e    # 소수가 맞으면 해당 값 더함
#         print(f"{e}: {result}")
#     return result
#
#
# n = int(input("정수 입력 : "))
# print(prime_func(n))

def prime_func(n):
    is_prime = True
    for i in range(2, n):   # 1과 자기 자신을 제외
        if n % i == 0: is_prime = False
    if is_prime: return n
    else: return 0

num = int(input("정수 입력 : "))
prime_sum = 0
for i in range(2, num):
    prime_sum += prime_func(i)
print(prime_sum)