import mysql.connector
import os

SQL_URI = os.getenv("SQL_URI") 

class SQLManager:
    cnx = None
    def __init__(self):
        try:
            if not SQLManager.cnx:
                SQLManager.cnx = mysql.connector.connect(SQL_URI)
            self.cnx = SQLManager.cnx
        except Exception as e:
            raise Exception(f"Could not connect to SQLDB, Error: {str(e)}")
        
    def get_cnx(self):
        return self.cnx