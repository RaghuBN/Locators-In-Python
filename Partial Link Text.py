import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.nopcommerce.com/en")
driver.maximize_window()
time.sleep(6)

partial_link = "nopCommerce"
link_element = driver.find_element(By.PARTIAL_LINK_TEXT, partial_link)
link_element.click()

