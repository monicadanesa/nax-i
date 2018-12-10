import attr
from alog import debug, error
from selenium import webdriver
from selenium.webdriver import ActionChains
from naxi.webdriver.driver.chrome import Chrome as ChromeDriver
from naxi.webdriver.driver.firefox import Firefox as FirefoxDriver
from naxi.webdriver.webelement.common_element import Common_element
from naxi.webdriver.webelement.element import Element

@attr.s
class Browser:
    def __attrs_post_init__(self):
        self.driver = None
        self.ce = Common_element()
        self.el = Element()

    def open_browser(self, url, driver_name='firefox', **kwargs):
        if driver_name == 'chrome':
            try:
                chrome = ChromeDriver()
                self.driver = chrome.chrome_driver(**kwargs)
            except KeyError:
                raise DriverNotFound('driver is not found' + driver_name)
        elif driver_name == 'firefox':
            try:
                firefox = FirefoxDriver()
                self.driver = firefox.firefox_driver(**kwargs)
            except KeyError:
                raise DriverNotFound('driver is not found' + driver_name)

        self.running_browser = self.driver.get(url)
        return self.driver

    def check_current_url(self):
        return self.ce.check_url(self.driver)

    def close_browser(self):
        return self.ce.close_browser(self.driver)

    def find_by(self, **kwargs):
        if 'id' in kwargs:
            element = 'id'
            element_value = kwargs.get('id')
        elif 'name' in kwargs:
            element = 'name'
            element_value = kwargs.get('name')
        elif 'css' in kwargs:
            element = 'css'
            element_value = kwargs.get('css')
        elif 'xpath' in kwargs:
            element = 'xpath'
            element_value = kwargs.get('xpath')
        elif 'link' in kwargs:
            element = 'link_text'
            element_value = kwargs.get('link')
        else:
            error('element cannot be found')

        return self.el.find_element(self.driver, element, element_value)
