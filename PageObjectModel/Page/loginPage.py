from PageObjectModel.LocatorsPackage.Locators import Locators


class loginPage():

    def __init__(self, driver):
        self.driver = driver

        self.userName_textbox_id = Locators.userName_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id
        self.invalid_username_message_id = 'spanMessage'

    def enterUserName(self, userName):
        self.driver.find_element_by_id(self.userName_textbox_id).clear()
        self.driver.find_element_by_id(self.userName_textbox_id).send_keys(userName)

    def enterPassword(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def clickOnLoginButton(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def checkInvalidUsernameMessage(self):
        return self.driver.find_element_by_id(self.invalid_username_message_id).text
