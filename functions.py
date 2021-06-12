"""A collection of function for doing my project."""
import random
import string
import base64

print("Hello! This program will provide you with an initial password for your UCSD student accounts that you can encrypt and decrypt using a passcode.")

def random_chars(characters, length):
    """Function to generate random characters for password."""
    
    #Found hasattr method from https://www.tutorialsteacher.com/python/hasattr-method
    #used to debug https://stackoverflow.com/questions/3854692/generate-password-in-python
    
    #set "rng" as an attribute in order to avoid reinitializing random.
    if not hasattr(random_chars, "rng"):
        
        random_chars.rng = random.SystemRandom()
        
    return ''.join([ random_chars.rng.choice(pw_character_set) for _ in range(length) ])

#defining the character set used to generate a string.
pw_character_set = string.ascii_letters + string.digits + string.punctuation

random_chars(pw_character_set, 8)

#defining variables which store user input and a string value for the final password.
firstname = input('\nEnter the first letter of your first name.:')
lastname = input('\nEnter the first letter of your last name.:')
favnum = input('\nEnter your favorite number!:')
ucsd = 'UCSD'

#combining the input from the user.
combined_input = firstname + lastname + favnum + ucsd

#generating random string for password. 
password_chars = random_chars(pw_character_set, 8)

#combining the random string and the user input into a combined password.
combined_password = combined_input + password_chars

print(combined_password)
pass


def password_encoder(passcode, combined_password):
    """Function used in order to encypt password."""
    
    #empty string to hold encoded values
    encoded_pw = []
       
    #the for loop takes the items in the combined password and reassigns the values from the length of the password to other ones.
    for item in range(len(combined_password)):
        
        #https://stackabuse.com/encoding-and-decoding-base64-strings-in-python
        passcode_new = passcode[item % len(passcode)]
        encoded_items = chr(ord(combined_password[item]) + ord(passcode_new) % 256)
        encoded_pw.append(encoded_items)
    
    #converts the list into a string
    encoded_string = ''.join(encoded_pw)
   
    return encoded_string
    
    print(encoded_string)
pass


def password_decoder(passcode, combined_password): 
    """Function to decode the encoded password"""
    
    decoded_pw = []
   
     #takes item from password and takes each value and finds its original value from the encryption. 
    for item in range(len(combined_password)):
        passcode_new = passcode[item % len(passcode)]
        decoded_items = chr(ord(combined_password[item]) - ord(passcode_new) % 256)
        
        #takes the decoded values and placed them in a list
        decoded_pw.append(decoded_items)
   
    #converts the list of decoded values into a string.
    decoded_string = ''.join(decoded_pw)
    print(decoded_string)
pass