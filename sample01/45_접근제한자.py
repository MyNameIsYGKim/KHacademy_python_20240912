# 접근 제한자란? 클래스 내부에 선언된 변수에 대한 접근을 제한하는 것.
# 내부 변수를 외부에서 접근하고자 할 때 지정된 getter와 setter 메서드를 통해서만 접근하도록 하는 것.
# private(__) : 같은 클래스 내에서만 접근 가능.
# protected(_) : 같은 클래스 내이거나 상속 관계가 존재하면 접근 가능.
# public(변수에 아무것도 안 붙임) : 아무데서나 접근 가능.

class TV:
    cnt = 0 # 클래스 맴버
    def __init__(self, name, isOn, channel, volume):
        self.__name = name      # private
        self.__isOn = isOn
        self.__channel = channel
        self.__volume = volume
        TV.cnt += 1
    def set_on(self, isOn):
        self.__isOn = isOn
    def set_channel(self, cnl):
        if 0 < cnl < 1000 :
            self.__channel = cnl
        else :
            print("채널 설정 범위가 아닙니다.")

    def set_volume(self, vol):
        self.__volume = vol
    def get_on(self):
        return self.__isOn
    def get_channel(self):
        return self.__channel
    def get_volume(self):
        return self.__volume
    def view_tv(self):
        power = ("OFF", "ON")
        print(f"이름 : {self.__name}")
        print(f"전원 : {power[self.__isOn]}")
        print(f"채널 : {self.__channel}")
        print(f"볼륨 : {self.__volume}")

lg_tv = TV("LG", True, 10, 20)
sam_tv = TV("LG", True, 10, 20)
print(lg_tv.get_on())
lg_tv.__name = "SAMSUNG" # 에러는 안나지만 변경은 안됨
lg_tv.__isOn = False # 에러는 안나지만 변경은 안됨
# lg_tv.set_channel(999)
# lg_tv.view_tv()
# print(TV.cnt)
