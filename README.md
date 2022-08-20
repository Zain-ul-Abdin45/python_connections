# python_connections

connecting python with databases or with data stream is one of the tackling task.
But you can connect Python with databases to manipulate the data in databases through python and to execute other opertions.
- To connect with SQL server make sure you have driver to integrate the python with SQL, ODBC driver 18. Then you can insert, update, or query data to the table.
- You can read csv, excel flat files from local machines or through servers with python, manipulate or convert the datatypes and ingest the data with the connections. 
- To connect with FTP or SFTP where data is shared, you can connect with ftp or sftp server, and then ingest the data to sql server or any database platform.


# Logging and logs generating
-The reason we need logs is because they hold information that can't be found anywhere else. For example, say you added something to a domain class but you forgot to run the migration. This will probably cause some problems. You don't want to tell users that you are missing a certain column in your table for a lot of reasons.

-An error like this will be recorded in the logs so that only someone with access to the server could see those kinds of errors. Most of the time this is where you should look when you can't figure out what's wrong with your code after hours of debugging. The answer might not always be here, but it will give you another place to go check.

-Once you start looking in the log files when you have weird errors, it becomes easier to find ways to fix them. At the minimum, you will rule out another place to look. -A lot of new developers don't know about logs so it's important that we take the time to teach them so they can learn how to better research bugs.
