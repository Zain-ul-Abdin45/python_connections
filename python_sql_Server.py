
import pyodbc
from datetime import datetime, timedelta
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart
import smtpd

date = datetime.today()
date = date.strftime("%Y-%m-%d")
server = 'DESKTOP-U2IISUC\SQLEXPRESS01'
database = 'Airbnb'

conn_str = ("DRIVER={SQL SERVER};"
            "SERVER=DESKTOP-U2IISUC\SQLEXPRESS01;"
            "DATABASE=Airbnb;"
            "Trusted_Connection=yes;")
cursor = pyodbc.connect(conn_str)

print(cursor.execute("SELECT TOP(100) * FROM [dbo].[airbnb_data]"))
