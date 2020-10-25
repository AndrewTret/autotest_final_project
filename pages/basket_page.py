from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_is_empty(self):
        basket_elements = self.browser.find_elements(*BasketPageLocators.EMPTY_BASKET)
        basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
        assert len(basket_elements) == 1 and basket_text.find("Your basket is empty.") != -1, \
            f"Basket is not empty. \b LEN = {len(basket_elements)} \b TEXT = {basket_text}"

    def should_be_basket_is_not_empty(self):
        basket_elements = self.browser.find_elements(*BasketPageLocators.EMPTY_BASKET)
        assert len(basket_elements) != 1, "Basket is empty"
