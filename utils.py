import hashlib

def calculate_hash(file_path, hash_type):
    hash_func = getattr(hashlib, hash_type.lower().replace("-", ""))
    hash_obj = hash_func()

    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except Exception as e:
        return f"Failed to calculate hash: {e}"
