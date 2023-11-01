from selenium import webdriver
import time


drive = webdriver.Chrome()
drive.get("https://google.com")
time.sleep(120)