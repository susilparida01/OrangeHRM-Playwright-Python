import os

class ConfigReader:
    def __init__(self, file_path="resources/config/config.properties"):
        self.config_data = {}
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        key, value = line.split("=", 1)
                        self.config_data[key.strip()] = value.strip()
        else:
            raise FileNotFoundError(f"Configuration file not found at {file_path}")

    def get_value(self, key):
        return self.config_data.get(key)

    @property
    def application_url(self):
        return self.get_value("application_url")

    @property
    def admin_username(self):
        return self.get_value("admin_username")

    @property
    def admin_password(self):
        return self.get_value("admin_password")

    @property
    def browser_name(self):
        return self.get_value("browser_name")

    @property
    def headless_mode(self):
        return self.get_value("headless_mode")
