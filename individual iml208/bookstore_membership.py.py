#sinaran bookstore membership registration
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from datetime import datetime, timedelta

# A simple list to act as an in-memory database
members = []

# Function to calculate membership expiration (1 year after the start date)
def calculate_expiration(start_date):
    return start_date + timedelta(days=365)

# Function to register a new member (Create)
def register_member():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get()
    dob = entry_dob.get_date()
    membership_type = membership_type_var.get()
    start_date = start_date_entry.get_date()
    expiration_date = calculate_expiration(start_date)

    # Validate input
    if not name or not email or not phone or not address:
        messagebox.showwarning("Input Error", "All fields must be filled.")
        return

    # Create a new member
    member = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "dob": dob,
        "membership_type": membership_type,
        "start_date": start_date,
        "expiration_date": expiration_date
    }

    # Add member to the list
    members.append(member)
    messagebox.showinfo("Success", "Member registered successfully.")
    clear_form()

# Function to view member details (Read)
def view_member():
    member_name = entry_name.get()

    # Search for the member by name
    for member in members:
        if member["name"].lower() == member_name.lower():
            messagebox.showinfo("Member Details", f"Name: {member['name']}\n"
                                                 f"Email: {member['email']}\n"
                                                 f"Phone: {member['phone']}\n"
                                                 f"Address: {member['address']}\n"
                                                 f"DOB: {member['dob']}\n"
                                                 f"Membership Type: {member['membership_type']}\n"
                                                 f"Start Date: {member['start_date']}\n"
                                                 f"Expiration Date: {member['expiration_date']}")
            return
    messagebox.showwarning("Not Found", "Member not found.")

# Function to update member details (Update)
def update_member():
    member_name = entry_name.get()

    for member in members:
        if member["name"].lower() == member_name.lower():
            # Update member data
            member["email"] = entry_email.get()
            member["phone"] = entry_phone.get()
            member["address"] = entry_address.get()
            member["dob"] = entry_dob.get_date()
            member["membership_type"] = membership_type_var.get()
            member["start_date"] = start_date_entry.get_date()
            member["expiration_date"] = calculate_expiration(member["start_date"])

            messagebox.showinfo("Success", "Member details updated successfully.")
            clear_form()
            return
    messagebox.showwarning("Not Found", "Member not found.")

# Function to delete member details (Delete)
def delete_member():
    member_name = entry_name.get()

    global members
    members = [member for member in members if member["name"].lower() != member_name.lower()]
    
    messagebox.showinfo("Success", "Member deleted successfully.")
    clear_form()

# Function to clear form fields
def clear_form():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_dob.set_date(datetime.today())
    membership_type_var.set("regular")
    start_date_entry.set_date(datetime.today())

#GUI 
# Create the main window
root = tk.Tk()
root.title("Sinaran Membership Bookstore Registration")
root.geometry("600x400")

# Set the window background color
root.configure(bg="#FC94AF")  # Rose colour background 

# Create labels and entry widgets for personal data
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, pady=5, padx=10, sticky="w")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, pady=5, padx=10, sticky="w")

label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, pady=5, padx=10, sticky="w")
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, pady=5, padx=10, sticky="w")

label_phone = tk.Label(root, text="Phone Number:")
label_phone.grid(row=2, column=0, pady=5, padx=10, sticky="w")
entry_phone = tk.Entry(root)
entry_phone.grid(row=2, column=1, pady=5, padx=10, sticky="w")

label_address = tk.Label(root, text="Address:")
label_address.grid(row=3, column=0, pady=5, padx=10, sticky="w")
entry_address = tk.Entry(root)
entry_address.grid(row=3, column=1, pady=5, padx=10, sticky="w")

label_dob = tk.Label(root, text="Date of Birth:")
label_dob.grid(row=4, column=0, pady=5, padx=10, sticky="w")
entry_dob = DateEntry(root, date_pattern='yyyy-mm-dd')
entry_dob.grid(row=4, column=1, pady=5, padx=10, sticky="w")

# Membership Type 
label_membership_type = tk.Label(root, text="Membership Type:")
label_membership_type.grid(row=5, column=0, pady=5, padx=10, sticky="w")
membership_type_var = tk.StringVar(value="regular")
membership_types = ["regular", "VIP", "premium", "student"]
for i, membership in enumerate(membership_types):
    tk.Radiobutton(root, text=membership.capitalize(), variable=membership_type_var, value=membership).grid(row=5, column=i+1, pady=5, padx=10, sticky="w")

# Membership Start Date
label_start_date = tk.Label(root, text="Start Date:")
label_start_date.grid(row=6, column=0, pady=5, padx=10, sticky="w")
start_date_entry = DateEntry(root, date_pattern='yyyy-mm-dd')
start_date_entry.grid(row=6, column=1, pady=5, padx=10, sticky="w")

# CRUD Buttons
button_register = tk.Button(root, text="Register", command=register_member)
button_register.grid(row=7, column=0, pady=10, padx=10)

button_view = tk.Button(root, text="View Member", command=view_member)
button_view.grid(row=7, column=1, pady=10, padx=10)

button_update = tk.Button(root, text="Update Member", command=update_member)
button_update.grid(row=8, column=0, pady=10, padx=10)

button_delete = tk.Button(root, text="Delete Member", command=delete_member)
button_delete.grid(row=8, column=1, pady=10, padx=10)

# Run the Tkinter event loop
root.mainloop()
