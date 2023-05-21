# AI-5_B1_RPGgame
# Python-RPGgame-Project
Terminal을 이용한 RPG Game!

## 🖥️ 프로젝트 소개
Python으로 작성된 코드를 Terminal에서 실행하는 RPG Game입니다.

## 🕰️ 개발 기간
* 23.03.29 - 23.03.31

### 🧑‍🤝‍🧑 팀원 구성 및 역할 분담
- 팀장😄  : 우소라 - 몬스터 클래스, 몬스터 딕셔너리
- 팀원😄1 : 김경수 - 전투 씬(app.py)
- 팀원😄2 : <a href="https://guco.tistory.com/">구민정</a> - 캐릭터 클래스, 직업별 공격 함수
- 팀원😄3 : 최준영 - 스크립트 및 플레이어 클래스
- 팀원😄4 : 장소은 - 직업별 레벨업 함수, 플레이어 객체 생성 함수

### ⚙️ 개발 환경
- `Python 3.11`
- **IDE** : `visual studio code`

### 🔑 프로젝트 실행 방법
- Ctrl + 백틱 (터미널 열기)
- python app.py (코드 실행)

## 📌 주요 기능
### 목차
#### [1. 마법사](#마법사)
#### [2. 전사](#전사)
#### [3. 도적](#검색)
#### [4. 일반공격](#일반공격)
#### [5. 특수공격](#특수공격)
#### [6. 게임 승리](#게임-승리)
#### [7. 게임 패배](#게임-패배)
#### [8. 입력 오류](#입력-오류)


------------
#### 마법사
- 레벨업 시 MP가 다른 직업에 비해 더 많이 상승함

#### 전사
- 레벨업 시 HP가 다른 직업에 비해 더 많이 상승함

#### 도적
- 도적 특수 스킬인 회피 능력이 있음
- 레벨업 시 회피율이 상승함(다른 직업은 회피율 고정)

#### 일반공격
- 일반공격 시에는 타겟을 무조건 고르게 되어 있음
- 몬스터가 사망하면 타겟 목록에서 사라짐
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/2000ad91-12b9-4f04-b338-e4a2769ab676)
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/fab1b6c3-5e1c-4c1e-b48e-81ee2e14bb77)

#### 특수공격
- 전부 공격하기, 타겟 고르기 중에 선택할 수 있음
- 몬스터가 사망하면 타겟 목록에서 사라짐
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/5f9f20c5-5bc5-447d-9eac-1e3cc227ca85)
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/5e071c74-c403-4349-baec-f4d523f87989)

#### 게임 승리 
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/ee36b44f-701d-44be-b05c-9be267a86fd2)
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/e3ca2279-2504-4364-b4fd-1506bf5cb308)
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/6cd2c0c7-fa90-4ed1-acc6-a13801104442)
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/86cf7345-12a1-4621-8832-edfa75dc0a7d)
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/90a83565-c672-436f-9fa2-65e1356c688a)
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/e826b424-a0bb-4611-abe3-2e036c87b121)
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/7fb9c802-95e6-483b-885b-6a0f57d11302)
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/341700e4-d367-4386-909f-0aa63c774df2)

#### 게임 패배 
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/65c78214-0a3d-45a1-bed1-559628f7ba19)
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/cb9c2f0c-c0a2-4b18-8a77-c265194377b0)
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/005ab155-f276-4824-a357-9d346392280c)
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/16e17ba6-29f4-4f7c-b652-f6c3c2ae2e47)
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/10d57d40-bd89-4380-a4ba-5f10a3e0376d)

#### 입력 오류
- 보기에 나와 있는 값 외의 값 입력 시 다시 입력하게끔 함
![image](https://github.com/goodminjeong/AI-5_RPGgame/assets/125722304/bd8b8e2b-59a6-49e3-b03a-7a0bf1c36ebb)
