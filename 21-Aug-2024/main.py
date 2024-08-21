import getpass
from textual_auth import authenticate_textual
from graphical_auth import authenticate_graphical
from biometric_auth import authenticate_biometric

def authenticate_user(username):
    password = getpass.getpass("Enter textual password: ")
    if not authenticate_textual(username, password):
        print("Textual password authentication failed")
        return False
    
    graphical_password = input("Enter graphical password (e.g., image1,image2,image3): ")
    if not authenticate_graphical(username, graphical_password):
        print("Graphical password authentication failed")
        return False
    
    biometric_data = input("Enter biometric data: ")
    if not authenticate_biometric(username, biometric_data):
        print("Biometric authentication failed")
        return False
    
    return True

if __name__ == "__main__":
    username = input("Enter your username: ")
    if authenticate_user(username):
        print("Authentication successful")
    else:
        print("Authentication failed")
