import attr
from alog import debug
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.common.exceptions import NoSuchElementException


@attr.s
class Element:
    def __attrs_post_init__(self):
        pass

    def find_element(self, driver, element, element_value):
        try:
            if element == 'id':
                result = driver.find_element_by_id(element_value)
            if element == 'name':
                result = driver.find_element_by_name(element_value)
            if element == 'css':
                result = driver.find_element_by_css_selector(element_value)
            if element == 'xpath':
                result = driver.find_element_by_xpath(element_value)
            if element == 'link_text':
                result = driver.find_element_by_link_text(element_value)
            if element == 'class_name':
                result = driver.find_element_by_class_name(element_value)

            return result
        except NoSuchElementException:
            return False
            raise ValueError('element is not found on '+ element + element_value )

    def title_contains(self, driver, title):
        try:
            element_title_contains = WebDriverWait(driver, 10).until(
                                EC.title_contains((title)))
            return True
        except TimeoutException:
            return False
            raise ValueError('title is not found' + title)

    def wait_element(self, driver, element, element_value, time):
        wait = WebDriverWait(driver, time)
        try:
            if element == 'ID':
                result = wait.until(EC.presence_of_element_located((By.ID, element_value)))
            if element == 'XPATH':
                result = wait.until(EC.presence_of_element_located((By.XPATH, element_value)))
            if element == 'CSS':
                result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element_value)))
            if element == 'CLASS':
                result = wait.until(EC.presence_of_element_located((By.CLASS, element_value)))
            return True
        except TimeoutException:
            return False
            raise ValueError('The element cannot be found/ time out')

    def action_click_element(self, driver, element, type_action):
        try:
            if type_action == 'click':
                action_element = element.click()
                return action_element
            elif type_action == 'click_and_hold':
                action_element = ActionChains(driver).click_and_hold(element).perform()
            elif type_action == 'double_click':
                action_element = ActionChains(driver).double_click(element).perform()
        except WebDriverException:
            err_message = 'Unable to start webdriver'
            return err_message
            raise WebDriverError(err_message)
        except NoSuchElementException:
            err_message = 'The element cannot cannot be found'
            return err_message
            raise ValueError(err_message)
        except ElementClickInterceptedException:
            err_message = 'The Element Click command could not be completed because the element receiving the events'
            return err_message
            raise ValueError(err_message)

    def action_drag_element(self, driver, **kwargs):
        try:
            if 'from' in kwargs and 'to' in kwargs:
                return ActionChains(driver).drag_and_drop(
                kwargs.get('from'), kwargs.get('to')).perform()
        except WebDriverException:
            raise WebDriverError('Error from webdriver')
        except NoSuchElementException:
            raise ValueError('The element cannot be found')
        except MoveTargetOutOfBoundsException:
            raise ValueError('ActionsChains move method is invalid')
