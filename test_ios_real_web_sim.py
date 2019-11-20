from time import sleep

from appium import webdriver


class TestIOS:

    def setup(self):
        caps = {}
        caps["platformName"] = "ios"
        # caps[
        #     "app"] = "/Users/seveniruby/Library/Developer/Xcode/DerivedData/UICatalog-dfavfehsvaabuqdpmxouzqphclvl/Build/Products/Debug-iphonesimulator/UICatalog.app"
        caps["automationName"] = "xcuitest"
        caps["deviceName"] = "iPhone X"
        caps["platformVersion"] = "11.0"
        #
        # caps["deviceName"] = "seveniruby ipad"
        # caps["udid"] = "9df22446af15919c494c85b4c1c8b00eaa3a5bd0"
        # caps["startIWDP"] = True
        caps["browserName"] = "Safari"
        #
        # caps["xcodeOrgId"] = "96NJEQL7Y2"
        # caps["xcodeSigningId"] = "iPhone Developer"
        # caps[
        #     "app"] = "/Users/seveniruby/Library/Developer/Xcode/DerivedData/UICatalog-dfavfehsvaabuqdpmxouzqphclvl/Build/Products/Debug-iphoneos/UICatalog.app"

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)
    def test_web_testerhome(self):
        self.driver.get("https://testerhome.com")
        print(self.driver.page_source)
        sleep(2)
        self.driver.save_screenshot("首页.png")
        self.driver.find_element_by_partial_link_text("MTSC2019").click()
        sleep(2)
        self.driver.save_screenshot("MTSC2019.png")

    def teardown(self):
        # sleep(10)
        self.driver.quit()
