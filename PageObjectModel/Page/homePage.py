from PageObjectModel.LocatorsPackage.Locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class homePage():

    def __init__(self, driver):
        self.driver = driver
        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_id = Locators.logout_link_id

    def click_welcom(self):
        EC.element_to_be_clickable(self.driver.find_element_by_id(self.welcome_link_id))
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        EC.element_to_be_clickable(self.driver.find_element_by_link_text(self.logout_link_id))
        self.driver.find_element_by_link_text(self.logout_link_id).click()
