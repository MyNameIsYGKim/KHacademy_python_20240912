# print("black, brown, red, orange, yellow")
# print("green, blue, violet, grey, white")
#
# total = 0
# colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
#
#
# num1 = input("첫 번째 색 입력 : ")
# for i in range(len(colors)):
#     if num1 == colors[i]:
#         total += i * 10
#
# num2 = input("두 번째 색 입력 : ")
# for j in range(len(colors)):
#     if num2 == colors[j]:
#         total += j
#
# num3 = input("세 번째 색 입력 : ")
# for k in range(len(colors)):
#     if num3 == colors[k]:
#         total = total * (10 ** k)
#
# print(total)

color = "black", "brown", "red", "orange", "yellow", \
    "green", "blue", "violet", "grey", "white"
f_name = color.index(input())   # 해당 문자열의 인덱스 반환
s_name = color.index(input())
t_name = color.index(input())
print(int(str(f_name) + str(s_name)) * (10 ** t_name))