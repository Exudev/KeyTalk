import SavedAccount
import datetime
import JsonFiles

# create a function that takes a list of accounts, where the user is prompted to create an account with it's website name, username, password and datecreated, and then the account is added to the list of accounts
def createAccount(accounts):
    websiteName = input("Please enter the website name: ")
    username = input("Please enter the username: ")
    password = input("Please enter the password: ")
    # [MODIFIED] changed dateCreated from imput to date.today
    dateCreated = datetime.date.today()
    # create a new account using the class Account from SavedAccount.py
    newAccount = SavedAccount.Account(len(accounts) + 1, websiteName, username, password, dateCreated, dateCreated, dateCreated)
    # add the new account to the list of accounts
    accounts.append(newAccount)
    # [MODIFIED] saved the accounts to json
    JsonFiles.writeAccountsToFile(accounts)
    # return the list of accounts
    import UI_Dashboard
    UI_Dashboard.displayMenu(accounts)

# create a function that takes a list of accounts, if it's empty, ask the user if it wants to create an account or exit the program, if yes, execute createAccount(), if no, exit the program
def newAccount(accounts):
    if len(accounts) == 0:
        print("There are no accounts.")
        userInput = input("Would you like to create an account? (Y/N): ")
        if userInput.upper() == "Y":
            createAccount(accounts)
        elif userInput.upper() == "N":
            quit()
        else:
            print("Error: Invalid input.")
            newAccount(accounts)
    # else:
    #     createAccount(accounts)