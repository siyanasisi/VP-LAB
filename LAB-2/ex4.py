contacts = {
    "Plamen": "0886 777 333",
    "Svetla": "0888 111 222",
    "David":  "0855 666 444",
    "Mimi":   "0877 444 111"
}

def add_contact(name, phone):
    contacts[name] = phone

def search_contact(name):
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found"

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted")
    else:
        print("Contact not found")

def show_contacts():
    for name, phone in contacts.items():
        print(name, phone)

add_contact("Sisi", "0888 888 888")

print("Sisi's phone number", search_contact("Sisi"))

delete_contact("David")

print("\nAll contacts")
show_contacts()