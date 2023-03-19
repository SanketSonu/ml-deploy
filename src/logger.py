# This file will help in create logging file. So that we can have track of the execution or errors encountered.

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # This will be a text file
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)             # Fie Path
os.makedirs(logs_path,exist_ok=True)                            # It will keep on appending files, even if there are files already in there.

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)