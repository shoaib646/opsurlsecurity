import os, sys
from SecurityFolder.constants.TrainingPipeline import  SAVE_MODEL_DIR, MODEL_FILE_NAME
from SecurityFolder.exception.exception import NetworkException
from SecurityFolder.logger.logger import logging


class NetworkModel:
    def __init__(self, preprocessor, model):
        try:
            self.preprocessor = preprocessor
            self.model  = model
        except Exception as e:
            raise NetworkException(e, sys)

    def predict(self, X):
        try:
            X_transform= self.preprocessor.transform(X)
            y_hat = self.model.predict(X_transform)
            return y_hat
        except Exception as e:
            raise NetworkException(e, sys)


class ModelResolver:
    def __init__(self, model_dir=SAVE_MODEL_DIR):
        try:
            self.model_dir = model_dir
        except Exception as e:
            raise NetworkException(e, sys)

    def get_best_model_path(self) -> str:
        try:
            timestamps = list(map(int, os.listdir(self.model_dir)))
            latest_timestamp = max(timestamps)
            latest_model_path = os.path.join(self.model_dir, f"{latest_timestamp}",MODEL_FILE_NAME)
            return str(latest_model_path)
        except Exception as e:
            raise NetworkException(e, sys)

    def is_model_exist(self) -> bool:
        try:
            if not  os.path.exists(self.model_dir):
                return False

            timestamps = os.listdir(self.model_dir)
            if len(timestamps) == 0:
                return False

            latest_model_path = self.get_best_model_path()

            if not os.path.exists(latest_model_path):
                return False
        except  Exception as e:
            raise NetworkException(e, sys)



