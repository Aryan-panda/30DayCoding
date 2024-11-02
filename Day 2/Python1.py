#                                                  DAY 2 - Python

"""

#Warm-up code

from math import pi 
r = int ( input ("Enter radius : "))
circumference = print ("Its circumference = ", 2*pi*r)

"""
#------------------------------------------------------------------------------------------------------------------
"""

# Pyramid code

Height = int ( input ( "Enter height for pyramid : " ) )
j = 1
for i in range (Height, 0, -1) : 
    print (" "*(i-1), "*"*j )
    j +=2 

"""
#------------------------------------------------------------------------------------------------------------------
"""

# Check username is proper or not 

def UserNameCHeck(Input) : 
    if len(Input) > 14 :
        print ("Invalid username.")
        return
    if Input[0].isdigit() : 
        print ("Invalid username.")
        return
    for char in Input : 
        if char == " " or not ( char.isalnum() or char == "_" ) : 
            print ("Invalid username ") 
            return
    print ("Welcome", Input)
    

UserName = input ( "Enter your username : " )
UserNameCHeck(UserName)

"""
#------------------------------------------------------------------------------------------------------------------
"""

# Fomrat specifiers 

a = +1000
b = 1000
c = 2.026
d = 2
e = 1000000000000000000000000000
print (f"{a:}") # Replace + sign with space
print (f"{b:+}") # Puts sign 
print (f"{c:.2f}") # Round off upto 2 decimal place
print (f"{d:03}") # Put 0 ahead
print (f"{e:,}") # Puts comma according to international system (place value) 
# and there are value:<, value:> and value:^ for left, right and centre alignment. 

"""
#------------------------------------------------------------------------------------------------------------------
"""

# Timer with time import 

import time 

GSec = int ( input ( "Enter time (in second): " ) )
for i in range (GSec,0,-1) : 
    Hours = i//3600
    Minutes = (i%3600)//60
    Seconds = (i%3600)%60
    print (f"{Hours:02}:{Minutes:02}:{Seconds:02}")
    time.sleep(1)
print ("OVER!!!")

"""
#------------------------------------------------------------------------------------------------------------------