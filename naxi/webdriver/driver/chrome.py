import attr
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from alog import debug

@attr.s
class Chrome:
    def __attrs_post_init__(self):
        options=None,
        user_agent=None,
        wait_time=2,
        fullscreen=False,
        incognito=False,
        headless=False

    def chrome_driver(self, **kwargs):
        options = Options()
        if 'headless' in kwargs:
            if kwargs.get('headless') is True:
                options.add_argument('--headless')
                options.add_argument('--disable-gpu')
                debug('Browser Chrome and headless is True')
            else:
                debug('Browser Chrome and headless is False')
        if 'fullscreen' in kwargs:
            if kwargs.get('fullscreen') is True:
                options.add_argument('--start-fullscreen')
                debug('Browser Chrome and fullscreen is True')
            else:
                debug('Browser Chrome and fullscreen is False')
        if 'incognito' in kwargs:
            if kwargs.get('incognito') is True:
                options.add_argument('--incognito')
                debug('Browser Chrome and incognito is True')
            else:
                debug('Browser Chrome and incognito is False')

        driver = webdriver.Chrome(chrome_options=options)

        return driver



# ch = Chrome()
# driver = ch.chrome_driver(headless=False)
# driver.get('https://docs.python.org/')
