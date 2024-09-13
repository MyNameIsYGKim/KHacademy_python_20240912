# 햄버거 가격 3개, 음료 가격 2개
# 출력 : 세트 메뉴 가격 = 제일 싼 햄버거 + 제일 싼 음료 - 50
# 입력 : 1000 1500 2000, 1200 750
# 세트 : 1000 + 750 - 50 = 1700
print("상덕버거, 중덕버거, 하덕버거, 콜라, 사이다의 가격을 띄어쓰기 기준으로 입력해주세요.")
burger = list(map(int, input("입력 : ").split(" ")))
c_burger = min(burger[:3])
c_drink = min(burger[3:])
print(f"세트 메뉴의 가격은 {c_burger + c_drink - 50}원 입니다.")

for i in range(len(burger)):
    if i < 3 and c_burger > burger[i]:
        c_burger = burger[i]
    if i > 2 and c_drink > burger[i]:
        c_drink = burger[i]
