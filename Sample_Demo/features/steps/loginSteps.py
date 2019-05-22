from selenium import webdriver
from behave import Given, When, Then
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Sample_Demo.features.pages.loginPage import LoginPage
from Sample_Demo.features.pages.homePage import HomePage


def login_details(self):
    driver = LoginPage(self.driver)
    return driver


def home_details(self):
    driver = HomePage(self.driver)
    return driver


@Given(u'Launch the browser')
def step_impl(self):
    self.driver = webdriver.Chrome(
        executable_path="C:/Users/Jeevan/Desktop/Jeevan/Python_Backup/FirstTest/src/chromedriver.exe")
    self.driver.implicitly_wait(10)
    self.driver.maximize_window()
    self.driver.get("https://opensource-demo.orangehrmlive.com/")


@When(u'User enter the username')
def step_impl(self):
    login_details(self).enter_username("Admin")


@When(u'User enter the password')
def step_impl(self):
    login_details(self).enter_password("admin123")


@When(u'click login button')
def step_impl(self):
    login_details(self).click_login_btn()


@Then(u'user verify the welcome link')
def step_impl(self):
    home_details(self).click_welcome()
    home_details(self).click_logout()

