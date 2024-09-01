import pandas as pd
import numpy as np
import os
import sys

from SecurityFolder.constants.TrainingPipeline import SCHEMA_FILE_PATH
from SecurityFolder.entities.artifacts import DataIngestionArtifact, DataValidationArtifact
from SecurityFolder.entities.config import DataValidationConfig
from SecurityFolder.exception.exception import NetworkException
from SecurityFolder.logger.logger import logging
from SecurityFolder.utils.Main.utils import read_yaml_file, write_yaml_file

from scipy.stats import ks_2samp

class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact,
                 data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkException(e, sys)

    def validate_number_of_columns(self, dataframe: pd.DataFrame) -> bool:
        try:
            number_of_columns = len(self._schema_config["columns"])
            logging.info(f"Required number of columns: {number_of_columns}")
            logging.info(f"Data frame has columns: {len(dataframe.columns)}")

            return len(dataframe.columns) == number_of_columns
        except Exception as e:
            raise NetworkException(e, sys)

    def is_numerical_column_exist(self, dataframe: pd.DataFrame) -> bool:
        try:
            numerical_columns = self._schema_config["numerical_columns"]
            dataframe_columns = dataframe.columns

            missing_numerical_columns = [col for col in numerical_columns if col not in dataframe_columns]
            logging.info(f"Missing numerical columns: {missing_numerical_columns}")

            return len(missing_numerical_columns) == 0
        except Exception as e:
            raise NetworkException(e, sys)

    @staticmethod
    def read_data(file_path) -> pd.DataFrame:
        try:
            return pd.read_csv(file_path)
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
                is_found = threshold > is_same_dist.pvalue
                report[column] = {
                    "p_value": float(is_same_dist.pvalue),
                    "drift_status": is_found
                }
                if is_found:
                    status = False

            drift_report_file_path = self.data_validation_config.drift_report_file_path

            # Create directory
            os.makedirs(os.path.dirname(drift_report_file_path), exist_ok=True)
            write_yaml_file(filepath=drift_report_file_path, data=report)

            return status
        except Exception as e:
            raise NetworkException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.trained_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            # Reading data from train and test file location
            train_dataframe = DataValidation.read_data(train_file_path)
            test_dataframe = DataValidation.read_data(test_file_path)

            # Validate number of columns
            if not self.validate_number_of_columns(dataframe=train_dataframe):
                raise NetworkException("Train dataframe does not contain all columns.", sys)

            if not self.validate_number_of_columns(dataframe=test_dataframe):
                raise NetworkException("Test dataframe does not contain all columns.", sys)

            # Check for data drift
            status = self.detect_dataset_drift(base_df=train_dataframe, current_df=test_dataframe)

            os.makedirs(os.path.dirname(self.data_validation_config.valid_train_file_path), exist_ok=True)

            train_dataframe.to_csv(self.data_validation_config.valid_train_file_path, index=False, header=True)
            test_dataframe.to_csv(self.data_validation_config.valid_test_file_path, index=False, header=True)

            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=self.data_validation_config.valid_train_file_path,
                valid_test_file_path=self.data_validation_config.valid_test_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path,
            )

            logging.info(f"Data validation artifact: {data_validation_artifact}")

            return data_validation_artifact
        except Exception as e:
            raise NetworkException(e, sys)
