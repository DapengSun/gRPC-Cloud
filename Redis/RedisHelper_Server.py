# -*- coding: utf-8 -*-
import json
import time
import grpc
import sys
sys.path.append('..')
from concurrent import futures
from Redis import RedisHelper_pb2,RedisHelper_pb2_grpc
from ConsulConf import addr_ip
from RedisOper import oper

class RedisHelper(RedisHelper_pb2_grpc.RedisHelperServicer):
    def RedisCacheStr(self, request, context):
        '''
        缓存str值入redis
        :param request:请求对象
        :param context:上下文
        :return:缓存结果
        '''
        try:
            key = request.Key
            value = request.Value
            expire = request.Expire

            if key == None or value == None:
                raise Exception('参数异常')

            oper.strSet(key,value)
            if expire != 0:
                oper.setKeyExpires(key,expire)
            return RedisHelper_pb2.RedisCacheResponse(Code=200,Message="缓存Redis值成功！",Content="")
        except Exception as ex:
            return RedisHelper_pb2.RedisCacheResponse(Code=500,Message=f'缓存Redis值异常:{ex}',Content="")

    def RedisCacheList(self, request, context):
        '''
        缓存List值入redis
        :param request:请求对象
        :param context:上下文
        :return:缓存结果
        '''
        try:
            key = request.Key
            value = request.Value
            expire = request.Expire

            if key == None or value == None:
                raise Exception('参数异常')

            oper.queuePut(key,value)
            if expire != 0:
                oper.setKeyExpires(key,expire)
            return RedisHelper_pb2.RedisCacheResponse(Code=200,Message="缓存Redis List值成功！",Content="")
        except Exception as ex:
            return RedisHelper_pb2.RedisCacheResponse(Code=500,Message=f'缓存Redis List值异常:{ex}',Content="")

    def RedisCacheHash(self, request, context):
        '''
        缓存Hash值入redis
        :param request:请求对象
        :param context:上下文
        :return:缓存结果
        '''
        try:
            key = request.Key
            value = request.Value
            name = request.Name
            expire = request.Expire

            if key == None or value == None:
                raise Exception('参数异常')

            oper.hashHset(key,name,value)
            if expire != 0:
                oper.setKeyExpires(key,expire)
            return RedisHelper_pb2.RedisCacheResponse(Code=200,Message="缓存Redis Hash值成功！",Content="")
        except Exception as ex:
            return RedisHelper_pb2.RedisCacheResponse(Code=500,Message=f'缓存Redis Hash值异常:{ex}',Content="")

    def RedisCacheHashMapping(self, request, context):
        '''
        缓存Hash Mapping值入redis
        :param request:请求对象 Mapping-JSON格式的Dict类型数据
        :param context:上下文
        :return:缓存结果
        '''
        try:
            key = request.Key
            mappingJson = request.Mapping
            expire = request.Expire

            if key == None or mappingJson == None:
                raise Exception('参数异常')

            mapping = json.loads(mappingJson)
            oper.hashHmset(key,mapping)
            if expire != 0:
                oper.setKeyExpires(key,expire)
            return RedisHelper_pb2.RedisCacheResponse(Code=200,Message="缓存Redis Hash值成功！",Content="")
        except Exception as ex:
            return RedisHelper_pb2.RedisCacheResponse(Code=500,Message=f'缓存Redis Hash值异常:{ex}',Content="")

    def GetSqlValue(self, request, context):
        '''
        获取SQL值并缓存结果
        :param request:请求对象
        :param context:上下文
        :return:缓存结果
        '''
        try:
            sql = request.SQL
            expire = request.Expire
            conn = request.ConnArgs

            if sql == None or conn == None:
                raise Exception('参数异常')

            dbArgs = {'host': conn.Host, 'user': conn.User, 'password': conn.PassWord, 'db': conn.Db, 'port': conn.Port}
            # dbArgs = conn['args']
            res = oper.getSqlVal(sql,expire,**dbArgs)
            return RedisHelper_pb2.RedisCacheResponse(Code=200, Message="缓存Redis值成功！", Content=f"{res}")
        except Exception as ex:
            return RedisHelper_pb2.RedisCacheResponse(Code=500, Message=f'获取缓存SQL值异常:{ex}', Content="")

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    service = RedisHelper()
    RedisHelper_pb2_grpc.add_RedisHelperServicer_to_server(service,server)
    server.add_insecure_port(f'{addr_ip}:8107')
    server.start()

    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    main()