# Python & Visual Studio Code Automated Setup

🚀 **Automated installer for Python 3.11.9 and Visual Studio Code with essential extensions**

This script provides a complete automated setup for Python development environment on Windows, including Python installation, Visual Studio Code installation, and a comprehensive collection of development extensions.

## ✨ Features

- **🐍 Python 3.11.9 Installation**: Automated download and silent installation
- **🗑️ Clean Previous Installations**: Removes existing Python installations to avoid conflicts
- **📝 Visual Studio Code Setup**: Downloads and installs VS Code if not present
- **🔧 Extension Management**: Installs 39+ essential development extensions
- **🎨 Colored Console Output**: Enhanced user experience with colored terminal messages
- **📊 Progress Tracking**: Real-time installation progress with percentages
- **📝 Comprehensive Logging**: Detailed logs saved to temp directory
- **🔄 PATH Management**: Automatic PATH environment variable updates

## 🔧 Prerequisites

- **Operating System**: Windows 10/11
- **Internet Connection**: Required for downloading installers and extensions
- **Administrator Privileges**: Recommended for system-wide installations
- **PowerShell**: Should be available (default on modern Windows)

## 🚀 Usage

1. **use the pythonvisualstudio.exe**.
2. extract or unzip folder to desktop.
3. double click the `pythonvisualstudio.exe`.
4. follow the instructions in the `Console window`. 

### What Happens When You Run It:

1. **Python Installation Check**: Script checks for existing Python installations
2. **Cleanup Process**: Removes conflicting Python versions if found
3. **Python Download**: Downloads Python 3.11.9 installer from official source
4. **Silent Installation**: Installs Python with optimal settings
5. **PATH Updates**: Configures environment variables
6. **VS Code Check**: Verifies if Visual Studio Code is installed
7. **VS Code Installation**: Downloads and installs VS Code if needed
8. **Extension Installation**: Installs all configured extensions
9. **Completion**: Provides summary of installed components

## 📦 What Gets Installed

### Python 3.11.9
- **Installation Location**: `%LocalAppData%\Programs\Python\Python311`
- **Features**: 
  - User-local installation (no admin required)
  - PATH automatically configured
  - pip, setuptools, and wheel included
  - _distutils_hack issues automatically resolved

### Visual Studio Code Extensions

#### **🐍 Python Development**
- `ms-python.python` - Python language support
- `ms-python.vscode-pylance` - Advanced Python IntelliSense
- `ms-python.debugpy` - Python debugging

#### **☁️ Cloud & Containers**
- `ms-azuretools.vscode-docker` - Docker support
- `ms-vscode-remote.remote-containers` - Container development
- `ms-vscode-remote.remote-wsl` - WSL integration

#### **🤖 AI & Productivity**
- `GitHub.copilot` - AI pair programmer
- `GitHub.copilot-chat` - AI chat assistant
- `VisualStudioExptTeam.vscodeintellicode` - AI-assisted development
- `WakaTime.vscode-wakatime` - Time tracking

#### **🌐 Web Development**
- `ms-vscode.live-server` - Live development server
- `oven.bun-vscode` - Bun JavaScript runtime
- `ms-vscode.vscode-typescript-next` - TypeScript support

#### **⚙️ System & Tools**
- `ms-vscode.powershell` - PowerShell support
- `NilsSoderman.batch-runner` - Batch file execution
- `ms-vscode.cmake-tools` - CMake support
- `twxs.cmake` - CMake language support

#### **📊 Data & Visualization**
- `mechatroner.rainbow-csv` - CSV file visualization
- `tomoki1207.pdf` - PDF viewer

#### **🔧 Languages & Frameworks**
- `rust-lang.rust-analyzer` - Rust language support
- `redhat.java` - Java language support
- `vscjava.vscode-java-pack` - Java extension pack
- `ms-dotnettools.csharp` - C# support
- `golang.go` - Go language support
- `mathiasfrohlich.Kotlin` - Kotlin support
- `Ionide.Ionide-fsharp` - F# support

#### **🎨 UI & Themes**
- `vscode-icons-team.vscode-icons` - File icons
- `ms-vscode.vscode-speech` - Speech features


## 📝 Logging

All installation activities are logged to:
```
%TEMP%\VSCodeInstallLog.txt
```

**Log Features**:
- Timestamped entries
- Installation progress tracking
- Error reporting and debugging info
- Extension installation status

**Sample Log Entry**:
```
2025-06-23 14:30:15 - Starting Visual Studio Code setup...
2025-06-23 14:30:20 - Found Visual Studio Code at C:\Users\...\code.cmd
2025-06-23 14:30:25 - Installing VS Code extension (1/39 - 2.56%): ms-python.python...
```

## 🔧 Troubleshooting

### Common Issues

#### **Python Installation Fails**
```bash
# Check if you have sufficient permissions
# Try running as administrator
# Verify internet connection
```

#### **VS Code Extensions Won't Install**
```bash
# Ensure VS Code is properly installed
# Check internet connectivity
# Verify the code command is in PATH
```

#### **PATH Not Updated**
```bash
# Restart your terminal/command prompt
# Check environment variables manually
# Run: echo $env:PATH (PowerShell) or echo %PATH% (CMD)
```

#### **Color Output Not Working**
```bash
# Windows Terminal supports ANSI colors
# Legacy Command Prompt may not display colors properly
# Consider using Windows Terminal or PowerShell
```

### Manual Verification

**Check Python Installation**:
```bash
python --version
pip --version
```

**Check VS Code Installation**:
```bash
code --version
code --list-extensions
```

## 📋 System Requirements

- **OS**: Windows 10 version 1809+ or Windows 11
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space for installations
- **Network**: Broadband internet connection

## 🛡️ Security Notes

- Script downloads from official sources only
- No elevated privileges required for user-local installations
- All installations use verified publishers
- Logs contain no sensitive information

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**🎉 Enjoy your automated Python and VS Code development environment!**

For support, please check the troubleshooting section or create an issue in the repository.
