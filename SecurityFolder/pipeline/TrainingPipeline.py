import os, sys

# components
from SecurityFolder.components.DataIngestion import  DataIngestion
from SecurityFolder.components.DataTransformation import  DataTransformation
from SecurityFolder.components.DataValidation import  DataValidation
from SecurityFolder.components.ModelRegistry import  ModelRegistry
from SecurityFolder.components.ModelEvaluation import  ModelEvaluation
from SecurityFolder.components.ModelTrainer import  ModelTrainer



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

    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact):
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)


            data_validation = DataValidation(data_validation_config=data_validation_config,
                                             data_ingestion_artifact = data_ingestion_artifact)


            data_validation_artifact = data_validation.initiate_data_validation()

            return data_validation_artifact


        except Exception as e:
            raise NetworkException(e,sys)

    def start_data_transformation(self,data_validation_artifact:DataValidationArtifact):
        try:
            data_transformation_config = DataTransformationConfig(
                training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact,
                                                     data_transformation_config=data_transformation_config)

            data_transformation_artifact = data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except Exception as e:
            raise NetworkException(e,sys)

    def start_model_training(self, data_transformation_artifact:DataTransformationArtifact) -> ModelTrainerArtifact:
        try:
            self.modeltrainingconfig = ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)

            model_trainer = ModelTrainer(data_transformation_artifact=data_transformation_artifact,
                                         model_trainer_config=self.modeltrainingconfig)

            model_trainer_artifact  = model_trainer.initiate_model_trainer()

            return model_trainer_artifact


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

            data_validation_artifact = self.start_data_validation(data_ingestion_artifact= data_ingestion_artifact)

            data_transformation_artifact = self.start_data_transformation(
                data_validation_artifact=data_validation_artifact)

            model_trainer_artifact = self.start_model_training(
                data_transformation_artifact=data_transformation_artifact)

        except Exception as e:
            raise NetworkException(e,sys)