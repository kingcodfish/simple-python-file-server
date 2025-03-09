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

> ⚠️ **Important**: Place the `fileserver.py` file outside of your `UPLOAD_FOLDER` directory to prevent it from being accessible or accidentally deleted through the web interface.

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

## License & Attribution

### MIT License (Modified)

Copyright © 2025 kingcodfish

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, and sublicense the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

1. The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
2. Attribution must be given to the original author in any derivative works.
3. Selling or commercially distributing this software or any derivative works is not permitted.

### Attribution Requirements

When using, modifying, or distributing this software, please:

1. **Repository Link**
   - Include a link to the original repository in your documentation
   - Example: `Based on [Simple Python File Server](https://github.com/kingcodfish/simple-python-file-server)`

2. **Author Credit**
   - Credit the original author (kingcodfish)
   - Include author's website: [kcodfish.com](https://kcodfish.com)

3. **Changes Documentation**
   - Document any modifications made to the original code
   - Maintain a list of changes in your documentation

4. **License Inclusion**
   - Include this complete license and attribution section in your documentation

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Credits

Originally created by [kingcodfish](https://kcodfish.com)

For bug reports or feature requests, visit: [kcodfish.com/contactme](https://kcodfish.com/contactme)
