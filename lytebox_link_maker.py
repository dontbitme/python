import os

def lytebox_link_maker(folder_location):

    for i in os.listdir(folder_location):
        print  '<a href="images"'+ i +'" class="lytebox" data-lyte-options="group:vacation" data-title="Some Title">Nazwa</a>'
    
lytebox_link_maker("c:\\users\\Konrad\\desktop\\foty\\")
