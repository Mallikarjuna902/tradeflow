from utils import read_csv, write_csv, append_csv

IMPORT_FILE = "import.csv"
EXPORT_FILE = "export.csv"
BILLING_FILE = "billing.csv"

def owner_menu():
    while True:
        print("\n--- Owner Menu ---")
        print("1. View Import Items")
        print("2. Add Item to Import")
        print("3. Update Import Item")
        print("4. Delete Import Item")
        print("5. View Billing")
        print("6. Exit")
        choice = input("Choose: ")

        if choice == '1':
            items = read_csv(IMPORT_FILE)
            for item in items:
                print(item)

        elif choice == '2':
            name = input("Item name: ")
            price = input("Price: ")
            qty = input("Quantity: ")
            append_csv(IMPORT_FILE, {'Item': name, 'Price': price, 'Quantity': qty})
            print("Item added.")

        elif choice == '3':
            items = read_csv(IMPORT_FILE)
            name = input("Item to update: ")
            for item in items:
                if item['Item'] == name:
                    item['Price'] = input("New price: ")
                    item['Quantity'] = input("New quantity: ")
            write_csv(IMPORT_FILE, items, ['Item', 'Price', 'Quantity'])
            print("Updated.")

        elif choice == '4':
            items = read_csv(IMPORT_FILE)
            name = input("Item to delete: ")
            updated = [item for item in items if item['Item'] != name]
            write_csv(IMPORT_FILE, updated, ['Item', 'Price', 'Quantity'])
            print("Deleted.")

        elif choice == '5':
            bills = read_csv(BILLING_FILE)
            for bill in bills:
                print(bill)

        elif choice == '6':
            break

def dealer_menu():
    print("\n--- Dealer View ---")
    items = read_csv(IMPORT_FILE)
    for item in items:
        print(item)

def customer_menu():
    print("\n--- Customer View ---")
    items = read_csv(IMPORT_FILE)
    for item in items:
        print(item)

    name = input("Your name: ")
    item_name = input("Item to buy: ")
    qty = int(input("Quantity: "))

    for item in items:
        if item['Item'] == item_name and int(item['Quantity']) >= qty:
            price = float(item['Price']) * qty
            item['Quantity'] = str(int(item['Quantity']) - qty)
            write_csv(IMPORT_FILE, items, ['Item', 'Price', 'Quantity'])

            append_csv(BILLING_FILE, {
                'Customer': name,
                'Item': item_name,
                'Quantity': qty,
                'Price': price
            })
            print("Purchase successful.")
            return
    print("Not enough stock or item not found.")

def main():
    print("Import/Export Business System")
    role = input("Enter role (owner/dealer/customer): ").lower()
    if role == 'owner':
        owner_menu()
    elif role == 'dealer':
        dealer_menu()
    elif role == 'customer':
        customer_menu()
    else:
        print("Invalid role.")

main()