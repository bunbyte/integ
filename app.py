
import json
from flask import Flask, render_template, request, redirect, url_for, flash
import hashlib
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Path to the JSON file for storing hashes
HASHES_FILE = 'hashes.json'

def calculate_hash(file_path, hash_type='sha256'):
    hasher = hashlib.new(hash_type)
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hasher.update(chunk)
    return hasher.hexdigest()

def load_hashes():
    if not os.path.exists(HASHES_FILE):
        return {}
    with open(HASHES_FILE, 'r') as f:
        return json.load(f)

def save_hashes(hashes):
    with open(HASHES_FILE, 'w') as f:
        json.dump(hashes, f, indent=4)

@app.route('/', methods=['GET', 'POST'])
def index():
    hashes = load_hashes()
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            file_path = f"uploads/{file.filename}"
            file.save(file_path)
            calculated_checksum = calculate_hash(file_path)
            if file.filename in hashes:
                stored_checksum = hashes[file.filename]
                if calculated_checksum == stored_checksum:
                    flash(f'File integrity verified. The file is unmodified.')
                else:
                    flash(f'File integrity check failed. The file may have been altered or corrupted.')
            else:
                hashes[file.filename] = calculated_checksum
                save_hashes(hashes)
                flash(f'File integrity verified. The file is new and its hash has been stored.')
            return redirect(url_for('index'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=5004)
