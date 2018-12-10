import attr
from alog import debug
from selenium import webdriver
from selenium.webdriver import Firefox

@attr.s
class Firefox:
    def __attrs_post_init__(self):
        options=None,
        incognito=False,
        headless=False

    def firefox_driver(self, **kwargs):
        options = webdriver.FirefoxOptions()
        if 'headless' in kwargs:
            if kwargs.get('headless') == True:
                options.add_argument('-headless')
                debug('Browser Firefox and headless is True')
            else:
                debug('Browser Firefox and headless is False')

        driver = webdriver.Firefox(firefox_options=options)

        return driver
