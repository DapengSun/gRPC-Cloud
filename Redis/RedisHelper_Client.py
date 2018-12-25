# -*- coding: utf-8 -*-

import grpc
import sys
sys.path.append('..')
from ConsulConf import addr_ip
from Redis import RedisHelper_pb2,RedisHelper_pb2_grpc

def main():
    channel = grpc.insecure_channel(f'{addr_ip}:8107')
    client = RedisHelper_pb2_grpc.RedisHelperStub(channel)
    sql = 'select * from accountinfo'
    conn = RedisHelper_pb2.DbConnArgs(Host='localhost',User='root',PassWord='sdmp',Db='spider',Port=3306)
    res = client.GetSqlValue(RedisHelper_pb2.RedisCacheSQLRequest(SQL=sql,Expire=20,ConnArgs=conn))
    print(res)

if __name__ == '__main__':
    main()