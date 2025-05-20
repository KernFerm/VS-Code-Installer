# VS Code Installer Script

💻 This script automates the installation of Visual Studio Code and its extensions on a Windows machine. ⚙️

## Features

- [https://discord.gg/FxJd3PxXbc](https://discord.gg/FxJd3PxXbc)

- Downloads and installs Visual Studio Code
- Will open `VSC` and continue to install the extensions for visual studio code 
- Adds VS Code to the `user PATH`
- Installs a list of predefined VS Code extensions
- Logs the installation process

## Prerequisites

- Python 3.11.9 installed on your machine
- If you don't have `Python` installed, use this installer in the repo:
  1. `python3119.bat`
  2. Run the `python3119.bat` and follow the prompts that appear during installation.
  3. After installation, open `CMD.exe` and type:
     ```
     python --version
     ```
     It should display the correct Python version you installed.

## Usage

A. Run the script:
   - Right-click on the `VS-Code-Installer-main` folder and copy the PATH.
   - Open `CMD.exe` (Admin Mode is NOT required).
   - Navigate to the folder by typing:
     ```
     cd <paste the location you copied>
     ```
   - Then run the script:
     ```
     python main.py
     ```

## Extensions Installed

The script installs the following VS Code extensions:

- ms-python.vscode-pylance
- ms-python.python
- ms-python.debugpy
- ms-azuretools.vscode-docker
- NilsSoderman.batch-runner
- oven.bun-vscode
- VisualStudioExptTeam.vscodeintellicode
- VisualStudioExptTeam.intellicode-api-usage-examples
- ms-vscode.live-server
- ms-vscode-remote.remote-wsl
- ms-vscode.vscode-speech
- rust-lang.rust-analyzer
- mechatroner.rainbow-csv
- ms-vscode.powershell
- ms-vscode-remote.remote-containers
- GitHub.copilot
- GitHub.copilot-chat
- vscode-icons-team.vscode-icons
- tomoki1207.pdf
- redhat.vscode-xml
- ms-dotnettools.vscode-dotnet-pack
- ms-dotnettools.vscode-dotnet-runtime
- ms-dotnettools.csharp
- twxs.cmake
- ms-vscode.cmake-tools
- GitHub.vscode-pull-request-github
- vscjava.vscode-java-debug
- vscjava.vscode-java-pack
- ms-vscode.vscode-typescript-next
- ms-vscode.js-debug-nightly
- redhat.java
- vscjava.vscode-maven
- vscjava.vscode-java-dependency

## Logging

The script logs all actions to a log file located at `%TEMP%\VSCodeInstallLog.txt`.

## License

This project is proprietary and all rights are reserved by the author.  
Unauthorized copying, distribution, or modification of this project is strictly prohibited.  
Unless you have written permission from the Developer or the FNBUBBLES420 ORG.
