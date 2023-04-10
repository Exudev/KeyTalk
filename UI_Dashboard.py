import JsonFiles
import UI_InitialSetUp

# check if accounts exists using accountsFileExists() from JsonFiles.py, if it does load it into a list of accounts using readAccountsFromFile() from JsonFiles.py
#def loadAccounts():
if JsonFiles.accountsFileExists() == True:
    accounts = JsonFiles.readAccountsFromFile()
# else:
#     return []
UI_InitialSetUp.createName()

#create an ascii menu with the title of "Dashboard", and options which can be executed by pressing a key: N = new account, M = modify account, Q = quit
def displayMenu():
    print("Dashboard")
    print("N = New Account")
    print("M = Modify Account")
    print("Q = Quit")
    # get user input
    userInput = input("Please enter a command: ")
    # if the user input is N, execute newAccount()
    if userInput == "N":
        newAccount()
    # if the user input is M, execute modifyAccount()
    elif userInput == "M":
        modifyAccount()
    # if the user input is Q, execute quit()
    elif userInput == "Q":
        quit()
    # if the user input is not N, M, or Q, display an error message and execute displayMenu()
    else:
        print("Error: Invalid input.")
        displayMenu()