from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.nopcommerce.com/en")
driver.maximize_window()
time.sleep(5)

all_links = driver.find_elements(By.XPATH, ".//a")
print(len(all_links))

for links in all_links:
    print(links.text)
    if links.get_attribute('href'):
        print("link present")
    else:
        print("link not present")

footer_links = driver.find_elements(By.XPATH, ".//div[@class='footer-upper-wrapper']//a")
print(len(footer_links))

for links in footer_links:
    print(links.text)
    if links.get_attribute('href'):
        print("link present")
    else:
        print("link not present")
