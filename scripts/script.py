from time import sleep
import os


def intro():
    # =============게임 스토리 소개====================
    # os.system('clear')  # for linux, mac
    os.system('cls') # for window
    str1 = "용감한 모험가 여러분, 신비로운 에테리아 왕국에 오신 것을 환영합니다!"
    str2 = "마법에 걸린 땅에서 운명을 개척하는 모험을 떠나보세요. 백성들의 마지막 희망인 당신은 왕국을 위협하는 어둠의 세력으로부터 왕국을 지켜야 합니다!"
    str3 = "용감한 모험가여, 에테리아의 운명은 당신의 손에 달려있습니다. 빛이 여러분의 창대한 여정을 인도하길 바랍니다. 여정을 시작하세요!"
    strs = [str1, str2, str3]

    for str in strs:
        print(str)
        print("")
        sleep(2)


def dungeon_script_level1():  # dungeon_script_leveln()
    str1 = "에테리아의 비밀의 숲은 어둠에게 가로 막혔습니다."
    str2 = "이제 이 곳에서는 어둠의 세력에게 쫓겨난 [유령], [좀비], [구울], [야수], [마귀]가 등장합니다! "
    str3 = "당신은 왕국을 지키기 위해 이 끝없는 숲 속으로 모험을 떠나야 합니다. "
    str4 = "주변의 자연을 이용하여, 몬스터 공격을 피해서 승리해야 합니다!"
    strs = [str1, str2, str3, str4]

    for str in strs:
        print(str)
        print("")
        sleep(2)
    # print("모험가여 승리 하셨군요! 축하드립니다. 하지만 방금 당신이 상대한 몬스터들은 어둠의 세력에게 쫓겨난, 비교적 약한 몬스터들입니다. ")
    # print("2단계 몬스터들과 전투 할 준비가 되셨다면 말을 걸어주세요..")


def dungeon_script_level2():
    str1 = ("늪지대로 이동합니다 . . .")
    str2 = ("늪지대 근처에는 에테리아 왕국의 주민들은 얼씬도 하지 않는 곳입니다. ")
    str3 = ("그 곳에선 망자와 미라들이 당신을 기다리고 있을 겁니다. ")
    str4 = ("하지만 당신은 왕국을 지켜야하는 모험가이자 운명의 주인공임을 잊지 마세요! ")
    strs = [str1, str2, str3, str4]

    for str in strs:
        print(str)
        print("")
        sleep(2)

    # print("역시 당신은 에테리아 왕국을 구해줄 구원자이십니다. 당신은 전투를 통해 더욱 강해졌군요.")
    # print("모험가여, 마침내 어둠의 본거지에서 에테리아 왕국을 위협하는 세력들과 맞서 싸울 수 있을 것 같군요!")


def dungeon_script_level3():
    str1 = ("운명의 전투를 맞이하러 이동합니다 . . .")
    str2 = ("어둠의 세력 본거지에 도착했습니다. 어둠의 오오라가 더욱 강력해졌습니다. ")
    str3 = ("신중하게 선택하셔야 합니다. 이 곳에는 독을 뿜는 거대 거미, 저승 꼭두각시, 황혼의 영혼, 총 세 마리의 무시무시한 몬스터가 도사리고 있습니다.. ")
    strs = [str1, str2, str3]

    for str in strs:
        print(str)
        print("")
        sleep(2)
