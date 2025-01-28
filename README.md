# AI Chat Application

A Python chat application using the OpenRouter API to interact with various AI models.

## System Requirements

- Windows 10/11 or Linux
- Python 3.7 or higher
- pip (Python package manager)
- Minimum 2GB free disk space
- Stable internet connection

## Installation

1. Install Python from the official website:
   https://www.python.org/downloads/

2. Verify Python and pip installation:
```cmd
python --version
pip --version
```

3. Install required packages:
```cmd
pip install -r requirements.txt
```

## Building the Application

### Windows

1. Navigate to project directory
2. Run build:
```cmd
python build.py
```
3. Executable will be created at `bin/AIChat.exe`

### Linux

1. Navigate to project directory
2. Run build:
```bash
python3 build.py
```
3. Executable will be created at `bin/aichat`
4. Make file executable:
```bash
chmod +x bin/aichat
```

## Configuration

The following environment variables can be configured in `.env`:

- `OPENROUTER_API_KEY`: Your OpenRouter API key
- `MAX_TOKENS`: Maximum tokens per response (default: 1000)
- `TEMPERATURE`: Response temperature (default: 0.7)

## Notes

- Build logs can be found in `build/logs/`
- If you encounter issues:
  1. Ensure internet connectivity
  2. Check available disk space
  3. Try running build again
  4. Check logs in `build/logs/`