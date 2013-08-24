#-*- coding:UTF-8 -*-
import random
def rzut_kostka():
    return random.randint(1,6)
#print rzut_kostka()   

imie = raw_input("Gracz1: Podaj imie: ")
imie2 = raw_input("Gracz2: Podaj imie: ")

ilosc_rzutow = 3

koles1 = 0
koles2 = 0  
for i in range(ilosc_rzutow):
    x = rzut_kostka()
    print "Gracz", imie, "wylosował",  x
    koles1 = koles1+x
 
    
for i in range(ilosc_rzutow):
    z = rzut_kostka()
    print "Gracz", imie2, "wylosował",  z
    koles2 = koles2+z





def kto_wygral():
    if koles1 > koles2:
        print "Wygral", imie, "!"
    elif koles1 == koles2:
        print " Remis!"    
    else:
        print "Wygral", imie2, "!"      
         
kto_wygral()   
