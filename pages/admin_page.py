from playwright.sync_api import Page
from pages.base_page import BasePage

class AdminPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._username_search = page.get_by_role("textbox").nth(1)
        self._search_button = page.get_by_role("button", name="Search")
        self._search_results = page.locator(".oxd-table-body")

    def search_user(self, username):
        self.fill(self._username_search, username)
        self.click(self._search_button)

    def get_search_results(self):
        return self._search_results
