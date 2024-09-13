# 튜플은 시퀀스 자료형
# 이뮤터블(immutable) : 읽기만 가능
# () 또는 괄호가 없으면 튜플
# 패킹과 언패킹 동작을 지원함
person = "장원영", 20, "서울시 강남구 역삼동"   # 패킹(Packing)
print(type(person))

name, age, addr = person    # 언패킹(Unpacking)
print(addr)

def get_person():
    name = "안유진"
    age = 21
    addr = "대전시 유성구"
    return name, age, addr

info = get_person()
print(info)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
# 합집합
print(s1.union(s2))
print(s1 | s2)
# 교집합
print(s1.intersection(s2))
print(s1 & s2)
# 차집합
print(s1.difference(s2))
print(s1 - s2)