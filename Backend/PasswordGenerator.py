#Password generator
import random 
import string 

def password_generator():
    password = []
    for i in range(10):
        password.append(random.choice(string.ascii_letters))
    return ''.join(password)

print("Password:")
print(password_generator())
