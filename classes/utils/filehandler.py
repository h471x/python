import os
from sys import path
from os.path import abspath as abs, join as jn, dirname as dir

class FileHandler:
    def __init__(self, destination):
        self.destination = abs(jn(dir(__file__), '..', '..', destination))
        if not os.path.exists(self.destination):
            os.makedirs(self.destination)

    def get_file_path(self, file):
        return jn(self.destination, file)

    def is_blank(self, file):
        file_path = self.get_file_path(file)
        file_exists = os.path.exists(file_path)

        if not file_exists:
            return True

        file_is_blank = os.path.getsize(file_path) == 0
        return file_is_blank

    def create_blank_file(self, file):
        created_file = self.get_file_path(file)
        with open(created_file, 'w'):
            pass
        return created_file

    def write_file(self, file, content):
        file_path = self.get_file_path(file)
        if self.is_blank(file_path):
            self.create_blank_file(file)
        with open(file_path, 'w') as f:
            f.write(content)
