from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_items_at_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket is not empty"

    def should_be_text_about_empty_basket(self):
        basket_text = self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text
        assert "Your basket is empty" in basket_text, "No message about empty basket"