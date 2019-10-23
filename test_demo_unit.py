
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from unittest import TestCase

class TestDemo(TestCase):
    def setUp(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "seveniruby"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        caps['unicodeKeyboard']=True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_demo(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("pdd")

    def test_capabilities(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("阿里巴巴")


    def tearDown(self):
        pass
        #self.driver.quit()
