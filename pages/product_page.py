from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage (BasePage):
    def should_be_button_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_TO_CART), "Button 'Add to basket' is not present"

    def put_product_to_cart(self):
        button_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_TO_CART)
        button_to_cart.click()

    