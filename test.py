from selenium import webdriver
import time

driver = webdriver.Chrome()  # 引数なしで動いた
driver.get("https://ai-inter1.com/python-selenium/")
time.sleep(3)
