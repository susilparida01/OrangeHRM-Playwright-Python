import os
import shutil
from datetime import datetime

class ReportManager:
    REPORT_DIR = "reports"
    HTML_REPORT_DIR = os.path.join(REPORT_DIR, "report")
    LOG_DIR = os.path.join(REPORT_DIR, "logs")
    SCREENSHOT_DIR = os.path.join(REPORT_DIR, "screenshots")

    @classmethod
    def initialize_reports(cls):
        """Creates necessary directories for reporting."""
        for directory in [cls.HTML_REPORT_DIR, cls.LOG_DIR, cls.SCREENSHOT_DIR]:
            if not os.path.exists(directory):
                os.makedirs(directory)

    @classmethod
    def clean_reports(cls):
        """Deletes the entire reports directory to start fresh."""
        if os.path.exists(cls.REPORT_DIR):
            shutil.rmtree(cls.REPORT_DIR)
        cls.initialize_reports()

    @classmethod
    def get_report_name(cls):
        """Returns a timestamped report name."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return os.path.join(cls.HTML_REPORT_DIR, f"report_{timestamp}.html")
