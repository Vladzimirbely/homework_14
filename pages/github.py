from selene import browser, have

class GithubPage:
    def open(self):
        browser.open('https://github.com')
        return self

    def click_on_sign_in_desktop(self):
        browser.element('.HeaderMenu-link--sign-in').click()

    def click_on_sign_in_mobile(self):
        browser.element('.Button-label').click()
        browser.element('.HeaderMenu-link--sign-in').click()

    def should_have_text_sign_in(self):
        browser.element('h1').should(have.text('Sign in to GitHub'))

github_page = GithubPage()
