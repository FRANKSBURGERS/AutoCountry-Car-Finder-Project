import time  

def main_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.2")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. Exit")

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

def main():
    allowed_vehicles_list = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
    while True:
        main_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            print_vehicles(allowed_vehicles_list)
        elif choice == "2":
            search_vehicle(allowed_vehicles_list)
        elif choice == "3":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            time.sleep(2)  
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
