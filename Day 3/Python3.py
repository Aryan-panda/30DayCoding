# Warm-up

"""

Name = ["Aryan", "Suresh", "Pikachu", "Ben"]
Name.append("McKenzie")
Name.remove("Suresh")
Name[2] = "Raichu"  
Name.insert(0,"Elon")
print("")
print ( Name.index("Aryan"),"\n" )
print(Name)
print ("")

"""

#-------------------------------------------------------------------------------------------------

# Stone, Papper and Scissor game

"""
def point() :
    print ( "  " )
    print ( " Now your point is ", points )

print ( " Let's play Stone, Paper , Scissor game " )

print ( "  " )

import random

print ( " Some instruction are followed : ")
print ( " Press 1 for Scissor " )
print ( " Press 2 for Paper " )
print ( " Press 3 for Stone " )

print ('')

i = 0
10
points = 0

j = int ( input ( " how many rounds you wanna play ? (max round could be 20) " ) )


while j > 20 or j < 0 :
    print ( " Invalid input !!! " )
    print (  "  " )
    j = ( int ( input ( " Enter valid input : " ) ) )


while i < j :

    print ( "  " )

    i = i + 1
    
    x1 = ( int ( input ( " What is you choice ? " )))

    while x1 > 3 or x1 < 1:
        print ( " Invaillid input !!! " )
        print ('')
        x1 = ( int ( input ( " Enter a valid choice ? " )))


    x2 = random.randrange(1, 4)

#    x2 = random.randint(1, 3)

    print ('')

    if x2 == 1:
        print ( " Computr choosed Scissor " )
    elif x2 == 2:
        print ( " Computer choosed Paper " )
    elif x2 == 3:
        print ( " Computer choosed Stone " )

    if x1 == 1 :
        print ( " You choosed Scissor " )
    elif x1 == 2 :
        print ( " You choosed Paper " )
    elif x1 == 3 :
        print ( " You choosed Stone " )
        
    print ('')

    if x1 == x2:
        print ( " Draw " )
        point()
    elif x1 == 1 and x2 == 2 :
        print ( " You WON !!! " )
        points += 1
        point()
    elif x1 == 1 and x2 == 3 :
        print ( " Upps, Computer won " )
        points -= 1
        point()
    elif x1 == 2 and x2 == 1 :
        print ( " Upps, Computer won " )
        points -= 1
        point()
    elif x1 == 2 and x2 == 3 :
        print ( " You WON !!! " )
        points += 1
        point()
    elif x1 == 3 and x2 == 1 :
        print ( " You WON !!! " )
        points += 1
        point()
    elif x1 == 3 and x2 == 2 :
        print ( " Upps, Computer won " )
        points -= 1
        point()
    else :
        print (" 404 error !!!")
        print ( " Please try again ")
        i = eval ( " i - 1 " )

    print ( " " )
    print ( "-------------------------------------------------------------------------------------------------------------------------------------" )
    print ( " " )

print ( " Your Total score is ", points )
print ( "  " )
print ( "-------------------------------------------------------------------------------------------------------------------------------------" )

"""