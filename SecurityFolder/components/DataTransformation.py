
import sys, os
import numpy as np
import pandas as pd
from sklearn.impute import  KNNImputer
from sklearn.pipeline import  Pipeline

from SecurityFolder.constants.TrainingPipeline import TARGET_COLUMN
from SecurityFolder.constants.TrainingPipeline import DATA_TRNSFORMATION_IMPUTER_PARAMS

from SecurityFolder.entities.artifacts import DataTransformationArtifact, DataValidationArtifact

from SecurityFolder.entities.config import DataTransformationConfig

from SecurityFolder.exception.exception import NetworkException
from SecurityFolder.logger.logger import logging

from SecurityFolder.utils.Main.utils import save_numpy_array_data, save_object




class DataTransformation:
    def __init__(self, data_validation_artifact = DataValidationArtifact,
                 data_transformation_config = DataTransformationConfig):
        pass