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


def save_numpy_array_data(filepath:str, array:np.ndarray ):
    try:
        dir_path  = os.path.dirname(filepath)
        os.makedirs(dir_path, exist_ok=True)
        with open(filepath, 'wb') as f:
            np.save(f, array)
    except Exception as exc:
        raise NetworkException(exc, sys)

def load_numpy_array_data(filepath:str) -> np.ndarray:
    try:
        with open(filepath, 'rb') as f:
            return np.load(f)
    except Exception as exc:
        raise NetworkException(exc, sys)

def save_object(filepath:str, obj:object) -> None:
    try:
        logging.INFO('Entered to save object under main utils')
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'wb') as f:
            pickle.dump(obj, f)
        logging.INFO('Dumped object to pickle file')
    except Exception as exc:
        raise NetworkException(exc, sys)


def load_object(filepath:str) -> object:
    try:
        if not os.path.exists(filepath):
            raise NetworkException(f'{filepath} does not exists.')
        with open(filepath, 'rb') as f:
            return pickle.load(f)
    except Exception as exc:
        raise NetworkException(exc, sys)
