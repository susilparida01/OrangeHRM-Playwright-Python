from playwright.sync_api import Playwright, Browser, BrowserType

class PlaywrightFactory:
    @staticmethod
    def get_browser(playwright: Playwright, browser_name: str, headless: bool = True) -> Browser:
        browser_name = browser_name.lower()
        
        if browser_name == "chrome":
            return playwright.chromium.launch(headless=headless, channel="chrome")
        elif browser_name == "edge":
            return playwright.chromium.launch(headless=headless, channel="msedge")
        elif browser_name == "firefox":
            return playwright.firefox.launch(headless=headless)
        elif browser_name == "safari" or browser_name == "webkit":
            return playwright.webkit.launch(headless=headless)
        elif browser_name == "chromium":
            return playwright.chromium.launch(headless=headless)
        else:
            raise ValueError(f"Unsupported browser: {browser_name}. Supported: chrome, edge, firefox, safari, chromium")
