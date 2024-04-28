Start the program

Define the filename for storing vehicle data as 'allowed_vehicles.txt'

Function load_vehicles:
    Try to open 'allowed_vehicles.txt'
    Read each line from the file and store it as a list of vehicles
    If file not found, return an empty list

Function save_vehicles:
    Open 'allowed_vehicles.txt' in write mode
    Write each vehicle from the list to the file

Function main_menu:
    Display the main menu with options:
        1. PRINT all Authorized Vehicles
        2. SEARCH for Authorized Vehicle
        3. ADD Authorized Vehicle
        4. DELETE Authorized Vehicle
        5. Exit

Function print_vehicles:
    Display "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
    List all vehicles
    Print a separation line

Function search_vehicle:
    Prompt the user to enter the full vehicle name
    Check if the vehicle is in the list
    If found, confirm the vehicle is authorized
    If not found, alert the user it is not authorized and suggest checking the spelling
    Print a separation line

Function add_vehicle:
    Prompt the user to enter the full vehicle name they wish to add
    Check if the vehicle is already in the list
    If not, add the vehicle to the list and save the updated list
    Confirm the vehicle has been added
    If already in the list, alert the user it is already authorized
    Print a separation line

Function delete_vehicle:
    Prompt the user to enter the full vehicle name they wish to remove
    Check if the vehicle is in the list
    If in the list, ask for confirmation to remove
    If confirmed, remove the vehicle from the list and save the updated list
    Confirm the vehicle has been removed
    If not confirmed, cancel the removal
    If the vehicle is not found, alert the user it is not in the list
    Print a separation line

Function main:
    Load vehicles using load_vehicles function
    While true:
        Call main_menu function
        Prompt the user to enter their choice
        If choice is "1", call print_vehicles function
        If choice is "2", call search_vehicle function
        If choice is "3", call add_vehicle function
        If choice is "4", call delete_vehicle function
        If choice is "5":
            Display "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
            Prompt "Press any key to exit..."
            Wait for any keypress
            Break the loop and terminate the program
        If invalid choice, inform the user and prompt again

End program
