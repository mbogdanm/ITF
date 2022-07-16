from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

chrome.get('https://formy-project.herokuapp.com/form')
first_name = chrome.finde_element(By.ID, "first-name")
first_name.send_keys("BLAAAAAA")

