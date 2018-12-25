import pytest
from naxi.browser import Browser

browser = Browser()

def test_navigate_url():
    url = 'https://www.python.org/'
    browser.navigate_url(url)

def test_check_url():
    url = 'https://www.python.org/'
    current_url = browser.check_current_url()
    assert url == current_url

def test_find_by_id():
    result = browser.find_by(id='id-search-field')
    assert result is not False

def test_find_by_xpath():
    result = browser.find_by(xpath="//input[@id='id-search-field']")
    assert result is not False

def test_find_by_css():
    result = browser.find_by(css='#id-search-field')
    assert result is not False

def test_find_by_execeptions():
    result = browser.find_by(id='asal')
    assert result == False

def test_wait_title_contains():
    browser.wait_title_contains('Welcome to Python.org')
    assert True

def test_wait_title_contains_exceptions():
    result = browser.wait_title_contains('asal')
    assert result == False

def test_wait_element_by_id():
    browser.wait_element_by(id='id-search-field',  time=5)
    assert True

def test_wait_element_by_xpath():
    browser.wait_element_by(xpath="//input[@id='id-search-field']",  time=5)
    assert True

def test_wait_element_by_css():
    browser.wait_element_by(css='#id-search-field',  time=5)
    assert True

def test_wait_element_exeception():
    result = browser.wait_element_by(id='asal',  time=5)
    assert result is False

def test_send_value():
    result = browser.send_value(id='id-search-field', value='test')
    assert result is not False

def test_send_value_exceptions():
    result = browser.send_value(id='asal', value='test')
    assert result is False

def test_get_value():
    result = browser.get_value(id='id-search-field')
    assert result in 'test'

def test_get_value_exceptions():
    result = browser.get_value(id='asal')
    assert result is False

def test_click_by_id():
    browser.click(id="submit")
    current_url = browser.check_current_url()
    url = 'https://www.python.org/search/?q=test&submit='

    assert current_url == url

def test_click_by_xpath():
    browser.click(xpath="//button[@id='submit']")
    current_url = browser.check_current_url()
    url = 'https://www.python.org/search/?q=test&submit='

    assert current_url == url

def test_click_by_css():
    browser.click(css="#submit")
    current_url = browser.check_current_url()
    url = 'https://www.python.org/search/?q=test&submit='

    assert current_url == url

def test_click_by_no_such_element_exeception():
    result = browser.click(id="asal")
    assert 'error exception' in result

def test_double_click_by_id():
    browser.double_click(id="submit")
    current_url = browser.check_current_url()
    url = 'https://www.python.org/search/?q=test&submit='

    assert current_url == url

def test_double_click_by_xpath():
    browser.double_click(xpath="//button[@id='submit']")
    current_url = browser.check_current_url()
    url = 'https://www.python.org/search/?q=test&submit='

    assert current_url == url

def test_double_click_by_css():
    browser.double_click(css="#submit")
    current_url = browser.check_current_url()
    url = 'https://www.python.org/search/?q=test&submit='

    assert current_url == url
