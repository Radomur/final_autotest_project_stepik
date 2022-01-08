from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def checks_add_product_to_basket(self):
        self.add_product_to_basket()
        self.should_product_name_equal_in_message()
        self.should_product_price_equal_in_basket()

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_BASKET).click()
        #self.solve_quiz_and_get_code() #с промокодом появляется алерт где высчитывает выражение

    def should_product_name_equal_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_MANE).text
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_MANE_MESSAGE).text
        print("product_name: ", product_name)
        print("product_name_in_message: ", product_name_in_message)
        assert product_name == product_name_in_message, "Product name and product name in basket didn`t match"

    def should_product_price_equal_in_basket(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text[1:5]
        product_price_basket_total = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_TOTAL).text[1:5]
        print("product_price: ", product_price)
        print("product_price_in_message: ", product_price_basket_total)
        assert product_price == product_price_basket_total, "Product price and price total in basket didn`t match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"
