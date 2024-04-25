import time

def main_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.1")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. Exit")

def print_vehicles(allowed_vehicles_list):
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in allowed_vehicles_list:
        print(vehicle)
    print("********************************")

def main():
    allowed_vehicles_list = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
    while True:
        main_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            print_vehicles(allowed_vehicles_list)
        elif choice == "2":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            time.sleep(5)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

