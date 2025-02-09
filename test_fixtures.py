from selene import browser, be, have


def test_first(setting_browser):
    browser.open("https://www.google.com/")


def test_second(setting_browser):
    browser.open("https://www.google.com/")


def test_failed_search():
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').should(be.blank).type('ghhaytytehejoljdjdosnghi').press_enter()
    browser.element('[role="heading"]').should(have.text('ничего не найдено'))
