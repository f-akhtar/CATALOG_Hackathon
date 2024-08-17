class Reporting:
    def __init__(self, inventory):
        self.inventory = inventory
        
    def generate_report(self):
        print("\n--- E-Waste Inventory Report ---")
        for item in self.inventory.get_items():
            print(f"Name: {item['name']}, Status: {item['status']}, Purchased On: {item['purchase_date'].date()}")
        print("\n")
