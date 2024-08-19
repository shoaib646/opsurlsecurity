import  logging, os
from datetime import datetime
import subprocess
windowname = subprocess.run(['xdotool', 'getactivewindow', 'getwindowname'], stdout=subprocess.PIPE, text=True).stdout.strip()


# LOG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
# LOG_FILE = f"{datetime.now().strftime('%m_%d_%H_%M_%S')}.log"
#
#
# os.makedirs(LOG_PATH, exist_ok=True)
#
# LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)
#
# logging.basicConfig(filename=LOG_FILE_PATH, level=logging.INFO,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %I:%M:%S %p',
#                     filemode='a')

def setup_logging(log_dir="logs"):
    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    logs_path = os.path.join(os.getcwd(), log_dir)
    os.makedirs(logs_path, exist_ok=True)
    LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,
    )

    logger = logging.getLogger()
    return logger

# Initialize the logger
log_setup = setup_logging()