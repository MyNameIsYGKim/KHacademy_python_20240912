# from 50_모듈과패키지 import add, sub
import1 = __import__('50_모듈과패키지')

print(import1.add(100, 200))

get_pwd = import1.password("http://naver.com")
print(get_pwd)