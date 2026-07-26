import os

UPLOAD_FOLDER = "uploads"

def save_uploaded_file(file):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return file_path