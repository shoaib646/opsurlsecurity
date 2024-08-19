
import subprocess
windowname = subprocess.run(['xdotool', 'getactivewindow', 'getwindowname'], stdout=subprocess.PIPE, text=True).stdout.strip()

import  datetime, os
from SecurityFolder.constants import TrainingPipeline


# print(TrainingPipeline.ARTIFACT_DIR)




class TrainingPipelineConfig:
    def __init__(self):
        pass

class DataIngestionConfig:
    def __init__(self):
        pass

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






