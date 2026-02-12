from mysql_connection import SQLManager
from kafka_consumer import listen

def main():
    sql_manager = SQLManager()
    sql_manager.init_db()
    listen(sql_manager)
    
if __name__ == "__main__":
    main()