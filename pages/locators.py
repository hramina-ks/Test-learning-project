from selenium.webdriver.common.by import By

class BasePageLocators:
    BUTTON_TO_BASKET_MAIN = (By.XPATH, ".//div[contains(@class,basket-mini)]/span[@class='btn-group']/a[contains(@href, 'basket')]") # Кнопка для перехода в корзину из шапки
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # Ссылка на авторизацию
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc") # Сломанная ссылка на авторизацию

#class MainPageLocators:
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form") # Форма авторизации
    REGISTER_FORM = (By.ID, "register_form") # Форма регистрации

class ProductPageLocators:
    BUTTON_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket[data-loading-text='Adding...']") # Кнопка "положить товар в корзину" на странице товара (любая локализация)
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1") # Название книги на странице товара
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color") # Цена книги на странице товара
    SUCCESS_MESSAGE = (By.XPATH, ".//div[@id='messages']/div[contains(@class, 'alert-success')][1]/div/strong") # Алерт, сообщает, что товар успешно положен в корзину
    TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info div p:first-child strong") # Общая сумма товаров в корзине (в шапке)

class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p") # Сообщение, что корзина пуста. ТОЛЬКО при пустой корзине
    BASKET_PRODUCTS_BLOCK = (By.CSS_SELECTOR, "#basket_formset") # Блок, в котором лежат товары. ТОЛЬКО если товары есть. 
