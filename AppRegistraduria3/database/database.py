from pymongo import MongoClient
import json
import certifi

ca = certifi.where()

def loadConfigFile():
    with open('database/config.json') as f:
        data = json.load(f)
    return data

def dbConnection():
    dataConfig = loadConfigFile()
    try:
        #conectar con Mongo atlas
        client = MongoClient(dataConfig['MONGO_URI_SERVER'], tlsCAFile=ca)
        db = client["Proyecto_Final_Ciclo4a_Grupo28-9"]
    except:
        print("Error de conexión en la DB")
    return db