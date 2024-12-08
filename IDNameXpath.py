
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
driver.maximize_window()
driver.implicitly_wait(10)

edit_box = driver.find_element(By.ID, 'email')
edit_box.send_keys('raghu.astepahead@gmail.com')
edit_box.send_keys(Keys.RETURN)

edit_box = driver.find_element(By.NAME, 'passwd')
edit_box.send_keys('raghuBN@123')
edit_box.send_keys(Keys.RETURN)

driver.find_element(By.XPATH, '//*[@id="SubmitLogin"]/span').click()


