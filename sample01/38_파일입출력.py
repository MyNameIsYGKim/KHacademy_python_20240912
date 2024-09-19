# 파일 입/출력 : 파일을 읽고 쓰는 동작
# 파일 객체, 파일명, "w" = "wt", 한글 깨짐 방지
# score_file = open("score.txt", "w", encoding="utf-8")
# print("수학 : 55", file=score_file)   # print()함수를 사용해 파일에 쓰기
# print("영어 : 70", file=score_file)
# score_file.write("국어 : 90" + "\n")  # 줄바꿈 문자 포함
# score_file.write("과학 : 87" + "\n")
# score_file.close()  # open한 파일은 반드시 닫아줘야 함.

# 파일 읽기
# read() 함수 : 파일 내의 모든 내용을 읽어 하나의 문자열로 반환
# readline() 함수 : 해당 파일의 내용을 한 라인씩 읽어들임.
# readlines() 함수 : 해당 파일의 모든 라인을 읽어 리스트로 반환
# score_file = open("score.txt", "r", encoding="utf-8")
# print(score_file.read())
# score_file.close()

# while True: # 더 이상 읽을 라인이 없을 때까지 반복 수행
#     line = score_file.readline()
#     if not line: break
#     print(line, end="")
# score_file.close()

# lines = score_file.readlines()
# for line in lines:
#     print(line, end="")
# score_file.close()

# with 키워드 : close()메서드를 호출하지 않아도 자동으로 닫아주는 기능
# with open("score.txt", "r", encoding="utf-8") as score_file:
#     lines = score_file.readlines()
#     for line in lines:
#         print(line, end="")

# 이 지점에서 자동으로 close() 함수 호출

# pickle : 파이썬 객체를 직렬화/역직렬화 하기 위한 모듈
import pickle
# data = {"name" : "안유진", "age" : 21, "addr" : "서울시 강남구 역삼동"}
# with open("data.pickle", "wb") as file:
#     pickle.dump(data, file) # 해당 객체를 파일에 직렬화해서 쓰기

with open("data.pickle", "rb") as file:
    rst = pickle.load(file) # 역직렬화
print(rst)