# 양의 정수 n을 입력 받아 n * n 크기의 행렬을 출력하는 프로그램 작성
# 이 떄 행렬의 값은 1부터 시작하여 왼쪽에서 오른쪽, 위에서 아래 순서대로 채워 넣음.
# 입력 : 3
# 1 2 3
# 4 5 6
# 7 8 9

# 1. 입력 받은 값으로 실제 출력 범위 작성
# 2. 줄바꿈에 대한 처리 (나머지 연산자 사용)
# 3. 줄맞춤

# n = int(input("정수 n 입력 : "))
# n2 = n * n
# count = 0
# while True:
#     if n2 // 10 == 0: break
#     n2 = n2 // 10
#     count += 1
# for i in range(1, n2 + 1, 1):
#     if i % 10 == 0:
#         count -= 1
#     print(f"{count * " "}" + f"{i}")
#     # print(count * " " + i)
#     if i % n == 0:
#         print("\n")

n = int(input("정수 입력 : "))
for i in range(1, n * n + 1):
    print(f"{i:5}", end=" ")
    if i % n == 0: print()