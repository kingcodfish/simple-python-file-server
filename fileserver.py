# =============================================================================
#   Simple Python File Server Configuration
# =============================================================================

# Network Configuration
# --------------------
SERVER_HOST = '0.0.0.0'  # Listen on all available interfaces
SERVER_PORT = 80         # HTTP default port

# Application Settings
# -------------------
APP_TITLE = 'File server - Made by kingcodfish'
UPLOAD_FOLDER = '/path/to/upload/directory'

# File Type Icons
# --------------
# Define custom icons for different file extensions
# Leave any extension undefined to show no icon
# Format: 'extension': 'emoji or text icon'
FILE_ICONS = {
    # Documents
    'pdf': '📄',
    'txt': '📝',
    'doc': '📄',
    'docx': '📄',
    
    # Spreadsheets
    'xls': '📊',
    'xlsx': '📊',
    'csv': '📊',
    
    # Images
    'jpg': '🖼️',
    'jpeg': '🖼️',
    'png': '🖼️',
    'gif': '🖼️',
    
    # Media
    'mp3': '🎵',
    'wav': '🎵',
    'mp4': '🎥',
    'avi': '🎥',
    
    # Archives
    'zip': '📦',
    'rar': '📦',
    '7z': '📦',
    
    # Programming Languages
    'py': '🐍',     # Python
    'js': '📜',     # JavaScript
    'ts': '📘',     # TypeScript
    'html': '🌐',   # HTML
    'css': '🎨',    # CSS
    'java': '☕',    # Java
    'cpp': '⚡',     # C++
    'c': '⚙️',      # C
    'cs': '🔷',     # C#
    'php': '🐘',    # PHP
    'rb': '💎',     # Ruby
    'go': '🔵',     # Go
    'rs': '⚙️',     # Rust
    'swift': '🔶',  # Swift
    'kt': '🟣',     # Kotlin
    
    # Web Development
    'json': '📋',   # JSON
    'xml': '📋',    # XML
    'yml': '📋',    # YAML
    'yaml': '📋',   # YAML
    'md': '📝',     # Markdown
    'sql': '🗃️',    # SQL
    
    # Scripts
    'sh': '⌨️',     # Shell
    'bat': '⌨️',    # Batch
    'ps1': '⌨️',    # PowerShell
}

# Directory icon (can be customized)
DIR_ICON = '📁'

# =============================================================================

from flask import Flask, request, render_template_string, send_file, redirect, url_for, Response
import os
import shutil
import mimetypes
from datetime import datetime

app = Flask(__name__)

# Configure upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Helper function to get the full path
def get_full_path(subpath=""):
    return os.path.join(app.config['UPLOAD_FOLDER'], subpath)

