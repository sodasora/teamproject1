import random

from creator.character import Character


class Monster(Character):
    # 몬스터도 랭크 말고 레벨로 변수명 똑같이 하는 거 어떨까요? 캐릭터클래스에 일반공격을 넣어놨는데 레벨(랭크)에 따라 공격성공률이 다르게 설정해가지구요..!! -민정
    def __init__(self, name, rank, skill):
        super().__init__(name)
        # self._name = name     <- 몬스터도 캐릭터 클래스를 상속받음 - 민정
        self._level = rank
        self._rank = rank
        self._skill = skill
        self._is_alive = True

        if self._rank == 1:
            self._current_hp = random.randint(60, 80)
            self._power = random.randint(8, 15)
        elif self._rank == 2:
            self._current_hp = random.randint(80, 100)
            self._power = random.randint(15, 25)
        else:
            self._current_hp = random.randint(100, 200)
            self._power = random.randint(25, 35)

    def show_skill(self):
        print(f"[{self._name}]몬스터가 [{self._skill}] 스킬을 사용했습니다.")

    def show_status(self):
        print(f"{self._name}의 상태\nHP {self._current_hp}")

# # 공격 받았을 때 쓰는 함수    <-캐릭터 클래스에 정의되어 있는데
#     def attacked(self, attack_info: list):
#         # attack_info = (is_attacked, damage)
#         if attack_info[0]:
#             print(
#                 f"{self._name}이(가) {attack_info[1]}의 데미지를 입었습니다.")
#             self.change_hp(attack_info[1])

#         else:
#             print(f"{self._name}이(가) 공격을 회피했습니다.")
#             self.change_hp()

    # 몬스터가 플레이어한테 일반 공격할 때 들어가는 함수
    # ❌ def attack(self):
    # ❌    return super().attack()

    def change_status(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, f"_{key}", value)

    def get_status(self, *args):
        return [getattr(self, f"_{arg}") for arg in args]
