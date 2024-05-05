import os
from sys import path
from os.path import abspath as abs, join as jn, dirname as dir

class FileGenerator():
    def __init__(self, destination):
        self.destination = abs(jn(dir(__file__), '..', '..', destination))
        if not os.path.exists(self.destination):
            os.makedirs(self.destination)

    def getFilePath(self, file):
        return jn(self.destination, file)

    def isBlank(self, file):
        filePath = self.getFilePath(file)
        fileExists = os.path.exists(filePath)
        fileSize = os.path.getsize(filePath)

        return not fileExists or fileSize == 0

    def createBlankFile(self, file):
        createdFile = self.getFilePath(file)
        with open(createdFile, 'w') as file:
            pass
        return createdFile

    def writeFile(self, file, content):
        filePath = self.getFilePath(file)
        if self.isBlank(file):
            self.createBlankFile(file)
        with open(filePath, 'w') as f:
            f.write(content)
