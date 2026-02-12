import mysql.connector
import os

config = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "port": int(os.getenv("MYSQL_PORT", 3306))
}

class SQLManager:
    cnx = None
    def __init__(self):
        try:
            if not SQLManager.cnx:
                cnx = mysql.connector.connect(**config)
                SQLManager.cnx = cnx
        except Exception as e:
            raise Exception(f"Could not connect to SQLDB, Error: {str(e)}")
        self.cnx = SQLManager.cnx
        
    def get_cnx(self):
        return self.cnx