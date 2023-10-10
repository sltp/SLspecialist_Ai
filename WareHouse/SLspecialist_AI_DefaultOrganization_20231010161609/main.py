'''
This file contains the Dashboard class which displays the user's accounts, contacts, transactions, and analytics.
'''
from tkinter import Tk, Label, Button, OptionMenu, StringVar, filedialog, messagebox
from account import Account
from transaction import Transaction
from machine_learning import MachineLearning
class Dashboard:
    def __init__(self, master):
        self.master = master
        master.title("Dashboard")
        self.label = Label(master, text="Select Date Range:")
        self.label.pack()
        self.date_range_var = StringVar(master)
        self.date_range_var.set("Month")  # Default value
        self.date_range_option_menu = OptionMenu(master, self.date_range_var, "Month", "Week", "Year", "Day")
        self.date_range_option_menu.pack()
        self.refresh_button = Button(master, text="Refresh", command=self.refresh)
        self.refresh_button.pack()
        self.account = Account()
        self.transaction = Transaction()
        self.machine_learning = MachineLearning()
        self.logged_in = False
    def refresh(self):
        if self.logged_in:
            date_range = self.date_range_var.get()
            # Perform logic to update dashboard components based on the selected date range
            self.account.update_accounts()
            self.transaction.update_transactions()
            transactions = self.transaction.get_transactions()
            self.machine_learning.update_predictions(transactions)
            # Display updated dashboard components
        else:
            messagebox.showwarning("Not Logged In", "Please log in first.")
    def import_transactions(self):
        if self.logged_in:
            file_path = filedialog.askopenfilename()
            self.transaction.import_transactions(file_path)
            self.refresh()
        else:
            messagebox.showwarning("Not Logged In", "Please log in first.")
    def export_transactions(self):
        if self.logged_in:
            file_path = filedialog.asksaveasfilename()
            self.transaction.export_transactions(file_path)
        else:
            messagebox.showwarning("Not Logged In", "Please log in first.")
    def create_account(self):
        if self.logged_in:
            name = input("Enter account name: ")
            self.account.create_account(name)
            self.refresh()
        else:
            messagebox.showwarning("Not Logged In", "Please log in first.")
    def delete_account(self):
        if self.logged_in:
            account_id = input("Enter account ID: ")
            self.account.delete_account(account_id)
            self.refresh()
        else:
            messagebox.showwarning("Not Logged In", "Please log in first.")
    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        # Perform logic to validate the username and password
        if username == "admin" and password == "password":
            self.logged_in = True
            messagebox.showinfo("Login Successful", "You have successfully logged in!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
if __name__ == "__main__":
    root = Tk()
    dashboard = Dashboard(root)
    root.mainloop()