# Any functionalities that we are writing in a common way, which will be used in entire application.
# Ex-- we can read a dataset from a database for that we need to create mongodb client here, if we want to save our model in cloud, etc all these codes will be written here.
# In end we will call this Utils code inside components module files whenever we are going to use that specific code for db, cloud, model evaluation, finding best models etc.

import os
import sys

import numpy as np
import pandas as pd
import dill              # Will help to create pickle file

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)             # Dump will save specific file in specific path

    except Exception as e:
        raise CustomException(e, sys)