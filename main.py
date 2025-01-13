import os
import subprocess
from datetime import datetime
import requests

# Define the path to the log file
log_file_path = os.path.join(os.getenv('TEMP'), 'VSCodeInstallLog.txt')

# Function to log messages
def log_message(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} - {message}"
    print(log_entry)
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_entry + '\n')

# Function to find the VS Code executable path
def find_vscode_executable():
    possible_paths = [
        os.path.join(os.getenv('LOCALAPPDATA'), 'Programs', 'Microsoft VS Code', 'bin', 'code.cmd'),  # Default installation path
        os.path.join(os.getenv('ProgramFiles'), 'Microsoft VS Code', 'bin', 'code.cmd'),  # Possible on 64-bit systems
        os.path.join(os.getenv('ProgramFiles(x86)'), 'Microsoft VS Code', 'bin', 'code.cmd'),  # Possible on 32-bit systems
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None  # Return None if not found

# Function to download and install VS Code
def install_vscode():
    log_message("Visual Studio Code is not installed. Downloading the installer...")
    vscode_installer_url = "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user"
    installer_path = os.path.join(os.getenv('TEMP'), 'VSCodeSetup.exe')
    
    # Download the installer
    try:
        response = requests.get(vscode_installer_url, stream=True)
        response.raise_for_status()
        with open(installer_path, 'wb') as installer_file:
            for chunk in response.iter_content(chunk_size=8192):
                installer_file.write(chunk)
        log_message(f"VS Code installer downloaded to {installer_path}.")
    except requests.RequestException as e:
        log_message(f"Failed to download VS Code installer. Error: {e}")
        return False

    # Run the installer
    log_message("Running the VS Code installer...")
    try:
        subprocess.run([installer_path, '/VERYSILENT', '/NORESTART'], check=True)
        log_message("Visual Studio Code installation completed.")
        return True
    except subprocess.CalledProcessError as e:
        log_message(f"Failed to install VS Code. Error: {e}")
        return False

# Function to check if an extension is already installed
def is_extension_installed(extension, vs_code_executable_path):
    try:
        result = subprocess.run([vs_code_executable_path, '--list-extensions'], capture_output=True, text=True)
        return extension in result.stdout
    except FileNotFoundError:
        log_message("The 'code' command is not available. Ensure VS Code is installed and PATH is configured correctly.")
        return False

# Function to install a single VS Code extension
def install_vscode_extension(extension, index, total, vs_code_executable_path):
    percentage = (index + 1) / total * 100
    log_message(f"Installing VS Code extension ({index + 1}/{total} - {percentage:.2f}%): {extension}...")
    if is_extension_installed(extension, vs_code_executable_path):
        log_message(f"Extension {extension} is already installed.")
        return
    try:
        subprocess.run([vs_code_executable_path, '--install-extension', extension, '--force'], check=True)
        log_message(f"Successfully installed extension: {extension}.")
    except subprocess.CalledProcessError as e:
        log_message(f"Failed to install extension: {extension}. Error: {e}")

# Function to install multiple VS Code extensions
def install_extensions(vs_code_executable_path):
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
        "vscjava.vscode-java-dependency",
        "mathiasfrohlich.Kotlin",
        "ms-vscode.remote-server",
        "WakaTime.vscode-wakatime",
        "Ionide.Ionide-fsharp",
        "vscjava.vscode-gradle",
        "golang.go"
    ]
    total_extensions = len(extensions)
    log_message(f"Checking and installing {total_extensions} extensions...")
    for index, extension in enumerate(extensions):
        install_vscode_extension(extension, index, total_extensions, vs_code_executable_path)
    log_message("VS Code extensions installation completed.")

# Main function to coordinate the installation
def main():
    log_message("Starting Visual Studio Code setup...")
    vs_code_executable_path = find_vscode_executable()
    if not vs_code_executable_path:
        log_message("Visual Studio Code not found. Proceeding to download and install...")
        if not install_vscode():
            log_message("Failed to install Visual Studio Code. Exiting setup.")
            return
        vs_code_executable_path = find_vscode_executable()
        if not vs_code_executable_path:
            log_message("Visual Studio Code executable not found after installation. Exiting setup.")
            return
    else:
        log_message(f"Found Visual Studio Code at {vs_code_executable_path}")
    install_extensions(vs_code_executable_path)

if __name__ == "__main__":
    main()
