from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://auth.hollandandbarrett.com/u/login")
driver.maximize_window()
time.sleep(6)

edit_box = driver.find_element(By.ID, 'username')
edit_box.send_keys('raghu.astepahead@gmail.com')
edit_box.send_keys(Keys.RETURN) # Enter values in Edit box by press keyboard
time.sleep(6)

edit_box = driver.find_element(By.NAME, 'password')
edit_box.send_keys('raghuBN@123')
edit_box.send_keys(Keys.RETURN)

