from signal import pause
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser,link) #Инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.should_be_button_to_cart()
    page.put_product_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_product_in_cart()
    page.is_book_name_ok()
    page.is_total_ok()
