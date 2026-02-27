import string
import random

# Initalize length that we want the password would be
def pass_gen(length : int = 10):
    password = ''
    # This line create a string of letter(upper + lower) and number and punctuation 
    alphabelt = string.ascii_letters + string.digits + string.punctuation
    for i in range (length):
        password = password + (random.choice(alphabelt))
    
    return password

print(pass_gen(13))