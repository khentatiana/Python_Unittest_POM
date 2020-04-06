
class LoginPage():
    # Locators of all elements on the login page
    textbox_user_id = "Email"
    textbox_user_password = "Password"
    checkbox = "RememberMe"
    login_button = "//input[@class='button-1 login-button']"

    # Initialize the driver
    def __init__(self, driver):
        self.driver = driver

    # Actions for web elements
    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_user_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_user_password).send_keys(password)

    # def selectCheckbox(self):
    #     self.driver.find_element_by_id(self.checkbox).selectCheckbox()

    def clickLoginBtn(self):
        self.driver.find_element_by_xpath(self.login_button).click()