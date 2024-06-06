import json
import os

class Storage:
    def __init__(self, file_name):
        self.file_name = file_name

    def load(self):
        if not os.path.exists(self.file_name):
            return []
        with open(self.file_name, 'r') as file:
            return json.load(file)

    def save(self, data):
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)
