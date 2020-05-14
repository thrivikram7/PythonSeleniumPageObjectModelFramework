from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("/Users/TKRPRASAD/Documents/Workspace/PythonSeleniumLearning/browserDrivers/chromedriver")

# driver = webdriver.Safari()

driver.set_page_load_timeout(10)
driver.get("http://www.google.com")

print(driver.current_url)

print(driver.title)

driver.find_element_by_name("q").send_keys("Hello Thriv")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
time.sleep(5)
driver.maximize_window()
driver.refresh()

driver.quit()
print("Test completed")