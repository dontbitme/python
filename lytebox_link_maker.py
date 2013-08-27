import os

def lytebox_link_maker(folder_location):
    cos = ".jpg", ".gif"
    for i in os.listdir(folder_location):
        (shortname, extension) = os.path.splitext(i)
        if extension == cos:
            print  '<a href="images"'+ i +'" class="lytebox" data-lyte-options="group:vacation" data-title="Some Title">Nazwa</a>'
        
lytebox_link_maker("c:\\users\\Konrad\\desktop\\foty\\")
