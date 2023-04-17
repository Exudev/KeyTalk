import Config.JsonFiles as JsonFiles
import UI.KeyManagement as KeyManagement
import UI.AccountManagement as AccountManagement
import Models.AccountList as AccountList
import time

accountList = AccountList.AccountList("", [])
# check if accounts exists using accountsFileExists() from JsonFiles.py, if it does load it into a list of accounts using readAccountsFromFile() from JsonFiles.py
#def loadAccounts():
if JsonFiles.accountsFileExists() == True:
    accountList = JsonFiles.readAccountsFromFile()
    KeyManagement.CheckKey(accountList.key)
# else:
#     return []
KeyManagement.checkIfFilesExist()
KeyManagement.createName()
AccountManagement.newAccount(accountList)
#create an ascii menu with the title of "Dashboard", and options which can be executed by pressing a key: N = new account, M = modify account, Q = quit
def displayMenu(accountList):
    # pause the program for a second, and then clear the console
    time.sleep(2)
    print("\033c")
    print("Dashboard")
    # show up to 15 accounts in accounts, if any, and give an option if there is more to the maximum
    if len(accountList.accounts) > 0:
        print("Accounts:")
        for i in range(0, len(accountList.accounts)):
            if i < 15:
                print("(" + str(accountList.accounts[i].id) + ")\t" + accountList.accounts[i].websiteName)
                print("\t\t" + accountList.accounts[i].username + "\tLastChecked: " + accountList.accounts[i].lastChecked.strftime("%m/%d/%Y"))
            else:
                print("...")
                break
    print("N = New Account")
    print("M = Modify Account")
    print("E = Export encripted data ")
    print("D = Delete all files")
    print("Q = Quit")
    # get user input
    userInput = input("Please enter a command: ")
    # if the user input is N, execute newAccount()
    if userInput.upper() == "N":
        AccountManagement.createAccount(accountList)
    # if the user input is M, execute modifyAccount()
    elif userInput.upper() == "M":
        # make a try catch block to check if the imput is a number, if it's not, display an error message and execute displayMenu()
        try:
            # promt the user to enter the id of the account they want to modify, save the inputs as "i" and substract 1 from it
            i = int(input("Please enter the ID of the account you want to modify: ")) - 1
            # execute printAccount() from AccountView.py
            import UI.AccountView as AccountView
            AccountView.printAccount(accountList.accounts[i], accountList)
        except ValueError:
            print("Error: Invalid input.")
            displayMenu(accountList)
        except IndexError:
            print("Error: Invalid input.")
            displayMenu(accountList)
            displayMenu(accountList)
    elif userInput.upper() == 'E':
        # excecute exportAccount
        import UI.AccountManagement as AM
        AM.exportAccount(accountList)
    # if the user input is Q, execute quit()
    elif userInput.upper() == "Q":
        quit()
    # if the user input is D, execute deleteAllFiles() from JsonFiles.py and ask if the user is sure
    elif userInput.upper() == "D":
        print("Are you sure you want to delete all files?")
        print("Y = Yes")
        print("N = No")
        userInput = input("Please enter a command: ")
        if userInput.upper() == "Y":
            
            JsonFiles.deleteAllFiles()
            print("All files have been deleted, the program will close now.")
            time.sleep(5)
            quit()    
        elif userInput.upper() == "N":
            displayMenu(accountList)
        else:
            print("Error: Invalid input.")
            displayMenu(accountList)
   
    # if the user input is not N, M, or Q, display an error message and execute displayMenu()
    else:
        print("Error: Invalid input.")
        displayMenu(accountList)

displayMenu(accountList)