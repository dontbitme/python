import os

def lytebox_link_maker(folder_location):
    for i in os.listdir(folder_location):
        (shortname, extension) = os.path.splitext(i)
        cos = [".jpg",".gif", ".png"]
        if extension in cos:
            print  '<a href="images"'+ i +'" class="lytebox" data-lyte-options="group:vacation" data-title="Some Title">Nazwa</a>'
        else:
            print "Plik "+i+"nie jest obrazem."
lytebox_link_maker("c:\\users\\Konrad\\desktop\\foty\\")

