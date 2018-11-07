# -*- coding: utf-8 -*-
from concurrent import futures
import socket
import time
import grpc
import sys
sys.path.append("..")
import asyncio
from Log import LogHelper_pb2,LogHelper_pb2_grpc
import json
# from celery import Celery
from CeleryConf import app
from EnumType.CommonEnum import LogLevel

@app.task(name='Log.LogHelper_Client.main')
def main(Title,Content,LogLevel):
    # print('start log')
    _channel = grpc.insecure_channel('127.0.0.1:8100')
    _client = LogHelper_pb2_grpc.LogHelperStub(_channel)
    # _hostName = socket.getfqdn(socket.gethostname())
    # _ipAddr = socket.gethostbyname(_hostName)
    _hostName = 'MyPC'
    _ipAddr = '127.0.0.1'

    _time = time.strftime('%Y-%m-%d %H:%M:%s',time.localtime())
    _outResponse = _client.WriteLog(LogHelper_pb2.InRequest(IpAddr=_ipAddr, CDate=_time, Level=LogLevelTrans(LogLevel), Title=Title, Content=Content))
    # print('end log')
    return {"Code":_outResponse.Code,"Message":_outResponse.Message,"Content":_outResponse.Content}

def FuncCallBack(future):
    # print(future.result())
    print(future.result()['Message'])

# 日志等级转换
def LogLevelTrans(Level):
    switch = {
        LogLevel.INFO.value : LogHelper_pb2.INFO,
        LogLevel.ERROR.value : LogHelper_pb2.ERROR,
        LogLevel.WARNING.value : LogHelper_pb2.WARNING
    }

    return switch[Level]

if __name__ == '__main__':
    # _future = futures.ThreadPoolExecutor(max_workers=1)
    # _task = _future.submit(main,'测试标题','测试内容').add_done_callback(FuncCallBack)

    # main()
    print(main('测试标题', '测试内容',LogLevel.INFO))