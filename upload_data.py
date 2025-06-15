from pymongo.mongo_client import MongoClient
import pandas as pd
import json


## MongoDB url 
url = "mongodb+srv://vineet:12345@cluster0.j5weyqm.mongodb.net/?retryWrites=true&w=majority"

## Create new client and connect to server
client = MongoClient(url)

## Create Database name and Collection name
MONGO_DATABASE_NAME="sensor_database"
MONGO_COLLECTION_NAME = "sensor_data"

## Load dataset into pandas dataframe
df = pd.read_csv(r"H:\My Drive\Data Science Projects\Sensor Fault Detection\notebooks\wafer_23012020_041211.csv")

## Drop unwanted column
df.drop("Unnamed: 0", axis=1, inplace = True)

## Convert pandas dataframe into a list of json records
json_record=list(json.loads(df.T.to_json()).values())

## Upload data into MongoDB collection
client[MONGO_DATABASE_NAME][MONGO_COLLECTION_NAME].insert_many(json_record)