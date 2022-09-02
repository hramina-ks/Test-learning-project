from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage (BasePage):
    def should_be_button_to_cart(self): # Проверяет наличие на странице товара кнопки "Положить в корзину" (в любой локализации)
        assert self.is_element_present(*ProductPageLocators.BUTTON_PRODUCT_TO_BASKET), "Button 'Add to basket' is not present"

    def put_product_to_cart(self): # Кладет товар в корзину
        button_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_PRODUCT_TO_BASKET)
        button_to_cart.click()

    def should_be_message_product_in_cart(self): # Проверяет, что появился алерт об успешном помещении товара в корзину (в любой локализации)
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not present" # проверяю, что появился алерт с успешным действием

    def is_book_name_ok(self): # Проверяет, что в корзину положена именно эта книга (название в алерте совпадает с названием на странице)
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name == message, "Book name in message is wrong" # проверяю, что в алерте название нужной книги

    def is_total_ok(self): # Проверяет, что цена товара в алерте совпадает с ценой на странице
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        total_message = self.browser.find_element(*ProductPageLocators.TOTAL_MESSAGE).text
        assert book_price == total_message, "Total price is wrong!"

    def should_not_be_success_message(self): # Проверяет, что алерта на странице нет
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is present on product page, but dont should" 

    def success_message_should_disappear(self): # Проверяет, что алерт исчез
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not dissapeared"
