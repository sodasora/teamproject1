import random


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
        print(f"{self._name}의 상태\nHP {self.current_hp}/{self.max_hp}")

    def attack(self):
        """ 공격할 때 쓰는 함수
        
        플레이어/몬스터가 일반공격 시도
        (레벨 1:85%/ 레벨2: 90%/ 레벨3: 95% 확률로 공격 성공, 레벨별 5%/10%/15% 확률로 공격 대성공(원래 데미지에 1.5배 큼))
        """
        print(f'{self._name}의 공격!!!')
        level_luck = (self._max_level - self._level + 1) * 0.05
        if random.random() > level_luck:
            is_critical = True if random.random() < self._level * 0.05 else False
            damage_ = random.randint(
                int(self._power * 0.8), int(self._power * 1.2))
            damage = damage_ if not is_critical else int(damage_ * 1.5)
            return [True, False, damage, is_critical]
        return [False, False, 0, False]

    def attacked(self, attack_info: list):
        """공격 받았을 때 쓰는 함수

        attack_info (list): [is_attack_success, is_area_attack, damage, is_critical]
            
        공격정보 (list): [공격 성공 여부, 전부공격(T)/타겟공격(F), 데미지, 기습공격 여부]
        """
        if self._is_alive:
            if attack_info[0]:
                if attack_info[3]:
                    print(
                        f"{self._name}이(가) 기습 공격을 당해 {attack_info[2]}의 데미지를 입었습니다.")
                else:
                    print(
                        f"{self._name}이(가) {attack_info[2]}의 데미지를 입었습니다.")
                self.change_hp(attack_info[2])

            else:
                print(f"{self._name}이(가) 공격을 회피했습니다.")
                self.change_hp()

    def change_hp(self, damage=-1):
        if not damage == -1:
            self._current_hp -= damage
            if self._current_hp < 0:
                self._current_hp = 0

            self._is_alive = True if self._current_hp > 0 else False
            self.show_hp()
        else:
            self.show_hp()

    def show_hp(self):
        print(f"{self._name}의 남은 HP : {self._current_hp}/{self._max_hp}\n")
