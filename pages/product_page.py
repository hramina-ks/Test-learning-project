from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage (BasePage):
    def should_be_button_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_TO_CART), "Button 'Add to basket' is not present"

    def put_product_to_cart(self):
        button_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_TO_CART)
        button_to_cart.click()

    def should_be_message_product_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success messaage is not present" # проверяю, что появился алерт с успешным действием

    def is_book_name_ok(self):
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        assert book_name == message, "Book name in message is wrong" # проверяю, что в алерте название нужной книги

    def is_total_ok(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        print(book_price)
        total_message = self.browser.find_element(*ProductPageLocators.TOTAL_MESSAGE).text
        print(total_message)
        assert book_price == total_message, "Total price is wrong!"