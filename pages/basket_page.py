from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_should_be_empty(self): # Проверяет наличие сообщения, что корзина пуста
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Text 'your basket empty' is not found"
    
    def should_be_basket_url(self): # Проверяет, что открыта корзина
        assert "basket" in self.browser.current_url, "It is not the basket page"

    def should_not_be_products(self): # Проверяет отсутствие продуктов в корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS_BLOCK), "there are products in the basket"