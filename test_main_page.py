from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage
import time
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,link) #Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        #page.solve_quiz_and_get_code()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    basket_link = "http://selenium1py.pythonanywhere.com/en-gb/basket/"
    page = MainPage(browser,link) #Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    basket_page = BasketPage(browser,basket_link)
    page.open()
    page.should_be_basket_button()
    basket_page.go_to_basket()
    basket_page.should_be_basket_url()
    basket_page.should_not_be_products()
    basket_page.basket_should_be_empty()
