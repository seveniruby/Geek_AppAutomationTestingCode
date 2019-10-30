import datetime
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *

class TestDemo:
    search_data=yaml.safe_load(open("search.yaml", "r"))
    print(search_data)

    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "seveniruby"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

        # sleep(20)
        # if len(self.driver.find_elements_by_id("image_cancel")) >=1:
        #     self.driver.find_element_by_id("image_cancel").click()
        #
        #



        # WebDriverWait(self.driver, 15).until(
        #     expected_conditions.visibility_of_element_located((By.ID, "image_cancel"))
        # )

        def loaded(driver):
            print(datetime.datetime.now())
            if len(self.driver.find_elements_by_id("image_cancel")) >=1:
                self.driver.find_element_by_id("image_cancel").click()
                return True
            else:
                return False

        try:
            WebDriverWait(self.driver, 20).until(loaded)
        except:
            print("no update")


    def test_demo(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("pdd")


    def test_xpath(self):
        self.driver.find_element_by_xpath("//*[@text='自选' and contains(@resource-id, 'tab_name') ]").click()

    @pytest.mark.parametrize("keyword, expected_price", [
        ("pdd", 20),
        ("alibaba", 100),
        ("jd",  10)
    ])
    def test_search(self, keyword, expected_price):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keyword)
        self.driver.find_element_by_id("name").click()

        price=self.driver.find_element_by_id("current_price")

        assert float(price.text) > expected_price
        assert "price" in price.get_attribute("resource-id")
        assert_that(price.get_attribute("package"), equal_to("com.xueqiu.android"))


    @pytest.mark.parametrize("keyword, expected_price", search_data)
    def test_search_from_yaml(self, keyword, expected_price):
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(keyword)
        self.driver.find_element_by_id("name").click()

        price=self.driver.find_element_by_id("current_price")

        assert float(price.text) > expected_price
        assert "price" in price.get_attribute("resource-id")
        assert_that(price.get_attribute("package"), equal_to("com.xueqiu.android"))

    def test_search_from_testcase(self):
        TestCase("testcase.yaml").run(self.driver)


    def teardown(self):
        self.driver.quit()

class TestCase:
    def __init__(self, path):
        file=open(path, "r")
        self.steps=yaml.safe_load(file)


    def run(self, driver: WebDriver):
        for step in self.steps:
            element=None
            print(step)

            if isinstance(step, dict):
                if "id" in step.keys():
                    element=driver.find_element_by_id(step["id"])
                elif "xpath" in step.keys():
                    element=driver.find_element_by_xpath(step["xpath"])
                else:
                    print(step.keys())

                if "input" in step.keys():
                    element.send_keys(step["input"])
                else:
                    element.click()

                if "get" in step.keys():
                    text=element.get_attribute(step["get"])
                    print(text)








