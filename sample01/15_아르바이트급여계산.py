# 주/야간 근무시간을 입력받아 아르바이트 급여 계산
# 주간 근무 시급 : 9860원
# 야간 근무 시급 : 주간 시급 * 1.5
# [입력] 주간근무 [1] 야간근무[2]를 입력하세요
# [입력] 근무 시간을 입력하세요
# [출력] print(f"{근무시간}시간 동안 근무한 {근무타입문자열} 급여는 {급여}원 입니다.)
work = int(input("주간근무 [1] 야간근무 [2]를 입력하세요. "))
money = 0
hour = 0
work_type = ""
if work != 1 and work != 2:
    print("1또는 2를 입력하세요.")
else:
    hour += int(input("근무 시간을 입력하세요 : "))
    if hour < 0:
        print("0 이상의 숫자만 입력하세요.")
    else:
        if work == 1:
            money += hour * 9860
            work_type += "주간 근무"
        elif work == 2:
            money += hour * 9860 * 1.5
            work_type += "야간 근무"
money = f"{money:,.0f}"
print(f"{hour}시간 동안 근무한 {work_type} 급여는 {money}원 입니다.")