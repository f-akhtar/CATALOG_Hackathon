users = {
    "farhan": {"bookings": []},
    # Add more users as needed
}

def add_booking(user, station_id, station_name):
    if user in users:
        users[user]["bookings"].append({"station_id": station_id, "station_name": station_name})
