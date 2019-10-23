# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "seveniruby"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.xueqiu.android:id/home_search")
el1.click()

TouchAction(driver).long_press().move_to().release().perform();
driver.swipe()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("pdd")

driver.quit()
