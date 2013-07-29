a = [1,2,3,4]
def fun(l):

    i = len(l)-1
    lista = []
    while i >= 0:
        lista.append(l[i])
        i = i-1
    return ' '.join(lista)


        

def cos(zdanie):
    lista1=[]
    


    
    for i in zdanie.split(" "):
        odwrocony = fun(i)
        lista1.append(odwrocony)
        
    print ' '.join(lista1)
        

    


cos("ala ma kota")
