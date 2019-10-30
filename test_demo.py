import datetime
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
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
            WebDriverWait(self.driver, 15).until(loaded)
        except:
            print("no update")


    def test_demo(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("pdd")


    def test_xpath(self):
        self.driver.find_element_by_xpath("//*[@text='自选' and contains(@resource-id, 'tab_name') ]").click()



    def teardown(self):
        self.driver.quit()
