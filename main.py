import re

contacts = []
userId = 1


def displayMenu():
    "Display the main menu."
    print("===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")


def validatePhone(phone):
    "Validate a phone number"
    pattern = r'^\+?\d{10,15}$'
    return re.match(pattern, phone.strip()) is not None


def validateEmail(email):
    "Validate a basic email format."
    pattern = r'^[\w\.\-]+@[\w\-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email.strip()) is not None


def GetNonEmpty(prompt):
    "ask the user for input until a non-empty value is given."
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty.")


def generateContactId():
    "Generate a unique, zero-padded 3-digit contact ID."
    global userId
    newId = f"{userId:03d}"
    userId += 1
    return newId


def findContactById(contactId):
    "Return the contact"
    for contact in contacts:
        if contact["id"] == contactId:
            return contact
    return None


def addContact():
    "add a new contact."
    print("--- Add Contact ---")
    try:
        name = GetNonEmpty("Full Name: ")

        while True:
            phone = GetNonEmpty("Phone Number: ")
            if validatePhone(phone):
                break
            print("Invalid phone number")

        while True:
            email = GetNonEmpty("Email Address: ")
            if validateEmail(email):
                break
            print("Invalid email format.")

        city = GetNonEmpty("City: ")
        company = GetNonEmpty("Company: ")

        contactId = generateContactId()
        contacts.append({
            "id": contactId,
            "name": name,
            "phone": phone,
            "email": email,
            "city": city,
            "company": company
        })

        print("\nContact added successfully!")
        print(f"Contact ID: {contactId}")

    except Exception as e:
        print(f"An error occurred while adding the contact: {e}")


def viewContact():
    "Display all saved contacts"
    print("--- View Contacts ---")
    if not contacts:
        print("No contacts found.")
        return

    print("-" * 90)
    print(f"{'ID':<6}{'Name':<18}{'Phone':<16}{'Email':<25}{'City':<12}{'Company'}")
    print("-" * 90)
    for c in contacts:
        print(f"{c['id']:<6}{c['name']:<18}{c['phone']:<16}{c['email']:<25}{c['city']:<12}{c['company']}")
    print("-" * 90)
    print(f"Total contacts: {len(contacts)}")


def updateContact():
    "Update an existing contact's details, selected by ID."
    print("--- Update Contact ---")
    if not contacts:
        print("No contacts found.")
        return

    try:
        contactId = GetNonEmpty("Enter Contact ID to update: ")
        contact = findContactById(contactId)

        if not contact:
            print(f"No contact found with ID {contactId}.")
            return

        print("Leave a field blank to keep its current value.")

        newName = input(f"Full Name [{contact['name']}]: ").strip()
        if newName:
            contact["name"] = newName

        while True:
            newPhone = input(f"Phone Number [{contact['phone']}]: ").strip()
            if not newPhone:
                break
            if validatePhone(newPhone):
                contact["phone"] = newPhone
                break
            print("Invalid phone number.")
        while True:
            newEmail = input(f"Email Address [{contact['email']}]: ").strip()
            if not newEmail:
                break
            if validateEmail(newEmail):
                contact["email"] = newEmail
                break
            print("Invalid email format")

        newCity = input(f"City [{contact['city']}]: ").strip()
        if newCity:
            contact["city"] = newCity

        newCompany = input(f"Company [{contact['company']}]: ").strip()
        if newCompany:
            contact["company"] = newCompany

        print(f"Contact updated successfully!")

    except Exception as e:
        print(f"An error occurred while updating the contact: {e}")


def deleteContact():
    "Delete a contact by ID, after user confirmation."
    print("--- Delete Contact ---")
    if not contacts:
        print("No contacts found.")
        return

    try:
        contactId = GetNonEmpty("Enter Contact ID to delete: ")
        contact = findContactById(contactId)

        if not contact:
            print(f"No contact found with ID {contactId}.")
            return

        confirm = input(f"Are you sure you want to delete Contact ID {contactId} "
                         f"({contact['name']})?\nEnter Y to confirm or N to cancel: ").strip().lower()

        if confirm == "y":
            contacts.remove(contact)
            print(f"Contact ID {contactId} deleted successfully!")
        elif confirm == "n":
            print("Deletion cancelled.")
        else:
            print("Invalid input. Deletion cancelled.")

    except Exception as e:
        print(f"An error occurred while deleting the contact: {e}")


def loadSampleData():
    "Some Data Here."
    global userId
    samples = [
        {"name": "Ali Ahmed", "phone": "03001234567", "email": "ali@example.com",
         "city": "Nawabshah", "company": "ABC Technologies"},
        {"name": "Sara Khan", "phone": "03111234567", "email": "sara@example.com",
         "city": "Karachi", "company": "Khan Traders"},
        {"name": "Bilal Hussain", "phone": "03211234567", "email": "bilal@example.com",
         "city": "Hyderabad", "company": "HK Educational Academy"},
    ]
    for s in samples:
        contactId = generateContactId()
        contacts.append({"id": contactId, **s})


def main():
    "Main program loop."
    loadSampleData()

    while True:
        displayMenu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            addContact()
        elif choice == "2":
            viewContact()
        elif choice == "3":
            updateContact()
        elif choice == "4":
            deleteContact()
        elif choice == "5":
            print("\nThank you for using this")
            break
        else:
            print("Invalid choice. Please select an option from 1 to 5.")


if __name__ == "__main__":
    main()