# Helper function to recursively delete a directory
def delete_directory(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(path)

# Helper function to get file details
def get_file_details(path):
    stats = os.stat(path)
    size = stats.st_size
    modified = stats.st_mtime
    
    # Convert size to human readable format
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            break
        size /= 1024.0
    size = f"{size:.1f} {unit}"
    
    # Convert timestamp to readable format with 12h time and dd/mm/yyyy date
    modified = datetime.fromtimestamp(modified).strftime('%d/%m/%Y %I:%M %p')
    
    return size, modified

# Helper function to get file icon
def get_file_icon(filename):
    """Get the icon for a given filename based on its extension."""
    if '.' in filename:
        ext = filename.lower().split('.')[-1]
        return FILE_ICONS.get(ext, '')  # Return empty string if no icon defined
    return ''  # No extension = no icon

# Home and file upload form
@app.route('/', defaults={'subpath': ''}, methods=['GET', 'POST'])
@app.route('/<path:subpath>', methods=['GET', 'POST'])
def file_manager(subpath):
    current_path = get_full_path(subpath)
    
    # Ensure the directory exists
    if not os.path.exists(current_path):
        return "Directory not found", 404
    
    # Handle file upload
    if request.method == 'POST':
        if 'file' in request.files:
            files = request.files.getlist('file')  # Get multiple files
            for file in files:
                if file.filename:
                    file.save(os.path.join(current_path, file.filename))
            return redirect(url_for('file_manager', subpath=subpath))
        elif 'folder_name' in request.form:
            folder_name = request.form['folder_name']
            os.makedirs(os.path.join(current_path, folder_name), exist_ok=True)
            return redirect(url_for('file_manager', subpath=subpath))
    
    # Get list of files and directories
    entries = []
    for entry in os.listdir(current_path):
        full_path = os.path.join(current_path, entry)
        is_dir = os.path.isdir(full_path)
        if not is_dir:
            size, modified = get_file_details(full_path)
            icon = DIR_ICON if is_dir else get_file_icon(entry)
        else:
            size = '-'
            modified = '-'
            icon = DIR_ICON
        entries.append({
            'name': entry,
            'is_dir': is_dir,
            'size': size,
            'modified': modified,
            'icon': icon
        })
    
    # Sort directories first, then files
    directories = [entry for entry in entries if entry['is_dir']]
    files = [entry for entry in entries if not entry['is_dir']]
    directories.sort(key=lambda x: x['name'].lower())
    files.sort(key=lambda x: x['name'].lower())
    entries = directories + files
    
    # Determine if we're at the root
    at_root = (subpath == "")
    
    # Set the "Go Back" URL to always go to the root (no subpath)
    go_back_url = url_for('file_manager', subpath="")

    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <title>''' + APP_TITLE + '''</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {
                    background-color: #2e2e2e;
                    color: #d3d3d3;
                    font-family: Arial, sans-serif;
                    margin: 20px;
                    font-size: 16px;
                }
                a {
                    color: #1e90ff;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
                button {
                    background-color: #444;
                    color: #d3d3d3;
                    border: none;
                    padding: 10px 20px;
                    cursor: pointer;
                    border-radius: 5px;
                }
                button:hover {
                    background-color: #555;
                }
                h1, h2 {
                    color: #ffffff;
                }
                ul {
                    list-style-type: none;
                    padding: 0;
                }
                li {
                    margin-bottom: 10px;
                }
                form {
                    display: inline;
                    margin-bottom: 10px;
                }
                .upload-container {
                    margin-bottom: 20px;
                }
                @media (max-width: 600px) {
                    body {
                        font-size: 14px;
                    }
                    button {
                        padding: 5px 10px;
                    }
                    .upload-container {
                        width: 100%;
                    }
                }
            </style>
            <script>
                function confirmDelete(item) {
                    return confirm("Are you sure you want to delete " + item + "?");
                }
            </script>
        </head>
        <body>
            <h2>Current Path: /{{ subpath }}</h2>
            {% if not at_root %}
                <a href="{{ go_back_url }}">Go Back</a>
            {% endif %}
            
            <div class="upload-container">
                <h3>Upload Files:</h3>
                <form method="post" enctype="multipart/form-data">
                    <input type="file" name="file" multiple>
                    <button type="submit">Upload (Files)</button>
                </form>
            </div>
            
            <div class="upload-container">
                <h3>Create a Directory:</h3>
                <form method="post">
                    <input type="text" name="folder_name" placeholder="New Folder Name" required>
                    <button type="submit">Create</button>
                </form>
            </div>
            
            <h3>Entries:</h3>
            <ul>
                {% for entry in entries %}
                    <li>
                        {{ entry.icon }}
                        {% if entry.is_dir %}
                            <a href="{{ url_for('file_manager', subpath=(subpath + '/' + entry.name).strip('/')) }}">{{ entry.name }}/</a>
                        {% else %}
                            <a href="{{ url_for('serve_file', subpath=(subpath + '/' + entry.name).strip('/')) }}">{{ entry.name }}</a>
                        {% endif %}
                        <span style="color: #888; margin-left: 10px;">{{ entry.size }} - {{ entry.modified }}</span>
                        <form method="post" action="{{ url_for('delete_entry', subpath=(subpath + '/' + entry.name).strip('/')) }}" style="display:inline;" onsubmit="return confirmDelete('{{ entry.name }}')">
                            <button type="submit">Delete</button>
                        </form>
                    </li>
                {% endfor %}
            </ul>
        </body>
        </html>
    ''', subpath=subpath, entries=entries, at_root=at_root, go_back_url=go_back_url)

# Serve files and force download
@app.route('/serve/<path:subpath>')
def serve_file(subpath):
    file_path = get_full_path(subpath)
    if not os.path.exists(file_path):
        return "File not found", 404

    try:
        return send_file(
            file_path,
            as_attachment=True,
            download_name=os.path.basename(file_path),
            mimetype='application/octet-stream'
        )
    except Exception as e:
        return f"Error serving file: {str(e)}", 500

# Delete files or directories
@app.route('/delete/<path:subpath>', methods=['POST'])
def delete_entry(subpath):
    full_path = get_full_path(subpath)
    parent_path = os.path.dirname(full_path)  # Get the parent directory
    
    if os.path.exists(full_path):
        if os.path.isdir(full_path):
            try:
                delete_directory(full_path)
            except Exception as e:
                return f"Failed to delete directory: {e}", 400
        else:
            os.remove(full_path)
        
        # Redirect to the root directory after deletion (always go back to "/")
        return redirect(url_for('file_manager', subpath=""))
    
    return "File or directory not found", 404

if __name__ == '__main__':
    # Create upload directory if it doesn't exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(host=SERVER_HOST, port=SERVER_PORT)


# =============================================================================
# Made by kingcodfish
# kcodfish.com
# To report bugs or request features, please visit:
# kcodfish.com/contactme
# =============================================================================
