from playwright.sync_api import Page
from pages.base_page import BasePage

class PIMPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._add_button = page.get_by_role("button", name="Add")
        self._first_name = page.get_by_placeholder("First Name")
        self._last_name = page.get_by_placeholder("Last Name")
        self._save_button = page.get_by_role("button", name="Save")
        self._success_toast = page.get_by_text("Success", exact=True)

    def add_employee(self, first_name, last_name):
        self.click(self._add_button)
        self.fill(self._first_name, first_name)
        self.fill(self._last_name, last_name)
        self.click(self._save_button)

    def get_success_toast(self):
        return self._success_toast
