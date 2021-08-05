import os
import json
import pickle

from starlette.config import Config


config = Config(".env")


SERVICE_NAME = config("SERVICE_NAME")


# **DATABASE SETTINGS
DB_NAME: str = config("DB_NAME", default="")
DB_HOST: str = config("DB_HOST", default="")
DB_PORT: int = config("DB_PORT", cast=int, default=3306)
DB_USER: str = config("DB_USER", default="")
DB_PASSWORD: str = config("DB_PASSWORD", default="")
POOL_SIZE: int = config("POOL_SIZE", cast=int, default=5)
 
 
# # **API
# API_TAM_TINH: str = config("API_TAM_TINH")

# # **KAFKA SETTINGS
# KAFKA_BROKERS = config("KAFKA_BROKERS").split(",")
# UPDATE_TIEN_TAM_TINH_BY_MA_KHANG_TOPIC_NAME = config("UPDATE_TIEN_TAM_TINH_BY_MA_KHANG_TOPIC_NAME")
# UPDATE_TIEN_TAM_TINH_BY_MA_KHANG_GROUP_ID = config("UPDATE_TIEN_TAM_TINH_BY_MA_KHANG_GROUP_ID")
# UPDATE_DOXA_BY_RANGE_DAY_TOPIC_NAME = config("UPDATE_DOXA_BY_RANGE_DAY_TOPIC_NAME")
# RECOMMENDATION_TOPIC_NAME = config("RECOMMENDATION_TOPIC_NAME")

# JSON_DESERIALIZER = lambda m: json.loads(m.decode('utf-8'))
# JSON_SERIALIZER = lambda m: json.dumps(m).encode('utf-8')
# PICKLE_DESERIALIZER = lambda m:pickle.loads(m) 
# PICKLE_SERIALIZER = lambda m:pickle.dumps(m)
# UTF8_DESERIALIZER = lambda m:m.decode("utf-8") 


# # **LOG SETTINGS
# LOG_LOCATION: str = config("LOG_LOCATION", default=os.path.join(os.getcwd(), "src/log"))  
# LOG_FILE: str = config("LOG_FILE", default="capnhat_tamtinh_log")