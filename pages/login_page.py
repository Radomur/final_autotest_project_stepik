import time
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Login URL form is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    #Регистрация нового юзера
    def register_new_user(self, email, password):
        #self.is_element_present(*BasePageLocators.LOGIN_LINK).click()
        time.sleep(3)
        self.browser.find_element(*LoginPageLocators.EMAIL_IN_REGISTER_FORM).send_keys(email)
        time.sleep(3)
        self.browser.find_element(*LoginPageLocators.PASSWORD_IN_REGISTER_FORM).send_keys(password)
        time.sleep(3)
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_IN_REGISTER_FORM).send_keys(password)
        time.sleep(3)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER_IN_REGISTER_FORM).click()
        time.sleep(3)
