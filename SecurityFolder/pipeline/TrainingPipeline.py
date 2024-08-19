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
from SecurityFolder.logger.logger import *

# configrations
from SecurityFolder.entities.config import (TrainingPipelineConfig,DataIngestionConfig, DataTransformationConfig,DataValidationConfig,
                                           ModelDeploymentConfig, ModelEvaluationConfig, ModelTrainerConfig)

#artifacts
from SecurityFolder.entities.artifacts import (DataIngestionArtifact,DataTransformationArtifact,DataValidationArtifact,
                                              ModelDeploymentArtifact,ModelEvaluationArtifact,ModelTrainerArtifact)


windowname = subprocess.run(['xdotool', 'getactivewindow', 'getwindowname'], stdout=subprocess.PIPE, text=True).stdout.strip()

class TrainingPipeline:
    def __init__(self):
        pass

    def start_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e, "Failed to start data ingestion", sys._getframe().f_lineno, windowname)


    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e,"Failed to Validate Data", sys._getframe().f_lineno, windowname)

    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e,"Failed to Transform Data", sys._getframe().f_lineno, windowname)


    def start_model_training(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e,"Failed to Train Model", sys._getframe().f_lineno, windowname)


    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e,"Failed to Evaluate Model", sys._getframe().f_lineno, windowname)

    def star_model_registy(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e,"Failed to Register Model", sys._getframe().f_lineno, windowname)


    def run_pipeline(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e,"Failed to Run  Training Pipeline", sys._getframe().f_lineno, windowname)








