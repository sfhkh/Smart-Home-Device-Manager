devices = []
# The code will run by give them the function and make sure evrithing is running smoothly ,without error
while True:
    print("\nSMART CLASSROOM DEVICE MANAGER")
    print("1. Add a device")
    print("2. Update device status")
    print("3. View all devices")
    print("4. Search for a device")
    print("5. Exit")

    choice = input("Choose an option from 1 to 5: ")

    # On this parth of the code we add the request of new devise by adding the name and all the function and request 
    if choice == "1":
        name = input("Enter device name: ").strip()
        room = input("Enter room: ").strip()
        status = input(
            "Enter status (online, offline, or under maintenance): "
        ).strip().lower()

        if name == "" or room == "":
            print("Error: Device name and room cannot be empty.")

        elif status not in ["online", "offline", "under maintenance"]:
            print("Error: Invalid device status.")

        else:
            device = {
                "name": name,
                "room": room,
                "status": status
            }

            devices.append(device)
            print("Device added successfully.")

    # Update the status, the 3th parth show the the loop and functiomn 
    elif choice == "2":
        search_name = input("Enter the device name: ").strip()
        device_found = False

        for device in devices:
            if device["name"].lower() == search_name.lower():
                new_status = input(
                    "Enter new status "
                    "(online, offline, or under maintenance): "
                ).strip().lower()

                if new_status in [
                    "online",
                    "offline",
                    "under maintenance"
                ]:
                    device["status"] = new_status
                    print("Device status updated successfully.")
                else:
                    print("Error: Invalid status.")

                device_found = True
                break

        if device_found == False:
            print("Device not found.")

    # View all devices
    elif choice == "3":
        if len(devices) == 0:
            print("No devices have been added.")
        else:
            print("\nDEVICE LIST")

            for device in devices:
                print("----------------------------")
                print("Device:", device["name"])
                print("Room:", device["room"])
                print("Status:", device["status"])

    # Search for a for function and make the choice of no by use no from 1-5 
    elif choice == "4":
        search_name = input("Enter the device name: ").strip()
        device_found = False

        for device in devices:
            if device["name"].lower() == search_name.lower():
                print("\nDevice found:")
                print("Device:", device["name"])
                print("Room:", device["room"])
                print("Status:", device["status"])
                device_found = True
                break

        if device_found == False:
            print("Device not found.")

    # Exit the program
    elif choice == "5":
        print("Thank you for using the program.")
        break

    else:
        print("Invalid option. Please choose from 1 to 5.")
