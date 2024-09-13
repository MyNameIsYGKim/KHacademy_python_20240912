# # 별찍기1
# # 입력 : 5
# # *
# # **
# # ***
# # ****
# # *****
# star = int(input("입력값 : "))
# for i in range(star):
#     for j in range(i+1):
#         print("*", end="")
#     print()


# # 별찍기2
# star = int(input("입력값 : "))
# for i in range(star):
#     for j in range(star - i, 0, -1):
#         print("*", end="")
#     print()

# # 별찍기3
# star = int(input("입력값 : "))
# for i in range(star):
#     for j in range(i):
#         print(" ", end="")
#     for k in range(star - i, 0, -1):
#         print("*", end="")
#     print()