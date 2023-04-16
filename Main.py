import Config.JsonFiles as JsonFiles
import UI.KeyManagement as KeyManagement
import UI.AccountManagement as AccountManagement
import time

accounts = []
# check if accounts exists using accountsFileExists() from JsonFiles.py, if it does load it into a list of accounts using readAccountsFromFile() from JsonFiles.py
#def loadAccounts():
if JsonFiles.accountsFileExists() == True:
    accounts = JsonFiles.readAccountsFromFile()
# else:
#     return []
KeyManagement.checkIfFilesExist()
KeyManagement.createName()
AccountManagement.newAccount(accounts)
#create an ascii menu with the title of "Dashboard", and options which can be executed by pressing a key: N = new account, M = modify account, Q = quit
def displayMenu(accounts):
    # pause the program for a second, and then clear the console
    time.sleep(2)
    print("\033c")
    print("Dashboard")
    # show up to 15 accounts in accounts, if any, and give an option if there is more to the maximum
    if len(accounts) > 0:
        print("Accounts:")
        for i in range(0, len(accounts)):
            if i < 15:
                print("(" + str(accounts[i].id) + ")\t" + accounts[i].websiteName)
                print("\t\t" + accounts[i].username + "\tLastChecked: " + accounts[i].lastChecked.strftime("%m/%d/%Y"))
            else:
                print("...")
                break
    print("N = New Account")
    print("M = Modify Account")
    print("Q = Quit")
    # get user input
    userInput = input("Please enter a command: ")
    # if the user input is N, execute newAccount()
    if userInput.upper() == "N":
        AccountManagement.createAccount(accounts)
    # if the user input is M, execute modifyAccount()
    elif userInput.upper() == "M":
        # make a try catch block to check if the imput is a number, if it's not, display an error message and execute displayMenu()
        try:
            # promt the user to enter the id of the account they want to modify, save the inputs as "i" and substract 1 from it
            i = int(input("Please enter the ID of the account you want to modify: ")) - 1
            # execute printAccount() from AccountView.py
            import UI.AccountView as AccountView
            AccountView.printAccount(accounts[i], accounts)
        except ValueError:
            print("Error: Invalid input.")
            displayMenu(accounts)
        except IndexError:
            print("Error: Invalid input.")
            displayMenu(accounts)
    # if the user input is Q, execute quit()
    elif userInput.upper() == "Q":
        quit()
    # if the user input is not N, M, or Q, display an error message and execute displayMenu()
    else:
        print("Error: Invalid input.")
        displayMenu(accounts)

displayMenu(accounts)