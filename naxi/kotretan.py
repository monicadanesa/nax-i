from naxi.browser import Browser


browser = Browser()
browser.navigate_url(url='https://mekar-test.xyz/')
browser.check_current_url()
browser.find_by(saaas='inline-display-name')
browser.wait_title_contains('Stack Overflow - Where Developers Learn, Share, & Build Careers')
result = browser.find_by(id='lang_english')

print(result)
browser.wait_element_by(id='lang_english', time=10)
browser.click(xpath="//a[contains(text(),'Login')]")

from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'lang_english')))
