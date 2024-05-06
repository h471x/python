import os
from sys import path
from os.path import abspath as abs, join as jn, dirname as dir

class FileGenerator:
    def __init__(self, destination):
        self.destination = abs(jn(dir(__file__), '..', '..', destination))
        if not os.path.exists(self.destination):
            os.makedirs(self.destination)

    def getFilePath(self, file):
        return jn(self.destination, file)

    def isBlank(self, file):
        filePath = self.getFilePath(file)
        fileExists = os.path.exists(filePath)

        if not fileExists:
            return True

        fileIsBlank = os.path.getsize(filePath) == 0
        return fileIsBlank

    def createBlankFile(self, file):
        createdFile = self.getFilePath(file)
        with open(createdFile, 'w') as file:
            pass
        return createdFile

    def writeFile(self, file, content):
        filePath = self.getFilePath(file)
        if self.isBlank(filePath):
            self.createBlankFile(file)
        with open(filePath, 'w') as f:
            f.write(content)
