import random
import time

from creator.character import Character


class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self._current_mp = 100
        self._max_mp = 100
        self._exp = 0
        self._exp_limit = 100
        self._gold = 0

    def show_status(self):
        super().show_status()
        print(f"MP : {self._current_mp} / {self._max_mp}")

    def show_hp(self):
        if self._current_hp == 0:
            print(f"{self._name}이(가) 사망했습니다.")
        else:
            print(f"{self._name}의 남은 HP : {self._current_hp}/{self._max_hp}")
            self.show_mp()

    def change_mp(self, value: int):
        self._current_mp -= value

    def show_mp(self):
        print(f"{self._name}의 남은 MP : {self._current_mp}/{self._max_mp}")

    def level_up(self):
        level_up_info = 10
        self._max_hp += level_up_info * 10
        self._max_mp += level_up_info * 10
        self._current_mp = self._max_mp  # current_hp에 max_hp값 할당,체력회복
        self._current_hp = self._max_hp
        self._power += level_up_info + 10
        self._exp = 0  # 경험치 초기화
        self._level += 1  # 플레이어 레벨 상승

    def change_status(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, f"_{key}", value)

    def get_status(self, *args):
        args_list = [getattr(self, f"_{arg}") for arg in args]
        return args_list


# ===========Magician class========

class Magician(Player):
    def __init__(self, name):
        super().__init__(name)
        self._magic_power = self._power * 2

    def level_up(self):  # level_up 메소드 오버라이딩
        super().level_up()
        level_up_info = 10
        self._magic_power += level_up_info + 30
        print(
            f"""
                    *** Level UP! 현재 스텟 ***
                이름    : {self._name}
                경험치  : {self._exp}/{self._exp_limit}
                HP      : {self._current_hp}/{self._max_hp}
                MP      : {self._current_mp}/{self._max_mp}
                골드    : {self._gold}
                    """)

    # 마법사 플레이어가 몬스터를 공격할 때 들어가는 함수
    def attack(self):
        while True:
            attack_type = str(input("공격 유형을 선택해주십시오. 1:일반공격, 2:특수공격: "))
            if attack_type != '1' and attack_type != '2':
                print("잘못된 입력입니다. 1 또는 2를 입력하세요")
            else:
                break
        if attack_type == '1':
            return super().attack()
        elif attack_type == '2':
            if self._current_mp > 20:
                while True:
                    attack_type2 = str(
                        input("\n공격 대상을 선택해주십시오. 1:전부 공격하기, 2:타겟몬스터 고르기: "))
                    if attack_type2 != '1' and attack_type2 != '2':
                        print("잘못된 입력입니다. 1 또는 2를 입력하세요")
                    else:
                        break
                self._current_mp = max(self._current_mp-20, 0)
                if random.random() > 0.01:
                    print(f'{self._name}의 메테오!!!!!')
                    skill_damage = random.randint(
                        int(self._magic_power * 0.8), int(self._magic_power * 1.2))
                    if attack_type2 == '1':
                        return [True, True, skill_damage, False]
                    elif attack_type2 == '2':
                        return [True, False, skill_damage, False]
                else:
                    return [False, False, 0, False]  # 이부분 [false false 0]으로
            else:
                print("MP가 부족합니다. 일반공격을 시도합니다.")
                return super().attack()

# ======Knight, Thief class 추후 추가해주세요=====


class Knight(Player):
    def __init__(self, name):
        super().__init__(name)
        self._strength_power = self._power * 2

    def level_up(self):  # super로 메소드 호출하고, 추가기능만 오버라이딩
        super().level_up()
        level_up_info = 10
        self._strength_power += level_up_info + 30
        print(
            f"""
                    *** Level UP! 현재 스텟 ***
                이름    : {self._name}
                경험치  : {self._exp}/{self._exp_limit}
                HP      : {self._current_hp}/{self._max_hp}
                MP      : {self._current_mp}/{self._max_mp}
                골드    : {self._gold}
                    """)

    # 전사 플레이어가 몬스터를 공격할 때 들어가는 함수
    def attack(self):
        while True:
            attack_type = str(input("공격 유형을 선택해주십시오. 1:일반공격, 2:특수공격: "))
            if attack_type != '1' and attack_type != '2':
                print("잘못된 입력입니다. 1 또는 2를 입력하세요")
            else:
                break
        if attack_type == '1':
            return super().attack()
        elif attack_type == '2':
            if self._current_mp > 20:
                while True:
                    attack_type2 = str(
                        input("\n공격 대상을 선택해주십시오. 1:전부 공격하기, 2:타겟몬스터 고르기: "))
                    if attack_type2 != '1' and attack_type2 != '2':
                        print("잘못된 입력입니다. 1 또는 2를 입력하세요")
                    else:
                        break
                self._current_mp = max(self._current_mp-20, 0)
                if random.random() > 0.01:
                    print(f'{self._name}의 차원 가르기!!!!!')
                    skill_damage = random.randint(
                        int(self._strength_power * 0.8), int(self._strength_power * 1.2))
                    if attack_type2 == '1':
                        return [True, True, skill_damage, False]
                    elif attack_type2 == '2':
                        return [True, False, skill_damage, False]
                else:
                    return [False, False, 0, False]  # 이부분 [false false 0]으로
            else:
                print("MP가 부족합니다. 일반공격을 시도합니다.")
                return super().attack()


