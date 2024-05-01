import pytest
from selene import browser
from pages.github import GithubPage

@pytest.fixture(params=[(1920, 1080), (400, 700)])
def driver(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]

def test_github_desktop(driver):
    if browser.config.window_width < 1000:
        pytest.skip('Test for mobile')
    github_page = GithubPage()
    github_page.open()
    github_page.click_on_sign_in_desktop()
    github_page.should_have_text_sign_in()


def test_github_mobile(driver):
    if browser.config.window_width > 1000:
        pytest.skip('Test for desktop')
    github_page = GithubPage()
    github_page.open()
    github_page.click_on_sign_in_mobile()
    github_page.should_have_text_sign_in()
