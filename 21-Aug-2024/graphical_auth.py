from user_data import get_user_data

def authenticate_graphical(username, graphical_password):
    user_data = get_user_data(username)
    if user_data and user_data["graphical_password"] == graphical_password:
        return True
    return False
