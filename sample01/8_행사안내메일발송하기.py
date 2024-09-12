# 행사 안내 메일 내용 자동 작성하기

# 이름 : 백이진
# 행사내용 : 현대 자동차 신차 발표회
# 일시 : 202220301 (연속해서 입력)
# 시간 : 14
# 1월 입니다.
# 2월 입니다.
# 3월 입니다.
# 4월 입니다.
# 5월 입니다.
# 6월 입니다.
# 7월 입니다.
# 8월 입니다.
# 9월 입니다.
# 10월 입니다.
# 11월 입니다.
# 12월 입니다.
name = input("이름 : ")
event = input("제목 : ")
date = input("날짜 : ")   # 202220301
time = input("시간 : ")   # 24시간제 입력

# 입력 받은 date에서 월 정보 추출
month = date[4:6]
greeting = ""
if month == "01":
    greeting = "1월 입니다."
elif month == "02":
    greeting = "2월 입니다."
elif month == "03":
    greeting = "3월 입니다."
elif month == "04":
    greeting = "4월 입니다."
elif month == "05":
    greeting = "5월 입니다."
elif month == "06":
    greeting = "6월 입니다."
elif month == "07":
    greeting = "7월 입니다."
elif month == "08":
    greeting = "8월 입니다."
elif month == "09":
    greeting = "9월 입니다."
elif month == "10":
    greeting = "10월 입니다."
elif month == "11":
    greeting = "11월 입니다."
elif month == "12":
    greeting = "12월 입니다."
else:
    print("월 정보가 잘못 입력 되었습니다.")

print(f"{name}님.")
print(greeting)
print(f"""아래의 일정으로 {event}를 진행하고자 하오니
자리를 빛내주시기 바랍니다.
""")
print("="*7, " 행사 안내 ", "="*7)
print("내용 : " + event)
print(f"날짜 : {date[:4]}년 {date[4:6]}월 {date[6:8]}일")
time = int(time)
if time > 12:
    time -= 12
    print(f"시간 : 오후 {time}시")
else:
    print(f"시간 : 오전 {time}시")