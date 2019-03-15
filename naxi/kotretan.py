from naxi.browser import Browser



browser = Browser()
browser.navigate_url(url='https://www.google.com/', driver_name='chrome')

browser.keyboard_move(key_up='keys.Keys.C')
browser.navigate_url(url='https://pypi.org/project/attrs/')
browser.check_current_url()
browser.find_by(id='inline-display-name')
browser.wait_title_contains('Stack Overflow - Where Developers Learn, Share, & Build Careers')
element = browser.find_by(xpath="//label[contains(text(),'E-mail')]")
element_2 = browser.find_by(id='id_login')
element_2.send_keys('coba')
element_2.get_attribute('value')

element.text
element = browser.send_value(id='id-search-field',value='test')
element = browser.find_by(id='id-search-field')
element.text


browser.get_value(xpath='/html/body/div[1]/div[3]/div/section/form/p/input[1]')
print(result)
browser.wait_element_by(id='lang_english', time=10)
browser.click(id="a")

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

selenium_grid_url = "http://198.0.0.1:4444/wd/hub"
DesiredCapabilities
# Create a desired capabilities object as a starting point.
capabilities = DesiredCapabilities.FIREFOX.copy()
capabilities['platform'] = "WINDOWS"
capabilities['version'] = "10"

# Instantiate an instance of Remote WebDriver with the desired capabilities.
driver = webdriver.Remote(desired_capabilities=capabilities,
                          command_executor=selenium_grid_url)
