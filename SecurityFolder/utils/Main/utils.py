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

def save_numpy_array_data(filepath: str, array: np.array):
    """
    Save numpy array data to file
    filepath: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(filepath)
        os.makedirs(dir_path, exist_ok=True)
        with open(filepath, "wb") as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise NetworkException(e, sys) from e


def load_numpy_array_data(filepath: str) -> np.array:
    """
    load numpy array data from file
    filepath: str location of file to load
    return: np.array data loaded
    """
    try:
        with open(filepath, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise NetworkException(e, sys) from e


def save_object(filepath: str, obj: object) -> None:
    try:
        logging.info("Entered the save_object method of MainUtils class")
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "wb") as file_obj:
            pickle.dump(obj, file_obj)
        logging.info("Exited the save_object method of MainUtils class")
    except Exception as e:
        raise NetworkException(e, sys) from e


def load_object(filepath: str, ) -> object:
    try:
        if not os.path.exists(filepath):
            raise Exception(f"The file: {filepath} is not exists")
        with open(filepath, "rb") as file_obj:
            print(file_obj)
            return pickle.load(file_obj)
    except Exception as e:
        raise NetworkException(e, sys) from e