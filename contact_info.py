# Python profram That Hepls To Access, Add, And REmove Com=ntact delatils

def contact_info():
    # Fixed syntax: Added quotes around dictionary keys and string values
    contact_details = { 
        "airtel": { "co_name": "airtel", "co_no": 123, "co_email": "airtel@123" }, 
        "jio": { "co_name": "jio", "co_no": 456, "co_email": "jio@456" }, 
        "bsnl": { "co_name": "bsnl", "co_no": 789, "co_email": "bsnl@789" } 
    }
    
    while True:
        print("\n--- Contact Menu ---")
        print("Choose 1 if u want to access existing contact!") 
        print("Choose 2 if u want to add new contact!") 
        print("Choose 3 if u want to delete existing contact!") 

        
        
        # Validating choice input
        try:
            choice = int(input("Enter choice like 1, 2 or 3 only: "))
        except ValueError:
            print("The choice should be integer only!")
            continue

        print("Displaying The Contact Info! \n")
        for keys, values in contact_details.items():
            for key, value in contact_details[keys].items():
                print(f"contact of '{contact_details[keys][key]}' is ")
                print(f"  {keys}: {values}")
                break

            
        if choice == 1:
            co_name = input("Enter the contact name: ").lower() # lower() helps match keys case-insensitively
            if co_name in contact_details:
                # Fixed logic: print only the searched contact details, not the whole dictionary loop
                print(f"\nDetails for {co_name}:")
                for key, value in contact_details[co_name].items():
                    print(f"  {key}: {value}")
            else:
                print("Name not found!")
                
        elif choice == 2:
            co_name = input("Enter new name: ").lower()
            co_no = input("Enter new number: ")
            co_email = input("Enter new email: ")
    
            contact_details[co_name] = {
                "co_name": co_name,
                "co_no": co_no,
                "co_email": co_email
            }
            print(f"\nContact '{co_name}' added successfully!")
            
        
                
        else:
            print("Invalid choice! Please select 1, 2, or 3.")
            continue # Skip the repeat prompt if choice was invalid

        # Ask to execute again (Fixed: .lower() simplifies checking for 'yes')
        attempt = input("\nWant to execute again? Type YES or NO: ").lower()
        if attempt != "yes":
            print("Exiting program. Goodbye!")
            break

# Call the function to run the program
contact_info()
