# 추상화? 실체화가 되지 않는 부모로부터 상속받는 것.
# 부모 클래스 내에 이름만 선언되고 구현부가 없는 추상 메서드를 포함.
# 상속 받은 클래스는 반드시 추상 메서드에 대해서 구현해줘야 함.
from abc import *   # 추상클래스를 사용하기 위해 import
from abc import ABC

class NetworkAdapter(metaclass=ABCMeta):    # 해당 클래스를 추상클래스로 만듬
    @abstractmethod
    def connect(self):
        pass

class WiFi(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company}의 WiFi에 연결되었습니다.")

class FiveG(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company}의 WiFi에 연결되었습니다.")

class Lte(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company}의 WiFi에 연결되었습니다.")

net = input("연결할 네트워크 [1]Wifi [2]5G [3]Lte : ")
adapter = None

if net == "1":
    adapter = WiFi("KT Megapass")
    adapter.connect()
elif net == "2":
    adapter = FiveG("SK Telecom")
    adapter.connect()
elif net == "3":
    adapter = Lte("LG U+")
    adapter.connect()
else:
    print("연결할 네트워크가 없습니다.")