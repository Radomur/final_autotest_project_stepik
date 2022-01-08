from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_not_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.VALID_PRODUCT_IN_BASKET), \
            "Basket is not empty!!!"
    def should_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
            "There is no message that basket is empty!!!"
