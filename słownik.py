def slownik(zdanie):

   num = 1
   index = 0
   library = {}
   library2 = {}
   lista =  zdanie.split(";;")
   for i in lista:
       if i == num:
           
           list1 = i.split(":")
           library["id"] = list1[0]
           library["imie"] = list1[1]
           library["nazwisko"] = list1[2]

           print library
           
           num + 2
       else:
           
           list1 = i.split(":")
           library2["id"] = list1[0]
           library2["imie"] = list1[1]
           library2["nazwisko"] = list1[2]

           print library2


    
slownik('1:Jan:Kowalski:Szczęśliwa:12/5;;2:Adam:Szczęsny:Zachlapana:10;;')      
