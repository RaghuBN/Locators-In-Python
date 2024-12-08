import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# Function to automate the test case
def automate_test(browser_name):
    # Initialize WebDriver
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_name.lower() == "edge":
        driver = webdriver.Edge()
    else:
        print("Unsupported browser.")
        return
    # Open the URL
    driver.get("https://www.easycalculation.com/index.php")
    driver.maximize_window()
    time.sleep(6)
    # Click on "Age Calculator" link
    driver.find_element(By.LINK_TEXT, "Age Calculator").click()
    time.sleep(6)
    # Count links and images on the page
    links = driver.find_elements(By.TAG_NAME, "a")
    images = driver.find_elements(By.TAG_NAME, "img")
    print(f"Total Links Found: {len(links)}")
    print(f"Total Images Found: {len(images)}")
    print("First 10 Links:")
    for link in links[:10]:
        print(link.get_attribute("href"))
    print("First 5 Images:")
    for img in images[:5]:
        print(img.get_attribute("src"))
    # Enter Date of Birth
    driver.find_element(By.ID, "i21").send_keys("03")  # Enter Date
    driver.find_element(By.ID, "i22").send_keys("06")  # Enter Month
    driver.find_element(By.ID, "i23").send_keys("2003")  # Enter Year
    time.sleep(6)
    # Click "GO" Button
    driver.find_element(By.XPATH, "//*[@id='dispCalcCounts']/div[3]/form/table/tbody/tr[10]/td/input[1]").click()
    time.sleep(6)
    # Print the result values
    print("Your Age is:", driver.find_element(By.ID, "age").text)
    print("Your Age in Days:", driver.find_element(By.ID, "days").text)
    print("Your Age in Hours:", driver.find_element(By.ID, "hours").text)
    print("Your Age in Minutes:", driver.find_element(By.ID, "minutes").text)
    # Click "Reset"
    driver.find_element(By.ID, "reset").click()
    time.sleep(6)
    # Close the browser
    driver.quit()
# Test using Chrome browser
automate_test("chrome")
# Uncomment the next line to test with Edge browser
# automate_test("edge")