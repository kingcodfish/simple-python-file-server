# Simple Python File Server

A lightweight, web-based file server built with Flask that allows easy file sharing across a network. It provides a simple interface for uploading, downloading, and managing files and directories.

## ⚠️ Security Warning

This file server is intended for local network use only. It does not include:
- Authentication system
- User permissions
- Access controls
- Encryption

**DO NOT** expose this server to the internet by port forwarding or hosting on a public server.

## Features

- 📤 Upload multiple files (no file type restrictions)
- 📥 Download files
- 📁 Create directories
- 🗑️ Delete files and directories
- 📱 Mobile-friendly interface
- 🔍 Automatic file sorting (directories first)
- 🎨 Customizable file type icons
- 📊 File size and modification date display

## Installation

1. Ensure Python is installed on your system
2. Install Flask:
```bash
pip install flask
```

## Configuration

The following settings can be modified in `fileserver.py`:

```python
# Network Configuration
SERVER_HOST = '0.0.0.0'  # Listen on all available interfaces
SERVER_PORT = 80         # HTTP default port

# Application Settings
APP_TITLE = 'File server - Made by kingcodfish'
UPLOAD_FOLDER = '/path/to/upload/directory'

# File Type Icons Configuration
FILE_ICONS = {
    # Documents
    'pdf': '📄',
    'txt': '📝',
    'doc': '📄',
    
    # Spreadsheets
    'xls': '📊',
    'xlsx': '📊',
    
    # Media
    'mp3': '🎵',
    'mp4': '🎥',
    
    # Add your own icons here
}

# Directory icon
DIR_ICON = '📁'
```

### Customizing File Icons

The file server now supports fully customizable file type icons:

1. **Adding New Icons**
   ```python
   FILE_ICONS = {
       'existing': '📄',
       'mynewtype': '🔮',  # Add custom file types
       'py': '🐍'         # Use any emoji or text
   }
   ```

2. **Icon Display Rules**
   - Files with matching extensions show their configured icon
   - Files with unknown extensions show no icon
   - Directories always show the DIR_ICON (📁 by default)
   - Icons can be emoji or text characters

3. **Changing Directory Icon**
   ```python
   DIR_ICON = '📂'  # Change to any icon you prefer
   ```

## Usage

1. Set your desired `UPLOAD_FOLDER` in the configuration
2. Run the server:
```bash
python fileserver.py
```
3. Access the file server through your web browser:
   - Local: `http://localhost`
   - Network: `http://[your-ip-address]`

## Contributing

Feel free to make pull requests or modify the code to fit your needs. To report bugs or request features, please visit [kcodfish.com/contactme](https://kcodfish.com/contactme).

## License

This project is open source and available for any use. If you redistribute or modify this project, please provide appropriate attribution:

- Link back to the original repository
- Credit the original author (kingcodfish)
- Include this attribution notice in your README
- State any significant changes made to the original code

## Credits

Created by [kingcodfish](https://kcodfish.com)
