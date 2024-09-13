# 영식(Y) 요금제 : 30초마다 10원
# 민식(M) 요금제 : 60초마다 15원
# 입력 : 통화 횟수, 각 통화당 통화시간
# M 45 <= 더 싼 요금제와 통화 요금
# Y M 50 <= 두 개의 요금이 같을 때
call = list(map(int, input("통화시간을 띄어쓰기 기준으로 나열 : ").split(" ")))
y = m = 0
for c in call:
    y += c // 30 * 10 + 10
    m += c // 60 * 15 + 15
print(f"Y요금제 : {y}, M요금제 : {m}")
if y == m:
    print(f"Y M {y}원")
elif y > m:
    print(f"M {m}원")
else:
    print(f"Y {y}원")