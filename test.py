import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# ローカルファイル読み込み
import my_confidential
import gmail_api

# VSCodeから実行する際、ディレクトリを変更
os.chdir(f"{my_confidential.Information.directory}")

# 認証メール取得
gmail_api.get_authentication_code()

# Webドライバー起動
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://ai-inter1.com/python-selenium/")
time.sleep(3)
