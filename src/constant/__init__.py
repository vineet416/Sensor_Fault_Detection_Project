import os


AWS_S3_BUCKET_NAME = "sensor-fault"
MONGO_DATABASE_NAME = "sensor_data"
MONGO_COLLECTION_NAME = "sensor_fault"


TARGET_COLUMN = "quality"
MONGO_DB_URL = "mongodb://localhost:27017/sensor_data"


MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"