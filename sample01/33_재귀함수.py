# 재귀함수 : 함수 내에서 자기 자신을 호출하는 구조
# 길찾기 등의 알고리즘에서 많이 사용, 효율적인 정렬 알고리즘에서도 사용됨

def for_sum(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

def while_sum(n):
    s = 0
    while n:
        s += n
        n -= 1
    return s

def recursive_sum(n):
    if n == 1: return 1
    return n +  recursive_sum(n - 1)

num = int(input("정수 입력 : "))
print(recursive_sum(num))