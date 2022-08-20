
import pyodbc
from datetime import datetime, timedelta
import logging.config

logging.basicConfig(filename='logs/loggers_sql.log',
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)
date = datetime.today()
date = date.strftime("%Y-%m-%d")
server = 'DESKTOP-U2IISUC\SQLEXPRESS01'
database = 'Airbnb'

conn_str = ("DRIVER={SQL SERVER};"
            "SERVER=DESKTOP-U2IISUC\SQLEXPRESS01;"
            "DATABASE=Airbnb;"
            "Trusted_Connection=yes;")
cursor = pyodbc.connect(conn_str)
conn_completed = 0
logger.info("--- SQL-SERVER ---")
while conn_completed == 0:
    try:
        logger.info("connecting to SQL-server: ")
        cursor = pyodbc.connect(conn_str)
        logger.info('Connected to SQL-server')
        conn_completed = 1
    except:
        logger.info("Sorry couldn't connect to SQL-server")
        conn_str.close()
        conn_str.sleep(60)
        conn_completed = 0

cursor.execute("SELECT TOP(100) * FROM [dbo].[airbnb_data]")
