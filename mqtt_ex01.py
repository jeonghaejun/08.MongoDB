from pymongo import MongoClient
from datetime import datetime
from mqtt_sub import subscribe

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']  # 데이터베이스 선택, 없으면 자동 생성
sensors_col = iot_db['sensors']    # 컬렉션 선택, 없으면 자동 생성


def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")  # byte 데이터를 utf-8 문자열로 변환
    print(msg.topic+" "+msg.payload)

    sensor_value = {
        "topic": msg.topic,
        "value": float(msg.payload),
        "reg_date": datetime.now()  # 현재 시간
    }
    sensors_col.insert_one(sensor_value)


subscribe('localhost', 'user1/home/#', on_message)
