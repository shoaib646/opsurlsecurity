
import  pandas as pd
import numpy as np


from SecurityFolder.constants.TrainingPipeline import SCHEMA_FILE_PATH
from SecurityFolder.entities.artifacts import DataIngestionArtifact, DataValidationArtifact
from SecurityFolder.entities.config import DataValidationConfig
from SecurityFolder.exception.exception import NetworkException

from SecurityFolder.logger.logger import logging

from SecurityFolder.utils.Main.utils import read_yaml_file, write_yaml_file
from scipy.stats import  ks_2samp

import os, sys



class DataValidation:
    def __init__(self, data_ingestion_artifact : DataIngestionArtifact,data_validation_config:DataValidationConfig ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkException(e, sys)


    def validate_noof_cols(self, dataframe: pd.DataFrame) -> bool:
        try:
            pass
        except Exception as e:
            raise NetworkException(e, sys)

    def is_numerical_column_exists(self, dataframe: pd.DataFrame) -> bool:
        try:
            pass
        except Exception as e:
            raise NetworkException(e, sys)

    @staticmethod
    def read_data(filepath) -> pd.DataFrame:
        try:
            return  pd.read_csv(filepath)
        except Exception as e:
            raise NetworkException(e, sys)


    def detect_dataset_drift(self, base_df, current_df, threshold=0.05) -> bool:
        try:
            pass
        except Exception as e:
            raise NetworkException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            data = self.read_data()
            self.validate_noof_cols(data)
            self.detect_dataset_drift(data, data)
        except Exception as e:
            raise NetworkException(e, sys)

