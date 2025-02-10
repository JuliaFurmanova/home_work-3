import pytest
from selene import browser, be, have


@pytest.fixture(autouse=True)
def setting_browser():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    browser.open("https://www.google.com/")
    yield
    browser.quit()


def test_sucsess_search():
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').should(be.blank).type('собака').press_enter()
    browser.element('[role="heading"]').should(have.text('Собака'))


def test_failed_search():
    browser.open("https://www.google.com/")
    browser.element('[name="q"]').should(be.blank).type('ghhaytytehejoljdjdosnghi').press_enter()
    browser.element('[role="heading"]').should(have.text('ничего не найдено'))
