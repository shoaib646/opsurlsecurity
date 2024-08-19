
import subprocess
windowname = subprocess.run(['xdotool', 'getactivewindow', 'getwindowname'], stdout=subprocess.PIPE, text=True).stdout.strip()

import  datetime, os
from SecurityFolder.constants import TrainingPipeline







class TrainingPipelineConfig:
    def __init__(self, timestamp = datetime.datetime.now().strftime("%y%m%d_%H%M%S")):
        time  = timestamp
        self.pipeline_name = TrainingPipeline.PIPELINE_NAME
        self.artifact_name = TrainingPipeline.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_dir, time)
        self.timestamp:str = time

class DataIngestionConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):

        # self.training_pipeline_config = training_pipeline_config
        self.data_ingestion_dir :str = os.path.join(self.training_pipeline_config.artifact_dir,
                                                    TrainingPipeline.DATA_INGESTION_DIR_NAME)

        self.feature_store_file_path =os.path.join(self.data_ingestion_dir,
                                                   TrainingPipeline.DATA_INGESTION_FEATURE_STORE_DIR_NAME)

        self.training_file_path = os.path.join(self.data_ingestion_dir, TrainingPipeline.DATA_INGESTED_DIR,
                                               TrainingPipeline.TRAIN_FILE_NAME)

        self.testing_file_path = os.path.join(self.data_ingestion_dir, TrainingPipeline.DATA_INGESTED_DIR,
                                               TrainingPipeline.TEST_FILE_NAME)

        self.train_test_split_ratio : float = TrainingPipeline.DATA_INGESTION_SPLIT_RATIO
        self.collection_name :str = TrainingPipeline.COLLECTION_NAME
        self.database_name :str = TrainingPipeline.DATABASE_NAME


class DataValidationConfig:
    def __init__(self):
        pass

class DataTransformationConfig:
    def __init__(self):
        pass

class ModelTrainerConfig:
    def __init__(self):
        pass

class ModelEvaluationConfig:
    def __init__(self):
        pass

class ModelRegistryConfig:
    def __init__(self):
        pass






