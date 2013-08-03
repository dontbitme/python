def slownik(zdanie):


    zdanie.split(':')
    library= {1:{'imie', 'nazwisko', 'ulica', 'mieszkanie'}}
    for i in zdanie:
        if i != ';;':
            library[1]['imie']=i        # TO JEST ZLE ALE POWINNO COS WYSWIETLIC 
            
            
            


    print library

    
slownik('Jan:Kowalski:Szczęśliwa:12/5;;2:Adam:Szczęsny:Zachlapana:10;;')  
