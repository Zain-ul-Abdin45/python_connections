import logging
import datetime

logging.basicConfig(filename='logs/loggers.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
try:
  date = datetime.datetime.now()
  logger.info("Your logs are working")
except:
  logger.info("An exception occurred")
