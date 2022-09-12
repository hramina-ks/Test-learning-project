from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import browser
from .locators import BasePageLocators, BasketPageLocators
import math
import random
import string

class BasePage():
    def __init__(self, browser, url, timeout=10): 
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    def generate_random_word(self,length):
            letters = string.ascii_lowercase
            rand_word = ''.join(random.choice(letters) for i in range(length))
            return rand_word

    def go_to_basket(self): # Переход в корзину с любой страницы
        button_to_cart_main = self.browser.find_element(*BasePageLocators.BUTTON_TO_BASKET_MAIN)
        button_to_cart_main.click()

    def go_to_login_page(self): # Переход на страницу авторизации с любой страницы
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def is_disappeared(self, how, what, timeout=4): # Проверить, что элемент исчез со страницы
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what): # Проверяет наличие на странице элемента
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
        
    def is_not_element_present(self, how, what, timeout=4): # Проверяет отсутствие на странице элемента
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how,what)))
        except TimeoutException:
            return True
        
        return False
        
    def open(self): # Открывает ссылку на страницу
        self.browser.get(self.url) 

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented,"\
                                                                     "probably unauthorised user"

    def should_be_basket_button(self): # Проверяет наличие кнопки корзмны в шапке
        assert self.is_element_present(*BasePageLocators.BUTTON_TO_BASKET_MAIN), "Basket button in header is not presented"
            
    def should_be_login_link(self): # Проверяет наличие ссылки на авторизацию
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def solve_quiz_and_get_code(self): # Техническая функция для выполнения заданий
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

