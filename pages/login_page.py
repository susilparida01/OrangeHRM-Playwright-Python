from playwright.sync_api import Page
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._username_input = page.get_by_placeholder("Username")
        self._password_input = page.get_by_placeholder("Password")
        self._login_button = page.get_by_role("button", name="Login")
        self._error_message = page.get_by_text("Invalid credentials")
        self._forgot_password_link = page.get_by_text("Forgot your password?")
        self._reset_password_header = page.get_by_role("heading", name="Reset Password")

    def login(self, username, password):
        self.fill(self._username_input, username)
        self.fill(self._password_input, password)
        self.click(self._login_button)

    def get_error_message(self):
        return self._error_message

    def click_forgot_password(self):
        self.click(self._forgot_password_link)

    def get_reset_password_header(self):
        return self._reset_password_header
