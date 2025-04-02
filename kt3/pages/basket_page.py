from .base_page import BasePage
from selenium.webdriver.common.by import By
from kt3.logg import logger

class BasketPage(BasePage):
    def product_in_basket(self,product):
        self.logger.info(f"Поиск продукта ({product}) в корзине")
        assert self.browser.find_element(By.LINK_TEXT,product).text == product
