from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWeb:

    def setup(self):
        caps={}
        caps["browserName"]="chrome"
        caps["deviceName"]="hogwarts"
        caps["platformName"]="android"
        caps["chromedriverExecutable"] = "/Users/seveniruby/projects/chromedriver/2.34/chromedriver"
        caps["showChromedriverLog"] = True
        # caps["noReset"]=True


        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_testerhome_search(self):
        self.driver.get("https://testerhome.com")
        self.driver.switch_to.context("NATIVE_APP")
        self.driver.find_element_by_id("com.android.chrome:id/button_secondary").click()
        self.driver.switch_to.context(self.driver.contexts[1])
        print(self.driver.current_context)
        print(self.driver.page_source)
        # self.driver.find_element_by_link_text("Sign In").click()

        self.driver.find_element_by_css_selector("#mobile-search-form > input").send_keys("hogwarts")
