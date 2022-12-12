# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from random import randint
import myInsta
# from datetime import datetime
# import time
# import logging

# # 로거 세팅
# logger = logging.getLogger("postprocessor")
# logger.setLevel(logging.DEBUG)

# # 일반 핸들러, 포매터 세팅
# formatter = logging.Formatter("%(asctime)s %(levelname)s:%(message)s")
# handler = logging.StreamHandler()
# handler.setFormatter(formatter)

# # 크리티컬 이벤트에 대한 핸들러, 포매터 세팅
# formatter_critical = logging.Formatter("%(asctime)s [%(levelname)s]: %(message)s")
# handler_critical = logging.FileHandler("insta_bot_"+datetime.today()+".log")
# handler_critical.setLevel(logging.DEBUG)
# handler_critical.setFormatter(formatter_critical)

# # 각 핸들러를 로거에 추가
# logger.addHandler(handler)
# logger.addHandler(handler_critical)

# logger.info("크롤링 시작")
# random_wait_min = 7
# random_wait_max = 15

# random_next_min = 1
# random_next_max = 5

# refresh_count = 0
# onetime_count = 25

# like_count = 0


# total_like_count = 150


# #화면 띄우기
# options = webdriver.ChromeOptions()
# options.add_argument("lang=ko_KR")
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument("user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")

# logger.debug("크롤링 시작")

# try:
#     browser = webdriver.Chrome('/home/ec2-user/chromedriver', options=options)
# except:
#     print("크롬 드라이버 옵션 오류")
# try:
#     browser.get("https://instagram.com")
# except:
#     print("크롬 드라이버 오류")

# #로딩하는 시간 기다리기
# time.sleep(4)

# #Login ID 속성값 찾고 입력하기
# login_id = browser.find_element(By.NAME, 'username')
# login_id.send_keys(ID)

# #Login PW 속성값 찾기 입력하기
# login_pw = browser.find_element(By.NAME, 'password')
# login_pw.send_keys(PW)
# login_pw.send_keys(Keys.RETURN)
# time.sleep(5)

# # 정보 저장 팝업 닫기
# print("정보 저장 팝업 닫기")
# popup = browser.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')
# popup.click()
# time.sleep(3)

# # 태그 검색 하기
# browser.get('https://www.instagram.com/explore/tags/' + tag[0] )
# print("태그 검색하기")
# time.sleep(3)

# prev_url = browser.current_url #이번 수정사항의 핵심 코드

# #다음 게시물 이동하기 함수
# def nextFeed():
#      print ("다음 게시물 이동하기!")
#      time.sleep(2)
#      nextFeed = browser.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button')
#      nextFeed.click()

# while like_count < total_like_count:

#     try :
#         # 최근 게시물 중 첫번쨰 게시물 선택하기
#         time.sleep(17)
#         feed = browser.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div/div[1]/div[1]/a')
#         feed.send_keys(Keys.ENTER)
#         nextFeed()
#     except Exception as e:
#         print ("게시물 선택 exception!" + e)
#         continue

#     for a in range(onetime_count):

#         # 좋아요 누르기
#         print ("좋아요 누르기!")
#         time.sleep(randint(random_wait_min,random_wait_max))
#         try:
#             like_list = browser.find_elements(By.XPATH, '//article//section/span/button')
#             likeBtnTxt = browser.find_elements(By.CLASS_NAME, '_8-yf5 ')
#             like_pass = False

#             for i in range ( len ( likeBtnTxt ) ) :
#                 if likeBtnTxt[i].get_attribute("aria-label") == 'Unlike' :
#                     like_pass = True
#                     print( likeBtnTxt[i].get_attribute("aria-label"), "Pass like" )
#                     break

#             if like_pass == False :
#                 like_list[0].click() #list 중 0번째 버튼을 선택
#                 like_count += 1
#                 print("like count = ", like_count )
#                 refresh_err = 0
#         except Exception as e:
#             print ("좋아요 exception!" + e)
#             browser.close()
#         # 다음 피드로 이동하기
#         for b in range(randint(random_next_min,random_next_max)):
#             nextFeed()

#     refresh_count += 1
#     browser.get('https://www.instagram.com/explore/tags/' + tag[refresh_count % len(tag) ] )
#     print("refresh for : ", tag[refresh_count % len(tag) ] )

# browser.close()
# print("end")
