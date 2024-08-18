import  logging, os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%H_%M_%S')}.log"
LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")

os.makedirs(LOG_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

logging.basicConfig(filename=LOG_FILE_PATH, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filemode='w')