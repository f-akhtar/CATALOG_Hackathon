stations = [
    {"id": 1, "name": "Station A", "location": "Downtown", "slots": 10, "available_slots": 5, "charger_type": "fast", "price": 0.25},
    {"id": 2, "name": "Station B", "location": "Uptown", "slots": 8, "available_slots": 2, "charger_type": "normal", "price": 0.20},
    # Add more stations as needed
]

def filter_stations(location=None, charger_type=None, min_slots=1, max_price=None):
    results = stations
    if location:
        results = [s for s in results if location.lower() in s["location"].lower()]
    if charger_type:
        results = [s for s in results if s["charger_type"] == charger_type]
    if max_price is not None:
        results = [s for s in results if s["price"] <= max_price]
    results = [s for s in results if s["available_slots"] >= min_slots]
    return results
