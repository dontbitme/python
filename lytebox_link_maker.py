import os

def lytebox_link_maker(folder_location):
    for i in os.listdir(folder_location):
        (shortname, extension) = os.path.splitext(i)
        cos = [".jpg",".gif", ".png"]
        plik = open("tekst.log", "w")        
        if extension in cos:
            plik2 = open("tekst.log")
            plik2.write( '<a href="images"'+ i +'" class="lytebox" data-lyte-options="group:vacation" data-title="Some Title">Nazwa</a>\n')
            plik2.close()
        else:
            print "Plik "+i+" nie jest obrazem."
            
        print plik2.read()
lytebox_link_maker("c:\\users\\Konrad\\desktop\\foty\\")

