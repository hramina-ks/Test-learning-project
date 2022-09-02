from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_form(self): # Проверяет наличие формы логина
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_login_page(self): # Общий метод для запуска трех проверок сразу (в боевых не надо так делать)
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self): # Проверяет, что открылась именно страница авторизации
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "It is not the login page"

    def should_be_register_form(self): # Проверяет наличие формы регистрации
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"
