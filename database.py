from pymongo import MongoClient


client = MongoClient('mongodb+srv://nietogmartin:1234@softmanantialdelsaber.enyfr.mongodb.net/')
db = client['task']

# Colecciones
task_list_collection = db['task_list']