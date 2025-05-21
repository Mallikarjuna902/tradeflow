from owner import owner_menu
from dealer import dealer_menu
from customer import customer_menu

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

if _name_ == "_main_":
    main()