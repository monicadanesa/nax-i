from naxi.browser import Browser


browser = Browser()
browser.open_browser(url='https://stackoverflow.com/')
browser.check_current_url()
browser.find_by(saaas='inline-display-name')
