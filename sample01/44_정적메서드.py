# 인스턴스 메서드 : 객체로 만들어질 때 함께 만들어지는 메서드
# 정적 메서드 : 클래스와 관련이 있음, 객체와 무관한 독립적인 동작 수행
# 클래스 메서드 : 클래스와 관련 있음, 클래스 변수를 사용하기 위함
class Car:
    is_instance_cnt = 0     # 클래스 변수(멤버), 클래스 소속, 객체로 만들어지지 않음.

    def __init__(self, size, model):
        self.size = size
        self.model = model
        self.speed = 0
        Car.is_instance_cnt += 1    # 클래스 변수 사용

    def move(self, speed):      # 인스턴스 메서드
        self.speed = speed
        print(f"자동차 {self.size} & {self.model}이 시속 {self.speed}로 달립니다.")

    @staticmethod
    def check_type(code):
        if code <= 10: print("전기차 입니다.")
        elif code <= 20: print("가솔린차 입니다.")
        elif code <= 30: print("디젤차 입니다.")
        else: print("분류 코드가 없습니다.")

    @classmethod
    def print_cnt(cls):     # 클래스 변수에 대해 접근하고자 하는 경우 사용
        print(f"자동차 객체 생성 수 : {cls.is_instance_cnt}")

santafe = Car("중형 SUV", "싼타페")
sorneto = Car("중형 SUV", "쏘렌토")
santafe.move(220)
sorneto.move(225)

Car.check_type(10)
Car.print_cnt()
