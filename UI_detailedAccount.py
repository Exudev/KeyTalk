import SavedAccount

# taking an account as input and printing the details of the account
def printAccount(account, accounts):
    print("ID: " + str(account.id))
    print("Website Name: " + account.websiteName)
    print("Username: " + account.username)
    print("Password: " + account.password)
    print("Date Created: " + account.dateCreated.strftime("%d/%m/%Y"))
    print("Date Modified: " + account.dateModified.strftime("%d/%m/%Y"))
    print("Last Checked: " + account.lastChecked.strftime("%d/%m/%Y"))

    readKey(account, accounts)

# read key as input, 'b' to go back to UI_Dashboard.py, 'm' to modify the account, 'd' to delete the account, 'q' to quit
def readKey(account, accounts):
    # print what every option does
    # Print an option to copy password to clipboard by pressing C
    print("C = Copy Password to Clipboard")
    print("M = Modify")
    print("D = Delete")
    print("B = Back")
    print("Q = Quit")
    key = input("Enter key: ")
    if key.upper() == 'B':
        # excecute displaymenu() from UI_Dashboard.py
        import UI_Dashboard
        UI_Dashboard.displayMenu(accounts)
        return key
    elif key.upper() == 'M':
        # excecute modifyAccount() from UI_AccountCreation.py
        import UI_AccountCreation
        UI_AccountCreation.modifyAccount(account, accounts)
        return key
    elif key.upper() == 'D':
        return key
    elif key.upper() == 'Q':
        return key
    elif key.upper() == 'C':
        # copy password to clipboard
        import pyperclip
        import UI_Dashboard
        pyperclip.copy(str(account.password))
        print("Password copied to clipboard!")
        UI_Dashboard.displayMenu(accounts)
        return key
    else:
        print("Invalid key!")
        return readKey()