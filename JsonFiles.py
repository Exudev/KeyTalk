import SavedAccount
import json

filename = "accounts.json"
encryptedFilename = "encryptedKey.txt"
nameFilename = "name.txt"
# take a list of accounts, turn them into a json string, and write them to a file
def writeAccountsToFile(accounts, filename):
    # turn list of accounts into a list of dictionaries
    accountDicts = []
    for account in accounts:
        accountDicts.append(account.__dict__)
    # turn list of dictionaries into a json string
    jsonString = json.dumps(accountDicts)
    # write json string to file
    file = open(filename, "w")
    file.write(jsonString)
    file.close()

# open file, read json string, turn json string into a list of dictionaries, turn list of dictionaries into a list of accounts, and return the list of accounts
def readAccountsFromFile(filename):
    # open file, read json string
    file = open(filename, "r")
    jsonString = file.read()
    file.close()
    # turn json string into a list of dictionaries
    accountDicts = json.loads(jsonString)
    # turn list of dictionaries into a list of accounts
    accounts = []
    for accountDict in accountDicts:
        account = SavedAccount.Account(accountDict["id"], accountDict["websiteName"], accountDict["username"], accountDict["password"], accountDict["dateCreated"], accountDict["dateModified"], accountDict["lastChecked"])
        accounts.append(account)
    return accounts

def writeEncryptedPasswordToFile(encryptedPassword):
    file = open(encryptedFilename, "w", encoding="utf-8")
    file.write(encryptedPassword)
    file.close()

def readEncryptedPasswordFromFile():
    file = open(encryptedFilename, "r", encoding="utf-8")
    encryptedPassword = file.read()
    file.close()
    return encryptedPassword

def writeNameToFile(name):
    file = open(nameFilename, "w")
    file.write(name)
    file.close()

def readNameFromFile():
    file = open(nameFilename, "r")
    name = file.read()
    file.close()
    return name

#check if nameFilename exists, return true or false
def nameFileExists():
    try:
        file = open(nameFilename, "r")
        file.close()
        return True
    except:
        return False

#check if filename exists, if it does, execute readAccountsFromFile()
def accountsFileExists():
    try:
        file = open(filename, "r")
        file.close()
        return True
    except:
        return False