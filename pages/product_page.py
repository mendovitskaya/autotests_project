from .base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element_by_css_selector(".btn-add-to-basket")
        button.click()