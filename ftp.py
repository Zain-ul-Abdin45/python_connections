import ftplib
import logging.config
logging.basicConfig(filename='logs/loggers.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
with ftplib.FTP('ftpserver.com') as ftp:
    try:
        logger.info('connecting to ftp..')
        ftp.connect('ftp.host.com')
        logger.info('connected to ftp server')
        ftp.pwd() # to get the directory
    except:
        logger.info('Sorry could not connect to ftp')
