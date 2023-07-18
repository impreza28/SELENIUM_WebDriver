import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from fixture.session import SessionHelper
from fixture.admin_panel import AdminPanelHelper
from selenium.webdriver.support.wait import WebDriverWait


class Application:
    def __init__(self, browser,base_url):

        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Не указан браузер")


        self.vars = {}
        self.session = SessionHelper(self)
        self.base_url = base_url
        self.admin_panel= AdminPanelHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        with allure.step('Открытие страницы litecart'):
            wd.get(self.base_url)
        with allure.step('Открытие окна браузера на полный экран'):
            wd.set_window_size(2000, 1100)

    def open_admin_page(self):
        wd = self.wd
        with allure.step('Открытие страницы админа'):
            wd.get("http://localhost/litecart/public_html/admin/")
        with allure.step('Открытие окна браузера на полный экран'):
            wd.set_window_size(2000, 1100)
        WebDriverWait(wd, 10).until(lambda x: x.find_element(By.NAME, "login"))


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False