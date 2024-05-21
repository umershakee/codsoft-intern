class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
            return
        print("\n--- Contact List ---")
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact.name}: {contact.phone}")

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, index, new_contact):
        self.contacts[index] = new_contact

    def delete_contact(self, index):
        del self.contacts[index]

def get_contact_details():
    name = input("Muhammad Umer: ")
    phone = input("03181394702: ")
    email = input("oshakeel27@gmail.com: ")
    address = input("Gulshan: ")
    return Contact(name, phone, email, address)

def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            contact = get_contact_details()
            contact_book.add_contact(contact)
            print("Contact added successfully!")

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            keyword = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(keyword)
            if results:
                print("\n--- Search Results ---")
                for i, contact in enumerate(results, start=1):
                    print(f"{i}. Name: {contact.name}, Phone: {contact.phone}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            index = int(input("Enter index of contact to update: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                new_contact = get_contact_details()
                contact_book.update_contact(index, new_contact)
                print("Contact updated successfully!")
            else:
                print("Invalid index.")

        elif choice == '5':
            index = int(input("Enter index of contact to delete: ")) - 1
            if 0 <= index < len(contact_book.contacts):
                contact_book.delete_contact(index)
                print("Contact deleted successfully!")
            else:
                print("Invalid index.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