class Thief(Player):
    def __init__(self, name):
        super().__init__(name)
        self._dexterity_power = self._power * 2

    def level_up(self):
        super().level_up()
        level_up_info = 10
        self._dexterity_power += level_up_info + 30
        print(
            f"""
                    *** Level UP! 현재 스텟 ***
                이름    : {self._name}
                경험치  : {self._exp}/{self._exp_limit}
                HP      : {self._current_hp}/{self._max_hp}
                MP      : {self._current_mp}/{self._max_mp}
                골드    : {self._gold}
                    """)

    # 도적 플레이어가 몬스터를 공격할 때 들어가는 함수
    def attack(self):
        while True:
            attack_type = str(input("공격 유형을 선택해주십시오. 1:일반공격, 2:특수공격: "))
            if attack_type != '1' and attack_type != '2':
                print("잘못된 입력입니다. 1 또는 2를 입력하세요")
            else:
                break
        if attack_type == '1':
            return super().attack()
        elif attack_type == '2':
            if self._current_mp > 20:
                while True:
                    attack_type2 = str(
                        input("\n공격 대상을 선택해주십시오. 1:전부 공격하기, 2:타겟몬스터 고르기: "))
                    if attack_type2 != '1' and attack_type2 != '2':
                        print("잘못된 입력입니다. 1 또는 2를 입력하세요")
                    else:
                        break
                self._current_mp = max(self._current_mp-20, 0)
                if random.random() > 0.01:
                    print(f'{self._name}의 쌔비지 블로우!!!!!')
                    skill_damage = random.randint(
                        int(self._dexterity_power * 0.8), int(self._dexterity_power * 1.2))
                    if attack_type2 == '1':
                        return [True, True, skill_damage, False]
                    elif attack_type2 == '2':
                        return [True, False, skill_damage, False]
                else:
                    return [False, False, 0, False]  # 이부분 [false false 0]으로
            else:
                print("MP가 부족합니다. 일반공격을 시도합니다.")
                return super().attack()

    # 도적의 공격 피하기 스킬 (전사는 레벨업할수록 hp 더 커지고, 마법사는 mp 더 커지고, 도적은 회피율 증가)

    def attacked(self, attack_info: list):
        # attack_info = [is_attack_success, is_area_attack, damage, is_critical]
        luck = self._dexterity_power * 0.008
        half_damage = int(attack_info[2] / 2)
        if attack_info[0]:
            if random.random() < luck:
                print(
                    f"{self._name}이(가) 몬스터의 공격을 살짝 피해 원래 데미지({attack_info[2]})의 절반인 {half_damage} 데미지만 입었습니다.")
                self.change_hp(half_damage)
            else:
                print(
                    f"{self._name}이(가) {attack_info[2]}의 데미지를 입었습니다.")
                self.change_hp(attack_info[2])
        else:
            print(f"{self._name}이(가) 공격을 회피했습니다.")
            self.change_hp()


def create_player():
    # =============캐릭터 입력 값으로 객체 생성==========
    while True:
        player_name = input("플레이어 이름을 입력해주세요: ")
        if player_name.strip():
            break
        else:
            continue

    while True:
        player_career = input("""\n직업을 선택해주세요. (1~3)
1. 마법사 2. 전사 3. 도적 
""")
        if player_career != "1" and player_career != "2" and player_career != "3":
            print("잘못된 입력입니다. 1~3 사이 숫자를 입력하세요")
        else:
            break

    career_dict = {
        "1": Magician(player_name),
        "2": Knight(player_name),
        "3": Thief(player_name)
    }
    career_list = {
        "1": "마법사",
        "2": "전사",
        "3": "도적"
    }
    career_skill = {
        "1": "메테오",  # meteor
        "2": "차원가르기",  # demension_slicing
        "3": "쌔비지 블로우"  # savage_blow
    }

    player_obj = career_dict[player_career]
    print(
        f"""
    ***플레이어가 생성되었습니다!*** 

    이름: {player_obj._name} / 직업: {career_list[player_career]}

    체력: {player_obj._max_hp} / 마나: {player_obj._max_mp}
    
    특수스킬: {career_skill[player_career]} 
    """)
    return player_obj

# #============= 스탯 부여 함수 =============
# def set_status():
#     power = 0

#     def func():
#         _power = random.random()
#         if _power < 0.05:
#             _power = random.randint(23, 25)
#         elif 0.05 < _power < 0.4:
#             _power = random.randint(20, 22)
#         else:
#             _power = random.randint(15, 19)

#         print(f"\033[0m현재 당신의 스탯은 \033[1m{_power}\033[0m 입니다. (15 ~ 25)")
#         return(_power)

#     (power) = func()

#     while True:
#         answer = input("스탯을 다시 부여받으시겠습니까? (y/n)\n").lower()
#         if answer =="y":
#             power = func()
#         if answer == "n":
#             break
#         elif answer != "y" and answer != "n":
#             print("잘못된 입력입니다. y 또는 n을 입력하세요. ")

#     #============= 스탯 부여 실행코드 =============
#     (power) = set_status() # 플레이어만 파워설정 되도록
