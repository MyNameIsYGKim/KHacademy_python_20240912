# 내장함수 : 원래 제공되는 것, import 필요 없음
from sys import maxsize

from dask.array import average

# # 매개변수로 전달된 값 중 가장 큰 값을 반환
# print(max(32, 45, 67, 12, 45))
# score = list(map(int, input("정수 입력 : ").split()))   # 리스트형으로 정수 값 반환
# print((max(score)))
# print(max([1,2,3,4,5,6,7,8]))

# print(min(32, 45, 67, 12, 45))
# score = list(map(int, input("정수 입력 : ").split()))   # 리스트형으로 정수 값 반환
# print((min(score)))
# print(min([1,2,3,4,5,6,7,8]))

# 시퀀스 자료형의 값을 모두 더해줌
print(sum([1,2,3,4,5]))
print(sum([1,2,3,4]) / 5)

# 몫과 나머지를 튜플 형태로 반환(unpacking)
print(divmod(sum([1, 2, 3, 4, 5]), 5))

# 정렬
my_list = [1,8,4,6,3,2,5,7,9]
print(sorted(my_list))  # 오름차순
print(sorted(my_list, reverse=True))    # 내림차순
print(len(my_list)) # 요소의 갯수

# 실습
n = list(map(int, input("정수 입력 : ").split()))
# 입력 받은 값의 최댓값
# 입력 받은 값은 최솟값
# 총점
# 평균
# 5로 나누었을 때의 몫과 나머지
print(f"최댓값 : {max(n)}")
print(f"최솟값 : {min(n)}")
print(f"총점 : {sum(n)}")
print(f"평균 : {sum(n)/len(n)}")
print(f"5로 나눈 몫과 나머지 : ", end="")
for i in range(len(n)):
    print(divmod(n[i], 5), end=",")

