import SavedAccount
import json
import datetime

class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)
        
def datetime_decoder(d):
    if isinstance(d, list):
        pairs = enumerate(d)
    elif isinstance(d, dict):
        pairs = d.items()
    result = []
    for k,v in pairs:
        if isinstance(v, str):
            try:
                # The %f format code is only supported in Python >= 2.6.
                # For Python <= 2.5 strip off microseconds
                # v = datetime.datetime.strptime(v.rsplit('.', 1)[0],
                #     '%Y-%m-%dT%H:%M:%S')
                v = datetime.datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
            except ValueError:
                try:
                    v = datetime.datetime.strptime(v, '%Y-%m-%d').date()
                except ValueError:
                    pass
        elif isinstance(v, (dict, list)):
            v = datetime_decoder(v)
        result.append((k, v))
    if isinstance(d, list):
        return [x[1] for x in result]
    elif isinstance(d, dict):
        return dict(result)
    
def dumps(obj):
    return json.dumps(obj, cls=JSONDateTimeEncoder, indent=4)

def loads(obj):
    return json.loads(obj, object_hook=datetime_decoder)
    
filename = "accounts.json"
encryptedFilename = "encryptedKey.txt"
nameFilename = "name.txt"
# take a list of accounts, turn them into a json string, and write them to a file
def writeAccountsToFile(accounts):
    # turn list of accounts into a list of dictionaries
    accountDicts = []
    for account in accounts:
        accountDicts.append(account.__dict__)
    # turn list of dictionaries into a json string
    jsonString = dumps(accountDicts)
    # write json string to file
    file = open(filename, "w")
    file.write(jsonString)
    file.close()

# open file, read json string, turn json string into a list of dictionaries, turn list of dictionaries into a list of accounts, and return the list of accounts
def readAccountsFromFile():
    # open file, read json string
    file = open(filename, "r")
    jsonString = file.read()
    file.close()
    # turn json string into a list of dictionaries
    accountDicts = loads(jsonString)
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