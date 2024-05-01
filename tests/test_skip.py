import pytest
from selene import browser
from pages.github import github_page

def test_github_desktop(driver_setup):
    if browser.config.window_width < 1000:
        pytest.skip('Test for mobile')
    github_page.open()
    github_page.click_on_sign_in_desktop()
    github_page.should_have_text_sign_in()


def test_github_mobile(driver_setup):
    if browser.config.window_width > 1000:
        pytest.skip('Test for desktop')
    github_page.open()
    github_page.click_on_sign_in_mobile()
    github_page.should_have_text_sign_in()
