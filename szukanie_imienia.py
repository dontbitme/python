data = '1:Jan:Kowalski:Szczęśliwa:12/5;;2:Adam:Szczęsny:Zachlapana:10'

def process_data(zdanie):
    lista = []
    lista_ziomkow =  zdanie.split(";;")
    for ziomek in lista_ziomkow:
        dane = ziomek.split(":")
        library = {}
        library["id"] = dane[0]
        library["imie"] = dane[1]
        library["nazwisko"] = dane[2]
        library["ulica"] = dane[3]
        library["numer"] = dane[4]
        lista.append(library)
    return lista

def get_names():
    lista = []
    for gosc in process_data(data):
        imie = gosc["imie"]
        lista.append(imie)
    return lista
 
    
    
    
#get_names()  


def find_person(imie):
    for gosc in process_data(data):        
        imie2 = gosc["imie"]
        if imie == imie2:
            return gosc
        else:
            print " "
    
find_person("Jan")
