from distutils.log import error
import pymongo
from dotenv import load_dotenv
import os

def create_connection(datos):
    try:
        load_dotenv()
        database = os.getenv("DATABASE")
        user = os.getenv("ADMIN")
        pwd = os.getenv("PASSWORD")
        client = pymongo.MongoClient(f"mongodb+srv://{user}:{pwd}@cluster0.cql9dta.mongodb.net/?retryWrites=true&w=majority")
        return client
    except error as e:
        print(e)