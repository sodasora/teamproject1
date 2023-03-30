from time import sleep
import os
import sys
import random
# 사용자 정의 모듈
from creator.player import create_player, Player
from creator.monster import Monster
from scripts.script import *

intro()

player = create_player()

# welcome_player(me.get_status("name"))

# 몬스터 사전
monster_dict = [
    {
    1: Monster("좀비", 1, "저주"), 2: Monster("구울", 1, "광신"), 3: Monster("가시 쥐", 1, "축복받은 조준"),
    4: Monster("가시 마귀", 1, "신성한 번개"), 5: Monster("가시 야수", 1, "신성한 불꽃"), 6: Monster("서슬 가시", 1, "위세"),
    7: Monster("설인", 1, "냉기 강화"), 8: Monster("어둠의 사냥꾼", 1, "암흑 화살")
    },

    {
        1 : Monster("미라", 2,"메테오"), 2 : Monster("메마른 시체",2,"세비지 블로우"), 3 : Monster("망자", 2,"암흑 주술"),
        4 : Monster("수호자", 2,"신성한 불꽃"), 5 : Monster("사브르 고양이", 2,"다발 사격"), 6 : Monster("모래 구더기",2,"스톤 스킨")
    },

    {
        1 : Monster("거대 거미", 3,"멀티플 샷"),2 : Monster("저승 꼭두각시", 3,"순간 이동"), 3 : Monster("황혼의 영혼", 3,"암흑 혼령")
    }
    ]

game_exit = False
first_town_visit = True

