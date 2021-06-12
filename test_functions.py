"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import my_func, my_other_func
##
##

#test functions
def test_randomgen():
    """Tests for the character generator."""
    
    #testing if the password is a string type 
    assert type(password_chars) == str
    
    #testing if the length of the password is within the parameters.
    assert len(combined_password) < 18
    
    #testing if the password contains the value "UCSD"
    assert "UCSD" in combined_password == True


def test_encoder():
    """Tests for the encoder"""
    
    #checking that the encoded password is a string. 
    assert type(encoded_string) == str
pass
    



                 
    