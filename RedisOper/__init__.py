# coding:utf-8
import redis
from RedisOper.RedisOperHelper import RedisOperHelper

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True,db=6)
db = redis.Redis(connection_pool=pool)
oper = RedisOperHelper(db)
