import hashlib
from user_data import get_user_data

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def authenticate_textual(username, password):
    user_data = get_user_data(username)
    if user_data and user_data["password"] == hash_password(password):
        return True
    return False
