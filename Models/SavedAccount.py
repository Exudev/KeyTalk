# Create a class account, with id, website name, username, password, dateCreated, dateModified and lastChecked

class Account:
    def __init__(self, id, websiteName, username, password, dateCreated, dateModified, lastChecked):
        self.id = id
        self.websiteName = websiteName
        self.username = username
        self.password = password
        self.dateCreated = dateCreated
        self.dateModified = dateModified
        self.lastChecked = lastChecked

    def __str__(self):
        return f"ID: {self.id}, Website Name: {self.websiteName}, Username: {self.username}, Password: {self.password}, Date Created: {self.dateCreated}, Date Modified: {self.dateModified}, Last Checked: {self.lastChecked}"
    # create a function that returns an account with all its attributes but the id encrypted, by moving their ascii value by 5, 2 and 3 respectively
    def encryptAccount(self):
        encryptedWebsiteName = ""
        encryptedUsername = ""
        encryptedPassword = ""
        for letter in self.websiteName:
            encryptedWebsiteName += chr(ord(letter) + 5)
        for letter in self.username:
            encryptedUsername += chr(ord(letter) + 2)
        for letter in self.password:
            encryptedPassword += chr(ord(letter) + 3)
        return Account(self.id, encryptedWebsiteName, encryptedUsername, encryptedPassword, self.dateCreated, self.dateModified, self.lastChecked) 
    # create a function that returns an account with all its attributes but the id decrypted, by moving their ascii value by -5, -2 and -3 respectively
    def decryptAccount(self):
        decryptedWebsiteName = ""
        decryptedUsername = ""
        decryptedPassword = ""
        for letter in self.websiteName:
            decryptedWebsiteName += chr(ord(letter) - 5)
        for letter in self.username:
            decryptedUsername += chr(ord(letter) - 2)
        for letter in self.password:
            decryptedPassword += chr(ord(letter) - 3)
        return Account(self.id, decryptedWebsiteName, decryptedUsername, decryptedPassword, self.dateCreated, self.dateModified, self.lastChecked)