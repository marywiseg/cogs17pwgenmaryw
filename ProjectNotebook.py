#!/usr/bin/env python
# coding: utf-8

# # Project Description

# In this project I have created a simple password generator that will generate each UCSD student a custom and strong password based off of their name, favorite number, and the college we attend. After the password is generated, the user has the choice of encrypting their password and saving a pin to correlate with it, so they can hide their password safely. I did this because it allows students to use a safe password that they can remember by use of a memorable pin, making their passwords more secure. 

# ## Project Code
# 
# If it makes sense for your project, you can have code and outputs here in the notebook as well.

# In[ ]:


from my_module.functions import *


# In[ ]:


print ("You can input your password and a pin into the functions below to encode and decode it!")

password_encoder()
password_decoder()


# In[ ]:


#Example!

password_encoder('examplepin', 'js13UCSDhdjska2#')


# In[ ]:


#test functions
test_randomgen()
test_encoder()


# #### Extra Credit (*optional*)
# 
# Replace all of this text with a brief explanation (~3 sentences) of: 
# 1. I have no python background at all, and have always wanted to explore coding languages and learning them. 
# 2. I challenged myself to learn something new with this project because I had little knowledge of putting a random character generator and user-generated input together through functions, and I worked through many miniscule errors that I did not expect. I at first thought my project was too simple, though after experiencing the time it took to complete the project and fix all the small errors, I had to continue of think of ways to adapt my project. I had not learned to adapt my work in such a way and enjoy the process of going back and making code more efficient.
# 

# In[ ]:




