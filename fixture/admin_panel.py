import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class AdminPanelHelper:


    def __init__(self, app):
        self.app = app

    def open_section_Appearence_Template(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=appearance&doc=template\']").click()
    def open_section_Appearence_Logotype(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=appearance&doc=logotype\']").click()
    def open_section_Catalog_Catalog(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=catalog\']").click()

    def open_section_Catalog_ProductGroups(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=product_groups\']").click()
    def open_section_Catalog_OptionGroups(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=option_groups\']").click()

    def open_section_Catalog_Manufacturers(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=manufacturers\']").click()

    def open_section_Catalog_Suppliers(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=suppliers\']").click()

    def open_section_Catalog_DeliveryStatuses(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=delivery_statuses\']").click()

    def open_section_Catalog_SoldOutStatuses(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=sold_out_statuses\']").click()

    def open_section_Catalog_QuantityUnits(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=quantity_units\']").click()

    def open_section_Catalog_CSVImportExport(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=csv\']").click()

    def open_section_Countries(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=countries&doc=countries\']").click()

    def open_section_Currencies(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=currencies&doc=currencies\']").click()

    def open_section_Customers_Customers(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=customers&doc=customers\']").click()

    def open_section_Customers_CSVImportExport(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=customers&doc=csv\']").click()

    def open_section_Customers_Newsletter(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=customers&doc=newsletter\']").click()

    def open_section_GeoZones(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=geo_zones&doc=geo_zones\']").click()

    def open_section_Languages_Languages(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=languages&doc=languages\']").click()

    def open_section_Languages_StorageEncoding(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=languages&doc=storage_encoding\']").click()

    def open_section_Modules_BackgroundJobs(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=modules&doc=jobs\']").click()

    def open_section_Modules_Customer(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=modules&doc=customer\']").click()

    def open_section_Modules_Shipping(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=modules&doc=shipping\']").click()

    def open_section_Modules_Payment(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=modules&doc=payment\']").click()

    def open_section_Modules_OrderTotal(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=modules&doc=order_total\']").click()

    def open_section_Modules_OrderSuccess(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=modules&doc=order_success\']").click()

    def open_section_Modules_OrderAction(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=modules&doc=order_action\']").click()

    def open_section_Orders_Orders(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=orders&doc=orders\']").click()

    def open_section_Orders_OrderStatuses(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=orders&doc=order_statuses\']").click()

    def open_section_Pages(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=pages&doc=pages\']").click()

    def open_section_Reports_MonthlySales(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=reports&doc=monthly_sales\']").click()

    def open_section_Reports_MostSoldProducts(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=reports&doc=most_sold_products\']").click()

    def open_section_Reports_MostShoppingCustomers(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=reports&doc=most_shopping_customers\']").click()

    def open_section_Settings_StoreInfo(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=store_info\']").click()

    def open_section_Settings_Defaults(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=defaults\']").click()

    def open_section_Settings_General(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=general\']").click()

    def open_section_Settings_Listings(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=listings\']").click()

    def open_section_Settings_Listings(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=images\']").click()

    def open_section_Settings_Checkout(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=checkout\']").click()

    def open_section_Settings_Advanced(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=advanced\']").click()

    def open_section_Settings_Security(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=security\']").click()

    def open_section_Slides(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=slides&doc=slides\']").click()

    def open_section_Tax_TaxClasses(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=tax&doc=tax_classes\']").click()

    def open_section_Tax_TaxRates(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=tax&doc=tax_rates\']").click()

    def open_section_Translations_SearchTranslations(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=translations&doc=search\']").click()

    def open_section_Translations_ScanFiles(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=translations&doc=scan\']").click()

    def open_section_Translations_CSVImportExport(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=translations&doc=csv\']").click()

    def open_section_Users(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=users&doc=users\']").click()

    def open_section_vQmods(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=vqmods&doc=vqmods\']").click()