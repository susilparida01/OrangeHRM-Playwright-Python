import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_success(page: Page, config):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    # Action: Navigate and Login
    login_page.navigate(config.application_url)
    login_page.login(config.admin_username, config.admin_password)
    
    # Assert: Dashboard is visible
    expect(dashboard_page.get_header()).to_be_visible()
    
def test_login_failure(page: Page, config):
    login_page = LoginPage(page)
    
    # Action: Navigate and Login with wrong credentials
    login_page.navigate(config.application_url)
    login_page.login("InvalidUser", "invalid123")
    
    # Assert: Error message is visible
    expect(login_page.get_error_message()).to_be_visible()
