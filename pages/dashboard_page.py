from playwright.sync_api import Page
from pages.base_page import BasePage

class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._header = page.get_by_role("heading", name="Dashboard")
        self._user_dropdown = page.locator(".oxd-userdropdown-name")
        self._logout_link = page.get_by_role("menuitem", name="Logout")
        self._pim_menu = page.get_by_role("link", name="PIM")
        self._admin_menu = page.get_by_role("link", name="Admin")

    def is_dashboard_visible(self):
        return self.is_visible(self._header)

    def get_header(self):
        return self._header

    def logout(self):
        self.click(self._user_dropdown)
        self.click(self._logout_link)

    def navigate_to_pim(self):
        self.click(self._pim_menu)

    def navigate_to_admin(self):
        self.click(self._admin_menu)
