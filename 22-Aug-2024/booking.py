from stations import stations

def get_station_by_id(station_id):
    for station in stations:
        if station["id"] == station_id:
            return station
    return None

def book_slot(station_id, user):
    station = get_station_by_id(station_id)
    if station and station["available_slots"] > 0:
        station["available_slots"] -= 1
        print(f"Slot booked at {station['name']} for {user}")
        return True
    print("Booking failed. No available slots.")
    return False
