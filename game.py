#-*- coding:UTF-8 -*-
import random
def rzut_kostka():
    return random.randint(1,6)
#print rzut_kostka()   

imie = raw_input("Gracz1: Podaj imie: ")
imie2 = raw_input("Gracz2: Podaj imie: ")

ilosc_rzutow = 3

for i in range(ilosc_rzutow):
    x = rzut_kostka()
    print "Gracz", imie, "wylosował",  x
    
for i in range(ilosc_rzutow):
    z = rzut_kostka()
    print "Gracz", imie2, "wylosował",  z





def kto_wygral():
    if x > z:
        print "Wygral", imie, "!"
    elif x == z:
        print " Remis!"    
    else:
        print "Wygral", imie2, "!"      
         
kto_wygral()   
