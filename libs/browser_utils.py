from playwright.sync_api import Page

class BrowserUtils:
    @staticmethod
    def get_page_title(page: Page):
        return page.title()

    @staticmethod
    def take_screenshot(page: Page, path: str):
        page.screenshot(path=path)
