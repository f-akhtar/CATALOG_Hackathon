from inventory import Inventory
from alerts import Alerts
from reporting import Reporting

def main():
    inventory = Inventory()
    alerts = Alerts(inventory)
    reporting = Reporting(inventory)
    
    # Example Workflow
    inventory.add_item("Laptop", "2022-01-01", 3)  # Adding an item with a 3-year lifespan
    inventory.add_item("Printer", "2021-06-15", 5)
    
    alerts.check_for_replacement()  # Check and alert if any items need replacing
    
    reporting.generate_report()  # Generate a report of the current inventory and e-waste

if __name__ == "__main__":
    main()
