import json # JSON parsing
import wget # Downloading files
import os # Handling folders, paths and directories
import zipfile # Decompressing zip files
import requests # Reading content of files hosted in the cloud
from shutil import rmtree # Tool for removing an entire folder

"""
https://sites.google.com/site/gdocs2direct/home
Use the following website above to convert google drive links into files that the program can use to read values directly from the cloud
or allow downloading files from a direct link.
"""

def error(message):
    """Display the captured error and stops the program for the user to view it and get in touch with the developer.
    Args:
    * message (string): A message to display, for example what caused the error.
    """
    print(f"An error has been found:\n{message}")
    print("Please try again or contact the developer https://github.com/gann4life")
    input()
    quit()

class Software:
    """Base class for the software updater application.
    Params:
    * data_path (string) : Folder name which contains all the application files.
    * config_file (string) : File name which contains the application config settings (inside data_path)
    """
    def __init__(self, data_path, config_file):

        self.config_file = config_file
        self.data_path = data_path

        self.json_config = json.loads(open(data_path + config_file, "r").read())

        self.FILE = self.get_config("software_file")
        self.EXEC_PATH = self.get_config("software_executable_path")
        self.INSTALL_PATH = self.get_config("software_install_path")
        self.NAME = self.get_config("software_name")
        self.PREFIX = self.get_config("software_prefix")

        self.VERSION_FILE = self.get_config("version_file")
        self.VERSION_PATH = self.get_config("version_path")

        self.setup_directories()
        self.verify_installation()
        self.verify_updates()
        self.launch_software()

    # GETTERS

    def get_config(self, param):
        """Returns the value of the parameter in the json file"""
        return self.json_config[param]

    def get_software_local_version(self):
        """Returns the currently installed version installed of the software."""

        if not os.path.exists(self.in_data(self.VERSION_PATH)):
            print(f"WARNING: The {self.PREFIX.lower()} seems to be installed, but the version text file was not found.\nA reinstall will be initialized.")
            return None
        else:
            return open(self.in_data(self.VERSION_PATH), "r").read()

    def get_software_cloud_version(self):
        """Returns the software's version stored in the cloud."""

        return requests.get(self.VERSION_FILE).content.decode()

    def is_software_downloaded(self):
        """Checks if the software from the configuration file has been downloaded.
        Returns: bool"""
        return os.path.exists(self.in_data(self.EXEC_PATH))

    def is_software_updated(self):
        """Checks if the software is up to date.
        Returns: bool"""

        print(f"Checking if the {self.PREFIX} is up to date...")
        return self.get_software_cloud_version() == self.get_software_local_version()

    # PROCESSING

    def in_data(self, path):
        """Returns a path relative to the updater's data folder."""

        return self.data_path + path

    def in_app(self, path=""):
        """Returns a path relative to the software's folder."""
        return self.data_path + self.INSTALL_PATH + path

    # ACTIONS
    
    def setup_directories(self):
        """Creates the required directories for the software."""

        if not os.path.exists(self.in_data(self.INSTALL_PATH)):
            print(f"Setting up directories for {self.NAME}")
            os.mkdir(self.in_data(self.INSTALL_PATH))

    def verify_installation(self):  
        """Executes installation verification."""

        if not self.is_software_downloaded():
            print(f"INSTALL REQUIRED: {self.EXEC_PATH} was not found.")
            self.download_software()

    def verify_updates(self):
        """Executes updates verification."""

        print(f"{self.EXEC_PATH} exists. Checking for updates...")

        if not self.is_software_updated():
            print("\nNew update was found, updating...")
            self.update_software()

    def download_software(self):
        """Downloads the software"""

        print(f"Downloading {self.PREFIX.lower()}...")
        
        filename = self.download_overriding(self.FILE, ".\\App.zip")
        self.extract_zip(filename)
        self.download_version_file()

    def update_software(self):
        """Updates the software version."""
        print(f"Updating {self.NAME}...")
        self.uninstall_software()
        self.download_software()

    def uninstall_software(self):
        """Removes all files inside the software's folder."""

        print(f"\nUninstalling {self.PREFIX.lower()}...")
        rmtree(self.in_data(self.INSTALL_PATH))

    def extract_zip(self, path):
        """Extracts the contents of the .zip file into software install path.
        Args:
        * path (string): Path of the .zip file to extract.
        """
        
        print(f"\nExtracting {path} to {self.INSTALL_PATH}")
        zip_file = zipfile.ZipFile(path)
        zip_file.extractall(path=self.in_data(self.INSTALL_PATH))

    def launch_software(self):
        """Executes the software"""

        print(f"\nLaunching {self.EXEC_PATH}")
        os.startfile(self.in_data(self.get_config("software_executable_path")))

    def download_version_file(self):
        """Downloads the version file into the data folder."""

        self.download_overriding(self.VERSION_FILE, self.in_data(self.VERSION_PATH))

    def download_overriding(self, url, path):
        """Downloads a file and overrides the existing file if it exists.
        Args:
        url (string): The url to download the file from.
        path (string): The path to download the file into.  
        """

        if os.path.exists(path): os.remove(path)
        return wget.download(url, out=path)

# Execute the program, if any error is captured, show the error into the console and display a way to contact the developer.
try: updater = Software(".\\data", "\\config.json")
except Exception as e: error(e)

