
from SecurityFolder.exception.exception import NetworkException
from SecurityFolder.logger.logger import *

from SecurityFolder.entities.artifacts import DataingestionArtifact
from SecurityFolder.entities.config import  DataIngestionConfig

import  os
import pandas as pd
import  numpy as np
import pymongo # reading data from mongo database
from typing import List


import subprocess
windowname = subprocess.run(['xdotool', 'getactivewindow', 'getwindowname'], stdout=subprocess.PIPE, text=True).stdout.strip()



class DataIngestion:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e, sys._getframe().f_lineno, windowname)

    def export_collection_as_dataframe(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e, sys._getframe().f_lineno, windowname)

    def export_feature_store(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e, sys._getframe().f_lineno, windowname)

    def split_data(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e, sys._getframe().f_lineno, windowname)

    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise NetworkException(e, sys._getframe().f_lineno, windowname)