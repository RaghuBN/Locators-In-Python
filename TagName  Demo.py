import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.hollandandbarrett.com/shop/vitamins-supplements/vitamins/")
driver.maximize_window()
time.sleep(6)

ts1 = driver.find_element(By.TAG_NAME, "img").get_attribute("src");
print(ts1);






links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.text)
    print(link.get_attribute("href"))