import pandas as pd
from time import sleep
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
import json
import threading
from datetime import datetime
now = datetime.now()
OPT_CODE = input('OTP코드 입력 :')
class_ = {
    '전체 직업':1,
    '버서커' : 2,
    '디스트로이어' : 3,
    '워로드':4,
    '홀리나이트':5,
    '아르카나':6,
    '서머너':7,
    '바드':8,
    '소서리스':9,
    '배틀마스터':10,
    '인파이터':11,
    '기공사':12,
    '창술사':13,
    '스트라이커':14,
    '블레이드':15,
    '데모닉':16,
    '리퍼':17,
    '호크아이':18,
    '데빌헌터':19,
    '블래스터':20,
    '스카우터':21,
    '건슬링어':22,
    '도화가':23,
    '기상술사':24,
}
skill_ = {"버서커": {"다이빙 슬래쉬": 1, "다크 러쉬": 2, "더블 슬래쉬": 3, "레드 더스트": 4, "마운틴 크래쉬": 5, "메일스톰": 6, "블러디 러쉬": 7, "소드 스톰": 8, "숄더 차지": 9, "스트라이크 웨이브": 10, "어설트 블레이드": 11, "오러 블레이드": 12, "윈드 블레이드": 13, "체인 소드": 14, "크라임 해저드": 15, "템페스트 슬래쉬": 16, "파워 브레이크": 17, "피니쉬 스트라이크": 18, "헬 블레이드": 19, "휠윈드": 20},
"디스트로이어": {"그라비티 임 팩트": 1, "그라비티 컴프레이션": 2, "그라비티 포스": 3, "뉴트럴라이저": 4, "드레드노트": 5, "러닝 크래쉬": 6, "사이즈믹 해머": 7, "어스 스매셔": 8, "어스 웨이브": 9, "어스 이터": 10, "인듀어 페인": 11, "점핑 스매쉬": 12, "파워 숄더": 13, "파워 스트라이크": 14, "퍼펙트 스윙": 15, "풀 스윙": 16, "헤비 크러쉬": 17, "중력 가중 스킬": 18},
"워로드": {"가디언의 낙뢰": 1, "가디언의 수호": 2, "갈고리 사슬": 3, "날카로운 창": 4, "넬라 시아의 기운": 5, "대쉬 어퍼 파이어": 6, "라이징 스피어": 7, "리프 어택": 8, "방패 격동": 9, "방패 돌진": 10, "방패 밀치기": 11, "배쉬": 12, "버스트 캐넌": 13, "스피어 샷": 14, "증오의 함성": 15, "차지 스팅거": 16, "카운터 스피어": 17, "파이어 불릿": 18},
"홀리나이트": {"돌진": 1, "빛의 충격": 2, "섬광 베기": 3, "섬광 찌르기": 4, "신성 지역": 5, "신성 폭발": 6, "신성검": 7, "신성한 보호": 8, "신의 분노": 9, "신의 율법": 10, "심판의 빛": 11, "정의 집행": 12, "정의의 검": 13, "질주 베기": 14, "집행자의 검": 15, "처단": 16, "천상의 축복": 17, "회전 베기": 18},
"아르카나": {"다크 리저렉션": 1, "댄싱 오브 스파인플라워": 2, "리턴": 3, "백 플러 쉬": 4, "세렌디피티": 5, "셀레스티얼 레인": 6, "스크래치 딜러": 7, "스트림 오브 엣지": 8, "스파이럴 엣지": 9, "시크릿 가든": 10, "신비한 쇄도": 11, "언리미티드 셔플": 12, "운명의 부름": 13, "이보크": 14, "체크메이트": 15, "쿼드라 엑셀레이트": 16, "포 카드": 17, "황제": 18},
"서머너": {"고대의 창": 1, "끈적이는 이끼늪": 2, "대지 붕괴": 3, "레이네의 가호": 4, "마력의 결정체": 5, "마력의 질주": 6, "마리린": 7, "물의 정령": 8, "방출된 의지": 9, "순간 폭발": 10, "슈르디": 11, "쏜살 바람새": 12, "엘씨드": 13, "윙드 스피릿": 14, "전기 폭풍": 15, "전류 방출": 16, "파우루": 17, "고대의 정령 스킬": 18},
"바드": {"리듬 벅샷": 1, "불협화음": 2, "빛 의 광시곡": 3, "사운드 쇼크": 4, "사운드 웨이브": 5, "사운드 홀릭": 6, "수호의 연주": 7, "스티그마": 8, "윈드 오브 뮤직": 9, "율동의 하프": 10, "음파 진동": 11, "음표 뭉치": 12, "죽음의 전주곡": 13, "천상의 연주": 14, "컨빅션 코어": 15, "폭풍의 서곡": 16, "행진곡": 17},
"소서리스": {"돌풍": 1, "라이트닝 볼텍스": 2, "라이트닝 볼트": 3, "리버스 그래비티": 4, "블레이즈": 5, "서릿발": 6, "숭고한 해일": 7, "아이스 애로우": 8, "에너지 방출": 9, "엘레기안의 손길": 10, "엘리멘탈 리액트": 11, "익스플로전": 12, "인페르노": 13, "종말의 날": 14, "천벌": 15, "혹한의 부름": 16},
"배틀마스터": {"내공연소": 1, "뇌명각": 2, "바람의 속삭임": 3, "방천격": 4, "붕천퇴": 5, "삼연권": 6, "섬열란아": 7, "오의 : 나선경": 8, "오의 : 뇌진격": 9, "오의 : 폭쇄진": 10, "오의 : 풍신초래": 11, "오의 : 화룡천상": 12, "용맹의 포효": 13, "월섬각": 14, "잠룡승천축": 15, "지뢰진": 16, "초풍각": 17, "화조강림": 18},
"인파이터": {"공명의 사슬": 1, "난타연권": 2, "맹호격": 3, "밀고 나가기": 4, "순간 타격": 5, "심판": 6, "연환파신권": 7, "용의 강림": 8, "일망 타진": 9, "전진의 일격": 10, "죽음의 선 고": 11, "지진쇄": 12, "진 용출권": 13, "철포난격": 14, "초신성 폭발": 15, "파쇄격": 16, "파쇄의 강타": 17, "회심의 일격": 18},
"기공사": {"기공장": 1, "낙영장": 2, "난화격": 3, "내공 방출": 4, "독마권": 5, "무공탄": 6, "번천장": 7, "벽력장": 8, "섬열파": 9, "섭물진기": 10, "순보": 11, "여래신장": 12, "탄지공": 13, "파쇄장": 14, "풍뢰일광포": 15, "회선격추": 16, "흡철장": 17},
"창술사": {"공의연무": 1, "굉열파": 2, "나선창": 3, "맹룡열파": 4, "반월섬": 5, "사두룡격": 6, "선풍참혼": 7, "연환섬": 8, "열공참": 9, "유성강천": 10, "이연격": 11, "일섬각": 12, "적룡포": 13, "절룡세": 14, "질풍참": 15, "철량추": 16, "청룡진": 17, "청룡출수": 18, "풍진격": 19, "회선창": 20},
"스트라이커": {"격호각": 1, "광폭진": 2, "뇌명각": 3, "방천격": 4, "번개의 속삭임": 5, "붕천퇴": 6, "삼연권": 7, "섬열란아": 8, "오의 : 나선경": 9, "오의 : 뇌호격": 10, "오의 : 폭쇄진": 11, "오의 : 풍신초래": 12, "오의 : 호왕출현": 13, "운룡각": 14, "월섬각": 15, "잠룡승천축": 16, "초풍각": 17, "화조강림": 18},
"블레이드": {"다크 악셀": 1, "데스 센텐스": 2, "마엘스톰": 3, "문라이트 소닉": 4, "보이드 스트라이크": 5, "블레이드 댄스": 6, "블리츠 러시": 7, "서프라이즈 어택": 8, "소울 앱소버": 9, "스핀 커터": 10, "어스 슬래쉬": 11, "어퍼 슬래쉬": 12, "윈드 컷": 13, "터닝 슬래쉬": 14, "트윈 쉐도우": 15, "페이탈 웨이브": 16, "폴스타": 17, "헤드 헌트": 18, "버스트 스킬": 19},
"데모닉": {"그라인드 체인": 1, "님블컷": 2, "데모닉 슬래쉬": 3, "데몬 그랩": 4, "데몬 비전": 5, "데몰리션": 6, "데시메이트": 7, "라이징 클로": 8, "브루탈 크로스": 9, "샤펀 컷": 10, "스피닝 다이브": 11, "스피닝 웨폰": 12, "슬래셔": 13, "쓰러스트 임팩트": 14, "제노사이드": 15, "크루얼 커터": 16, "피어스 쏜": 17, "하울링": 18, "악마 스킬": 19},
"리퍼": {"나이트메어": 1, "댄싱 오브 퓨리": 2, "데스 사이드": 3, "디스토션": 4, "라스트 그래피티": 5, "레이지 스피어": 6, "블랙 미스트": 7, "블링크": 8, "사일런트 스매셔": 9, "샤벨 스팅거": 10, "쉐도우 닷": 11, "쉐도우 스톰": 12, "쉐도우  트랩": 13, "스피닝 대거": 14, "스피릿 캐치": 15, "이블리스토": 16, "콜 오브 나이프": 17, "팬텀 댄서": 18},
"호크아이": {"DM-42": 1, "그림자 화살": 2, "급소 베기": 3, "래피드 샷": 4, "블레이드 스톰": 5, "샤프 슈터": 6, "스나이프": 7, "아토믹 애로우": 8, "애로우 샤워": 9, "애로우 해일": 10, "연막 화살": 11, "이동 베기": 12, "일렉트릭 노바": 13, "일제 사격": 14, "집요한 추적": 15, "차징 샷": 16, "크레모아 지뢰": 17, "회피 사격": 18, "실버호크 스킬": 19},
"데빌헌터": {"AT02 유탄": 1, "나선의 추적자": 2, "대재앙": 3, "데스파이어": 4, "메테오 스트림": 5, "민첩한 사격": 6, "사형 집행": 7, "샷건 연사": 8, "샷건의 지배자": 9, "스파이럴 플레임": 10, "심판의 시간": 11, "썸머솔트샷": 12, "이퀄리브리엄": 13, "잔혹한 추적자": 14, "조준 사격": 15, "종말의 전조": 16, "최후의 만찬": 17, "퀵 샷": 18, "트리플 익스플로젼": 19, "퍼펙트 샷": 20, "플라즈마 불릿": 21},
"블래스터": {"강화탄": 1, "개틀링건": 2, "고압열탄": 3, "곡사포": 4, "공중 폭격": 5, "네이팜탄": 6, "다연장로켓포": 7, "미사일 폭격": 8, "산탄": 9, "에너지 필드": 10, "전방 포격": 11, "점프 포격": 12, "중력 폭발": 13, "포탑 소환": 14, "플라즈마 스톰": 15, "화염방사기": 16, "휘두르기": 17, "포격 스킬": 18},
"스카우터": {"고전압탄": 1, "과충전 배터리": 2, "기동 타격": 3, "명령 : M143 기관총": 4, "명령 : 레이드 미사일": 5, "명령 : 베이비 드론": 6, "명령 : 블록케이드": 7, "명령 : 액티브 펄스": 8, "명령 : 카펫": 9, "명령 : 플레어 빔": 10, "백플립 스트라이크": 11, "불릿 해일": 12, "아발란체": 13, "어나힐레이션 모드": 14, "에너지 버스터": 15, " 이스케이프": 16, "전술 사격": 17, "펄스 파이어": 18, "싱크 스킬": 19},
"건슬링어": {"AT02 유탄": 1, "나선의 추적자": 2, "대재앙": 3, "데스파이어": 4, "레인 오브 불릿": 5, "마탄의 사수": 6, "메테오 스트림": 7, "민첩 한 사격": 8, "샷건 연사": 9, "스파이럴 플레임": 10, "심판의 시간": 11, "썸머솔트샷": 12, "이퀄리브리엄": 13, "절멸의 탄환": 14, "최후의 만찬": 15, "퀵 스텝": 16, "타겟 다운": 17, "퍼펙트 샷": 18, "포커스 샷": 19, " 플라즈마 불릿": 20, "피스키퍼": 21},
"도화가": {"묵법 : 난치기": 1, "묵법 : 달그리기": 2, "묵법 : 두루미나래": 3, "묵법 : 먹오름": 4, "묵법 : 미리내": 5, "묵법 : 범가르기": 6, "묵법 : 옹달샘": 7, "묵법 : 해그리기": 8, "묵법 : 해우물": 9, "묵법 : 호접몽": 10, "묵법 : 환영의 문": 11, "필법 : 먹물세례": 12, "필법 : 올려치기": 13, "필법 : 콩콩이": 14, "필법 : 한획긋기": 15, "필법 : 흩뿌리기": 16},
"기상술사": {"날아가기": 1, "내려찍기": 2, "돌개바람": 3, "뙤약볕": 4, "마주바람": 5, "몰아치기": 6, "바람송곳": 7, "봄바람": 8, "센바람": 9, "소나기": 10, "소용돌이": 11, "싹쓸바람": 12, "짙은 안개": 13, "칼바람": 14, "펼치기": 15, "회오리 걸음": 16, "여우비 스킬": 17}}

