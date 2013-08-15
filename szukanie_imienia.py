def find_person(imie):
    for gosc in process_data(data):        
        imie2 = gosc["imie"]
        if imie == imie2:
            return gosc
        else:
            print " "
    
find_person("Jan")
