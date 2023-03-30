import random

from creator.character import Character

class Monster:
    def __init__(self, name,rank, skill):
        self._name = name
        self._rank = rank
        self._skill = skill
        self._is_alive = True

        if self._rank == 1:
            self._hp = random.randint(60,80)
            self._power = random.randint(8,15)
        elif self._rank == 2:
            self._hp = random.randint(80,100)
            self._power = random.randint(15, 25)
        else:
            self._hp = random.randint(100,200)
            self._power = random.randint(25,35)

    def show_skill(self):
        print(f"[{self._name}]몬스터가 [{self._skill}] 스킬을 사용했습니다.")

    def show_status(self):
        print(f"{self._name}의 상태\nHP {self._hp}")

# 공격 받았을 때 쓰는 함수
    def attacked(self, attack_info: list):
        # attack_info = (is_attacked, damage)
        if attack_info[0]:
            print(
                f"{self._name}이(가) {attack_info[1]}의 데미지를 입었습니다.")
            self.change_hp(attack_info[1])

        else:
            print(f"{self._name}이(가) 공격을 회피했습니다.")
            self.change_hp()

    # 전투 메소드
    def attack(self):
        print(f"{self._name}이(가) 일반 공격을 시도합니다.")

        if random.random() > 0.1:
            is_critical = True if random.random() < 0.1 else False
            if is_critical:
                print(f"{self._name}이(가) 일반 공격에 대성공했습니다!")
            else:
                print(f"{self._name}이(가) 일반 공격에 성공했습니다!")
            damage = self._power + random.randint(0, 3) if not is_critical else round(
                (self._power + random.randint(0, 3)) * 1.5)

            return [True, damage]

        else:
            return [False]

    def change_hp(self, damage=-1):
        if not damage == -1:
            self._hp -= damage

            if self._hp < 0:
                self._hp = 0
            self._is_alive = True if self._hp > 0 else False
            self.show_hp()

        else:
            self.show_hp()

    def get_status(self, *args):
        # 배열로 반환하도록 수정
        for arg in args:
            if arg == "name":
                return self._name
            elif arg == "rank":
                return self._rank
            elif arg == "hp":
                return self._hp
            elif arg == "alive":
                return self._is_alive


dict_monster_rank1 = {
    "1": Monster("좀비", 1, "저주"), "2": Monster("구울", 1, "광신"), "3": Monster("가시 쥐", 1, "축복받은 조준"),
    "4": Monster("가시 마귀", 1, "신성한 번개"), "5": Monster("가시 야수", 1, "신성한 불꽃"), "6": Monster("서슬 가시", 1, "위세"),
    "7": Monster("설인", 1, "냉기 강화"), "8": Monster("어둠의 사냥꾼", 1, "암흑 화살")
}

dict_monster_rank2 = {
    "1" : Monster("미라", 2,"메테오"), "2" : Monster("메마른 시체",2,"세비지 블로우"), "3" : Monster("망자", 2,"암흑 주술"),
    "4" : Monster("수호자", 2,"신성한 불꽃"),"5" : Monster("사브르 고양이", 2,"다발 사격"), "6" : Monster("모래 구더기",2,"스톤 스킨")
}

dict_monster_rank3 = {
    "1" : Monster("거대 거미", 3,"멀티플 샷"),"2" : Monster("저승 꼭두각시", 3,"순간 이동"), "3" : Monster("황혼의 영혼", 3,"암흑 혼령")
}

dict_monster_rank1["1"].show_skill()
dict_monster_rank1["1"].show_status()
dict_monster_rank3["1"].attack()
dict_monster_rank1["1"].show_status()
