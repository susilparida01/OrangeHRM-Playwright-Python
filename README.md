# OrangeHRM Playwright-Python Automation Framework

This repository contains a professional, industrial-standard automation framework for testing the [OrangeHRM](https://opensource-demo.orangehrmlive.com/) demo application using **Playwright-Python** and **Pytest**.

## 🚀 Key Features

- **Page Object Model (POM):** Clean separation of UI locators, actions, and test logic.
- **Dynamic Configuration:** Manage URLs, credentials, browser selection, and headless mode via `config.properties`.
- **Browser Factory:** Supports Chrome, Firefox, Edge, and Safari (WebKit) out of the box.
- **Custom Logging:** Automated, timestamped logs for every test action, stored in `reports/logs`.
- **Advanced Reporting:**
  - Customized HTML reports with project-specific metadata (Project Name, Base URL, OS, Python Version).
  - Timestamped report filenames to preserve execution history.
  - Automatic screenshots and videos for failed tests.
- **Base Page Architecture:** Reusable generic methods for all Playwright interactions.

## 📁 Project Structure

```text
├── pages/                # Page Object classes (BasePage, LoginPage, etc.)
├── tests/                # Test suites (Login, Dashboard Features)
├── libs/                 # Utility classes (ConfigReader, Logger, PlaywrightFactory, ReportManager)
├── resources/config/     # Configuration files (config.properties)
├── reports/              # Test execution artifacts
│   ├── report/           # Timestamped HTML reports
│   ├── logs/             # Execution logs
│   └── screenshots/      # Screenshots for failed tests
├── pytest.ini            # Pytest configuration
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## 🛠 Prerequisites

- Python 3.10+
- `pip` (Python package manager)

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd PlaywrightAutomation
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Unix/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**
   ```bash
   playwright install chromium firefox webkit
   ```

## 📝 Configuration

You can customize the execution by modifying `resources/config/config.properties`:

- `browser_name`: `chrome`, `firefox`, `edge`, `safari`, or `chromium`.
- `headless_mode`: `True` or `False`.
- `application_url`: The base URL of the application.
- `admin_username` & `admin_password`: Default login credentials.

## 🏃 Running Tests

### Run all tests (Default config)
```bash
pytest
```

### Run with command-line overrides
```bash
# Run in headed mode
pytest --headless_mode False

# Run on a specific browser
pytest --browser_name firefox
```

## 📊 Viewing Reports

After execution, the HTML reports are generated in the `reports/report/` folder with names like `report_YYYYMMDD_HHMMSS.html`. Open these files in any web browser to see detailed results, environment metadata, and failure screenshots.

Logs are available in `reports/logs/` for deeper debugging.

## 🚀 CI/CD Integration (Jenkins)

To integrate this framework with Jenkins, follow these steps:

### 1. Prerequisites
- **Jenkins:** Installed and running.
- **Node Tools:** Python, Pip, and Git installed on the Jenkins agent/node.
- **Plugins:** Install the **HTML Publisher Plugin** in Jenkins to view the test reports.

### 2. Jenkins Pipeline Configuration
Create a new **Pipeline** job and use the following script (adjust for Linux/Windows agents):

```groovy
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/your-repo.git'
            }
        }
        
        stage('Setup Environment') {
            steps {
                // For Windows
                bat """
                python -m venv venv
                .\\venv\\Scripts\\activate
                pip install -r requirements.txt
                playwright install chromium
                """
            }
        }
        
        stage('Run Tests') {
            steps {
                // For Windows
                bat """
                .\\venv\\Scripts\\activate
                pytest
                """
            }
        }
    }
    
    post {
        always {
            // Publish the most recent HTML report
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'reports/report',
                reportFiles: '*.html',
                reportName: 'OrangeHRM Automation Report'
            ])
            // Optional: Archive logs and screenshots
            archiveArtifacts artifacts: 'reports/logs/*.log, reports/screenshots/*.png', allowEmptyArchive: true
        }
    }
}
```

### 3. Freestyle Project Configuration (Alternative)
1. **Source Code Management:** Select **Git** and provide your repository URL.
2. **Build Steps:** Add **Execute Windows batch command**:
   ```batch
   python -m venv venv
   call .\venv\Scripts\activate
   pip install -r requirements.txt
   playwright install chromium
   pytest
   ```
3. **Post-build Actions:** Add **Publish HTML reports**:
   - HTML directory to archive: `reports/report`
   - Index page[s]: `*.html`
   - Report title: `OrangeHRM Test Report`

---
*Created with ❤️ using Playwright and Pytest.*
