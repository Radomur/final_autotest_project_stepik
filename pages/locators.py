from selenium.webdriver.common.by import By


#class MainPageLocators():

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    BUTTON_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_MANE = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    PRICE_PRODUCT_TOTAL = (By.CSS_SELECTOR, "div.alertinner  > p > strong")
    PRODUCT_MANE_MESSAGE = (By.CSS_SELECTOR, ".alertinner > strong")
    SUCCESS_MESSAGE = (By.XPATH, '//div[contains(@class, "alert-success")]/div[contains(@class,"alertinner") \
    and contains(text(), "has been added to your basket.")]')
