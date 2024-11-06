'''
Created on Oct 22, 2024

@author: ssherki
'''

contact_book = {
    "Alice": {"phone": "123-456-7890", "email": "alice@example.com"},
    "Bob": {"phone": "987-654-3210", "email": "bob@example.com"},
}

# function to display contact 
def display_contact(contact):    
    for name, info in contact_book:
        print(f"Name : {name} Contact : {info['phone']}")

# adding new contact 
contact_book["Sachin"]= {"phone": "744-747-7464", "email": "sachin@example.com"}
print("\n\n")



# Initial inventory
inventory = {
    "Apple": {"price": 0.5, "quantity": 100, "category": "Fruit"},
    "Banana": {"price": 0.3, "quantity": 150, "category": "Fruit"},
    "Broccoli": {"price": 1.0, "quantity": 50, "category": "Vegetable"},
}

# Function to display the inventory
def display_inventory(inv):
    print(f"{'Product':<10} {'Price':<10} {'Quantity':<10} {'Category':<10}")
    for product, details in inv.items():
        print(f"{product:<10} {details['price']:<10} {details['quantity']:<10} {details['category']:<10}")

# 1. Display initial inventory
print("Initial Inventory:")
display_inventory(inventory)

# 2. Adding a new product
inventory["Carrot"] = {"price": 0.4, "quantity": 75, "category": "Vegetable"}
print("\nAdded Carrot:")
display_inventory(inventory)

# 3. Modifying an existing product's price and quantity
inventory["Apple"]["price"] = 0.55  # Increase price
inventory["Banana"]["quantity"] -= 20  # Sell 20 bananas
print("\nModified Apple Price and Sold Bananas:")
display_inventory(inventory)

# 4. Removing a product (e.g., out of stock)
del inventory["Broccoli"]
print("\nRemoved Broccoli from Inventory:")
display_inventory(inventory)

# 5. Checking available products (keys)
print("\nAvailable Products:", inventory.keys())

# 6. Checking product prices (values)
print("\nProduct Prices:", [details["price"] for details in inventory.values()])

# 7. Total inventory value
total_value = sum(details["price"] * details["quantity"] for details in inventory.values())
print("\nTotal Inventory Value: $", total_value)

# 8. Using get() to check for a product's details safely
carrot_details = inventory.get("Carrot", "Not Found")
print("\nCarrot Details:", carrot_details)

# 9. Clearing the inventory (for demonstration purposes)
# inventory.clear()
# print("\nCleared Inventory:", inventory)  # Uncomment to clear

# 10. Displaying items in the inventory
print("\nFinal Inventory:")
display_inventory(inventory)
