
import os, sys

from timm import is_model

from SecurityFolder.exception.exception import NetworkException
from SecurityFolder.logger.logger import logging

from SecurityFolder.entities.config import ModelEvaluationConfig
from SecurityFolder.entities.artifacts import DataValidationArtifact, ModelTrainerArtifact, ModelEvaluationArtifact

from SecurityFolder.utils.ML.metrics.Classification_metrics import get_classification_score
from SecurityFolder.utils.ML.model.estimator import NetworkModel
from SecurityFolder.utils.Main.utils import save_object, load_object, load_numpy_array_data, write_yaml_file

from SecurityFolder.utils.ML.model.estimator import ModelResolver
from SecurityFolder.constants.TrainingPipeline import TARGET_COLUMN

import pandas as pd



class ModelEvaluation:
    def __init__(self, model_evaluation_config: ModelEvaluationConfig,
                 data_validation_artifact: DataValidationArtifact,
                 model_trainer_artifact: ModelTrainerArtifact):
        try:
            self.model_evaluation_config = model_evaluation_config
            self.data_validation_artifact = data_validation_artifact
            self.model_trainer_artifact = model_trainer_artifact
        except Exception as e:
            raise NetworkException(e,sys)


    def initiate_model_evaluation(self) -> ModelEvaluationArtifact:
        try:
            valid_train_file_path = self.data_validation_artifact.valid_train_file_path
            valid_test_file_path = self.data_validation_artifact.valid_test_file_path

            train_df = pd.read_csv(valid_train_file_path)
            test_df = pd.read_csv(valid_test_file_path)

            df = pd.concat([train_df, test_df])
            y_true = df[TARGET_COLUMN]
            y_true.replace(-1,0, inplace=True)

            df.drop(TARGET_COLUMN, axis=1, inplace=True)

            train_model_path =self.model_trainer_artifact.trained_model_path
            model_resolver = ModelResolver()

            is_model_accepted = True


            if not model_resolver.is_model_exist():
                model_evaluation_artifact = ModelEvaluationArtifact(
                    is_model_accepted=is_model_accepted,
                    improved_accuracy_score=None,
                    best_model_path=None,
                    trained_model_path=train_model_path,
                    train_model_metric_artifact=self.model_trainer_artifact.test_metric_artifact,
                    best_model_metric_artifact=None,
                )
                logging.info(f'Model Evaluation Artifact:{model_evaluation_artifact}' )
                return model_evaluation_artifact

            latest_model_path = model_resolver.get_best_model_path()
            latest_model = load_object(filepath=latest_model_path)
            train_model = load_object(filepath=train_model_path)

            y_trained_pred = train_model.predict(df)
            y_latest_pred = latest_model.predict(df)

            trained_metric = get_classification_score(y_true, y_trained_pred)
            latest_metric = get_classification_score(y_true, y_latest_pred)

            improved_accuracy = trained_metric.f1_score - latest_metric.f1_score
            if self.model_evaluation_config.change_threshold <  improved_accuracy:
                is_model_accepted = True
            else:
                is_model_accepted = False

            model_evaluation_artifact = ModelEvaluationArtifact(
                is_model_accepted=is_model_accepted,
                improved_accuracy_score=improved_accuracy,
                best_model_path=latest_model_path,
                trained_model_path=train_model_path,
                train_model_metric_artifact=self.model_trainer_artifact.test_metric_artifact,
                best_model_metric_artifact=trained_metric,
            )

            model_eval_report = model_evaluation_artifact.__dict__

            write_yaml_file(self.model_evaluation_config.report_file_path,model_eval_report)
            logging.info(f'Model Evaluation Artifact:{model_evaluation_artifact}' )
            return model_evaluation_artifact
        except Exception as e:
            raise NetworkException(e,sys)