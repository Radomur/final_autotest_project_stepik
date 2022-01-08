from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def __init__(self, *args, **kwargs): #заглушка
        super(MainPage, self).__init__(*args, **kwargs)
