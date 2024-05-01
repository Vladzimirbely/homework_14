import pytest
from pages.github import GithubPage
from selene import browser

@pytest.fixture(params=['desktop', 'mobile'])
def driver(request):
    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    else:
        browser.config.window_width = 400
        browser.config.window_height = 700

    yield
    browser.quit()

@pytest.mark.parametrize('driver', ['desktop'], indirect=True)
def test_github_desktop(driver):
    github_page = GithubPage()
    github_page.open()
    github_page.click_on_sign_in_desktop()
    github_page.should_have_text_sign_in()

@pytest.mark.parametrize('driver', ['mobile'], indirect=True)
def test_github_mobile(driver):
    github_page = GithubPage()
    github_page.open()
    github_page.click_on_sign_in_mobile()
    github_page.should_have_text_sign_in()
