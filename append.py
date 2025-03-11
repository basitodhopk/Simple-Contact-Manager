import json

CONTACT_FILE = "contacts.json"


try:
    with open(CONTACT_FILE, "r") as file:
        contacts = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    contacts = {} 

name = input("Enter Name: ")
phone = input("Enter Phone: ")
email = input("Enter Email: ")


contacts[name] = {"Phone": phone, "Email": email}


with open(CONTACT_FILE, "w") as file:
    json.dump(contacts, file, indent=4)

print(f"{name}'s contact added successfully!")
