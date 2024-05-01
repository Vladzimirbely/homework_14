from pages.github import github_page

def test_github_desktop(desktop):
    github_page.open()
    github_page.click_on_sign_in_desktop()
    github_page.should_have_text_sign_in()

def test_github_mobile(mobile):
    github_page.open()
    github_page.click_on_sign_in_mobile()
    github_page.should_have_text_sign_in()