token_auction1 = ''
token_auction2 = ''
token_auction3 = ''
token_auction4 = ''
token_auction5 = ''
token_auction6 = ''
gem_9 = {
    "ItemLevelMin": 0,
    "ItemLevelMax": 0,
    "ItemGradeQuality": 0,
 
    "Sort": "BUY_PRICE",
    "CategoryCode": 210000,
    "CharacterClass": "",
    "ItemTier": 3,
    "ItemGrade": "",
    "ItemName": "9레벨",
    "PageNo": 0,
    "SortCondition": "ASC"
  }
gem_7 = {
    "ItemLevelMin": 0,
    "ItemLevelMax": 0,
    "ItemGradeQuality": 0,
 
    "Sort": "BUY_PRICE",
    "CategoryCode": 210000,
    "CharacterClass": "",
    "ItemTier": 3,
    "ItemGrade": "",
    "ItemName": "7레벨",
    "PageNo": 0,
    "SortCondition": "ASC"
  }
gem_10 = {
    "ItemLevelMin": 0,
    "ItemLevelMax": 0,
    "ItemGradeQuality": 0,
 
    "Sort": "BUY_PRICE",
    "CategoryCode": 210000,
    "CharacterClass": "",
    "ItemTier": 3,
    "ItemGrade": "",
    "ItemName": "10레벨",
    "PageNo": 0,
    "SortCondition": "ASC"
  }
