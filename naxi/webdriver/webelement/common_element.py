import attr
from alog import debug

@attr.s
class Common_element:
    def __attrs_post_init__(self):
        pass

    def check_url(self, driver):
        return driver.current_url

    def close_browser(self, driver):
        driver.close()

    def get_value(self, element):
        try:
            return element.get_attribute('value')
        except Exception as Argument:
            return False
            raise ValueError(Argument)

    def get_text(self, element):
        try:
            return element.text
        except Exception as Argument:
            return False
            raise ValueError(Argument)
