import os
from psycopg2 import pool
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

# Disable SSL by setting sslmode to 'disable'
connection_pool = pool.SimpleConnectionPool(
    1, 10,
    dbname=os.getenv('DATABASE_NAME'),
    user=os.getenv('DATABASE_USER'),
    password=os.getenv('DATABASE_PASSWORD'),
    host=os.getenv('DATABASE_HOST'),
    port=os.getenv('DATABASE_PORT'),
    sslmode='disable'
)
# Check if the connection pool was created successfully
if(connection_pool):
    print("Connection Pool created successfully")
