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