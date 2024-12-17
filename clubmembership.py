members = []

fees = {"Premium": 215, "Gold": 189, "Silver": 125, "Basic": 89}

# CREATE DATA
def create_member():
    firstname = input("First Name: ")
    lastname = input("Last Name: ")
    phone = int(input("No. Tel: "))
    email = input("Email Address: ")

    package = ['Premium', 'Gold', 'Silver', 'Basic']
    print("\nAvailable Packages:")
    for i, item in enumerate(package):
        print(str(i) + ": " + str(item))

    index = int(input("\nChoose your monthly package plan: "))
    if 0 <= index < len(package):
        selected_item = package[index]
        print("\nYou have chosen: " + str(selected_item) + " Plan Package.")
    else:
        print("\nInvalid choice!")
        return

    import random
    member_id = random.randrange(1000, 9999)
    print("Your ID number is: " + str(member_id)) 
    membership_fee = fees[selected_item]
    print("Your membership fee is: RM" + str(membership_fee) + " . Please complete your payment before the end of the month.")
    
    members.append({
        "id": member_id,
        "firstname": firstname,
        "lastname": lastname,
        "phone": phone,
        "email": email,
        "membership_type": selected_item,
        "membership_fee": membership_fee
    })
    print("\nMember added successfully!")

# READ DATA
def read_records():
    if not members:
        print("\nNo records found.")
        return
        
    print("\nList of Members:")
    for member in members:
        print("\nMember Found:")
        print("Member ID      : " + str(member['id']))
        print("First Name     : " + member['firstname'])
        print("Last Name      : " + member['lastname'])
        print("Phone          : " + str (member['phone']))
        print("Email          : " + member['email'])
        print("Membership Type: " + member['membership_type'])
        print("Membership Fee : RM" + str(member['membership_fee']))
        print("_" * 55)

# SEARCH MEMBER
def search_member_id():
    member_id = int(input("\nEnter Your Member ID: "))
    for member in members:
        if member["id"] == member_id:
            print("\nMember Found:")
            print("Member ID      : " + str(member['id']))
            print("First Name     : " + member['firstname'])
            print("Last Name      : " + member['lastname'])
            print("Phone          : " + str (member['phone']))
            print("Email          : " + member['email'])
            print("Membership Type: " + member['membership_type'])
            print("Membership Fee : RM" + str(member['membership_fee']))
            print("_" * 55)
            return member
    print("\nMember not found.")
    return None

# UPDATE DATA
def update_data():
    member = search_member_id()
    if member:
        print("\nWhat Do You Want To Update?:")
        print("1. First Name")
        print("2. Last Name")
        print("3. Phone")
        print("4. Email")
        print("5. Membership Type")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            member['firstname'] = input("Correct your First Name: ")
        elif choice == "2":
            member['lastname'] = input("Correct your Last Name: ")
        elif choice == "3":
            member['phone'] = input("Enter your new phone number: ")
        elif choice == "4":
            member['email'] = input("Enter your new email address: ")
        elif choice == "5":
            package = ['Premium', 'Gold', 'Silver', 'Basic']
            print("\nAvailable Packages:")
            for i, item in enumerate(package):
                print(f"{i}: {item}")
            index = int(input("\nChoose your monthly package plan: "))
            if 0 <= index < len(package):
                member['membership_type'] = package[index]
                member['membership_fee'] = fees[package[index]]
                print("\nYour data have been updated successfully!")
        else:
            print("\nInvalid Choice")

# DELETE DATA
def delete_data():
    member = search_member_id()
    if member:
        confirm = input("\nAre you sure you want to delete this member? (y/n): ").lower()
        if confirm == "y":
            members.remove(member)
            print("\nMember deleted successfully!")
        else:
            print("\nDeletion cancelled.")
    else:
        print("\nMember not found.")

# MAIN MENU
def main():
    while True:
        print("\nMembership System")
        print("1. Add Member")
        print("2. View Members")
        print("3. Search Member")
        print("4. Update Information")
        print("5. Delete Account")
        print("6. Exit")
        choice = input("\nHow can I help you?: ")

        if choice == "1":
            create_member()
        elif choice == "2":
            read_records()
        elif choice == "3":
            search_member_id()
        elif choice == "4":
            update_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            print("\nYou've successfully logged out. Come back soon!")
            break
        else:
            print("\nInvalid choice. Please try again.")

main()