# Contact Management System

## Project Objective
A Python-based Command-Line Interface (CLI) application that demonstrates core
programming fundamentals — functions, lists/dictionaries, loops, conditionals,
CRUD operations, input validation, and exception handling — by managing a
list of contacts. This is Project 1, Part 1 of the HK Educational Academy
Python Developer work-experience program.

## Features
- Add a new contact with an auto-generated unique Contact ID
- View all contacts in a clean, tabular format
- Update any field of an existing contact (blank input keeps the old value)
- Delete a contact by ID, with a confirmation prompt
- Input validation for phone numbers and email addresses
- Graceful exception handling — invalid input never crashes the program
- Modular code: each operation lives in its own function
- Preloaded sample data so the app can be demoed immediately

## Technologies Used
- Python 3
- Standard library only (`re` for validation) — no external dependencies

## How to Run the Application
1. Make sure Python 3 is installed.
2. Open a terminal in the project folder.
3. Run:
   ```
   python main.py
   ```

## How to Use the Menu
```
===== CONTACT MANAGEMENT SYSTEM =====
1. Add Contact
2. View Contacts
3. Update Contact
4. Delete Contact
5. Exit
```
Enter the number of the option you want and follow the prompts.

## Example Usage

**Adding a contact:**
```
Enter your choice (1-5): 1
--- Add Contact ---
Full Name: Junaid Baloch
Phone Number: 03451112233
Email Address: junaid@example.com
City: Sukkur
Company: Baloch Enterprises

Contact added successfully!
Contact ID: 004
```

**Viewing contacts:**
```
Enter your choice (1-5): 2
--- View Contacts ---
------------------------------------------------------------------------------------------
ID    Name              Phone           Email                    City        Company
------------------------------------------------------------------------------------------
001   Ali Ahmed         03001234567     ali@example.com          Nawabshah   ABC Technologies
002   Sara Khan         03111234567     sara@example.com         Karachi     Khan Traders
------------------------------------------------------------------------------------------
Total contacts: 2
```

**Deleting a contact:**
```
Enter your choice (1-5): 4
--- Delete Contact ---
Enter Contact ID to delete: 002
Are you sure you want to delete Contact ID 002 (Sara Khan)?
Enter Y to confirm or N to cancel: Y
Contact ID 002 deleted successfully!
```

## Project Structure
```
contact-management-system/
│
├── main.py
├── README.md
├── sample_data.md
└── screenshots/
```
