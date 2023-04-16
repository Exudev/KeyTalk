import Models.SavedAccount as SavedAccount
import Models.AccountList as AccountList
import json
import datetime
import pickle

# [DateTime management on Json files taken from StackOverflow]
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
    
filename = "./Files/accounts.json"
encryptedFilename = "./Files/encryptedKey.txt"
nameFilename = "./Files/name.txt"

# create a function that recieves an accountList, turns it into a dictionary and writes it into a json file located on filename
def writeAccountsToFile(accountList):
    # file = open(filename, "w")
    # file.write(dumps(accountList.__dict__))
    # file.close()
    with open(filename, "wb") as file:
        pickle.dump(accountList, file)

# create a function that reads the json file located on filename, turns it into an accountList and returns it
def readAccountsFromFile():
    # file = open(filename, "r")
    # accounts = loads(file.read())
    # file.close()
    with open(filename, "rb") as file:
        accounts = pickle.load(file)
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

def deleteAccountFile():
    import os
    os.remove(filename)