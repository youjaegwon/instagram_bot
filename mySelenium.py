from selenium import webdriver
from util import logger
import chromedriver_autoinstaller
import os
import util.crypto
import config

log = logger.logger
simpleEnDecrypt = util.crypto.SimpleEnDecrypt(config.ende_key)
# 크롬드라이버 실행


def startChromeDriver(url):
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    driver_path = f'./{chrome_ver}/chromedriver'
    if os.path.exists(driver_path):
        log.info(f"이미 설치된 크롬 드라이버: {driver_path}")
    else:
        log.info(f"크롬 드라이버 설치 (ver: {chrome_ver})")
        chromedriver_autoinstaller.install(True)

    # 옵션 설정
    options = webdriver.ChromeOptions()
    options.add_argument("lang=ko_KR")
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument(
        "user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")

    # 드라이버 객체 생성 및 URL Open
    driver = webdriver.Chrome(driver_path, options=options)
    driver.get(url)

    return driver

# 아이디, 패스워드 입력


def checkLogin(browser, By, Keys):
    log.info("로그인")
    # Login ID 속성값 찾고 입력하기
    login_id = browser.find_element(By.NAME, 'username')
    login_id.send_keys(config.user_id)

    # Login PW 속성값 찾기 입력하기
    login_pw = browser.find_element(By.NAME, 'password')
    login_pw.send_keys(simpleEnDecrypt.decrypt(config.user_pw))
    login_pw.send_keys(Keys.RETURN)
    log.info("로그인 성공")

# 정보저장 팝업 닫기


def closePopInfo(browser, By, xPath):
    log.info("정보 저장 팝업 닫기")
    try:
        popup = browser.find_element(By.XPATH, xPath)
        popup.click()
    except Exception as e:
        log.error("정보 저장 팝업 오류 ===> " + e)

# 태그 검색


def searchTag(browser, tag):
    log.info("태그 검색하기")
    browser.get('https://www.instagram.com/explore/tags/' + tag[0])

# 다음 게시물 이동하기


def nextFeed(browser, By, xPath):
    log.info("다음 게시물 이동하기")
    try:
        nextFeed = browser.find_element(By.XPATH, xPath)
        nextFeed.click()
    except Exception as e:
        log.error("다음 게시물 이동하기 오류 ===> " + e)

# 최근 게시물 중 첫번쨰 게시물 선택하기


def selectFirstFeed(browser, By, Keys, xPath):
    try:
        # 최근 게시물 중 첫번째 게시물 선택하기
        feed = browser.find_element(By.XPATH, xPath)
        feed.send_keys(Keys.ENTER)
    except Exception as e:
        log.error("첫번째 게시물 선택 오류 ===>" + e)

# 좋아요 누르기


def likeClick(browser, By, like_count):
    log.info("좋아요 누르기")
    try:
        like_list = browser.find_elements(
            By.XPATH, '//article//section/span/button')
        likeBtnTxt = browser.find_elements(By.CLASS_NAME, '_8-yf5 ')
        like_pass = False

        for i in range(len(likeBtnTxt)):
            if likeBtnTxt[i].get_attribute("aria-label") == 'Unlike':
                like_pass = True
                log.info(likeBtnTxt[i].get_attribute(
                    "aria-label"), "Pass like")
                break

        if like_pass == False:
            like_list[0].click()  # list 중 0번째 버튼을 선택
            like_count += 1
            log.info("좋아요 개수 = ", like_count)
            refresh_err = 0
    except Exception as e:
        print("좋아요 클릭 오류 ===>" + e)
