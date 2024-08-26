import  os
import sys


import numpy as np
import pandas as pd

from dotenv import load_dotenv

load_dotenv()



'''
Comman varaibles for trainigng pipeline
'''

TARGET_COLUMN : str = 'Result'
PIPELINE_NAME : str = 'OpsURLSecurity'
ARTIFACT_DIR : str = 'Artifacts'
FILE_NAME : str = 'UrlstructureData.csv'

TRAIN_FILE_NAME : str = 'train.csv'
TEST_FILE_NAME : str = 'test.csv'

PREPROCESSING_OBJECT_FILE_NAME = 'Preprocessing.pkl'
MODEL_FILE_NAME     = 'Model.pkl'
SCHEMA_FILE_PATH    = os.path.join("data-schema", "schema.yaml")
SCHEMA_DROP_COLS    = "drop_columns"

SAVE_MODEL_DIR = os.path.join("saved_models")


DB_URL : str = os.getenv('MONGO_URL')
COLLECTION_NAME : str = os.getenv('MONGO_COLLECTION')
DATABASE_NAME : str  = os.getenv('MONGO_DB')


'''
Data Ingestion related constant variables
'''

DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2



'''
Data Validation related constant variables
'''
DATA_VALIDATION_DIR_NAME : str = 'Data_Validation_DIR'
DATA_VALIDATION_VALID_DIR : str = 'Valid_Data_DIR'
DATA_VALIDATION_INVALID_DIR : str = 'Invalid_Data_DIR'
DATA_VALIDATION_DRIFT_REPORT_DIR : str = 'Drift_Report_DIR'
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME : str = 'report.yaml'



'''
Data Transformation related constant variables
'''



'''
Data Trainer related constant variables
'''