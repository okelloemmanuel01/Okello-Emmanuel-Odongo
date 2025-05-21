def inventory_management():
    # Initialize inventory 
    inventory = {
        "Laptop": 15,
        "Hard disk": 42,
        "Keyboard": 30,
        "Monitor": 25,
        "Headphones": 50
    }
    
    while True:
        print("\n=== OKELLO's INVENTORY MANAGEMENT SYSTEM ===")
        print("1. View Current Inventory")
        print("2. Add New Stock Item")
        print("3. Update Stock Quantity")
        print("4. Remove Stock Item")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        # View Current Inventory
        if choice == '1':
            print("\nCurrent Inventory:")
            print("-----------------")
            for item, quantity in inventory.items():
                print(f"{item}: {quantity} units")
        
        # Add New Stock Item
        elif choice == '2':
            new_item = input("Enter new item name: ").title()
            if new_item in inventory:
                print("Item already exists in inventory!")
            else:
                try:
                    quantity = int(input(f"Enter quantity for {new_item}: "))
                    inventory[new_item] = quantity
                    print(f"{new_item} added to inventory with {quantity} units")
                except ValueError:
                    print("Invalid quantity! Please enter a number.")
        
        # Update Stock Quantity
        elif choice == '3':
            item = input("Enter item name to update: ").title()
            if item in inventory:
                try:
                    new_quantity = int(input(f"Enter new quantity for {item}: "))
                    inventory[item] = new_quantity
                    print(f"{item} quantity updated to {new_quantity}")
                except ValueError:
                    print("Invalid quantity! Please enter a number.")
            else:
                print("Item not found in inventory!")
        
        # Remove Stock Item
        elif choice == '4':
            item = input("Enter item name to remove: ").title()
            if item in inventory:
                del inventory[item]
                print(f"{item} removed from inventory")
            else:
                print("Item not found in inventory!")
        
        # Exit Program
        elif choice == '5':
            print("Exiting inventory management system. Goodbye!")
            break
        
        # Invalid Choice
        else:
            print("Invalid choice! Please enter a number between 1-5.")

# Start the inventory management system
inventory_management()