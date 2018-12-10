import attr
from alog import debug

@attr.s
class Element:
    def __attrs_post_init__(self):
        pass

    def find_element(self, driver, element, element_value):
        if element == 'id':
            try:
                return driver.find_element_by_id(element_value)
            except NameError:
                raise ElementNotFound('element is not found' + element_value)
        if element == 'name':
            try:
                return driver.find_element_by_name(element_value)
            except NameError:
                raise ElementNotFound('element is not found' + element_value)
        if element == 'css':
            try:
                return driver.find_element_by_css_selector(element_value)
            except NameError:
                raise ElementNotFound('element is not found' + element_value)
        if element == 'xpath':
            try:
                return driver.find_element_by_xpath(element_value)
            except NameError:
                raise ElementNotFound('element is not found' + element_value)
        if element == 'link_text':
            try:
                return driver.find_element_by_link_text(element_value)
            except NameError:
                raise ElementNotFound('element is not found' + element_value)
