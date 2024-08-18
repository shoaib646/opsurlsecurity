# connecting or pushing data into MongoDB

import os, sys, json,certifi, pymongo
from dotenv import  load_dotenv
import pandas as pd
import  numpy as np
from SecurityFolder.exception.exception import NetworkException
from SecurityFolder.logger.logger import *


load_dotenv()
mongo_url = os.getenv('MONGO_URL')
ca = certifi.where()


class DataExtraction():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e, sys)

    def csv_2_json(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e, sys)


    def commiting_data_2_mongodb(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e, sys)


    if __name__ == "__main__":
        pass




