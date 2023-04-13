import time
import UI_InitialSetUp

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
        #ask the user to reintroduce their password and check it with the password in the file using comparePassword() from UI_InitialSetup.py
        password = input("Please enter your password: ")
        if UI_InitialSetUp.comparePassword(password):
            startTimer()
        else:
            print("Error: Password does not match.")
            #sleep for 2 seconds
            time.sleep(2)
            exit()