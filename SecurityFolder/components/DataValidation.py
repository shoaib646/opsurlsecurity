
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
            number_of_columns = len(self._schema_config['columns'])
            logging.info(f"Required number of columns")
            logging.info(f"DataFrame has {len(dataframe.columns)} columns")

            if number_of_columns == len(self._schema_config['columns']):
                return True
            return False
        except Exception as e:
            raise NetworkException(e, sys)

    def is_numerical_column_exists(self, dataframe: pd.DataFrame) -> bool:
        try:
            numerical_cols = self._schema_config['numerical_columns']
            is_numeric = True
            non_numerical_columns = []
            for column in dataframe.columns:
                if column in numerical_cols:
                    is_numeric = False
                    non_numerical_columns.append(column)
            logging.info(f"Numerical columns: {non_numerical_columns}")
            return is_numeric
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
            status = True
            report = {}
            for column in base_df.columns:
                d1 = base_df[column]
                d2 = current_df[column]
                is_same_dist = ks_2samp(d1, d2)
                if threshold <= is_same_dist.pvalue:
                    is_found = False
                else:
                    is_found = True
                    status = False
                report.update({column: {
                    "p_value": float(is_same_dist.pvalue),
                    "drift_status": is_found

                }})

            drift_report_file_path = self.data_validation_config.drift_report_file_path

            dir_path = os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path, exist_ok=True)
            write_yaml_file(filepath=drift_report_file_path, data=report)
            return status

        except Exception as e:
            raise NetworkException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            train_data = DataValidation.read_data(train_file_path)
            test_data = DataValidation.read_data(test_file_path)

            status = self.validate_noof_cols(train_data)
            if not status:
                error_message = f"{error_message} Train DataFrame does not contain all columns"

            status = self.validate_noof_cols(test_data)
            if not status:
                error_message = f"{error_message} Test DataFrame does not contain all columns"


            status = self.detect_dataset_drift(base_df=train_data, current_df=test_data)


            dataset_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=train_file_path,
                valid_test_file_path=test_file_path,

                invalid_train_file_path=None,
                invalid_test_file_path=None,

                drift_report_file_path=self.data_validation_config.drift_report_file_path,



            )

            logging.info(f"Data Validation Completed artifact: {dataset_validation_artifact}")


        except Exception as e:
            raise NetworkException(e, sys)








