# 함수란? 코드의 특정 블럭을 하나의 이름으로 묶는 것, 코드의 재사용성을 높임, 가독성 향상.
# 함수는 매개변수를 가질 수 있고, 반환값을 가질 수 있음.
# 식별자는 스네이크 표기법으로 작성하고, 식별자 뒤에 ()소괄호가 있음.
# 일반적으로 매개변수와 함수가 호출하는 인자의 갯수가 일치해야 함.
# def 키워드로 정의.

# 함수의 반복호출, 매개변수는 존재하고 반환값은 없는 함수 정의
def name_card(name, addr, phone, position): # 함수를 선언하고 매개변수로 4개의 값을 입력 받음.
    print(f"{position} : {name}")
    print(f"전화번호 : {phone}")
    print(f"주소 : {addr}")
    print("="*30)

# name_card("안유진", "서울시 강남구 역삼동", "010-1234-5678", "리더")
# name_card("장원영", "서울시 강남구 삼성동", "010-1234-1234", "센터")
# name_card("가을", "서울시 강남구 신사동", "010-1234-5678", "싱어")

# 은행 계좌 개설하기
def open_account(name): # 매개변수도 있고, 반환값도 있는 함수 선언
    print(f"{name}님의 계좌를 개설하였습니다.")

def deposit(balance, in_val):   # 잔액과 입금을 매개변수로 전달 받음
    print(f"{in_val} 입금 되었습니다. 잔액은 {balance + in_val} 입니다.")
    return balance + in_val # 기존 잔액에서 입금 금액을 더해서 반환

def withdraw(balance, out_val): # 잔액과 출금을 매개변수로 전달 받음
    if balance >= out_val:
        print(f"{out_val}이 출금 되었습니다. 잔액은 {balance - out_val} 입니다.")
        return balance - out_val
    else:
        print(f"출금이 실패했습니다. 잔액은 {balance}입니다.")
    return balance

# balance = 0 # 외부에서 선언한 변수
# name = input("계좌 개설할 이름을 입력 : ")
# open_account(name)   # 인자값으로 전달한 이름을 반환값으로 되돌려 받음.
# balance = deposit(balance, 1000)    # 외부에서 선언한 잔액을 인자값으로 전달, 입금액을 인자값으로 전달
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 500)
# print(f"{name}의 잔액은 {balance} 입니다.")

# 기본값 인자 : 함수 선언 시 매개변수에 대한 기본값을 정의.
# 매개변수에 기본값이 정의 되어 있는 경우 호출 시 인자값을 넣지 않으면 기본값으로 호출
def profile(name, grade = 2, age = 18, school = "태양고"):
    print(f"이름 : {name}, 학교 : {school}, 학년 : {grade}, 나이 : {age}")

# profile("나희도")
# profile("고유림")
# # profile() # name은 기본값 인자가 아니므로 반드시 인자값을 전달해야 함.
# profile("백이진", None, 22)

# 가변 매개변수 : 함수의 매개변수 앞에 *(별표)를 붙이면 인자값으로 몇 개를 전달하든 튜플로 인식해서 처리 가능.
def profile2(name, age, *lang):
    print(f"이름 : {name}, 나이 : {age}", end=" ")
    for e in lang:
        print(e, end=" ")
    print()

# profile2("유재석", 40, "Python", "Java", "C", "C++", "React", "Kotlin", "Swift")
# profile2("조세호", 30, "Python", "JavaScript")

# 지역 변수, 전역 변수
# 대부분의 언어는 블록스코프를 기반으로 변수의 생명주기를 관리
# 파이썬의 경우는 함수 스코프 기반의 언어, 외부에서 선언한 변수의 값을 함수내에서 변경하기 위해서는 global 키워드를 사용해야 함
knife = 10
def game(player):
    global knife
    knife -= player # knife = knife - player
    print(f"남아 있는 칼은 {knife} 자루 입니다.")

def game2(knife, player):
    knife -= player # knife = knife - player
    print(f"남아 있는 칼은 {knife} 자루 입니다.")

# in_val = int(input("경기에 참여하는 선수의 수 입력 : "))
# game2(knife, in_val)

# 키를 입력 받아 표준 체중 구하기
# 키는 cm 단위로 입력 받음
# 체중에 대한 출력은 소수점 2자리까지 출력 (반올림 함수 사용)
def std_weight(height, gender):
    hm = height / 100   # 입력 받은 cm 키를 미터 단위로 변경
    if gender == 1:
        return hm * hm * 22
    else:
        return hm * hm * 21
h = int(input("키 입력 : "))
g = int(input("성별 [1]남성 / [2]여성 : "))
weight = round(std_weight(h, g), 2)   # 소숫점 3번째 자리를 반올림
gender_str = "", "남성", "여성"
print(f"키 : {h}cm {gender_str[g]}의 표중 체중은 {weight}kg 입니다.")
