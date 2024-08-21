from user_data import get_user_data

def authenticate_biometric(username, biometric_data):
    user_data = get_user_data(username)
    if user_data and user_data["biometric_data"] == biometric_data:
        return True
    return False
