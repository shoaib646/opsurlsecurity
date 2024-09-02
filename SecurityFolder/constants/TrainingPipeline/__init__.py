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
MODEL_FILE_NAME     = 'model.pkl'
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
DATA_TRANSFORMATION_DIR_NAME: str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR: str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR: str = "transformed_object"

DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": np.nan,
    "n_neighbors": 3,
    "weights": "uniform",
}

DATA_TRANSFORMATION_TRAIN_FILE_PATH: str = "train.npy"

DATA_TRANSFORMATION_TEST_FILE_PATH: str = "test.npy"

'''
Data Trainer related constant variables
'''
MODEL_TRAINER_DIR_NAME : str = 'Model_Trainer'
MODEL_TRAINER_TRAINED_MODEL_DIR :str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME : str = 'model.pkl'
MODEL_TRAINER_EXPECTED_SCORE : float = 0.6
MODEL_TRAINER_OVER_UNDER_FIT_THRESH : float = 0.05

'''
Data Evaluation related constant variables
'''

MODEL_EVALUATION_DIR_NAME : str = 'ModelEvaluation'
MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE : float = 0.02
MODEL_EVALUATION_REPORT_NAME : str = 'EvaluationReport.yaml'

MODEL_REGISTRY_DIR_NAME : str = 'ModelRegistry'
MODEL_REGISTRY_SAVED_MODEL_DIR :str = SAVE_MODEL_DIR