while not game_exit:
    def in_town(player:Player, first_town_visit:bool):
        if first_town_visit:
            print("용사여! 마법의 세계 에테리아에 오신 것을 환영합니다.\n")
        else:
            print("...던전 탐색을 마치고 에테리아에 돌아왔다...\n")
        
        go_dungeon = False
        
        while not go_dungeon:
            dungeon_level = None
            answer_list = [1, 2]
            
            print("1. 상점 방문 2. 던전 탐색")
            answer = int(input("어디로 향하시겠습니까? : "))
            
            while answer not in answer_list:
                answer = int(input("\n입력이 잘못됐습니다. 어디로 향하시겠습니까? : "))
            
            while answer == 1:
                # ❌ 상점 구현
                print("\n상점을 방문했습니다.")    
                print("\n상점에서 나왔습니다.")
                break
            
            if answer == 2:
                dungeon_level_list = [1,2,3]
                
                print("\n던전을 탐색합니다. 던전은 총 세 종류입니다.")
                print("1. 초급 던전 2. 중급 던전 3. 상급 던전 ")
                dungeon_level = int(input("어디로 향하시겠습니까? : "))
                
                while dungeon_level not in dungeon_level_list:
                    print("\n입력이 잘못됐습니다.")
                    print("던전은 총 세 종류입니다.")
                    print("1. 초급 던전 2. 중급 던전 3. 상급 던전 ")
                    dungeon_level = int(input("어디로 향하시겠습니까? : "))
                
                if dungeon_level == 1:
                    print("초급 던전으로 향합니다.")
                elif dungeon_level == 2:
                    print("중급 던전으로 향합니다.")
                else:
                    print("상급 던전으로 향합니다.")
                
                go_dungeon = True
        
        return dungeon_level
    
    
    dungeon_level = in_town(player, first_town_visit)
    first_town_visit = False
    
    
    # def in_dungeon(player:Player, dungeon_level: int):
    #     return None
    # 1. 던전 진입
    is_in_dungeon = True
    while is_in_dungeon:
        
        # 2. 몬스터 생성
        def create_monster_list_with_name_list(_monster_dict:dict):
            def func(__monster_dict:dict, __monster_list:list, __monster_name_list:list, round:int):
                for _ in range(round):
                    length = len(__monster_dict)
                    monster_number = random.randint(1, length)
                    __monster_list.append(__monster_dict[monster_number])
                    __monster_name_list.append(__monster_dict[monster_number].get_status("name"))
            
            _monster_list = []
            _monster_name_list = []
            
            p = random.random()
            if p <0.4:
                func(_monster_dict, _monster_list, _monster_name_list, 1)
                   
            elif p < 0.8:
                func(_monster_dict, _monster_list, _monster_name_list, 2)
                  
            else:
                func(_monster_dict, _monster_list, _monster_name_list, 3)
                  
            
            return _monster_list, _monster_name_list
        
        
        selected_monster_dict = monster_dict[dungeon_level - 1]
        monster_list, monster_name_list = create_monster_list_with_name_list(selected_monster_dict)
        
        monster_name_string = ""
        for i, monster_name in enumerate(monster_name_list):
            monster_name_string += f"{i+1}. {monster_name} "
        
        print("몬스터가 나타났다!")
        print(f"{monster_name_string}", end="\n\n")
        
        # 3. 전투 여부 선택
        def is_battle_or_not():
            no_answer_check = False
            yes_answer_list = ["y", "yes"]
            no_answer_list = ["n", "no"]
            
            answer = input("전투하시겠습니까? (Y/N) : ").lower()
            print("")
            
            while answer not in yes_answer_list:
                if answer in no_answer_list:
                    if not no_answer_check:
                        no_answer_check = True
                        answer = input("정말로 도망치시겠습니까? (Y/N) : ").lower()
                        print("")
                        
                        if answer in yes_answer_list:
                            print("전투에서 비참하게 도망칩니다.")
                            return False
                        
                        elif answer in no_answer_list:
                            break
                        
                else:
                    if not no_answer_check:
                        answer = input("입력이 잘못됐습니다. 전투하시겠습니까? (Y/N) : ").lower()
                        print("")
                    else:
                        answer = input("입력이 잘못됐습니다. 정말로 도망치시겠습니까? (Y/N) : ")
                        print("")
                        
                        if answer in yes_answer_list:
                            print("전투에서 비참하게 도망칩니다.")
                            return False
                        
                        elif answer in no_answer_list:
                            break
                    
            print("전투에 돌입합니다!")
            return True
        
        
        is_battle = is_battle_or_not()
        
        # 4. 전투 돌입
        while is_battle:
            # 보상
            # rewards에는 몬스터가 죽을 때마다 reward가 append된다. reward = [exp, gold]
            rewards = []
            
            # 5. 플레이어가 공격
            # attack_info = [is_attack_success, is_area_attack, damage]
            attack_info = player.attack()
            
            # 6. 몬스터가 피격
            # 광역 공격일 때
            if attack_info[1]:
                for monster in monster_list:
                    monster.attacked(attack_info)
                    
            # 광역 공격 아닐 때
            else:
                def select_target(_monster_name_list:list):
                    for i, _monster_name in enumerate(_monster_name_list):
                        print(f"{i+1}. {_monster_name}", end=" ")
                    target = int(input("목표를 선택하세요 : ")) - 1
                    
                    # 유효한 입력인지 확인
                    while not _monster_name_list[target]:
                        target = int(input("입력이 잘못됐습니다. 목표를 선택하세요 : ")) - 1
                    
                    return target
                
                target = select_target(monster_name_list)
                
                monster_list[target].attacked(attack_info)
                
            # 7. 몬스터 생사확인
            for i, monster in enumerate(monster_list):
                monster_is_alive = monster.get_status("alive")
                if not monster_is_alive:
                    print(f"{monster_name_list[i]}을(를) 무찔렀습니다!")
                    monster_list.pop(i)
                    monster_name_list.pop(i)
                    
                    # 보상 누적
                    exp = 15 + round((dungeon_level*1.5) * 5)
                    gold = 10 + dungeon_level * 5 + random.randint(0,10)
                    reward = [exp, gold]
                    rewards.append(reward)

            if not monster_list:
                print("전투에서 승리했습니다.")
                # 보상 획득 및 전투 종료
                exp = 0
                gold = 0
                for reward in rewards:
                    exp += reward[0]
                    gold += reward[1]
                    
                player.change_status(gold=gold, exp=exp)
                print(f"보상으로 {gold} 골드와 {exp} 경험치를 얻었습니다.", end="\n\n")
                is_in_dungeon = False
                break
            
            # 8. 몬스터가 공격
            attack_info_list = []
            for monster in monster_list:
                attack_info = monster.attack()
                attack_info_list.append(attack_info)
            
            # 9. 플레이어가 피격
            for attack_info in attack_info_list:
                player.attacked(attack_info)
            
            # 10. 플레이어 생사 확인
            player_is_alive = player.get_status("alive")
            if not player_is_alive:
                print("사망했습니다. 게임이 종료됩니다.")
                game_exit = True
                
            


