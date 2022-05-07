import json # JSON parsing
import wget # Downloading files
import os # Handling folders, paths and directories
import zipfile # Decompressing zip files
import shutil # Tool for removing an entire folder
import requests # Reading content of files hosted in the cloud

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

class SoftwareUpdater:
    """Base class for the software updater application.
    Params:
    * data_path (string) : Folder name which contains all the application files.
    * config_file (string) : File name which contains the application config settings (inside data_path)
    """
    def __init__(self, data_path, config_file):

        self.config_file = config_file
        self.data_path = data_path

        with open(data_path + config_file, "r") as f:
            json_content = json.loads(f.read())

            self.software_file = json_content["software_file"]
            self.software_executable_path = json_content["software_executable_path"]
            self.software_install_path = json_content["software_install_path"]
            self.software_name = json_content["software_name"]

            self.version_file = json_content["version_file"]
            self.version_path = json_content["version_path"]

            self.setup_directories()
            self.verify_installation()
            self.verify_updates()
            self.launch_software()

    def is_software_downloaded(self):
        """Checks if the software from the configuration file has been downloaded.
        Returns: bool"""
        return os.path.exists(self.path_inside_data(self.software_install_path))

    def is_software_updated(self):
        """Checks if the software is up to date.
        Returns: bool"""

        print("Checking if the software is up to date...")
        return self.get_software_cloud_version() == self.get_software_local_version()

    def verify_installation(self):  
        """Executes installation verification."""

        if not os.path.exists(self.path_inside_data(self.software_executable_path)):
            print(f"{self.software_executable_path} was not found. Installation required.")
            self.download_software()

    def verify_updates(self):
        """Executes updates verification."""

        print(f"{self.software_executable_path} exists. Checking for updates...")

        if not self.is_software_updated():
            print("\nNew update was found, updating...")
            self.update_software()

    def update_software(self):
        """Updates the software version."""
        self.uninstall_software()
        self.download_software()

    def uninstall_software(self):
        """Removes all files inside the software's folder."""

        print("\nUninstalling software...")
        shutil.rmtree(self.path_inside_data(self.software_install_path))

    # Downloads the file from the link used in config.json
    def download_software(self):
        """Downloads the software"""

        print("Downloading software")
        # filename = wget.download(self.software_file)
        filename = self.download_overriding(self.software_file, ".\\App.zip")
        self.extract_zip(filename)
        self.download_version_file()

    # Extracts the contents of the .zip file into software insall path.
    def extract_zip(self, path):
        """Extracts the contents of the .zip file into software install path.
        Args:
        * path (string): Path of the .zip file to extract.
        """
        print(f"\nExtracting {path} to {self.software_install_path}")
        zip_file = zipfile.ZipFile(path)
        zip_file.extractall(path=self.path_inside_data(self.software_install_path))

    def launch_software(self):
        """Executes the software"""

        print(f"\nLaunching {self.software_executable_path}")
        os.startfile(self.path_inside_data(self.software_executable_path))

    def path_inside_data(self, path):
        """Returns a path relative to the updater's data folder."""
        return self.data_path + path

    def get_software_local_version(self):
        """Returns the currently installed version installed of the software."""
        return open(self.path_inside_data(self.version_path), "r").read()

    def get_software_cloud_version(self):
        """Returns the software's version stored in the cloud."""
        return requests.get(self.version_file).content.decode()

    def download_version_file(self):
        """Downloads the version file into the data folder."""

        self.download_overriding(self.version_file, self.path_inside_data(self.version_path))

    def setup_directories(self):
        """Creates the required directories for the software."""

        if not os.path.exists(self.path_inside_data(self.software_install_path)):
            print("Setting up folders...")
            os.mkdir(self.path_inside_data(self.software_install_path))

    def download_overriding(self, url, path):
        """Downloads a file and overrides the existing file if it exists.
        Args:
        url (string): The url to download the file from.
        path (string): The path to download the file into.
        """

        if os.path.exists(path): os.remove(path)
        return wget.download(url, out=path)

# Execute the program, if any error is captured, show the error into the console and display a way to contact the developer.
try: updater = SoftwareUpdater(".\\data", "\\config.json")
except Exception as e: error(e)

