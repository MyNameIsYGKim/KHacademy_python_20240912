# 자연수 A, B, C
# A x B x C의 결과에 각각의 숫자가 몇 번 쓰였는지 알아보자
a, b, c = map(int, input("자연수 3개 입력(\" \"띄어쓰기로 구분) : ").split(" "))
num = str(a * b * c)
print(f"입력값(a * b * c) : {num}")
for i in range(10):
    print(f"{i}의 갯수: {num.count(str(i))}개")

# 실습 2번 : 문자열 반전, 문자열을 입력 받아서 문자열 반전 출력
# ex) ABCDEF => FEDCBA
string = input("문자열 입력 : ")
# string2 = ""
# for i in range(1, len(string) + 1):
#     string2 += string[-i]
# print("입력된 문자열 : " + string)
# print("반전된 문자열 : " + string2)
print("반전된 문자열 : ", end="")
for i in range(1, len(string) + 1):
    print(string[-i], end="")
print()
reverse_str = string[::-1]
print(reverse_str)

