import SavedAccount

# taking an account as input and printing the details of the account
def printAccount(account):
    print("ID: " + str(account.id))
    print("Website Name: " + account.websiteName)
    print("Username: " + account.username)
    print("Password: " + account.password)
    print("Date Created: " + account.dateCreated)
    print("Date Modified: " + account.dateModified)
    print("Last Checked: " + account.lastChecked)

# [MODIFIED] read key as input, 'b' to go back to UI_Dashboard.py, 'm' to modify the account, 'd' to delete the account, 'q' to quit
def readKey():
    key = input("Enter key: ")
    if key == 'b':
        # excecute UI_Dashboard.py
        return key
    elif key == 'm':
        return key
    elif key == 'd':
        return key
    elif key == 'q':
        return key
    else:
        print("Invalid key!")
        return readKey()

# read key as input, 'b' to go back to UI_Dashboard.py, 'm' to modify the account, 'd' to delete the account, 'q' to quit   
# def readKey():
#     key = input("Enter key: ")
#     if key == 'b':
#         return key
#     elif key == 'm':
#         return key
#     elif key == 'd':
#         return key
#     elif key == 'q':
#         return key
#     else:
#         print("Invalid key!")
#         return readKey()