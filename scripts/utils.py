import os

def ensure_dir_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_file_name(path):
    return os.path.splitext(os.path.basename(path))[0]

def list_sorted_images(folder, prefix=None):
    files = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if prefix:
        files = [f for f in files if f.startswith(prefix)]
    return sorted(files)
