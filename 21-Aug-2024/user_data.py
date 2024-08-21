users = {
    "farhan": {
        "password": "5f4dcc3b5aa765d61d8327deb882cf99",  # MD5 hash for 'password'
        "graphical_password": "image1,image2,image3",
        "biometric_data": "f1a0c6e7b11c0f94e019ef0bc7ffb6b5"  # Sample MD5 hash
    }
}

def get_user_data(username):
    return users.get(username, None)
