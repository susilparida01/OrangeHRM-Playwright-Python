import pytest
import os
import platform
from datetime import datetime
from playwright.sync_api import sync_playwright
from libs.playwright_factory import PlaywrightFactory
from libs.config_reader import ConfigReader
from libs.report_manager import ReportManager

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", help="Browser name: chrome, edge, firefox, safari")
    parser.addoption("--headless_mode", action="store", help="Headless mode: True or False")

def pytest_configure(config):
    # Initialize report directories
    ReportManager.initialize_reports()
    
    # Load configuration
    cfg = ConfigReader()
    base_url = cfg.application_url
    
    # Set timestamped report path
    report_path = os.path.join("reports", "report", f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html")
    config.option.htmlpath = report_path
    config.option.self_contained_html = True
    
    # Add metadata to HTML report
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]['Project Name'] = 'OrangeHRM Automation'
        config.stash[metadata_key]['Base URL'] = base_url
        config.stash[metadata_key]['Framework'] = 'Playwright-Python (POM)'
        config.stash[metadata_key]['OS'] = platform.system()
        config.stash[metadata_key]['Execution Time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@pytest.hookimpl(tryfirst=True)
def pytest_html_report_title(report):
    report.title = "Test Execution Report"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"<h2>OrangeHRM Automation Report</h2>"])

@pytest.fixture(scope="session")
def config():
    return ConfigReader()

@pytest.fixture(scope="function")
def page(request, config):
    # Use command line option if provided, else use config file value
    browser_name = request.config.getoption("--browser_name")
    if not browser_name:
        browser_name = config.browser_name
        
    headless_opt = request.config.getoption("--headless_mode")
    if headless_opt:
        headless = headless_opt.lower() == "true"
    else:
        headless = config.headless_mode.lower() == "true"
    
    with sync_playwright() as p:
        browser = PlaywrightFactory.get_browser(p, browser_name, headless)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()
