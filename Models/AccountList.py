# Create a class "AccountList" with a key and a list of accounts


class AccountList:
    def __init__(self, key, accounts):
        self.key = key
        self.accounts = accounts

    def __str__(self):
        return f"Key: {self.key}, Accounts: {self.accounts}"