import random
import time

# Player class merge, test file

class Character:
    def __init__(self, name):
        self._name = name
        self._current_hp = 100
        self._max_hp = 100
        self._power = 10
        self._level = 1
        self._max_level = 3
        self._is_alive = True

    def show_status(self):
        print(f"{self._name}의 상태창")
        print(f"HP : {self._current_hp} / {self._max_hp}")

    # 일반 공격할 때 쓰는 함수
    def attack(self):
        # 플레이어/몬스터가 일반공격 시도 (레벨 1:85%/ 레벨2: 90%/ 레벨3: 95% 확률로 공격 성공, 레벨별 5%/10%/15% 확률로 공격 대성공(원래 데미지에 1.5배 큼))        
        print(f'{self._name}이(가) 공격을 시도합니다.')
        level_luck = (self._max_level - self._level + 1) * 0.05
        if random.random() > level_luck:
            is_critical = True if random.random() < self._level * 0.05 else False
            if is_critical():
                print(f'{self._name}이(가) 공격에 대성공하였습니다!')
            else:
                print(f'{self._name}이(가) 공격에 성공하였습니다!')
            
            damage_ = random.randint(int(self._power * 0.8), int(self._power * 1.2))
            damage = damage_ if not is_critical else int(damage_ * 1.5)
            return [True, False, damage]
        return [False]

    # 공격 받았을 때 쓰는 함수
    def attacked(self, attack_info):
        if attack_info[0]:
            print(
                f"{self._name}이(가) {attack_info[1]}의 데미지를 입었습니다.")
            if self._current_hp < 0:
                print(f'{self._name}이(가) 죽었습니다.')
                self._is_alive = False                
        else:
            print(f"{self._name}이(가) 공격을 회피했습니다.")
        return self._is_alive

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
            gold_ = (self._max_level - self._level + 1) * 15 # 경험치는 레벨 비례로 덜 얻게 했는데 골드 기준 생각해보기 아니면 반대로 랭크 높은곳가면 골드많이
            self._gold += random.randint(int(gold_*0.7), int(gold_*1.3))
            print(f'{self._gold}골드를 획득하였습니다! 현재 골드: {self._gold}')

        #어택인포 1. 공격성공했는지, 2. 광역공격인지, 3. 데미지

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
            f"Level UP! 현재 스텟 - 파워:{self._power} 체력:{self._current_hp} 마법파워:{self._magic_power}, 맥스체력:{self._max_hp}")


#======Knight, Thief class 추후 추가해주세요=====

class Knight(Player):
    def __init__(self, name):
        super().__init__(name)
        self._strength_power = self._power * 2

    def level_up(self):
        level_up_info = 10
        self._current_hp += level_up_info * 10
        self._current_mp += level_up_info * 10
        self._power += level_up_info + 10
        self._strength_power += level_up_info + 30
        print(
            f"Level UP! 현재 스텟 - power:{self._power} hp:{self._current_hp} strength_power:{self._strength_power}") 
        
    # 플레이어가 몬스터를 공격할 때 들어가는 함수
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
        level_up_info = 10
        self._current_hp += level_up_info * 10
        self._current_mp += level_up_info * 10
        self._power += level_up_info + 10
        self._dexterity_power += level_up_info + 30
        print(
            f"Level UP! 현재 스텟 - power:{self._power} hp:{self._current_hp} dex_power:{self._dexterity_power}")


#=============게임 스토리 소개====================
# """


# 용감한 모험가 여러분, 신비로운 엘다리아 왕국에 오신 것을 환영합니다!


# """
# time.sleep(0.3)

# """


# 마법에 걸린 땅에서 운명을 개척하는 모험을 떠나보세요. 백성들의 마지막 희망인 당신은 왕국을 위협하는 어둠의 세력으로부터 왕국을 지켜야 합니다!






# 용감한 모험가여, 엘다리아의 운명은 당신의 손에 달려있습니다. 빛이 여러분의 창대한 여정을 인도하길 바랍니다. 
# 여정을 시작하세요! 


# """
# time.sleep(0.3)


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


#============= 스탯 부여 함수 =============
def set_status():
    power = 0

    def func():
        _power = random.random()
        if _power < 0.05:
            _power = random.randint(23, 25)
        elif 0.05 < _power < 0.4:
            _power = random.randint(20, 22)
        else:
            _power = random.randint(15, 19)
        
        print(f"\033[0m현재 당신의 스탯은 \033[1m{_power}\033[0m 입니다. (15 ~ 25)")
        return(_power)
    
    (power) = func()



    answer_list = ["y", "yes", "n", "no"]

    while True:
        if answer == "n" or answer == "no":
            break

        if answer not in answer_list:
            print("입력이 잘못 되었습니다.")
            answer = input("스탯을 다시 부여받으시겠습니까? (y/n)\n").lower()

        else:
            (power) = func()
            answer = input("스탯을 다시 부여받으시겠습니까? (y/n)\n").lower()

    return(power)


#============= 스탯 부여 실행코드 =============
(power) = set_status() # 플레이어만 파워설정 되도록
