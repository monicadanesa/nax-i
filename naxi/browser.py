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

    def navigate_url(self, url, driver_name='firefox', **kwargs):
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

    def __element_template(self, **kwargs):
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
        elif 'class' in kwargs:
            element = 'class_name'
            element_value = kwargs.get('class')
        else:
            error('element '+ element_value + 'cannot be found')

        time = kwargs.get('time')
        dictionary_element = {'element':element, 'element_value':element_value, 'time':time}
        return dictionary_element

    def find_by(self, **kwargs):
        get_element = self.__element_template(**kwargs)
        element = get_element.get('element')
        element_value = get_element.get('element_value')

        return self.el.find_element(self.driver, element, element_value)

    def wait_title_contains(self, title):
        return self.el.title_contains(self.driver, title)

    def wait_element_by(self, **kwargs):
        get_element = self.__element_template(**kwargs)
        element = get_element.get('element')
        element_value = get_element.get('element_value')
        time = get_element.get('time')

        return self.el.wait_element(self.driver, element.upper(), element_value, time)

    def click(self, **kwargs):
        element_for_click = self.find_by(**kwargs)
        return self.el.action_click_element(
        self.driver, element_for_click,
        type_action='click')

    def click_and_hold(self, **kwargs):
        element_for_click = self.find_by(**kwargs)

        return self.el.action_click_element(
        self.driver, element_for_click,
        type_action='click_and_hold')

    def double_click(self, **kwargs):
        element_for_click = self.find_by(**kwargs)

        return self.el.action_click_element(
        self.driver, element_for_click,
        type_action='double_click')

    def send_value(self, **kwargs):
        element_for_input = self.find_by(**kwargs)

        if 'value' in kwargs is None:
            return False
            error('The value is empty, please input the value')
        else:
            value = kwargs.get('value')
            return self.el.type(element_for_input, value)

    def get_value(self, **kwargs):
        element_for_get_value = self.find_by(**kwargs)
        return self.ce.get_value(element_for_get_value)

    def get_text(self, **kwargs):
        element_for_get_text = self.find_by(**kwargs)
        return self.ce.get_text(element_for_get_text)
