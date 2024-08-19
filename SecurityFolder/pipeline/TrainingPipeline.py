import os, sys

# components
from SecurityFolder.components.DataIngestion import  DataIngestion
from SecurityFolder.components.DataTransformation import  DataTransformation
from SecurityFolder.components.DataValidation import  DataValidation
from SecurityFolder.components.ModelDeployment import  ModelDeployment
from SecurityFolder.components.ModelEvaluation import  ModelEvaluation
from SecurityFolder.components.ModelTrainer import  ModelTrainer

# Exceptions & loggers
from SecurityFolder.exception.exception import NetworkException
from SecurityFolder.logger.logger import *

# configrations
from SecurityFolder.entities.config import (TrainingPipelineConfig,DataIngestionConfig, DataTransformationConfig,DataValidationConfig,
                                           ModelDeploymentConfig, ModelEvaluationConfig, ModelTrainerConfig)

#artifacts
from SecurityFolder.entities.artifacts import (DataIngestionArtifact,DataTransformationArtifact,DataValidationArtifact,
                                              ModelDeploymentArtifact,ModelEvaluationArtifact,ModelTrainerArtifact)

class TrainingPipeline:
    def __init__(self):
        pass

    def start_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e, "Failed to start data ingestion", sys)


    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e,"Failed to Validate Data", sys)

    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e,"Failed to Transform Data", sys)


    def start_model_training(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e,"Failed to Train Model", sys)


    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e,"Failed to Evaluate Model", sys)

    def star_model_deployment(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e,"Failed to Deploy Model", sys)


    def run_pipeline(self):
        try:
            print('Successfull')
        except Exception as e:
            raise NetworkException(e,"Failed to Run  Training Pipeline", sys)








