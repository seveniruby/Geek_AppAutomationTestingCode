import datetime
import os
from socket import socket

from appium import webdriver
from selenium.webdriver.common import utils
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from page.main_page import MainPage


class App:
    driver: WebDriver = None

    @classmethod
    def start(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "seveniruby"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        # caps["udid"] = "emulator-5556"
        caps['udid'] = os.getenv("udid", None)
        caps['systemPort'] = utils.free_port()
        caps['chromedriverPort'] = utils.free_port()



        caps["chromedriverExecutable"] = "/Users/seveniruby/projects/chromedriver/2.20/chromedriver"
        caps["showChromedriverLog"] = True

        print(caps)

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(5)

        # sleep(20)
        # if len(self.driver.find_elements_by_id("image_cancel")) >=1:
        #     self.driver.find_element_by_id("image_cancel").click()
        #
        #

        # WebDriverWait(self.driver, 15).until(
        #     expected_conditions.visibility_of_element_located((By.ID, "image_cancel"))
        # )

        # def loaded(driver):
        #     print(datetime.datetime.now())
        #     if len(cls.driver.find_elements_by_id("image_cancel")) >=1:
        #         cls.driver.find_element_by_id("image_cancel").click()
        #         return True
        #     else:
        #         return False
        #
        # try:
        #     WebDriverWait(cls.driver, 20).until(loaded)
        # except:
        #     print("no update")

        return MainPage(cls.driver)

    @classmethod
    def get_free_port(cls):
        """
        获得可用的端口
        :return:
        """
        with socket() as s:
            s.bind(('', 0))
            return s.getsockname()[1]

    @classmethod
    def quit(cls):
        cls.driver.quit()
