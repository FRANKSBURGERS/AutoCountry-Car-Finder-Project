Start the program

Define the filename for storing vehicle data as 'allowed_vehicles.txt'

Load vehicles from the file:
    Open 'allowed_vehicles.txt'
    Read each line from the file and store it as a list of vehicles

Loop continuously until the user decides to exit:
    Display the main menu:
        Show program version (v0.4) and name (AutoCountry Vehicle Finder)
        Present options:
            1. PRINT all Authorized Vehicles
            2. SEARCH for Authorized Vehicle
            3. ADD Authorized Vehicle
            4. DELETE Authorized Vehicle
            5. Exit

  Prompt the user to enter their choice

 If the user chooses "1":
        Display the message: "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
        List all vehicles from the list
        Print a separation line for clarity

   If the user chooses "2":
        Prompt the user: "Please Enter the full Vehicle name:"
        Get the vehicle name input from the user
        Check if the entered vehicle name is in the list of allowed vehicles
        If the vehicle is found:
            Confirm: "[Vehicle Name] is an authorized vehicle"
        If the vehicle is not found:
            Alert the user: "[Vehicle Name] is not an authorized vehicle, if you received this in error please check the spelling and try again"
        Print a separation line for clarity

  If the user chooses "3":
        Prompt the user: "Please Enter the full Vehicle name you would like to add:"
        Get the vehicle name input from the user
        Check if the vehicle is already in the list
        If not in the list:
            Add the new vehicle to the list
            Save the updated list to 'allowed_vehicles.txt'
            Confirm: "You have added '[Vehicle Name]' as an authorized vehicle"
        Else:
            Alert the user: "[Vehicle Name] is already an authorized vehicle"
        Print a separation line for clarity

If the user chooses "4":
        Prompt the user: "Please Enter the full Vehicle name you would like to REMOVE:"
        Get the vehicle name input from the user
        Check if the vehicle is in the list
        If in the list:
            Ask for confirmation: "Are you sure you want to remove '[Vehicle Name]' from the Authorized Vehicles List?"
            If confirmed 'yes':
                Remove the vehicle from the list
                Save the updated list to 'allowed_vehicles.txt'
                Confirm: "You have REMOVED '[Vehicle Name]' as an authorized vehicle"
            Else:
                Alert the user: "Removal cancelled."
      Else:
            Alert the user: "[Vehicle Name] is not found in the authorized vehicles list."
        Print a separation line for clarity

 If the user chooses "5":
        Display the goodbye message: "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
        Pause for 2 seconds so the user can read the message
        Terminate the program

 If the user enters an invalid choice:
        Inform the user that the choice is invalid
        Prompt the user to try again

End program
