from selenium import webdriver

import time
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from PageObjectModel.Page.loginPage import loginPage
from PageObjectModel.Page.homePage import homePage
import HtmlTestRunner


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            "../../browserDrivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def testLoginValid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = loginPage(driver)
        login.enterUserName("Admin")
        login.enterPassword("admin123")
        login.clickOnLoginButton()

        homepage = homePage(driver)
        homepage.click_welcom()
        homepage.click_logout()
        time.sleep(3)

    def testLoginInValid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = loginPage(driver)
        login.enterUserName("Admin1")
        login.enterPassword("admin1234")
        login.clickOnLoginButton()

        message = login.checkInvalidUsernameMessage()
        print(message)
        self.assertEqual(message, "Invalid credentials")
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='../reports'))
