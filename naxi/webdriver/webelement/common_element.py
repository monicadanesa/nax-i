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
