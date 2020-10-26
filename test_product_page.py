from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(self, browser):
    page = ProductPage(browser, f"{self.link}?promo=newYear2019")
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_right_product_name()
    page.should_be_right_basket_price()


@pytest.mark.xfail()
def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
    page = ProductPage(browser, self.link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(self, browser):
    page = ProductPage(browser, self.link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(self, browser):
    page = ProductPage(browser, self.link)
    page.open()
    page.add_product_to_basket()
    page.should_be_is_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(self, browser):
    page = ProductPage(browser, self.link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(self, browser):
    page = ProductPage(browser, self.link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
    page = ProductPage(browser, self.link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, self.link)
    basket_page.should_be_basket_is_empty()


@pytest.mark.user_basket
class TestUserAddToBasketFromProductPage:
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        new_email = f"{str(time.time())}@mail.net"
        new_password = str(time.time())
        page = ProductPage(browser, self.link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, self.link)
        login_page.register_new_user(new_email, new_password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_authorized_user()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.should_be_authorized_user()
        page.add_product_to_basket()
        page.should_be_right_product_name()
        page.should_be_right_basket_price()

