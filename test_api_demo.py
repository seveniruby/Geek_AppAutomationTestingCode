import datetime
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
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




    def teardown(self):
        self.driver.quit()
