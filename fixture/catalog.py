
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.wait import WebDriverWait

class CatalogHelper:
    def __init__(self, app):
        self.app = app

    def find_all_items_from_catalog(self):
        wd = self.app.wd
        return wd.find_elements(By.XPATH, ".//ul[@class='listing-wrapper products']//li")

    def find_sticker_new(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, ".sticker.new")

    def count_all_stickers(self):
        wd = self.app.wd
        sum_stickers = self.count_stickers_new() + self.count_stickers_sale()
        return sum_stickers
    def count_stickers_new(self):
        wd = self.app.wd
        return len(wd.find_elements(By.CSS_SELECTOR, ".sticker.new"))
    def count_stickers_sale(self):
        wd = self.app.wd
        return len(wd.find_elements(By.CSS_SELECTOR, ".sticker.sale"))

    def count_all_items_in_catalog(self):
        wd = self.app.wd
        count_items= len(wd.find_elements(By.CSS_SELECTOR, ".product.column.shadow.hover-light"))
        return count_items





