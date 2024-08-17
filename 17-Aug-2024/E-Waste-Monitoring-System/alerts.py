from datetime import datetime

class Alerts:
    def __init__(self, inventory):
        self.inventory = inventory
        
    def check_for_replacement(self):
        for item in self.inventory.get_items():
            if item['status'] == 'active':
                age = (datetime.now() - item['purchase_date']).days / 365.25
                if age >= item['lifespan_years']:
                    print(f"Alert: {item['name']} needs to be replaced.")
                    self.inventory.mark_for_recycling(item['name'])
