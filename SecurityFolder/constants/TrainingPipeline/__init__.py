import  os
import sys


import numpy as np
import pandas as pd

from dotenv import load_dotenv
from networkx import non_neighbors

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
DATA_VALIDATION_DIR_NAME : str = 'Data_Validation'
DATA_VALIDATION_VALID_DIR : str = 'Valid_Data'
DATA_VALIDATION_INVALID_DIR : str = 'Invalid_Data'
DATA_VALIDATION_DRIFT_REPORT_DIR : str = 'Drift_Report'
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME : str = 'report.yaml'


'''
Data Transformation related constant variables
'''

DATA_TRANSFORM_DIR_NAME : str = 'Data_Transformation'
DATA_TRANSFORM_TRANSFORMED_DATA_DIR : str = 'Transformed_Data'
DATA_TRANSFORM_TRANSFORMED_OBJECT_DIR : str = 'Transformed_Object'

DATA_TRNSFORMATION_IMPUTER_PARAMS : dict = {
    'missing_values':np.nan,
    'non_neighbors':3,
    'weights':'uniform',
}

DATA_TRANSFORM_TRAIN_FILE_PATH : str = 'train.npy'

DATA_TRNSFORMA_TEST_FILE_PATH : str = 'test.npy'


'''
Data Trainer related constant variables
'''