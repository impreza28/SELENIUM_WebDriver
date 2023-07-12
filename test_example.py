import pytest
from selenium import webdriver



class Test_example():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_example(self):
        self.driver.get("https://www.google.com/")
