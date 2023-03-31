import random

from creator.character import Character


class Monster(Character):
    def __init__(self, name, rank, skill):
        super().__init__(name)
        self._level = rank
        self._rank = rank
        self._skill = skill
        self._is_alive = True

        if self._rank == 1:
            random_value = random.randint(60, 80)
            self._current_hp = random_value
            self._max_hp = random_value
            self._power = random.randint(8, 15)
        elif self._rank == 2:
            random_value = random.randint(80, 100)
            self._current_hp = random_value
            self._max_hp = random_value
            self._power = random.randint(15, 25)
        else:
            random_value = random.randint(100, 200)
            self._current_hp = random_value
            self._max_hp = random_value
            self._power = random.randint(25, 35)

    def show_skill(self):
        print(f"[{self._name}]몬스터가 [{self._skill}] 스킬을 사용했습니다.")

    def show_status(self):
        print(f"{self._name}의 상태\nHP {self._current_hp}")

    def change_status(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, f"_{key}", value)

    def get_status(self, *args):
        return [getattr(self, f"_{arg}") for arg in args]


dict_monster_rank1 = {
    "1": Monster("좀비", 1, "저주"), "2": Monster("구울", 1, "광신"), "3": Monster("황혼의 유령", 1, "축복받은 조준"),
    "4": Monster("가시 마귀", 1, "가시폭풍"), "5": Monster("가시 야수", 1, "서슬퍼런 칼날"), "6": Monster("서슬 가시", 1, "위세"),
    "7": Monster("가시 박쥐", 1, "맹공"), "8": Monster("어둠의 사냥꾼", 1, "암흑 화살")
}
dict_monster_rank2 = {
    "1": Monster("미라", 2, "암흑 최면"), "2": Monster("발굴된 시체", 2, "독"), "3": Monster("망자", 2, "암흑 주술"),
    "4": Monster("카데바", 2, "감염"), "5": Monster("지네", 2, "근접"), "6": Monster("모래 구더기", 2, "스톤 스킨")
}
dict_monster_rank3 = {
    "1": Monster("거대 거미", 3, "멀티플 샷"), "2": Monster("저승 꼭두각시", 3, "순간 이동"), "3": Monster("황혼의 영혼", 3, "암흑 혼령")
}
