#-*- coding:UTF-8 -*-
import random
def rzut_kostka():
    return random.randint(1,6)
#print rzut_kostka()   



print "Kolej gracza player1"
a = raw_input("Czy chcesz rzucić kostką?: ")
if a == "tak":
    x = rzut_kostka()
    print "Wylosowałeś",  x
else:
    print "Nie to nie..."
    x = 0
    print "Masz", x
        


print "Kolej gracza player2"
a = raw_input("Czy chcesz rzucić kostką?: ")
if a == "tak":
    z = rzut_kostka()
    print "Wylosowałeś",  z
else:
    print "Nie to nie..."
    z = 0
    print "Masz", z

def kto_wygral():
    if x > z:
        print "Wygral player1!"
    elif x == z:
        print " Remis!"    
    else:
        print "Wygral player2!"      
         
kto_wygral()   
