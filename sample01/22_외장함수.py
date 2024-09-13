# 외장함수는 import 해서 사용하는 함수, 파이썬 기본적으로 제공하는 것
# 랜덤 함수 : 지정한 범위 내에서 임의의 숫자를 만들어 내는 것

import random

# for i in range(30):
#     rand = random.randrange(1, 11)  # 0 ~ 10 미만의 임의의 값을 생성
#     print(rand, end=" ")
# print()

# 중복되지 않는 로또 번호 생성 : 1 ~ 45 사이의 임의의 수 6개
lotto = []
while len(lotto) < 6:
    num = random.randrange(1, 46)
    if num not in lotto:
        lotto.append(num)
print(lotto)

lotto2 = set()
while len(lotto2) < 6:
    num = random.randrange(1, 46)
    lotto2.add(num)
print(lotto2)