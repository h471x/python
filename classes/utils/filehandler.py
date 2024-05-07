import os
from sys import path
from os.path import abspath as abs, join as jn, dirname as dir

class FileHandler:
    def __init__(self, destination):
        self.destination = abs(jn(dir(__file__), '..', '..', destination))
        if not os.path.exists(self.destination):
            os.makedirs(self.destination)

    def getFilePath(self, file):
        return jn(self.destination, file)

    def writeFile(self, file, content):
        filePath = self.getFilePath(file)
        if self.isBlank(filePath):
            self.createBlankFile(file)
        with open(filePath, 'w') as f:
            f.write(content)
