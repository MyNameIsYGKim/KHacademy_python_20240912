print("파이썬을 공부하겠습니다.") # 주석 넣기.
print(100) # 정수값 출력.
print(33.333333) # 실수값 출력.
print(100+200) # 연산자 사용
print(100 < 200) # True

"""
 - 파이썬은 값이 대입될 때 데이터형이 결정된다.
 - "", '' 모두 문자열 의미.
 - 따로 구분하지 않음.
 - == 같다는 의미. = 대입을 의미.
"""

name = "김연규"
print(name)
name = 10
print(name)

''' 식별자 사용 규칙
 - 키워드(예약어) 사용 금지
 - 특수문자는 언더바(_)만 사용 가능.
 - 숫자는 사용 가능하지만 앞에 오면 안됨.
 - snake_case : 스네이크 표기법
'''

name = ("김연규")
email = "kelen536"
phone = "010-5588-9259"
addr = "서울시 강남구"

print(f"""
    name : {name}
    email : {email}@gmail.com
    phone : {phone}
    address : {addr}
""")
