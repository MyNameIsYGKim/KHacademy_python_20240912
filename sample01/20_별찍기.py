# 별찍기1
# 입력 : 5
# *
# **
# ***
# ****
# *****
star = int(input("입력값 : "))
for i in range(star):
    for j in range(i+1):
        print("*", end="")
    print()
    if i == 4:
        print("별이 다섯 개 ★★★★★!!")
