import datetime
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.gsm import GsmCallActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestApiDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "seveniruby"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        caps["autoGrantPermissions"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)


    def test_toast(self):
        self.driver.find_element_by_accessibility_id("Views").click()
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Popup Menu").instance(0));'
        ).click()

        #self.driver.swipe()
        #self.driver.find_element_by_accessibility_id("Popup Menu").click()

        self.driver.find_element_by_accessibility_id("Make a Popup!").click()
        assert len(self.driver.find_elements_by_xpath('//*[@text="Edit"]')) == 1

        self.driver.find_element_by_xpath("//*[@text='Search']").click()

        assert "Clicked popup menu item Search XXX" in self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text


    def test_gsm_call(self):
        self.driver.send_sms("15600534760", "Hello, From Seveniruby")
        self.driver.make_gsm_call("15600534760", GsmCallActions.CALL)

    def test_performance(self):
        print(self.driver.get_performance_data_types())
        for p in self.driver.get_performance_data_types():
            try:
                print(self.driver.get_performance_data("io.appium.android.apis", p, 5))
            except:
                pass

    def teardown(self):
        self.driver.quit()
