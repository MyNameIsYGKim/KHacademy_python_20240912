# 제어문이란? 조건문과 반복문
# num = int(input("정수값 입력 : "))
#
# if num > 100:
#     print(f"{num}은 100보다 크다")
# elif num < 100:
#     print(f"{num}은 100보다 작다.")
# else:
#     print(f"{num}은 100과 같다")

# 실습문제
# 성적 입력 받아서 0 ~ 100 이 아니면 성적을 잘못 입력했다고 표기.
# 성적 0 ~ 100이고, 90점 이상이면 "A", 80점 이상 "B", 70점 이상 "C", 60점 이상 "D", 나머지는 "F"
while True:
    score = int(input("성적 입력 : "))
    if 0 <= score <=100: break
    print("잘못된 성적 입력")
if      score >= 90:    print("성적은 A 입니다.")
elif    score >= 80:    print("성적은 B 입니다.")
elif    score >= 70:    print("성적은 C 입니다.")
elif    score >= 60:    print("성적은 D 입니다.")
else:                   print("성적은 F 입니다.")

# 3자리 정수 입력 받아서 100의 자리, 10의 자리, 1의 자리로 나눠 담고
# 이 중 가장 큰 수 출력
# num = int(input("정수 3자리 입력 : "))
# a = num // 100
# b = (num % 100) // 10
# c = num % 10
# if a >= b and a >= c:
#     print(f"가장 큰 수는 {a}입니다.")
# elif b >= c:
#     print(f"가장 큰 수는 {b}입니다.")
# else:
#     print(f"가장 큰 수는 {c}입니다.")
