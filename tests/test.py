import pytest
from naxi.browser import Browser

browser = Browser()

def test_navigate_url():
    url = 'https://stackoverflow.com/'
    browser.navigate_url(url)

def test_check_url():
    url = 'https://stackoverflow.com/'
    current_url = browser.check_current_url()
    assert url == current_url

def test_find_by_id():
    result = browser.find_by(id='display-name')
    assert result is not False

def test_find_by_xpath():
    result = browser.find_by(xpath="//input[@id='display-name']")
    assert result is not False

def test_find_by_css():
    result = browser.find_by(css='#display-name')
    assert result is not False

def test_find_by_execeptions():
    result = browser.find_by(id='asal')
    assert result is False

def test_wait_title_contains():
    browser.wait_title_contains('Stack Overflow - Where Developers Learn, Share, & Build Careers')
    assert True

def test_wait_title_contains_exceptions():
    result = browser.wait_title_contains('asal')
    assert result == False

def test_wait_element_by_id():
    browser.wait_element_by(id='display-name',  time=5)
    assert True

def test_wait_element_by_xpath():
    browser.wait_element_by(xpath="//input[@id='display-name']",  time=5)
    assert True

def test_wait_element_by_css():
    browser.wait_element_by(css='#display-name',  time=5)
    assert True

def test_wait_element_exeception():
    result = browser.wait_element_by(id='asal',  time=5)
    assert result == False

def test_click_by_id():
    browser.click(id="submit-button")
    current_url = browser.check_current_url()
    url = 'https://stackoverflow.com/'

    assert current_url == url

def test_click_by_xpath():
    browser.click(xpath="//input[@id='submit-button']")
    current_url = browser.check_current_url()
    url = 'https://stackoverflow.com/'

    assert current_url == url

def test_click_by_css():
    browser.click(css="#submit-button")
    current_url = browser.check_current_url()
    url = 'https://stackoverflow.com/'

    assert current_url == url
