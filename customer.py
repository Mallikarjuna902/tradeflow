from utils import read_csv, write_csv, append_csv
IMPORT_FILE = "import.csv"
BILLING_FILE = "billing.csv"

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