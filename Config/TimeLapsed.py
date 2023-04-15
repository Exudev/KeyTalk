import time
import UI.KeyManagement as KeyManagement

# Make this timer a singleton
class TimeLapsed:
    __instance = None
    @staticmethod
    def getInstance():
        if TimeLapsed.__instance == None:
            TimeLapsed()
        return TimeLapsed.__instance

    def __init__(self):
        if TimeLapsed.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            TimeLapsed.__instance = self

active = True

# start a timer, if it goes over 5 minutes, change active to false
def startTimer():
    global active
    active = True
    time.sleep(300)
    active = False

# Check if the user is active, if they are, start the timer again
def checkIfActive():
    global active
    if active == True:
        startTimer()
    else:
        #ask the user to reintroduce their password and check it with the password in the file using comparePassword() from KeyManagement.py
        checkPasswordForTimer()

# Create a variable "i" and set it to 1. Ask the user to  introduce their password and check it with the password in the file using comparePassword() from KeyManagement.py, if it fails add 1 to i, if i = 5 exit the application
def checkPasswordForTimer():
    i = 1
    while i < 5:
        # when i is 3 or more, print "Warning: You have X attempts left", where X is 5 - i
        if i >= 3:
            print(f"Warning: You have {5 - i} attempts left.")
        password = input("Please enter your password: ")
        if KeyManagement.comparePassword(password):
            startTimer()
            break
        else:
            print("Error: Password does not match.")
            #sleep for 2 seconds
            time.sleep(2)
            i += 1
    exit()