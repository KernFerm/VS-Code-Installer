# VS Code Installer Script

💻 This script automates the installation of Visual Studio Code and its extensions on a Windows machine. ⚙️

## Features

- Downloads and installs Visual Studio Code
- Adds VS Code to the user PATH
- Installs a list of predefined VS Code extensions
- Logs the installation process

## Prerequisites

- Python 3.11.6 installed on your machine
- If you don't have `Python` installed, use this installer in the repo:
  1. `install_python.bat`
  2. - run the `install_python.bat` follow the prompts that appear when installing.
     - open up `CMD.exe` type
```
python --version
```
should show in terminal the correct python verison you installed.

## Usage

1. Clone this repository to your local machine:
    ```
    git clone https://github.com/kernferm/vscode-installer.git
    cd vscode-installer
    ```

2. Run the script:
3. `Right Click` on `VS-Code-Installer-main` copy PATH, Open `CMD.exe` in **ADMIN MODE**
- paste the location you just copied to `CMD.exe`
- `CD` paste `<location you just copied>`
- type below or copy and paste in `CMD.exe`
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
