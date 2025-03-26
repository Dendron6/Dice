from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("[data-testid='email-input'] input")
        self.password_input = page.locator("[data-testid='password-input'] input")
        self.continue_button = page.locator("[data-testid='sign-in-button']")
        self.sign_in_button = page.locator("[data-testid='submit-password']")

    def login(self, username, password):
        self.email_input.fill(username)
        self.continue_button.click()
        self.password_input.fill(password)
        self.sign_in_button.click()
