import time

def load_vehicles(filename):
    try:
        with open(filename, 'r') as file:
            vehicles = [line.strip() for line in file.readlines()]
        return vehicles
    except FileNotFoundError:
        return []

def save_vehicles(allowed_vehicles_list, filename):
    with open(filename, 'w') as file:
        for vehicle in allowed_vehicles_list:
            file.write(vehicle + "\n")

def main_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.6")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")

def print_vehicles(allowed_vehicles_list):
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in allowed_vehicles_list:
        print(vehicle)
    print("********************************")

def search_vehicle(allowed_vehicles_list):
    vehicle_search = input("Please Enter the full Vehicle name: ")
    if vehicle_search in allowed_vehicles_list:
        print(f"{vehicle_search} is an authorized vehicle")
    else:
        print(f"{vehicle_search} is not an authorized vehicle, if you received this in error please check the spelling and try again")
    print("********************************")

def add_vehicle(allowed_vehicles_list, filename):
    new_vehicle = input("Please Enter the full Vehicle name you would like to add: ")
    if new_vehicle not in allowed_vehicles_list:
        allowed_vehicles_list.append(new_vehicle)
        save_vehicles(allowed_vehicles_list, filename)
        print(f"You have added \"{new_vehicle}\" as an authorized vehicle")
    else:
        print(f"{new_vehicle} is already an authorized vehicle")
    print("********************************")

def delete_vehicle(allowed_vehicles_list, filename):
    vehicle_to_remove = input("Please Enter the full Vehicle name you would like to REMOVE: ")
    if vehicle_to_remove in allowed_vehicles_list:
        confirmation = input(f"Are you sure you want to remove \"{vehicle_to_remove}\" from the Authorized Vehicles List? (yes/no): ")
        if confirmation.lower() == "yes":
            allowed_vehicles_list.remove(vehicle_to_remove)
            save_vehicles(allowed_vehicles_list, filename)
            print(f"You have REMOVED \"{vehicle_to_remove}\" as an authorized vehicle")
        else:
            print("Removal cancelled.")
    else:
        print(f"{vehicle_to_remove} is not found in the authorized vehicles list.")
    print("********************************")

def main():
    filename = 'allowed_vehicles.txt'
    allowed_vehicles_list = load_vehicles(filename)
    while True:
        main_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            print_vehicles(allowed_vehicles_list)
        elif choice == "2":
            search_vehicle(allowed_vehicles_list)
        elif choice == "3":
            add_vehicle(allowed_vehicles_list, filename)
        elif choice == "4":
            delete_vehicle(allowed_vehicles_list, filename)
        elif choice == "5":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            input("Press any key to exit...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
