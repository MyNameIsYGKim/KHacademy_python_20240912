import decimal
from decimal import Decimal

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Order:
    products = []
    total = 0

    def add_item(self, p:Product):    # 제품 추가하기
        self.products.append(p)
        self.total += int(p.get_price())

    def get_item(self, get_name: str):  # 제품 찾기
        for p in self.products:
            if get_name == p.get_name():
                return print(f"{p.get_name()} : {p.get_price()}")
        return print(None)

    def remove_item(self, del_name: str):    # 제품 삭제
        for i in self.products:
            if del_name == i.get_name():
                self.products.remove(i)
                return True
        return False

    def calculate_final_price(self, tax_rate: decimal.Decimal):
        self.total = self.total + self.total * tax_rate
        return self.total

    def show_list(self):
        for pdt in self.products:
            print(pdt)

my_order = Order()
while True:
    print("[1] 제품 추가 [2] 제품 제거 [3] 목록 [4] 상세보기 [5] 최종 가격 [6] 종료")
    num = int(input("선택 : "))
    if num == 1:
        print("[ 제품 추가 ]")
        # ls = list(input("이름, 가격 : ").split(" "))
        # my_order.add_item(Product(ls[0], ls[1]))
        name = input("제품명 : ")
        price = input("가격 : ")
        my_order.add_item(Product(name, price))
    elif num == 2:
        print("[ 제품 삭제 ]")
        product = input("제품명 : ")
        my_order.remove_item(product)
    elif num == 3:
        print("===== 제품 목록 =====")
        for pdt in my_order.products:
            print(f"{pdt.get_name()}")
        print("====================")
    elif num == 4:
        print("[ 상세보기 ]")
        product = input("제풍명 : ")
        my_order.get_item(product)
    elif num == 5:
        tax = decimal.Decimal(input("판매세 입력 : "))
        print("[ 최종 가격 ]")
        print(my_order.calculate_final_price(tax))
    elif num == 6:
        print("종료.")
        break
    else:
        "잘못된 입력."
