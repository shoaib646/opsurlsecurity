import os, sys
from SecurityFolder.exception.exception import NetworkException
from SecurityFolder.logger.logger import *

from SecurityFolder.pipeline.TrainingPipeline import TrainingPipeline


def main():
    try:
        model_train = TrainingPipeline()
        model_train.run_pipeline()
    except Exception as e:
        raise Exception(e, sys)



if __name__ == '__main__':
    main()
