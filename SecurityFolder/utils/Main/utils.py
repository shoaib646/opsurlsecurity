import  yaml, os, sys, dill, pickle
from SecurityFolder.exception.exception import  NetworkException
from SecurityFolder.logger.logger import logging
import  numpy as np




def read_yaml_file(filepath:str) -> dict:
    try:
        with open(filepath, 'r') as ymlfile:
            return yaml.safe_load(ymlfile)
    except yaml.YAMLError as exc:
        raise NetworkException(exc, sys)



def write_yaml_file(filepath:str, data:dict, replace:bool=False) -> None:
    try:
        if replace:
            if os.path.exists(filepath):
                os.remove(filepath)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w') as ymlfile:
            yaml.dump(data, ymlfile)
    except Exception as exc:
        raise NetworkException(exc, sys)
