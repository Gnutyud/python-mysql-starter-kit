import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

db_config = {
    "host": os.getenv("MYSQL_DATABASE_HOST"),
    "database": os.getenv("MYSQL_DATABASE_DB"),
    "user": os.getenv("MYSQL_DATABASE_USER"),
    "password": os.getenv("MYSQL_DATABASE_PASSWORD"),
    "port": os.getenv("MYSQL_DATABASE_PORT"),
}

def create_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Successfully connected to the database!")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None    