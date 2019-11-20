from time import sleep

from appium import webdriver


class TestIOS:

    def setup(self):
        caps = {}
        caps["platformName"] = "ios"
        # caps[
        #     "app"] = "/Users/seveniruby/Library/Developer/Xcode/DerivedData/UICatalog-dfavfehsvaabuqdpmxouzqphclvl/Build/Products/Debug-iphonesimulator/UICatalog.app"
        caps["automationName"] = "xcuitest"
        # caps["deviceName"] = "iPhone X"
        # caps["platformVersion"] = "11.0"

        caps["deviceName"] = "seveniruby ipad"
        caps["udid"] = "9df22446af15919c494c85b4c1c8b00eaa3a5bd0"

        caps["xcodeOrgId"] = "96NJEQL7Y2"
        caps["xcodeSigningId"] = "iPhone Developer"
        caps[
            "app"] = "/Users/seveniruby/Library/Developer/Xcode/DerivedData/UICatalog-dfavfehsvaabuqdpmxouzqphclvl/Build/Products/Debug-iphoneos/UICatalog.app"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

    def test_buttons(self):
        el1 = self.driver.find_element_by_accessibility_id("Buttons")
        el1.click()

    def teardown(self):
        sleep(20)
        self.driver.quit()
