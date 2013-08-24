#-*- coding:UTF-8 -*-
import random
def rzut_kostka():
    return random.randint(1,6)
#print rzut_kostka()   

imie = raw_input("Gracz1: Podaj imie: ")
imie2 = raw_input("Gracz2: Podaj imie: ")



print "Kolej gracza", imie
a = raw_input("Czy chcesz rzucić kostką?: ")
if a == "tak":
    x = rzut_kostka()
    print "Wylosowałeś",  x
else:
    print "Nie to nie..."
    x = 0
    print "Masz", x
        


print "Kolej gracza", imie2
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
        print "Wygral", imie, "!"
    elif x == z:
        print " Remis!"    
    else:
        print "Wygral", imie2, "!"      
         
kto_wygral()   
