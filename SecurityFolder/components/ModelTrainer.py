from SecurityFolder.exception.exception import NetworkException
from SecurityFolder.logger.logger import logging

from SecurityFolder.entities.artifacts import DataTransformationArtifact, ModelTrainerArtifact
from SecurityFolder.entities.config import ModelTrainerConfig

import os, sys
from xgboost import  XGBClassifier

from SecurityFolder.utils.ML.metrics.Classification_metrics import get_classification_score
from SecurityFolder.utils.ML.model.estimator import NetworkModel
from SecurityFolder.utils.Main.utils import save_object, load_object, load_numpy_array_data

class ModelTrainer:
    def __init__(self,data_transformation_artifact:DataTransformationArtifact, model_trainer_config:ModelTrainerConfig):
        try:
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise NetworkException(e, sys)


    def perform_hyper_param_tuning(self):
        pass

    def train(self, X_train, y_train):
        try:
            model = XGBClassifier()
            model.fit(X_train, y_train)
            return model
        except Exception as e:
            raise NetworkException(e, sys)

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            train_file_path = self.data_transformation_artifact.transformed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path

            # loading training and testing array's
            train_arr = load_numpy_array_data(train_file_path)
            test_arr = load_numpy_array_data(test_file_path)

            X_train, y_train, X_test, y_test = train_arr[:,:-1], train_arr[:,-1], test_arr[:,:-1], test_arr[:, -1]

            model = self.train(X_train, y_train)
            y_train_pred = model.predict(X_train)

            classification_train_metric  = get_classification_score(y_true=y_train, y_pred=y_train_pred)


            if classification_train_metric.f1_score <= self.model_trainer_config.expected_accuracy:
                raise Exception("Trained model is not in good expected accuracy range")

            y_test_pred =  model.predict(X_test)

            classification_test_metric = get_classification_score(y_true=y_test, y_pred=y_test_pred)

            # overfitting and underfitting
            diff = abs(classification_train_metric.f1_score - classification_test_metric.f1_score)

            preprocessor = load_object(filepath=self.data_transformation_artifact.transformed_object_file_path)

            model_dir_path = os.path.dirname(self.model_trainer_config.trained_model_file_path)
            os.makedirs(model_dir_path, exist_ok=True)
            Network_Model = NetworkModel(preprocessor=preprocessor, model=model)

            save_object(self.model_trainer_config.trained_model_file_path,obj=Network_Model)

            #artifact
            model_trainer_artifact = ModelTrainerArtifact(trained_model_path=self.model_trainer_config.trained_model_file_path,
                                                          train_metric_artifact=classification_train_metric,
                                                          test_metric_artifact=classification_test_metric
                                                          )
            logging.info(f'Model Training Artifcact:{model_trainer_artifact}', )
            return model_trainer_artifact

        except Exception as e:
            raise NetworkException(e, sys)








