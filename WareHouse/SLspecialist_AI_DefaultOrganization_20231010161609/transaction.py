'''
This file contains the Transaction class which handles transaction history.
'''
import pandas as pd
class Transaction:
    def __init__(self):
        self.transactions = []
    def update_transactions(self):
        # Perform logic to update transactions from the database or any other data source
        # Your implementation here
        print("Updating transactions...")
    def import_transactions(self, file_path):
        # Perform logic to import transactions from a CSV or Excel file
        # Your implementation here
        df = pd.read_csv(file_path)
        self.transactions = df.to_dict('records')
        print("Transactions imported successfully.")
    def export_transactions(self, file_path):
        # Perform logic to export transactions to a CSV or Excel file
        # Your implementation here
        df = pd.DataFrame(self.transactions)
        df.to_csv(file_path, index=False)
        print("Transactions exported successfully.")
    def get_transactions(self):
        # Return the list of transactions
        return self.transactions