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

# create a function that takes an account and a list of accounts, ask the user if it wants to modify the WebSite name with W, the username with U or the password with P, or B to go back, if W, ask for the new website name and save it to the account, if U, ask for the new username and save it to the account, if P, ask for the new password and save it to the account, if B, execute displayMenu(). If the user changed anything, update the lastModified date to today
def modifyAccount(account, accounts):
    # import time and use time sleep to make the program wait for 1 second, then clear the console
    import time
    import os
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Account ID: " + str(account.id))
    print("Website Name: " + account.websiteName)
    print("Username: " + account.username)
    print("Password: " + account.password)
    print("Date Created: " + account.dateCreated.strftime("%m/%d/%Y"))
    print("Last Modified: " + account.dateModified.strftime("%m/%d/%Y"))
    print("Last Checked: " + account.lastChecked.strftime("%m/%d/%Y"))
    print("W = Modify Website Name")
    print("U = Modify Username")
    print("P = Modify Password")
    print("B = Back")
    userInput = input("Please enter a command: ")
    if userInput.upper() == "W":
        account.websiteName = input("Please enter the new website name: ")
        account.lastModified = datetime.date.today()
        JsonFiles.writeAccountsToFile(accounts)
        modifyAccount(account, accounts)
    elif userInput.upper() == "U":
        account.username = input("Please enter the new username: ")
        account.lastModified = datetime.date.today()
        JsonFiles.writeAccountsToFile(accounts)
        modifyAccount(account, accounts)
    elif userInput.upper() == "P":
        account.password = input("Please enter the new password: ")
        account.lastModified = datetime.date.today()
        JsonFiles.writeAccountsToFile(accounts)
        modifyAccount(account, accounts)
    elif userInput.upper() == "B":
        import UI_Dashboard
        UI_Dashboard.displayMenu(accounts)
    else:
        print("Error: Invalid input.")
        modifyAccount(account, accounts)