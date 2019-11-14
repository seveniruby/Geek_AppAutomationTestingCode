import datetime
from time import sleep

import pytest
import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *

from page.app import App
from page.search_page import SearchPage


class TestDemo:

    def setup(self):
        self.search_page=App.start().to_search()

    def test_search_po(self):
        self.search_page.search("alibaba")
        assert self.search_page.get_current_price() > 10

    def teardown(self):
        App.quit()







