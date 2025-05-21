import csv

def read_csv(filename):
    try:
        with open(filename, 'r') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []

def write_csv(filename, data, headers):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

def append_csv(filename, row):
    data = read_csv(filename)
    headers = row.keys()
    data.append(row)
    write_csv(filename, data, headers)