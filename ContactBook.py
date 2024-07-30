import sys

contact_book = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    if name and phone:
        contact_book.append({
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        })
        print("\nContact added successfully!")
    else:
        print("\nName and phone number are required.")

def view_contacts():
    if not contact_book:
        print("\nNo contacts available.")
        return

    for contact in contact_book:
        contact_info = (
            f"Name: {contact['name']}\n"
            f"Phone: {contact['phone']}\n"
            f"Email: {contact['email']}\n"
            f"Address: {contact['address']}\n"
        )
        print(contact_info)

def search_contact():
    search_term = input("\nEnter name or phone number to search: ")

    if not search_term:
        print("\nSearch term cannot be empty.")
        return

    results = [contact for contact in contact_book if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]

    if not results:
        print("\nNo contacts found.")
        return

    for contact in results:
        contact_info = (
            f"Name: {contact['name']}\n"
            f"Phone: {contact['phone']}\n"
            f"Email: {contact['email']}\n"
            f"Address: {contact['address']}\n"
        )
        print(contact_info)

def update_contact():
    name = input("\nEnter the name of the contact to update: ")

    if not name:
        print("\nName cannot be empty.")
        return

    contact = next((c for c in contact_book if c['name'].lower() == name.lower()), None)

    if contact:
        new_phone = input(f"Enter new phone (current: {contact['phone']}): ")
        new_email = input(f"Enter new email (current: {contact['email']}): ")
        new_address = input(f"Enter new address (current: {contact['address']}): ")

        contact['phone'] = new_phone if new_phone else contact['phone']
        contact['email'] = new_email if new_email else contact['email']
        contact['address'] = new_address if new_address else contact['address']

        print("\nContact updated successfully!")
    else:
        print("\nContact not found.")

def delete_contact():
    name = input("\nEnter the name of the contact to delete: ")

    if not name:
        print("\nName cannot be empty.")
        return

    global contact_book
    initial_length = len(contact_book)
    contact_book = [contact for contact in contact_book if contact['name'].lower() != name.lower()]

    if len(contact_book) == initial_length:
        print("\nContact not found.")
    else:
        print("\nContact deleted successfully!")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exited.")
            sys.exit()
        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
