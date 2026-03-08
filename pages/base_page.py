from playwright.sync_api import Page, Locator, expect
from libs.logger import Logger

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.log = Logger.get_logger(self.__class__.__name__)

    def navigate(self, url: str):
        self.log.info(f"Navigating to: {url}")
        self.page.goto(url)

    def click(self, locator: Locator):
        self.log.info(f"Clicking on element: {locator}")
        locator.click()

    def fill(self, locator: Locator, text: str):
        self.log.info(f"Filling text '{text}' into: {locator}")
        locator.fill(text)

    def get_text(self, locator: Locator) -> str:
        text = locator.inner_text()
        self.log.info(f"Retrieved text: '{text}' from: {locator}")
        return text

    def is_visible(self, locator: Locator) -> bool:
        visible = locator.is_visible()
        self.log.info(f"Element visibility check for {locator}: {visible}")
        return visible

    def wait_for_selector(self, selector: str, state: str = "visible"):
        self.log.info(f"Waiting for selector: {selector} with state: {state}")
        self.page.wait_for_selector(selector, state=state)

    def expect_to_be_visible(self, locator: Locator):
        self.log.info(f"Expecting element to be visible: {locator}")
        expect(locator).to_be_visible()

    def get_title(self) -> str:
        title = self.page.title()
        self.log.info(f"Page title retrieved: {title}")
        return title

    def take_screenshot(self, name: str):
        path = f"reports/screenshots/{name}.png"
        self.log.info(f"Taking screenshot at: {path}")
        self.page.screenshot(path=path)
