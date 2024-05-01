from pages.github import GithubPage

def test_github_desktop():
    github_page = GithubPage()
    github_page.open()
    github_page.click_on_sign_in_desktop()
    github_page.should_have_text_sign_in()


def test_github_mobile():
    github_page = GithubPage()
    github_page.open()
    github_page.click_on_sign_in_mobile()
    github_page.should_have_text_sign_in()
