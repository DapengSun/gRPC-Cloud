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

def main(Title,Content):
    # print('start log')
    _channel = grpc.insecure_channel('127.0.0.1:8100')
    _client = LogHelper_pb2_grpc.LogHelperStub(_channel)
    _hostName = socket.getfqdn(socket.gethostname())
    _ipAddr = socket.gethostbyname(_hostName)

    _time = time.strftime('%Y-%m-%d %H:%M:%s',time.localtime())
    _outResponse = _client.WriteLog(LogHelper_pb2.InRequest(IpAddr=_ipAddr, CDate=_time, Level=LogHelper_pb2.ERROR, Title=Title, Content=Content))
    # print('end log')
    return {"Code":_outResponse.Code,"Message":_outResponse.Message,"Content":_outResponse.Content}

def FuncCallBack(future):
    # print(future.result())
    print(future.result()['Message'])

if __name__ == '__main__':
    # print('start')
    # _coroutine = dosomething()
    # _loop = asyncio.get_event_loop()
    # _loop.run_until_complete(_coroutine)
    # _loop.close()
    # print('end')

    _future = futures.ThreadPoolExecutor(max_workers=1)
    _task = _future.submit(main,'测试标题','测试内容').add_done_callback(FuncCallBack)

    # main('测试标题', '测试内容')