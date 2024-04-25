Start the program

Define a list of allowed vehicles:
  - Ford F-150
  - Chevrolet Silverado
  - Tesla CyberTruck
  - Toyota Tundra
  - Nissan Titan

Loop continuously until the user decides to exit:
  - Display the main menu:
    - Show program version (v0.2) and name (AutoCountry Vehicle Finder)
    - Present options:
      1. PRINT all Authorized Vehicles
      2. SEARCH for Authorized Vehicle
      3. Exit
  
  - Prompt the user to enter their choice

  - If the user chooses "1":
    - Display the message: "The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:"
    - List all vehicles from the allowed vehicles list
    - Print a separation line for clarity

  - If the user chooses "2":
    - Prompt the user: "Please Enter the full Vehicle name:"
    - Get the vehicle name input from the user
    - Check if the entered vehicle name is in the list of allowed vehicles
    - If the vehicle is found:
      - Confirm: "[Vehicle Name] is an authorized vehicle"
    - If the vehicle is not found:
      - Alert the user: "[Vehicle Name] is not an authorized vehicle, if you received this in error please check the spelling and try again"
    - Print a separation line for clarity

  - If the user chooses "3":
    - Display the goodbye message: "Thank you for using the AutoCountry Vehicle Finder, good-bye!"
    - Pause for 2 seconds so the user can read the message
    - Terminate the program

  - If the user enters an invalid choice:
    - Inform the user that the choice is invalid
    - Prompt the user to try again

End program
