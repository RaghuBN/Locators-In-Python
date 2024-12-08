from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://auth.hollandandbarrett.com/u/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID, 'username').send_keys("raghu.astepahead@gmail.com")
driver.find_element(By.NAME, "password").send_keys("raghuBN@123")
driver.find_element(By.XPATH, '/html/body/main/section/div/div/div/form/div[2]/button').click()
time.sleep(5)