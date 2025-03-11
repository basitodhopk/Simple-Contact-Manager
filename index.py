import json
import os

CONTACT_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts[name] = {"Phone": phone, "Email": email}
    save_contacts(contacts)
    print(f"{name}'s contact has been saved!")


def search_contact(name):
    contacts = load_contacts()
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found!"

def update_contact(name, phone=None, email=None):
    contacts = load_contacts()
    if name in contacts:
        if phone:
            contacts[name]["Phone"] = phone
        if email:
            contacts[name]["Email"] = email
        save_contacts(contacts)
        print(f"{name}'s contact has been updated!")
    else:
        print("Contact not found!")

def delete_contact(name):
    contacts = load_contacts()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"{name}'s contact has been deleted!")
    else:
        print("Contact not found!")

if __name__ == "__main__":
    while True:
        print("\n📞 Contact Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Show All Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            add_contact(name, phone, email)
        elif choice == "2":
            name = input("Search Name: ")
            print(search_contact(name))
        elif choice == "3":
            name = input("Name to update: ")
            phone = input("New Phone (Press Enter to skip): ")
            email = input("New Email (Press Enter to skip): ")
            update_contact(name, phone if phone else None, email if email else None)
        elif choice == "4":
            name = input("Name to delete: ")
            delete_contact(name)
        elif choice == "5":
            contacts = load_contacts()
            for name, details in contacts.items():
                print(f"{name} - {details}")
        elif choice == "6":
            print("Exiting Contact Book...")
            break
        else:
            print("Invalid choice! Try again.")
