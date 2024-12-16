import os
import subprocess
import urllib.request
from datetime import datetime

# Define the path to the log file
log_file_path = os.path.join(os.getenv('TEMP'), 'VSCodeInstallLog.txt')

# Function to log messages
def log_message(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} - {message}"
    print(log_entry)
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_entry + '\n')

# Function to download a file
def download_file(url, dest_path):
    try:
        urllib.request.urlretrieve(url, dest_path)
        log_message(f"Downloaded {url} to {dest_path}")
    except Exception as e:
        log_message(f"Failed to download {url}: {e}")
        exit(1)

# Function to run a command
def run_command(command):
    try:
        subprocess.run(command, check=True)
        log_message(f"Command '{' '.join(command)}' executed successfully.")
    except subprocess.CalledProcessError as e:
        log_message(f"Command '{' '.join(command)}' failed: {e}")
        exit(1)

# Function to check if VS Code is installed
def is_vscode_installed():
    vs_code_path = os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'Programs', 'Microsoft VS Code', 'bin', 'code.cmd')
    return os.path.exists(vs_code_path)

# Check if VS Code is installed
if is_vscode_installed():
    log_message("Visual Studio Code is already installed.")
else:
    # Define the URL for the VS Code installer
    url = "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user"

    # Define the path where the installer will be downloaded
    installer_path = os.path.join(os.getenv('TEMP'), 'VSCodeSetup.exe')

    # Download the installer
    log_message("Downloading Visual Studio Code installer...")
    download_file(url, installer_path)

    # Run the installer with user-level installation
    log_message("Running the Visual Studio Code installer...")
    try:
        subprocess.run([installer_path, '/verysilent', '/mergetasks=!runcode'], check=True)
        log_message("Installation completed.")
    except subprocess.CalledProcessError as e:
        log_message(f"Failed to run the Visual Studio Code installer: {e}")
        exit(1)

    # Check if VS Code was installed successfully
    if not is_vscode_installed():
        log_message("Visual Studio Code installation failed or VS Code executable not found.")
        exit(1)

    # Add VS Code to the user PATH
    log_message("Adding Visual Studio Code to the user PATH...")
    try:
        old_path = os.environ.get('Path', '')
        vs_code_bin_path = os.path.join(os.getenv('USERPROFILE'), 'AppData', 'Local', 'Programs', 'Microsoft VS Code', 'bin')
        if vs_code_bin_path not in old_path:
            new_path = f"{old_path};{vs_code_bin_path}"
            os.environ['Path'] = new_path
            subprocess.run(['setx', 'Path', new_path], check=True)
            log_message("Visual Studio Code path added to user PATH.")
        else:
            log_message("Visual Studio Code path already exists in user PATH.")
    except Exception as e:
        log_message(f"Failed to update user PATH: {e}")
        exit(1)

    # Clean up the installer file
    log_message("Cleaning up...")
    try:
        os.remove(installer_path)
        log_message("Cleanup completed.")
    except Exception as e:
        log_message(f"Failed to clean up the installer file: {e}")

# Install VS Code extensions
extensions = [
    "ms-python.vscode-pylance",
    "ms-python.python",
    "ms-python.debugpy",
    "ms-azuretools.vscode-docker",
    "NilsSoderman.batch-runner",
    "oven.bun-vscode",
    "VisualStudioExptTeam.vscodeintellicode",
    "VisualStudioExptTeam.intellicode-api-usage-examples",
    "ms-vscode.live-server",
    "ms-vscode-remote.remote-wsl",
    "ms-vscode.vscode-speech",
    "rust-lang.rust-analyzer",
    "mechatroner.rainbow-csv",
    "ms-vscode.powershell",
    "ms-vscode-remote.remote-containers",
    "GitHub.copilot",
    "GitHub.copilot-chat",
    "vscode-icons-team.vscode-icons",
    "tomoki1207.pdf",
    "redhat.vscode-xml",
    "ms-dotnettools.vscode-dotnet-pack",
    "ms-dotnettools.vscode-dotnet-runtime",
    "ms-dotnettools.csharp",
    "twxs.cmake",
    "ms-vscode.cmake-tools",
    "GitHub.vscode-pull-request-github",
    "vscjava.vscode-java-debug",
    "vscjava.vscode-java-pack",
    "ms-vscode.vscode-typescript-next",
    "ms-vscode.js-debug-nightly",
    "redhat.java",
    "vscjava.vscode-maven",
    "vscjava.vscode-java-dependency"
]

def install_vscode_extension(extension, index, total):
    percentage = (index + 1) / total * 100
    log_message(f"Installing VS Code extension ({index + 1}/{total} - {percentage:.2f}%): {extension}...")
    if is_extension_installed(extension):
        log_message(f"Extension {extension} is already installed.")
        return
    try:
        subprocess.run(['code', '--install-extension', extension, '--force'], check=True)
        log_message(f"Successfully installed extension: {extension}.")
    except subprocess.CalledProcessError as e:
        log_message(f"Failed to install extension: {extension}. Error: {e}")

def is_extension_installed(extension):
    result = subprocess.run(['code', '--list-extensions'], capture_output=True, text=True)
    return extension in result.stdout

total_extensions = len(extensions)
for index, extension in enumerate(extensions):
    install_vscode_extension(extension, index, total_extensions)

log_message("VS Code extensions installation completed.")
log_message("Visual Studio Code installation completed.")
