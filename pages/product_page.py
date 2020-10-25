from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_right_product_name(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT).text, "Product name in alert is wrong"

    def should_be_right_basket_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.BASKET_PRICE_ALERT).text, "Basket price in alert is wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be is disappeared"
