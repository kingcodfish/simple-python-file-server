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

- 📤 Upload multiple files
- 📥 Download files
- 📁 Create directories
- 🗑️ Delete files and directories
- 📱 Mobile-friendly interface
- 🔍 Automatic file sorting (directories first)

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

# File Icons
FILE_ICONS = {
    'pdf': '📄',    # Customize icons for each file type
    'txt': '📝',    # Use emoji or text characters
    'jpg': '🖼️',    # Add your own extensions and icons
}
DIR_ICON = '📁'     # Icon used for directories
```

### Customizing File Icons

You can add or modify file type icons by editing the `FILE_ICONS` dictionary:

1. To add a new file type icon:
```python
FILE_ICONS = {
    'existing': '📄',
    'mynewtype': '🔮'  # Add your new file type and icon
}
```

2. To remove an icon for a file type, simply remove it from the dictionary
3. Files with undefined extensions will show no icon
4. You can use emoji or text characters as icons

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
