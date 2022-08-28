from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

#class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    BUTTON_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket[data-loading-text='Adding...']")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.XPATH, ".//div[@id='messages']/div[contains(@class, 'alert-success')][1]/div/strong")
    TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info div p:first-child strong")
