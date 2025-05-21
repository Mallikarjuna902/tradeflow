from utils import read_csv
IMPORT_FILE = "import.csv"

def dealer_menu():
    print("\n--- Dealer View ---")
    items = read_csv(IMPORT_FILE)
    for item in items:
        print(item)