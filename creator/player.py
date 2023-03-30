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
    
    # 플레이어가 몬스터에게 일반 공격할 때 들어가는 함수
    def attack(self):
        return super().attack()

    def get_exp(self, is_alive):
        # is_alive에 바로 직전 attacked() 함수에서 생사여부 값이 반환됨. 살았으면 True -> pass, 죽었으면 False -> 경험치 얻기
        if is_alive:
            pass
        else:
            if self._exp >= self._exp_limit:  # exp_limit달성 시 level_up함수 호출
                self.level_up()
            exp_ = (self._max_level - self._level + 1) * 15
            self._exp += random.randint(int(exp_*0.8), int(exp_*1.2))
            print(f'{self._exp}포인트를 획득하였습니다! 현재 경험치: {self._exp}/{self._exp_limit}')

    def get_gold(self, is_alive):
        # is_alive에 바로 직전 attacked() 함수에서 생사여부 값이 반환됨. 살았으면 True -> pass, 죽었으면 False -> 골드 얻기
        if is_alive:
            pass
        else:
            gold_ = (self._max_level - self._level + 1) * 15 # 경험치는 레벨 비례로 덜 얻게 했는데 골드 기준 생각해보기
            self._gold += random.randint(int(gold_*0.7), int(gold_*1.3))
            print(f'{self._gold}골드를 획득하였습니다! 현재 골드: {self._gold}')


    def level_up(self):
        level_up_info = 10
        self._max_hp += level_up_info * 10
        self._max_mp += level_up_info * 10
        self._current_mp = self._max_mp  # current_hp에 max_hp값 할당,체력회복
        self._current_hp = self._max_hp
        self._power += level_up_info + 10
        self._exp = 0  # 경험치 초기화
        self._level += 1  # 플레이어 레벨 상승


#===========Magician class======== 

class Magician(Player):
    def __init__(self, name):
        super().__init__(name) 
        self._magic_power = self._power * 2

    def level_up(self): #level_up 메소드 오버라이딩 
        super().level_up()
        level_up_info = 10
        self._magic_power += level_up_info + 30
        print(
            f"Level UP! 현재 스텟 - 파워:{self._power}, 마법파워:{self._magic_power}, 체력:{self._current_hp}, 맥스체력:{self._max_hp}")


#======Knight, Thief class 추후 추가해주세요=====

class Knight(Player):
    def __init__(self, name):
        super().__init__(name)
        self._strength_power = self._power * 2

    def level_up(self):  # super로 메소드 호출하고, 추가기능만 오버라이딩
        super().level_up()
        level_up_info = 10
        self._strength_power += level_up_info + 30
        print(
            f"Level UP! 현재 스텟 - 파워:{self._power} 체력:{self._current_hp}, 맥스체력:{self._max_hp}, 전사파워:{self._strength_power}, ") 
    
    # 전사 플레이어가 몬스터를 공격할 때 들어가는 함수
    def attack(self):
        attack_type = str(input("공격 유형을 선택해주십시오. 1:일반공격, 2:특수공격: "))               
        if attack_type == '1':
            return super().attack()
        elif attack_type == '2':
            attack_type2 = str(input("공격 유형을 선택해주십시오. 1:광역공격, 2:타겟공격: ")) 
            if random.random() > 0.01:
                print(f'{self._name}의 차원 가르기!!!!!')      
                skill_damage = random.randint(int(self._strength_power * 0.8), int(self._strength_power * 1.2))
                if attack_type2 == '1':
                    return [True, True, skill_damage]
                elif attack_type2 == '2':
                    return [True, False, skill_damage]
            else:
                return [False]

class Thief(Player):
    def __init__(self, name): 
        super().__init__(name)
        self._dexterity_power = self._power * 2

    def level_up(self):
        super().level_up()
        level_up_info = 10
        self._dexterity_power += level_up_info + 30
        print(
            f"Level UP! 현재 스텟 - power:{self._power} hp:{self._current_hp} dex_power:{self._dexterity_power}")



def create_player():
    #=============캐릭터 입력 값으로 객체 생성========== 
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
        "1" : Magician(player_name),
        "2" : Knight(player_name),
        "3" : Thief(player_name)
    }
    career_list = {
        "1" : "마법사",
        "2" : "전사",
        "3" : "도적"
    }
    career_skill = { 
        "1" : "메테오", # meteor
        "2" : "차원가르기", #demension_slicing
        "3" : "세비지 블로우" # savage_blow
    }

    player_obj = career_dict[player_career]
    print(
        f"""
    ***플레이어가 생성되었습니다!*** 

    이름: {player_obj._name} / 직업: {career_list[player_career]}

    체력: {player_obj._max_hp} / 특수스킬: {career_skill[player_career]} 
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
    