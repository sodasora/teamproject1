import random
import time

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
        print(f"HP : {self.current_hp} / {self.max_hp}")

    # 공격할 때 쓰는 함수
    def nomal_attack(self):
        # 플레이어가 일반공격 시도 (레벨 1:85%/ 레벨2: 90%/ 레벨3: 95% 확률로 공격 성공, 레벨별 5%/10%/15% 확률로 공격 대성공(원래 데미지에 1.5배 큼))        
        print(f'{self._name}님이 일반 공격을 시도합니다.')
        level_luck = (self._max_level - self._level + 1) * 0.05
        if random.random() > level_luck:
            is_critical = True if random.random() < self._level * 0.05 else False
            if is_critical():
                print(f'{self._name}님이 일반 공격에 대성공하였습니다!')
            else:
                print(f'{self._name}님이 일반 공격에 성공하였습니다!')
            
            damage_ = random.randint(int(self._power * 0.8), int(self._power * 1.2))
            damage = damage_ if not is_critical else int(damage_ * 1.5)
            return [True, damage]
        return [False]

    # 공격 받았을 때 쓰는 함수
    def nomal_attacked(self, nomal_attack_info):
        if nomal_attack_info[0]:
            print(
                f"{self._name}이(가) {nomal_attack_info[1]}의 데미지를 입었습니다.")
            if self._current_hp < 0:
                print(f'{self._name}이(가) 죽었습니다.')
                self._is_alive = False                
        else:
            print(f"{self._name}이(가) 공격을 회피했습니다.")
        return self._is_alive

class Player(Character):
    def __init__(self, name):
        super.__init__(name)
        self._current_mp = 100
        self._max_mp = 100
        self._exp = 0
        self._exp_limit = 100
        self._gold = 0

    def show_status(self):
        super().show_status()
        print(f"MP : {self.current_mp} / {self.max_mp}")

    def get_exp(self, is_alive):
        # is_alive에 바로 직전 attacked() 함수에서 생사여부 값이 반환됨. 살았으면 True -> pass, 죽었으면 False -> 경험치 얻기
        if is_alive:
            pass
        else:
            exp_ = (self._max_level - self._level + 1) * 15
            self._exp = random.randint(int(exp_*0.8), int(exp_*1.2))
            print(f'{self._exp}포인트를 획득하였습니다! 현재 경험치: {self._exp}/{self._exp_limit}')

        #어택인포 1. 공격성공했는지, 2. 광역공격인지, 3. 데미지



        # 플레이어 클래스에 get_exp() 함수 정의했습니다 - 민정
        #몬스터 처치 후 경험치 획득 / 경험치 limit달성 시 level_up 함수 호출
        #if 몬스터 체력 == 0:
            #self._exp += random.randint(30, 40)
            #print(f"경험치를 획득하였습니다! 획득한 경험치: {self._exp}")
            #if self._exp >= 100:
                #self.level_up()


    def level_up(self):
        pass # 여기는 pass로 놔두고 각 클래스에서 level_up 메소드 오버라이딩 해주시면 될 것 같습니다.

    # show_status(self)함수 캐릭터 클래스랑 플레이어 클래스에 정의했습니다 - 민정
    # def show_status(self):
    #     print(f"{self._name}의 상태창")
    #     print(f"HP : {self._current_hp} / {self._max_hp}")
    #     print(f"MP : {self._current_mp} / {self._max_mp}")  

#===========Magician class======== 

class Magician(Player):
    def __init__(self, name):
        Player.__init__(self, name) #부모(플레이어)의 부모(캐릭터)클래스 인잇은 안 해도 되는걸까요...? 부모(플레이어)클래스에 조부모(캐릭터) 인잇값이 들어갔으니 굳이인가요?! 일단 전사클래스엔 넣긴 했는데 넣는 게 맞는지 안 넣는 게 맞는지 모르겠어요...!! -민정
        self._magic_power = self._power * 2

    def level_up(self):
        level_up_info = 10
        self._current_hp += level_up_info * 10
        self._current_mp += level_up_info * 10
        self._power += level_up_info + 10
        self._magic_power += level_up_info + 30
        print(
            f"Level UP! 현재 스텟 - power:{self._power} hp:{self._current_hp} magic_power:{self._magic_power}")


#======Knight, Thief class 추후 추가해주세요=====

class Knight(Player):
    def __init__(self, name):
        Character.__init__(self, name)
        Player.__init__(self, name)
        self._strength_power = self._power * 2

    def level_up(self):
        level_up_info = 10
        self._current_hp += level_up_info * 10
        self._current_mp += level_up_info * 10
        self._power += level_up_info + 10
        self._strength_power += level_up_info + 30
        print(
            f"Level UP! 현재 스텟 - power:{self._power} hp:{self._current_hp} magic_power:{self._strength_power}") # magic strength로

class Thief(Player):
    def __init__(self, name): #name제외 삭제해도 될 것 같습니다~! 
        Character.__init__(self, name)
        Player.__init__(self, name)
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
"""


용감한 모험가 여러분, 신비로운 엘다리아 왕국에 오신 것을 환영합니다!


"""
time.sleep(0.3)

"""


마법에 걸린 땅에서 운명을 개척하는 모험을 떠나보세요. 백성들의 마지막 희망인 당신은 왕국을 위협하는 어둠의 세력으로부터 왕국을 지켜야 합니다!






용감한 모험가여, 엘다리아의 운명은 당신의 손에 달려있습니다. 빛이 여러분의 창대한 여정을 인도하길 바랍니다. 
여정을 시작하세요! 


"""
time.sleep(0.3)


#=============캐릭터 입력 값으로 객체 생성========== 
player_name = input("플레이어 이름을 입력해주세요: ")
player_career = input("""\n직업을 선택해주세요. (1~3)
1. 마법사 2. 전사 3. 도적 
""")
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
    "1" : "메테오", 
    "2" : "차원가르기", 
    "3" : "세비지 블로우" 
}

player_obj = career_dict[player_career]
print(f"플레이어가 생성되었습니다! 이름: {player_obj._name} 직업: {career_list[player_career]} 특수스킬: {career_skill[player_career]}")