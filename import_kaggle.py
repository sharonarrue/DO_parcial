import json
import zipfile
import os

api_token = {"username":"sharonarrusnchez","key":"659835f27335ade7df3ffd6e6555e8f1"} ##contenido de archivo kaggle

##conectar a kaggle
with open("C:/Users/Sharon/.kaggle/kaggle.json","w") as file:
    json.dump(api_token,file)
location = "C:/Users/Sharon/Desktop/proyecto_parcial/dataset"
##Validar que la carpeta exista para que no arroje error
if not os.path.exists(location):
    ##si no existe la creo
    os.mkdir(location)
else:
    ##si la carpeta si existe, entonces voy a borrar su contenido(si lo corro va a tener varias datas,voy borrando y cargando)
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove(os.path.join(root,name)) ##elimino todos los archivos
        for name in dirs:
            os.rmdir(os.path.join(root,name)) #Elimino todas las carpetas
##Descargar dataset de kaggle
os.system("kaggle datasets download -d henryshan/starbucks -p C:/Users/Sharon/Desktop/proyecto_parcial/dataset")

##Descomprimir el archivo Kaggle
os.chdir(location)
for file in os.listdir():
    zip_ref = zipfile.ZipFile(file,"r") #Lee archivo.zip
    zip_ref.extractall() ##extrae contenido de archivo.zip
    zip_ref.close() ##cierra archivo
    

