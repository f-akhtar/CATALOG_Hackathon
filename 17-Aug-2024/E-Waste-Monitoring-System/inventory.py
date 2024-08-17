from datetime import datetime

class Inventory:
    def __init__(self):
        self.items = []
        
    def add_item(self, name, purchase_date, lifespan_years):
        item = {
            "name": name,
            "purchase_date": datetime.strptime(purchase_date, "%Y-%m-%d"),
            "lifespan_years": lifespan_years,
            "status": "active"
        }
        self.items.append(item)
        print(f"Added {name} to inventory.")
    
    def mark_for_recycling(self, name):
        for item in self.items:
            if item['name'] == name:
                item['status'] = 'to be recycled'
                print(f"Marked {name} for recycling.")
                break

    def get_items(self):
        return self.items
