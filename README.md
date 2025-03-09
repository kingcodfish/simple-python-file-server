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
# Server Configuration
SERVER_HOST = '0.0.0.0'  # Default host (0.0.0.0 allows external connections)
SERVER_PORT = 80         # Default port number

# Application Configuration
APP_TITLE = 'File server - Made by kingcodfish'  # Browser title
UPLOAD_FOLDER = '/path/to/upload/directory'      # Storage directory
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
