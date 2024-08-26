import os, sys

# components
from SecurityFolder.components.DataIngestion import  DataIngestion
from SecurityFolder.components.DataTransformation import  DataTransformation
from SecurityFolder.components.DataValidation import  DataValidation
from SecurityFolder.components.ModelRegistry import  ModelRegistry
from SecurityFolder.components.ModelEvaluation import  ModelEvaluation
from SecurityFolder.components.ModelTrainer import  ModelTrainer

import subprocess # for getting filename of error while debugging

# Exceptions & loggers
from SecurityFolder.exception.exception import NetworkException
from SecurityFolder.logger.logger import logging

# configrations
from SecurityFolder.entities.config import (TrainingPipelineConfig,DataIngestionConfig, DataTransformationConfig,DataValidationConfig,
                                           ModelRegistryConfig, ModelEvaluationConfig, ModelTrainerConfig)

#artifacts
from SecurityFolder.entities.artifacts import (DataIngestionArtifact,DataTransformationArtifact,DataValidationArtifact,
                                              ModelRegistrytArtifact,ModelEvaluationArtifact,ModelTrainerArtifact)




class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self):
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion completed and artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            raise NetworkException(e, sys)

    def start_data_validation(self,data_ingestion_artifact=DataIngestionArtifact):
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Starting data validation")
            data_validation = DataValidation(data_validation_config=data_validation_config, data_ingestion_artifact = data_ingestion_artifact)
            data_validation_artifact = data_validation.initiate_data_validation()
            return data_validation_artifact


        except Exception as e:
            raise NetworkException(e,sys)

    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e,sys)

    def start_model_training(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e,sys)

    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e,sys)

    def star_model_registy(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e,sys)

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation = self.start_data_validation()

        except Exception as e:
            raise NetworkException(e,sys)








