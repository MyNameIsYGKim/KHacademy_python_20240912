# 영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤,
# 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오.
# for 문을 사용
# isLower() : 소문자이면 True, 아니면 False 반환.

rst = ""
for e in input("영단어 입력 : "):
    if e.islower():
        rst += e.upper()
    else:
        rst += e.lower()

print(rst)
