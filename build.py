# Import required standard Python libraries
import os  # For OS operations
import sys  # For system parameters and functions
import shutil  # For file and directory operations
import subprocess  # For running external processes
from pathlib import Path  # For filesystem path operations

def build_windows():
    """Build Windows executable using PyInstaller"""
    print("Building Windows executable...")
    
    # Install project dependencies for Windows from requirements.txt
    # sys.executable - path to current Python interpreter
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # Create bin directory if it doesn't exist
    # exist_ok=True prevents error if directory already exists
    bin_dir = Path("bin")
    bin_dir.mkdir(exist_ok=True)
    
    # Run PyInstaller with parameters:
    # --onefile: create single executable
    # --windowed: run without console window
    # --name: set output filename
    # --clean: clean PyInstaller cache before building
    # --noupx: don't use UPX for compression
    # --uac-admin: request admin rights on launch
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=AI Chat",
        "--clean",
        "--noupx",
        "--uac-admin",
        "src/main.py"
    ])
    
    # Move built file to bin directory
    # Use try/except to handle potential move errors
    try:
        shutil.move("dist/AI Chat.exe", "bin/AIChat.exe")
        print("Windows build completed! Executable location: bin/AIChat.exe")
    except:
        print("Windows build completed! Executable location: dist/AI Chat.exe")

def build_linux():
    """Build Linux executable using PyInstaller"""
    print("Building Linux executable...")
    
    # Install project dependencies for Linux
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    
    # Create bin directory if it doesn't exist
    bin_dir = Path("bin")
    bin_dir.mkdir(exist_ok=True)
    
    # Run PyInstaller for Linux with parameters:
    # --onefile: create single executable
    # --windowed: run without console window
    # --icon: set application icon
    # --name: set output filename
    subprocess.run([
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--icon=assets/icon.ico",
        "--name=aichat",
        "src/main.py"
    ])
    
    # Move built file to bin directory
    try:
        shutil.move("dist/aichat", "bin/aichat")
        print("Linux build completed! Executable location: bin/aichat")
    except:
        print("Linux build completed! Executable location: dist/aichat")

def main():
    """Main build function
    
    Determines operating system and runs appropriate build function
    """
    # Check operating system type
    if sys.platform.startswith('win'):  # If Windows
        build_windows()
    elif sys.platform.startswith('linux'):  # If Linux
        build_linux()
    else:  # If other OS
        print("Unsupported platform")

# Script entry point
# If script is run directly (not imported as module),
# run main function
if __name__ == "__main__":
    main()