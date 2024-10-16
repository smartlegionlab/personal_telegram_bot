# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import json
import os


class ConfigLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = {}

    def load_config(self):
        if not self._file_exists():
            print(f"Error: File '{self.file_path}' not found. Please create it.")
            return False

        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self.config = json.load(file)

            if not self._validate_config():
                return False

            return True

        except json.JSONDecodeError:
            print("Error: Invalid JSON format in file. Please check syntax.")
            return False
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False

    def _file_exists(self):
        return os.path.exists(self.file_path)

    def _validate_config(self):
        required_keys = ['name', 'description', 'url']
        for key in required_keys:
            if key not in self.config:
                print(f"Error: Missing key '{key}' in configuration.")
                return False
        return True

    def get_company_name(self):
        return self.config.get('name')

    def get_company_description(self):
        return self.config.get('description')

    def get_company_url(self):
        return self.config.get('url')
