from time import sleep

from appium import webdriver


class TestIOS:

    def setup(self):
        caps = {}
        caps["platformName"] = "ios"
        caps[
            "app"] = "/Users/seveniruby/Library/Developer/Xcode/DerivedData/UICatalog-dfavfehsvaabuqdpmxouzqphclvl/Build/Products/Debug-iphonesimulator/UICatalog.app"
        caps["automationName"] = "xcuitest"
        caps["deviceName"] = "iPhone X"
        caps["platformVersion"] = "11.0"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def test_buttons(self):
        el1 = self.driver.find_element_by_accessibility_id("Buttons")
        el1.click()

    def teardown(self):
        sleep(20)
        self.driver.quit()
