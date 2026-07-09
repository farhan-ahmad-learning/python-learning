# CONTACT BOOK
# Week 2 - Wednesday mini challenge
# Concepts used - nested dictionaries, loops, f-strings, .get(), .lower()

contacts = {
    "1": {
        "name": "Farhan Ahmad",
        "phone": "9876543210",
        "email": "farhanxyz@xyz.com"
    },
    "2": {
        "name": "Uvais Khan",
        "phone": "1234567890",
        "email": "uvaisxyz@xyz.com"
    },
    "3": {
        "name": "Yusuf Ansari",
        "phone": "1234509876",
        "email": "yusufxyz@xyz.com"
    }
}

# Display all contacts
print("===== CONTACT BOOK =====")
print()
for number, details in contacts.items():
    print(f"{number}. {details['name']}")
    print(f"Phone   : +91-{details['phone']}")
    print(f"Email   : {details['email']}")
    print()

print("============================")

# Search for a contact
while True:
    print()
    search = input("Search contact (or type 'exit' to quit): ").lower().strip()
    if search == "exit":
        print("Goodbye!")
        break

        # Search through all contacts
    found = False
    for number, details in contacts.items():
        if search in details["name"].lower():
            print("Found!")
            print(f"Name     :{details['name']}")
            print(f"Phone    :{details['phone']}")
            print(f"Email    :{details['email']}")
            found = True
            break
    if not found:
        print("Contact not found!")