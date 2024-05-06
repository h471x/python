import subprocess
from .filecreator import FileGenerator

class InitFilesGenerator:
    def __init__(self, file):
        self.file = file

    def runShell(self):
        try:
            subprocess.check_call(['bash', self.file])
        except subprocess.CalledProcessError as e:
            print(f"Error executing {self.file}: {e}")
