# connecting or pushing data into MongoDB

import os, sys, json,certifi, pymongo
from dotenv import  load_dotenv
import pandas as pd
import  numpy as np
from qdrant_client.http.api.service_api import to_json

from SecurityFolder.exception.exception import NetworkException
from SecurityFolder.logger.logger import *
import pandas as pd


load_dotenv()
mongo_url = os.getenv('MONGO_URL')
dbname = os.getenv('MONGO_DB')
collectionname = os.getenv('MONGO_COLLECTION')
ca = certifi.where()


class DataExtraction():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e, sys)

    def csv_2_json(self, filepath):
        try:
            data = pd.read_csv(filepath)
            json_str = data.to_json(orient='records')
            records = json.loads(json_str)
            return records

        except Exception as e:
            raise NetworkException(e, sys)


    def commiting_data_2_mongodb(self, data, db, collection):
        try:
            self.db = db
            self.collection = collection
            self.data = data

            self.client = pymongo.MongoClient(mongo_url)
            self.db = self.client[self.db]
            self.collection = self.db[collection]
            self.collection.insert_many(self.data)
            return len(self.data)

        except Exception as e:
            raise NetworkException(e, sys)


if __name__ == "__main__":
    object = DataExtraction()
    FILE_PATH = 'Data/UrlstructureData.csv'
    json_records = object.csv_2_json(FILE_PATH)
    print(object.commiting_data_2_mongodb(data=json_records, db=dbname, collection=collectionname))