gem_1 = {
    "ItemLevelMin": 0,
    "ItemLevelMax": 0,
    "ItemGradeQuality": 0,
 
    "Sort": "BUY_PRICE",
    "CategoryCode": 210000,
    "CharacterClass": "",
    "ItemTier": 3,
    "ItemGrade": "",
    "ItemName": "1레벨",
    "PageNo": 0,
    "SortCondition": "ASC"
  }

requestUrl = 'https://developer-lostark.game.onstove.com/auctions/items'
header1= {
    "accept" : "application/json",
    "authorization": f"bearer {token_auction1}",
    "Content-Type" : "application/json",
}
header2= {
    "accept" : "application/json",
    "authorization": f"bearer {token_auction2}",
    "Content-Type" : "application/json",
}
header3= {
    "accept" : "application/json",
    "authorization": f"bearer {token_auction3}",
    "Content-Type" : "application/json",
}
header4= {
    "accept" : "application/json",
    "authorization": f"bearer {token_auction4}",
    "Content-Type" : "application/json",
}
header5= {
    "accept" : "application/json",
    "authorization": f"bearer {token_auction5}",
    "Content-Type" : "application/json",
}
header6= {
    "accept" : "application/json",
    "authorization": f"bearer {token_auction6}",
    "Content-Type" : "application/json",
}
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(url='https://lostark.game.onstove.com/Auction')
driver.find_element(By.NAME,'user_id').send_keys("id")
driver.find_element(By.NAME,'user_pwd').send_keys("pw")
driver.find_element(By.XPATH,'//*[@id="idLogin"]/div[4]/button').click()
sleep(1)
driver.find_element(By.XPATH,'//*[@id="otp"]').send_keys(OPT_CODE)
sleep(0.3)
driver.find_element(By.XPATH,'/html/body/div[1]/section/div/div/section/article[2]/nav/a').click()
sleep(0.3)

