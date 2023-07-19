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
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Template\')]")
        assert len(h1) > 0, "Не найден заголовок"


    def open_section_Appearence_Logotype(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=appearance&doc=logotype\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\'Logotype\')]")
        assert len(h1) > 0, "Не найден заголовок"
    def open_section_Catalog_Catalog(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=catalog\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\'Catalog\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Catalog_ProductGroups(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=product_groups\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Product Groups\')]")
        assert len(h1) > 0, "Не найден заголовок"
    def open_section_Catalog_OptionGroups(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=option_groups\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Option Groups\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Catalog_Manufacturers(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=manufacturers\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Manufacturers\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Catalog_Suppliers(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=suppliers\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Suppliers\')]")
        assert len(h1) > 0, "Не найден заголовок"


    def open_section_Catalog_DeliveryStatuses(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=delivery_statuses\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Delivery Statuses\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Catalog_SoldOutStatuses(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=sold_out_statuses\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Sold Out Statuses\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Catalog_QuantityUnits(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=quantity_units\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Quantity Units\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Catalog_CSVImportExport(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=catalog&doc=csv\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' CSV Import/Export\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Countries(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=countries&doc=countries\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Countries\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Currencies(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=currencies&doc=currencies\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Currencies\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Customers_Customers(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=customers&doc=customers\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Customers\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Customers_CSVImportExport(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=customers&doc=csv\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' CSV Import/Export\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Customers_Newsletter(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=customers&doc=newsletter\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Newsletter\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_GeoZones(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=geo_zones&doc=geo_zones\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Geo Zones\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Languages_Languages(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=languages&doc=languages\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Languages\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Languages_StorageEncoding(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=languages&doc=storage_encoding\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Storage Encoding\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Modules_BackgroundJobs(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                                 "//a[@href=\'http://localhost/litecart/public_html/admin/?app=modules&doc=jobs\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Job Modules\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Modules_Customer(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=modules&doc=customer\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Customer Modules\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Modules_Shipping(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=modules&doc=shipping\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Shipping Modules\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Modules_Payment(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=modules&doc=payment\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Payment Modules\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Modules_OrderTotal(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=modules&doc=order_total\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Order Total Modules\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Modules_OrderSuccess(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=modules&doc=order_success\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Order Success Modules\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Modules_OrderAction(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=modules&doc=order_action\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Order Action Modules\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Orders_Orders(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=orders&doc=orders\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Orders\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Orders_OrderStatuses(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=orders&doc=order_statuses\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Order Statuses\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Pages(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=pages&doc=pages\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Pages\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Reports_MonthlySales(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=reports&doc=monthly_sales\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Monthly Sales\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Reports_MostSoldProducts(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=reports&doc=most_sold_products\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Most Sold Products\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Reports_MostShoppingCustomers(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=reports&doc=most_shopping_customers\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Most Shopping Customers\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Settings_StoreInfo(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=store_info\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Settings\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Settings_Defaults(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=defaults\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Settings\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Settings_General(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=general\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Settings\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Settings_Listings(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=listings\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Settings\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Settings_Images(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=images\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Settings\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Settings_Checkout(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=checkout\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Settings\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Settings_Advanced(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=advanced\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Settings\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Settings_Security(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=settings&doc=security\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Settings\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Slides(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=slides&doc=slides\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Slides\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Tax_TaxClasses(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=tax&doc=tax_classes\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Tax Classes\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Tax_TaxRates(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=tax&doc=tax_rates\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Tax Rates\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Translations_SearchTranslations(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=translations&doc=search\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Search Translations\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Translations_ScanFiles(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=translations&doc=scan\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Scan Files For Translations\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Translations_CSVImportExport(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=translations&doc=csv\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' CSV Import/Export\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_Users(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=users&doc=users\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' Users\')]")
        assert len(h1) > 0, "Не найден заголовок"

    def open_section_vQmods(self):
        wd = self.app.wd
        wd.find_element(By.XPATH,
                        "//a[@href=\'http://localhost/litecart/public_html/admin/?app=vqmods&doc=vqmods\']").click()
        h1 = wd.find_elements(By.XPATH, "//h1[contains(.,\' vQmods\')]")
        assert len(h1) > 0, "Не найден заголовок"