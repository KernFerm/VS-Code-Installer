import os
import subprocess
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

# Function to find the VS Code executable path
def find_vscode_executable():
    possible_paths = [
        os.path.join(os.getenv('LOCALAPPDATA'), 'Programs', 'Microsoft VS Code', 'bin', 'code.cmd'),  # Default installation path
        os.path.join(os.getenv('ProgramFiles'), 'Microsoft VS Code', 'bin', 'code.cmd'),  # Possible on 64-bit systems with 64-bit VS Code
        os.path.join(os.getenv('ProgramFiles(x86)'), 'Microsoft VS Code', 'bin', 'code.cmd'),  # Possible on 64-bit systems with 32-bit VS Code
    ]
    for path in possible_paths:
        if os.path.exists(path):
            return path
    return None  # Return None if not found

vs_code_executable_path = find_vscode_executable()

# Function to check if an extension is already installed
def is_extension_installed(extension):
    if not vs_code_executable_path:
        log_message("Visual Studio Code executable not found.")
        return False
    try:
        result = subprocess.run([vs_code_executable_path, '--list-extensions'], capture_output=True, text=True)
        return extension in result.stdout
    except FileNotFoundError:
        log_message("The 'code' command is not available. Ensure VS Code is installed and PATH is configured correctly.")
        return False

# Function to install a single VS Code extension
def install_vscode_extension(extension, index, total):
    if not vs_code_executable_path:
        log_message("Cannot install extensions without a valid path to VS Code.")
        return
    percentage = (index + 1) / total * 100
    log_message(f"Installing VS Code extension ({index + 1}/{total} - {percentage:.2f}%): {extension}...")
    if is_extension_installed(extension):
        log_message(f"Extension {extension} is already installed.")
        return
    try:
        subprocess.run([vs_code_executable_path, '--install-extension', extension, '--force'], check=True)
        log_message(f"Successfully installed extension: {extension}.")
    except subprocess.CalledProcessError as e:
        log_message(f"Failed to install extension: {extension}. Error: {e}")

# Function to install multiple VS Code extensions
def install_extensions():
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
    if not vs_code_executable_path:
        log_message("Visual Studio Code executable not found. Cannot install extensions.")
        return
    total_extensions = len(extensions)
    log_message(f"Checking and installing {total_extensions} extensions...")
    for index, extension in enumerate(extensions):
        install_vscode_extension(extension, index, total_extensions)
    log_message("VS Code extensions installation completed.")

# Main function to coordinate the installation
def main():
    log_message("Starting Visual Studio Code setup...")
    if vs_code_executable_path:
        log_message(f"Found Visual Studio Code at {vs_code_executable_path}")
        install_extensions()
    else:
        log_message("Visual Studio Code is not installed. Please install it first and ensure 'code' command is available in PATH.")

if __name__ == "__main__":
    main()
