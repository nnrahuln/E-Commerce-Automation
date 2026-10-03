from playwright.sync_api import Page

from utils.config import BASE_URL


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_button = page.locator("#login-button")

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()