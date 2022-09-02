from signal import pause
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
import pytest
import time

"""@pytest.mark.parametrize('offer_number', ["0",
                                  "1",
                                  "2",
                                  "3",
                                  "4",
                                  "5",
                                  "6",
                                  pytest.param("7", marks=pytest.mark.xfail(reason="don't fixed")),
                                  "8",
                                  "9"])"""

def test_guest_can_add_product_to_basket(browser): # Чтобы запустить этот тест с параметром выше, нужно добавить offer_number в параметры функции 
    # и изменить ссылку на f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link) #Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.should_be_button_to_cart()
    page.put_product_to_cart()
    #page.solve_quiz_and_get_code()
    page.should_be_message_product_in_cart()
    page.is_book_name_ok()
    page.is_total_ok()

@pytest.mark.xfail(reason="shouldnt work")
def test_guest_cant_see_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.put_product_to_cart()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="shouldnt work")
def test_message_disappearred_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser,link)
    page.open()
    page.put_product_to_cart()
    page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser,link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser,link)
    page.open()
    page.go_to_login_page()
