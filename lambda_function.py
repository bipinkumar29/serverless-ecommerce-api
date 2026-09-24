import os
import pymysql
import json

# Credentials ab safely Environment Variables se fetch honge
DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')

def lambda_handler(event, context):
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            connect_timeout=5
        )
        return {"statusCode": 200, "body": json.dumps("Database connected securely!")}
    except Exception as e:
        return {"statusCode": 500, "body": json.dumps("Connection failed")}
