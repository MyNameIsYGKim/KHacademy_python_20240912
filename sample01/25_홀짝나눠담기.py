# 무작위 수를 공백 기준으로 입력 받아 홀수와 짝수로 리스트에 나눠 담아 출력
num = list(map(int, input("공백 기준으로 무작위 수 입력 : ").split()))
# odd, even  = [], []
# for e in num:
#     if e % 2 == 1:
#         odd.append(e)
#     else:
#         even.append(e)
# print(f"홀수 : {odd}")
# print(f"짝수 : {even}")
odd = list(filter(lambda x: x % 2 == 1, num))
even = list(filter(lambda x: x % 2 == 0, num))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")