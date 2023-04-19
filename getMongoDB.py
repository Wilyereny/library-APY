import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
ConnectionString = os.getenv('HOST_URL')
DBName = os.getenv('DATABASE_NAME')

def getDatabase(dbName):
   
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = ConnectionString
   
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client[dbName]