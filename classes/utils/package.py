import subprocess

class PackageManager:

    @staticmethod
    def get_pkg():
        return 'config/libs/requirements.txt'

    def __init__(self, file_path):
        self.file_path = file_path

    def install(self):
        try:
            with open(self.file_path, 'r') as file:
                packages = file.readlines()
                for package in packages:
                    # Remove leading/trailing whitespace
                    package = package.strip()
                    if not self.is_installed(package):
                        self.pkg_install(package)
                    else:
                        print(f"{package} is already installed.")
        except FileNotFoundError:
            print(f"File {self.file_path} not found.")

    def is_installed(self, package_name):
        try:
            subprocess.check_output(['pip', 'show', package_name])
            return True
        except subprocess.CalledProcessError:
            return False

    def pkg_install(self, package_name):
        try:
            subprocess.check_call(['pip', 'install', package_name])
            print(f"Installed {package_name}.")
        except subprocess.CalledProcessError as e:
            print(f"Error installing {package_name}: {e}")
