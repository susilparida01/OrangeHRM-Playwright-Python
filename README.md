# Playwright Python Automation for OrangeHRM

This repository contains Playwright-Python automation tests for the OrangeHRM demo site.

## Prerequisites

- Python 3.10+
- `pip`

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - **Windows:** `.\venv\Scripts\activate`
   - **Unix/macOS:** `source venv/bin/activate`

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Playwright browsers:
   ```bash
   playwright install chromium
   ```

## Running Tests

To run the tests, execute:
```bash
pytest
```

The tests are configured to run in Chromium with a 1-second delay (`slowmo 1000`) for visibility, as specified in `pytest.ini`.

## Test Scenarios

- **test_login_success:** Verifies successful login with valid credentials (`Admin` / `admin123`).
- **test_login_failure:** Verifies the error message when using invalid credentials.
