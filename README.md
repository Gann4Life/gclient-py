# GClient-py
GClient-py is an application written in python that allows you to handle updates for your own software or games by setting parameters on a json file. <br>
C# and JS version will come after this gets finished.

# Disclaimer
I won't recommend using this right now as it is in constant development and unstable. <br>
I suggest to make your own fork or contribute to this repository.

# Goals
- [ ] Python version
    - [x] Console version (core)
    - [ ] TKInter version
    - [ ] Kivy version
    - [ ] PyQt version
- [ ] C# version (GUI)
- [ ] JS version (GUI)

# How it works
1. Verifies if the software has been installed/downloaded.
    1. `if YES`: verify if it is up to date
        1. `if NOT`: remove software and download it again.
    1. `if NOT`: download it
1. Execute the software.

![Class Diagram](http://www.plantuml.com/plantuml/proxy?src=https://raw.githubusercontent.com/Gann4Life/gclient-py/main/UML/concept.puml)


# Setup
1. Host your software's zip file and version.txt file in a service that allows direct access to the files content or binary data.<br>
For this program i'd recommend using Google Drive along [this tool.](https://sites.google.com/site/gdocs2direct/home)
1. Download the release (if available)
1. Open `data` folder and modify `config.json`
1. Set parameters (`config.json`):<br>

    `software_file`<br>
    The file hosted in the cloud that the program will download.<br>
    Use your own URL.<br>
    **Disclaimer**: *It has to be a .zip file!*<br>

    `software_install_path`<br>
    Where is the software going to be extracted.<br>
    I recommend to leave the default value.<br>

    `software_executable_path`<br>
    The path of the file that will be executed, this refers to files and folders inside `software_install_path`.<br>

    `software_name`<br>
    The name of your software.<br>

    `software_prefix`<br>
    The prefix of your software. (Game/Software/Prototype/Etc)

    `version_file`<br>
    The file hosted in the cloud that stores your latest software's version.<br>
    Use your own URL.<br>

    `version_path`<br>
    Where is the version file going to be stored.<br>
    I recommend to leave the default value.<br>

    `force_update`<br>
    _Not implemented._<br>
    Forces the software to be updated.<br>
    Probably useful for multiplayer games.

# Example
```json
{
    "software_file": "https://link-to-your/app.zip",
    "software_install_path": "\\app",
    "software_executable_path": "\\app.exe",
    "software_name": "My App Name.",
    "software_prefix": "Application",
    "version_file": "https://link-to-your/version-file.txt",
    "version_path": "\\version.txt"
}
```
