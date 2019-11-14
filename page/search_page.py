from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page.base_page import BasePage


class SearchPage(BasePage):

    _input_locator=(By.ID, "com.xueqiu.android:id/search_input_text")
    _name_locator=(By.ID, "name")
    def search(self, keyword):
        self.find_element(self._input_locator).send_keys(keyword)
        self.find_element(self._name_locator).click()

        # self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keyword)
        # self.driver.find_element_by_id("name").click()

        return self

    def get_current_price(self):
        return float(self.driver.find_element_by_id("current_price").text)