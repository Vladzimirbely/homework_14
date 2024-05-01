import pytest
from selene import browser
from pages.github import GithubPage

@pytest.fixture
def desktop():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield
    browser.quit()

@pytest.fixture
def mobile():
    browser.config.window_width = 400
    browser.config.window_height = 700

    yield
    browser.quit()

def test_github_desktop(desktop):
    github_page = GithubPage()
    github_page.open()
    github_page.click_on_sign_in_desktop()
    github_page.should_have_text_sign_in()

def test_github_mobile(mobile):
    github_page = GithubPage()
    github_page.open()
    github_page.click_on_sign_in_mobile()
    github_page.should_have_text_sign_in()
