class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button = "btnLogin"
        self.invalidUsername_msg_xpath = "//span[@id='spanMessage']"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element_by_id(self.login_button).click()

    def check_invalid_username_message(self):
        msg = self.driver.find_element_by_xpath(self.invalidUsername_msg_xpath).text()
        return msg