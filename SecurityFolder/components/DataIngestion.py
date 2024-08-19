
from SecurityFolder.exception.exception import NetworkException
from SecurityFolder.logger import  log_setup

from SecurityFolder.entities.artifacts import DataIngestionArtifact
from SecurityFolder.entities.config import  DataIngestionConfig

import  os
import pandas as pd
import  numpy as np
from sklearn.model_selection import train_test_split
import pymongo # reading data from mongo database
from typing import List
from dotenv import load_dotenv
load_dotenv()
DB_URL = os.getenv("MONGO_URL")



import subprocess
windowname = subprocess.run(['xdotool', 'getactivewindow', 'getwindowname'], stdout=subprocess.PIPE, text=True).stdout.strip()



class DataIngestion:

    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkException(e, sys._getframe().f_lineno, windowname)

    # getting dataframe from Mongo DB
    def export_collection_as_dataframe(self):
        try:
            db_name = self.data_ingestion_config.database_name     #access
            collection_name = self.data_ingestion_config.collection_name #access

            self.mongo_client = pymongo.mongo_client(DB_URL)
            collection = self.mongo_client[db_name][collection_name]

            dataframe = pd.DataFrame(list(collection.find()))

            if "_id" in dataframe.columns.to_list():
                dataframe = dataframe.drop(["_id"], axis=1)
            dataframe.replace({"na":np.nan}, inplace=True)

            return dataframe

        except Exception as e:
            raise NetworkException(e, sys._getframe().f_lineno, windowname)

    def export_feature_store(self, dataframe: pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path #access

            directory = os.path.dirname(feature_store_file_path)
            os.makedirs(directory, exist_ok=True)

            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        except Exception as e:
            raise NetworkException(e, sys._getframe().f_lineno, windowname)

    def split_data(self, dataframe: pd.DataFrame):
        try:
            train_set, test_set = train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio, random_state=42) #access

            train_file_name = self.data_ingestion_config.training_file_path #access
            test_file_name = self.data_ingestion_config.testing_file_path #access

            directory = os.path.dirname(self.data_ingestion_config.training_file_path)  #access
            os.makedirs(directory, exist_ok=True)

            log_setup.INFO(f"Exporting train and test directories")

            train_set.to_csv(train_file_name, index=False, header=True)
            test_set.to_csv(test_file_name, index=False, header=True)

            log_setup.INFO(f"Completed! Exporting, train and test data")


        except Exception as e:
            raise NetworkException(e, sys._getframe().f_lineno, windowname)

    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_dataframe()
            dataframe = self.export_feature_store(dataframe=dataframe)
            self.split_data(dataframe=dataframe)

            data_ingestion_artifact = DataIngestionArtifact(
                                  trained_file_path= self.data_ingestion_config.training_file_path ,
                                  test_file_path = self.data_ingestion_config.testing_file_path,
                                  )
            return data_ingestion_artifact


        except Exception as e:
            raise NetworkException(e, sys._getframe().f_lineno, windowname)