from naxi.browser import Browser



browser = Browser()
browser.navigate_url(url='https://mekar-test.xyz/accounts/login/')
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

from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'lang_english')))
