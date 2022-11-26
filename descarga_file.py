import os
import zipfile

def descarga_f(orig, destino):
#Descomprime archivo, cuya ruta y nombre se indica en el parametro orig y lo deja en la ruta /tmp/destino/
    #unzip orig -d /tmp/destino/
    zip = zipfile.ZipFile(orig,'r') 
    zip.extractall(destino)
    return 0  
