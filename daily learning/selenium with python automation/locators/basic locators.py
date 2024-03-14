import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://mpulse.co.in/login"

username_xpath = ""

broswer = webdriver.Chrome()

broswer.get(url)
time.sleep(5)


broswer.find_element(By.CSS_SELECTOR,"")