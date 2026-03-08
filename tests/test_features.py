import pytest
import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.admin_page import AdminPage
from pages.pim_page import PIMPage

def test_logout(page: Page, config):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    login_page.navigate(config.application_url)
    login_page.login(config.admin_username, config.admin_password)
    
    # Action: Logout
    dashboard_page.logout()
    
    # Assert: Redirected to login page
    expect(page).to_have_url(re.compile(r".*login.*"))

def test_admin_search_user(page: Page, config):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    admin_page = AdminPage(page)
    
    login_page.navigate(config.application_url)
    login_page.login(config.admin_username, config.admin_password)
    
    # Action: Navigate to Admin and Search
    dashboard_page.navigate_to_admin()
    admin_page.search_user("Admin")
    
    # Assert: Search results contain "Admin"
    expect(admin_page.get_search_results()).to_contain_text("Admin")

def test_pim_add_employee(page: Page, config):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    pim_page = PIMPage(page)
    
    login_page.navigate(config.application_url)
    login_page.login(config.admin_username, config.admin_password)
    
    # Action: Navigate to PIM and Add Employee
    dashboard_page.navigate_to_pim()
    pim_page.add_employee("John", "Doe")
    
    # Assert: Success toast is visible (or partially visible text)
    expect(pim_page.get_success_toast()).to_be_visible()

def test_forgot_password_navigation(page: Page, config):
    login_page = LoginPage(page)
    
    login_page.navigate(config.application_url)
    
    # Action: Click Forgot Password
    login_page.click_forgot_password()
    
    # Assert: Redirected to Reset Password page
    expect(login_page.get_reset_password_header()).to_be_visible()

def test_dashboard_menu_visibility(page: Page, config):
    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    
    login_page.navigate(config.application_url)
    login_page.login(config.admin_username, config.admin_password)
    
    # Assert: Various menu items are visible
    expect(page.get_by_role("link", name="Leave")).to_be_visible()
    expect(page.get_by_role("link", name="Time")).to_be_visible()
    expect(page.get_by_role("link", name="Recruitment")).to_be_visible()
    expect(page.get_by_role("link", name="Performance")).to_be_visible()
