# 상근이 알람 : 45분 일찍 알람을 울리도록 하는 문제
# 입력 : 시간과 분을 입력 받음, 24시간제

# 입력은 h, m으로 ":"기준으로 입력받음

# 시간을 분으로 환산 하기

#  분으로 환산한 시간이 45보다 작으면 시간을 변도 계산해야 함.

# 45분을 뺴줌

# 다시 시간과 분으로 환산해서 출력

# # 내 1번째 방법
# time = input("시간을 \"00:00\" 형식으로 입력하세요 : ")
# h = int(time.split(':')[0])
# m = int(time.split(':')[1])
# if m < 45:
#     m += 15
#     h -= 1
# else:
#     m -= 45
# if h < 0:
#     h = 23
# if h < 10: h = "0" + str(h) # 시간 00으로 설정
# if m < 10: m = "0" + str(m) # 시간 00으로 설정
# print(f"{h}:{m} 으로 알람 설정 완료")

# # 내 2번째 방법
# time = input("시간 입력 \"00:00\" ")
# h = int(time.split(':')[0])
# m = int(time.split(':')[1])
# time = h * 60 + m - 45
# if time < 0:
#     h = 23
# else:
#     h = time // 60
# m = time % 60
# if h < 10: h = "0" + str(h) # 시간 00으로 설정
# if m < 10: m = "0" + str(m) # 시간 00으로 설정
# print(f"{h}:{m} 으로 알람 설정 완료")

# 강사님 방법
h, m = map(int, input("시간 입력 : ").split(":"))   # 중요!!!!!!!!!!
calc_min = h * 60 + m   # 입력받은 시간을 분으로 환산
if calc_min < 45:
    calc_min = 24 * 60 + m
calc_min -= 45
print(f"{calc_min // 60}:{calc_min % 60}")