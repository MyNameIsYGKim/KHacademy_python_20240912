# 하나의 어플리케이션 내에서 여러 개의 일을 동시에 수행하는 것.
from simple_colors import *     # 터미널 출력 시 컬러를 지원하기 위해서
import threading    #멀티쓰레드를 지원하기 위해서
import time         # sleep()을 사용하기 위해서. 주어진 시간만큼 해당 쓰레드를 잠재운다
import random       # 난수 발생

class Unit:
    def __init__(self, pp, mp, ph, mh, hp):
        self.pPower = pp  # Physical power
        self.mPower = mp  # Magical power
        self.pHit = ph  # 물리 적중률
        self.mHit = mh  # 마법 적중률
        self.hp = hp  # 체력
        self.isAlive = True  # 생사 여부

    def set_damage(self, damage):
        if self.hp > damage:
            self.hp -= damage
            self.isAlive = True
        else:
            self.isAlive = False

    def is_alive(self):
        return self.isAlive

class Character(Unit):  # Unit을 상속받아 캐릭터 클래스를 만듬
    def __init__(self, pp, mp, ph, mh, hp, um, job):
        super().__init__(pp, mp, ph, mh, hp)  # 부모의 생성자 호출
        self.ultimate = um  # 궁극기 특성 추가
        self.job = job  # 직업 추가

    def p_attack(self):  # 물리 공격
        return self.pPower * self.pHit

    def m_attack(self):  # 마법 공격
        return self.mPower * self.mHit

    def attack_ultra(self):  # 궁극기
        return self.ultimate

# 스레드에서 실행할 함수
def wizard_th():
    print(f"{wizard.job}가 전투 준비를 완료 했습니다.")
    time.sleep(1)
    while True:
        time.sleep(5)
        if not warrior.is_alive() or not wizard.is_alive():
            break
        perform_attack(wizard, warrior)

def perform_attack(attacker, defender):
    val = random.choice(["physical", "magical"])
    ul = random.randrange(0, 18)

    if val == "physical":
        damage = attacker.p_attack()
        print(f"{blue('물리공격')} >> {defender.job}에게 {yellow(f'{damage:.2f}')} 데미지를 입혔습니다.")
    else:
        damage = attacker.m_attack()
        print(f"{yellow('마법공격')} >> {defender.job}에게 {yellow(f'{damage:.2f}')} 데미지를 입혔습니다.")

    defender.set_damage(damage)
    print_status(defender)

    if ul == 1:
        damage = attacker.attack_ultra()
        print(f"{red('궁극기 발동')} >> {defender.job}에게 {red(f'{damage:.2f}')} 데미지를 입혔습니다.")
        defender.set_damage(damage)
        print_status(defender)

def print_status(character):
    if character.is_alive():
        print(f"남아 있는 {green(character.job)}의 체력은 {blue(f'{character.hp:.2f}')} 입니다.")
    else:
        print(f"{green(character.job)}가 죽었습니다. 게임을 종료 합니다.")

# 메인 영역
if __name__ == "__main__":  # main thread 흐름을 타는 시작점

    name1 = input("전사는 강력한 체력의 물리공격형 캐릭터 (이름 입력) : ")
    name2 = input("마법사는 강력한 마법 공격형 캐릭터 (이름 입력) : ")

    warrior = Character(8, 2, 0.8, 0.5, 150, 40, name1)  # 물공,마공, 물방, 마방, 물적,마적,체력,궁극기
    wizard = Character(2, 20, 0.5, 0.9, 60, 55, name2)  # 물공,마공, 물방, 마방, 물적,마적,체력,궁극기

    x = threading.Thread(target=wizard_th)
    print(f"{warrior.job}가 전투 준비를 완료 했습니다.")
    time.sleep(1)
    x.start()  # 서브 스레드 시작

    while True:
        time.sleep(5)
        if not warrior.is_alive() or not wizard.is_alive():
            break
        perform_attack(warrior, wizard)