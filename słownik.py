def slownik(zdanie):

 #  num = 1
  # index = 0
   library = {}
   lista =  zdanie.split(";;")
   for i in lista:
       list1 = i.split(":")
       e = ' '.join(list1)
       library["cos"] = e
       
       print library
   
   


    
slownik('1:Jan:Kowalski:Szczęśliwa:12/5;;2:Adam:Szczęsny:Zachlapana:10;;')    
