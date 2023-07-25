import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login_in_catalog(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        with allure.step('Ввести логин'):
            wd.find_element(By.NAME, "email").clear()
            wd.find_element(By.NAME, "email").send_keys(username)
        with allure.step('Ввести пароль'):
            wd.find_element(By.NAME, "password").clear()
            wd.find_element(By.NAME, "password").send_keys(password)
        with allure.step('Нажать кнопку Login'):
            wd.find_element(By.NAME, 'login').click()

    def login_in_admin_panel(self, username, password):
        wd = self.app.wd
        self.app.open_admin_page()
        with allure.step('Ввести логин'):
            wd.find_element(By.NAME, "username").clear()
            wd.find_element(By.NAME, "username").send_keys(username)
        with allure.step('Ввести пароль'):
            wd.find_element(By.NAME, "password").clear()
            wd.find_element(By.NAME, "password").send_keys(password)
        with allure.step('Нажать кнопку Login'):
            wd.find_element(By.NAME, 'login').click()



    def logout_from_catalog(self):
        wd = self.app.wd
        with allure.step('Нажать на ссылку Logout'):
            wd.find_element(By.LINK_TEXT, "Logout").click()
        WebDriverWait(wd, 10).until(lambda x: x.find_element(By.NAME, "login"))

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout_from_catalog()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username):
        user = self.get_logged_user()
        return user == username

    def get_logged_user(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Edit Account").click()

        user = wd.find_element(By.NAME, "email").text
        return user

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout_from_catalog()
        self.login_in_catalog(username, password)

    def wait_5s(self):
        wd = self.app.wd
        wd.implicitly_wait(5)