request_data_set={
    '1': header1,
    '2': header2,
    '3': header3,
    '4': header4,
    '5': header5,
    '6': header6,
}

def set_chrome_driver():
    repeat = True
    f = open('gem9_log.txt','a',encoding='utf-8')
    threading_repeat = threading.Timer(1,set_chrome_driver)
    driver.get(url='https://lostark.game.onstove.com/Auction')
    current_money = driver.find_element(By.XPATH,'//*[@id="lostark-wrapper"]/div/main/div/div[1]/div[4]/dl/dd[1]').text
    current_money = current_money.replace(',','')
    driver.find_element(By.XPATH,'//*[@id="lostark-wrapper"]/div/main/div/div[3]/div[2]/form/fieldset/div/div[5]/button[2]').click()
    #보석 카테고리 선택
    driver.find_element(By.XPATH,'//*[@id="selCategoryDetail"]/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="selCategoryDetail"]/div[2]/label[16]').click()
    #3티어 선택
    driver.find_element(By.XPATH,'//*[@id="modal-deal-option"]/div/div/div[1]/div[1]/table/tbody/tr[4]/td[1]/div/div[1]').click()
    driver.find_element(By.XPATH,'//*[@id="modal-deal-option"]/div/div/div[1]/div[1]/table/tbody/tr[4]/td[1]/div/div[2]/label[4]').click()
    #api 데이터 함수 넣기
    count = 0


    while(repeat):
        sleep(0.3)
        count+=1
        gem_data=[]
        now = datetime.now()
        if count > 6:
            count=1

        request_data = requests.post(requestUrl,headers=request_data_set[str(count)],data = json.dumps(gem_7))
        request_data = request_data.json()
        if request_data == None:
            f.write(str(now)+' 요청 횟수 오류\n')
            continue
        Items = request_data['Items']
        Item = Items[0]
        Item_info = Item['AuctionInfo']
        Item_option = Item['Options']
        Item_option = Item_option[0]
        if Item_info['BuyPrice']<3000:
            gem_data.append([Item['Name'],Item_info['BuyPrice'],Item_option['ClassName'],Item_option['OptionName'],now])
            repeat = False
        else:
            print(str(count)+' '+str(Item['Name'])+' 옵션 '+str(Item_option['OptionName'])+' 보석값 정상')
    

                
    search_data = gem_data[0]

    try:
        #검색어 입력
        driver.find_element(By.XPATH,'//*[@id="txtItemNameDetail"]').send_keys(search_data[0])
        #직업 선택
        driver.find_element(By.XPATH,'//*[@id="selClassDetail"]/div[1]').click()
        driver.find_element(By.XPATH,f'//*[@id="selClassDetail"]/div[2]/label[{class_[search_data[2]]}]').click()
        #스킬 선택
        skill = skill_[search_data[2]]
        skill__ = skill[search_data[3]]
        driver.find_element(By.XPATH,'//*[@id="selSkill_0"]/input').click()
        driver.find_element(By.XPATH,f'//*[@id="selSkill_0"]/div/ul/li[{skill__}]/a').click()
        #검색
        driver.find_element(By.XPATH,'//*[@id="modal-deal-option"]/div/div/div[2]/button[1]').click()
        sleep(0.4)
        #즉구가 정렬
        driver.find_element(By.XPATH,'//*[@id="BUY_PRICE"]').click()
        sleep(0.4)  
        #구매하려는 보석 가격
        price = driver.find_element(By.XPATH,'//*[@id="auctionListTbody"]/tr[1]/td[6]/div/em').text
        price = price.replace(',','')

        #검색가격이랑 같으면 구매
        if int(price) == int(search_data[1]):
            try:
                driver.find_element(By.XPATH,'//*[@id="auctionListTbody"]/tr[1]/td[7]/button').click()
                driver.find_element(By.XPATH,'//*[@id="modal-deal-buy"]/div/div/div/div[4]/label').click()
                driver.find_element(By.XPATH,'//*[@id="modal-deal-buy"]/div/div/div/div[2]/div[3]/table/tbody/tr[3]/td/a').click()
                driver.find_element(By.XPATH,'//*[@id="password-input"]/div[2]/div/button[text()="1"]').click()
                driver.find_element(By.XPATH,'//*[@id="password-input"]/div[2]/div/button[text()="5"]').click()
                driver.find_element(By.XPATH,'//*[@id="password-input"]/div[2]/div/button[text()="9"]').click()
                driver.find_element(By.XPATH,'//*[@id="password-input"]/div[2]/div/button[text()="8"]').click()
                driver.find_element(By.XPATH,'//*[@id="password-input"]/div[2]/div/button[text()="4"]').click()
                driver.find_element(By.XPATH,'//*[@id="password-input"]/div[2]/div/button[text()="7"]').click()
                driver.find_element(By.XPATH,'//*[@id="password-input"]/div[2]/div/button[text()="0"]').click()
                driver.find_element(By.XPATH,'//*[@id="password-input"]/div[2]/div/button[text()="0"]').click()
                driver.find_element(By.XPATH,'//*[@id="password-input"]/div[1]/div[2]/button[1]').click()
                data = '\n올라온 시간: '+str(search_data[4])+'\n보석 이름: '+str(search_data[0])+'\n보석 가격: '+str(search_data[1])+'\n보석 종류 : '+str(search_data[3])+'\n직업 : '+str(search_data[2])+'\n'
                f.write('구매 성공!!\n구매 정보\n'+str(data)+'\n')
            except:
                now = datetime.now()
                data = '\n올라온 시간: '+str(now)+'\n보석 이름: '+str(search_data[0])+'\n보석 가격: '+str(search_data[1])+'\n보석 종류 : '+str(search_data[3])+'\n직업 : '+str(search_data[2])+'\n'
                f.write(str(now)+' 구매 실패\n'+str(data)+'\n')
        else:
            now = datetime.now()
            f.write(str(now)+'구매 실패\n')
        f.close()
        threading_repeat.start()
    except:
        now = datetime.now()
        f.write(str(now)+' 셀레니움 오류\n')
        
    f.close()
    threading_repeat.start()
   

set_chrome_driver()
