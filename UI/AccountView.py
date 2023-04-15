import Models.SavedAccount as SavedAccount

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

# read key as input, 'b' to go back to Main.py, 'm' to modify the account, 'd' to delete the account, 'q' to quit
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
        # excecute displaymenu() from Main.py
        import Main
        Main.displayMenu(accounts)
        return key
    elif key.upper() == 'M':
        # excecute modifyAccount() from AccountManagement.py
        import UI.AccountManagement as AccountManagement
        AccountManagement.modifyAccount(account, accounts)
        return key
    elif key.upper() == 'D':
        # excecute deleteAccount() from AccountManagement.py
        import UI.AccountManagement as AccountManagement
        AccountManagement.deleteAccount(account, accounts)
        
        return key
    elif key.upper() == 'Q':
        return key
    elif key.upper() == 'C':
        # copy password to clipboard
        import pyperclip
        #make a try cath where you copy the password to the clipboard, catch any exception and print it to the user
        try:
            pyperclip.copy(str(account.password))
            print("Password copied to clipboard!")
            import Main
            Main.displayMenu(accounts)
        except Exception as e:
            print(e)
    else:
        print("Invalid key!")
        return readKey()