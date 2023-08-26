import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import time

# ローカルファイル読み込み
import my_confidential
import gmail_api

# VSCodeから実行する際、ディレクトリを変更
os.chdir(f"{my_confidential.Information.DIRECTORY}")
# 認証メール取得
authentication_mail_string = gmail_api.get_authentication_code()


# Webドライバー起動
options = Options()
# options.add_argument("--headless")
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)
driver.get("https://www.pairs.lv/")
time.sleep(2)

try:
    # Topページ ～ 認証メール送信まで
    login_button = driver.find_element(
        By.XPATH,
        "//*[@id='__next']/div/div[2]/div[2]/header/div/div/div[2]/div/div/button",
    )
    login_button.click()
    time.sleep(3)
    mail_button = driver.find_element(
        By.XPATH,
        "//*[@id='headlessui-dialog-panel-:r1:']/div[2]/div/div/div[2]/nav/div[1]/ul/li[4]/div/a/span",
    )
    mail_button.click()
    time.sleep(1)
    mail_text_area = driver.find_element(
        By.XPATH,
        "//*[@id='maincontent']/div/div/main/div/form/div[2]/div/input",
    )
    mail_text_area.send_keys(my_confidential.Information.MAIL)
    time.sleep(1)
    submit_button = driver.find_element(
        By.XPATH,
        "//*[@id='maincontent']/div/div/main/div/form/div[2]/button/span",
    )
    submit_button.click()
    time.sleep(3)

    # 次へボタン ～ ログイン
    tugihe_button = driver.find_element(
        By.XPATH,
        "//*[@id='maincontent']/div/div/main/div/div[2]/div[2]/a/span",
    )
    tugihe_button.click()
    time.sleep(3)

    authentication_text_area1 = driver.find_element(
        By.XPATH,
        "//*[@id='maincontent']/div/div/main/div/div[2]/div[1]/div[1]",
    )
    authentication_text_area2 = driver.find_element(
        By.XPATH,
        "//*[@id='maincontent']/div/div/main/div/div[2]/div[1]/div[2]",
    )
    authentication_text_area3 = driver.find_element(
        By.XPATH,
        "//*[@id='maincontent']/div/div/main/div/div[2]/div[1]/div[3]",
    )
    authentication_text_area4 = driver.find_element(
        By.XPATH,
        "//*[@id='maincontent']/div/div/main/div/div[2]/div[1]/div[4]",
    )
    authentication_text_area5 = driver.find_element(
        By.XPATH,
        "//*[@id='maincontent']/div/div/main/div/div[2]/div[1]/div[5]",
    )
    authentication_text_area6 = driver.find_element(
        By.XPATH,
        "//*[@id='maincontent']/div/div/main/div/div[2]/div[1]/div[6]",
    )

    for i, authentication_code_char in enumerate(authentication_mail_string):
        authentication_text_area = authentication_text_area + i
        authentication_text_area.send_keys(authentication_code_char)

    time.sleep(10)

except Exception as e:
    print("例外発生")
    print(e)
