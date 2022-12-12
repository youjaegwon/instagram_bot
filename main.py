# -*- coding: utf-8 -*-
from util import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
import os
import myInsta
import mySelenium
import time
import random

# 로그 설정
log = logger.logger
# URL 설정
url = "https://instagram.com"

random_wait_min = 7
random_wait_max = 15
random_next_min = 1
random_next_max = 5
refresh_count = 0
onetime_count = 25  # 태그당 시간
like_count = 0  # 현재 좋아요 개수
total_like_count = 150  # 총 좋아요 개수

log.info("***************크롤링 시작***************")
try:
    # 크롬드라이버 오픈
    browser = mySelenium.startChromeDriver(url)
    time.sleep(7)

    # 로그인
    mySelenium.checkLogin(browser, By, Keys)
    time.sleep(7)

    # 정보 저장 팝업 닫기
    mySelenium.closePopInfo(
        browser, By, '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button')
    time.sleep(4)

    # 태그 가져오기
    tags = myInsta.getHashTagList("A0001")
    time.sleep(4)

    # 태그 검색 하기
    mySelenium.searchTag(browser, tags[0])
    time.sleep(10)

    while like_count < total_like_count:

        # 최근 게시물 중 첫번쨰 게시물 선택하기
        mySelenium.selectFirstFeed(
            browser, By, Keys, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a')
        time.sleep(4)

        # 다음 게시물 이동하기
        mySelenium.nextFeed(
            browser, By, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button')
        time.sleep(4)

        for a in range(onetime_count):

            # 좋아요 누르기
            time.sleep(random.randint(random_wait_min, random_wait_max))
            mySelenium.likeClick(browser, By, like_count)

            # 다음 피드로 이동하기
            for b in range(random.randint(random_next_min, random_next_max)):
                mySelenium.nextFeed(
                    browser, By, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button')

        refresh_count += 1
        # 태그 검색 하기
        mySelenium.searchTag(browser, tags[refresh_count % len(tags)])
        log.info("refresh for : ", tags[refresh_count % len(tags)])
except:
    log.error("예기치 못한 오류가 발생하였습니다")
finally:
    browser.close()
    log.info("***************크롤링 종료***************")
