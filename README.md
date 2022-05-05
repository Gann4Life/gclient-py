# GClient-py
GClient-py is an application written in python that allows you to handle updates for your own software or games by setting parameters on a json file. <br>
C# and JS version will come after this gets finished.

# Disclaimer
I won't recommend using this right now as it is in constant development and unstable. <br>
I suggest to make your own fork or contribute to this repository.

# How it works
1. Verifies if the software has been installed/downloaded.
    1. `if YES`: verify if it is up to date
        1. `if NOT`: remove software and download it again.
    1. `if NOT`: download it
1. Execute the software.


# Setup
1. Download the release (if available)
1. Open `data` folder and modify `config.json`
1. Set parameters (`config.json`):<br>
- [x] `software_file`: The file hosted in the cloud that the program will download.<br>
    - **Disclaimer**: *It has to be a .zip file!*
- [x] `software_install_path`: Where is the software going to be extracted.<br>
- [x] `software_executable_path`: The path of the file that will be executed once the software has been downloaded.<br>
- [x] `software_name`: The name of your software.<br>
- [x] `version_file`: The file hosted in the cloud that stores your latest software's version.<br>
- [x] `version_path`: Where is the version file going to be stored.
- [ ] _`force_update`: Not implemented._<br>

* Example:
```json
{
    "software_file": "https://link-to-your/file.zip",
    "software_install_path": "\\app",
    "software_executable_path": "\\app\\game.exe",
    "software_name": "Name of your software.",
    "version_file": "https://link-to-your/version-file.txt",
    "version_path": "\\version.txt"
}
```