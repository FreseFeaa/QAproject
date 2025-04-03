import math
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from kt3.logg import logger
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self,browser,url,timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.logger = logger

    def open(self):
        self.browser.get(self.url)
        self.logger.info(f"Запущен браузер по юрлу: {self.url}")

    
    def is_element_present(self,how,what):
        self.logger.info(f"Проверка есть ли обьект: {what}")
        try:
            self.browser.find_element(how, what)

        except NoSuchElementException:
            self.logger.info(f"Обьект ({what}) нет")
            return False
        
        self.logger.info(f"Обьект ({what}) есть")
        return True


    def is_not_element_present(self,how,what,timeout=5):
        self.logger.info(f"Проверка отсутстивия обьекта: {what}")
        try:
            WebDriverWait(self.browser,timeout).until(EC.presence_of_element_located((how,what)))

        except TimeoutException:
            self.logger.info(f"Обьекта ({what}) нет")
            return True
        
        self.logger.info(f"Обьекта ({what}) есть (Не должен быть)")
        return False
    
    
    def is_disappeared(self,how,what,timeout=5):
        self.logger.info(f"Этот обьект ({what}) должен исчезнуть за {timeout}")
        try:
            WebDriverWait(self.browser,timeout,poll_frequency=TimeoutException).until(EC.presence_of_element_located((how,what)))

        except TimeoutException:
            self.logger.info(f"Этот обьект ({what}) исчез")
            return True
        self.logger.info(f"Этот обьект ({what}) не исчез")
        return False
    

    def should_be_login_button(self):
        self.logger.info(f"Проверка существования кнопки профиля")
        try:
            assert self.is_element_present(*BasePageLocators.ACCOUNT_BUTTON), "Нет кнопки профиля"
        except AssertionError as erorr:
            self.logger.error(f"{erorr}")
            raise erorr
        
    
    def login_button_click(self):
        self.logger.info(f"Кликаем по кнопки профиля")
        self.browser.find_element(*BasePageLocators.ACCOUNT_BUTTON).click()

    def catalog_search(self, product):
        self.logger.info(f"Поиск в каталоге - продукта {product}")
        self.browser.find_element(*BasePageLocators.CATALOG_SEARCH).send_keys(product) 
