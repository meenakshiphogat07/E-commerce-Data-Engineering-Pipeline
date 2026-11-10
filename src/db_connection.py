import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def create_connection(db,user, password, host, port):
    try:
        connection = psycopg2.connect(
            database=db,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("Connection to PostgreSQL database successful")
        return connection
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL database: {e}")
        return None


connection = create_connection(
    db=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

if connection:
    connection.close()
    print("Database connection closed.")