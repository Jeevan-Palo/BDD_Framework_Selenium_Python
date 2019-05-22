class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_ID = "welcome"
        self.logout_btn_linktext = "Logout"

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_ID).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_btn_linktext).click()

