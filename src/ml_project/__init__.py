import os 
import logging 
import sys

log_str = '[%(asctime)s : %(levelname)s :%(module)s : %(message)s]'

lo = 'logs'
filepath = os.path.join(lo, 'current_logs.log')
os.makedirs(lo, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=log_str,
    handlers=[
        logging.FileHandler(filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('ML_pro_logger')