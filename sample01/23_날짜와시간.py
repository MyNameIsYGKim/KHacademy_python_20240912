# 날짜와 시간 관련 함수
from datetime import datetime   # datetime 모듈에서 datetime 함수만 가져옴

print(datetime.today())
print(datetime.today().date())
print(datetime.today().month)
print(datetime.today().time())
print(datetime.today().hour)

import calendar
# print(calendar.calendar(2024))

# math 모듈 : 수학과 관련된 기능을 처리 할 떄 사용
import math
print(math.sin(1))
print(math.cos(1))
print(math.tan(1))
print(math.ceil(1.000000000001))
print(math.floor(1.999999999))