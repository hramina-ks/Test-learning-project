from signal import pause
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
import pytest
import time

@pytest.mark.parametrize('offer_number', ["0",
                                  "1",
                                  "2",
                                  "3",
                                  "4",
                                  "5",
                                  "6",
                                  pytest.param("7", marks=pytest.mark.xfail(reason="don't fixed")),
                                  "8",
                                  "9"])

def test_guest_can_add_product_to_basket(browser,offer_number):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    page = ProductPage(browser,link) #Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.should_be_button_to_cart()
    page.put_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_product_in_cart()
    #time.sleep(20)
    page.is_book_name_ok()
    page.is_total_ok()
