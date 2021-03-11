# 여러 문서 읽기


from pymongo import MongoClient
from datetime import datetime
import random

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

rows = sensors_col.find()

for x in rows:
    print(x)
