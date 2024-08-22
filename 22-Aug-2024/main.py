from stations import filter_stations
from booking import book_slot
from user_data import add_booking

def find_and_book_station(user):
    location = input("Enter location: ")
    charger_type = input("Enter charger type (fast/normal): ")
    min_slots = int(input("Enter minimum slots required: "))
    max_price = float(input("Enter maximum price per kWh: "))
    
    available_stations = filter_stations(location, charger_type, min_slots, max_price)
    
    if available_stations:
        print("Available Stations:")
        for station in available_stations:
            print(f"ID: {station['id']}, Name: {station['name']}, Available Slots: {station['available_slots']}, Price: ${station['price']}/kWh")
        
        station_id = int(input("Enter station ID to book: "))
        if book_slot(station_id, user):
            station = next((s for s in available_stations if s["id"] == station_id), None)
            if station:
                add_booking(user, station_id, station["name"])
    else:
        print("No stations found with the specified criteria.")

if __name__ == "__main__":
    user = input("Enter your username: ")
    find_and_book_station(user)
