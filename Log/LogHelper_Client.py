# -*- coding: utf-8 -*-
import socket
import time
import grpc
import sys
sys.path.append("..")
from Log import LogHelper_pb2,LogHelper_pb2_grpc
import json
# from celery import Celery
from CeleryConf import app
from EnumType.CommonEnum import LogLevel
from ConsulConf import ConsulHelper,addr_ip
from concurrent import futures

def writeLog(client,**requestArgs):
    '''
    异步调用服务端写入日志
    :param client:客户端
    :param requestArgs:参数
    :return:
    '''
    # print(f'thread:开始写入日志')
    return client.WriteLog(LogHelper_pb2.InRequest(**requestArgs))

def resultCallBack(future):
    '''
    日志结果回调
    :param future:
    :return:
    '''
    _outResponse = future.result()
    print({"Code": _outResponse.Code, "Message": _outResponse.Message, "Content": _outResponse.Content})
    # return {"Code": _outResponse.Code, "Message": _outResponse.Message, "Content": _outResponse.Content}


@app.task(name='Log.LogHelper_Client.main')
def main(Title,Content,LogLevel):
    try:
        # print('start log')
        ip = port = None
        # ip, port = ConsulHelper.GetIpPort("Log_Server")
        if ip == None and port == None:
            ip = addr_ip
            port = 8111
        _channel = grpc.insecure_channel(f'{ip}:{port}')
        _client = LogHelper_pb2_grpc.LogHelperStub(_channel)
        # _hostName = socket.getfqdn(socket.gethostname())
        # _ipAddr = socket.gethostbyname(_hostName)
        _hostName = 'MyPC'
        _ipAddr = f'{ip}:{port}'

        _time = time.strftime('%Y-%m-%d %H:%M:%s',time.localtime())
        # 此处采用多线程concurrent.futures.ThreadPoolExecutor
        # gRPC底层已经封装了异步请求gevent

        # _outResponse = _client.WriteLog(LogHelper_pb2.InRequest(IpAddr=_ipAddr, CDate=_time, Level=LogLevelTrans(LogLevel), Title=Title, Content=Content))
        # print({"Code": _outResponse.Code, "Message": _outResponse.Message, "Content": _outResponse.Content})
        requestArgs = {'IpAddr':_ipAddr, 'CDate':_time, 'Level':LogLevelTrans(LogLevel), 'Title':Title, 'Content':Content}
        pool = futures.ThreadPoolExecutor(max_workers=5)
        pool.submit(writeLog,_client,**requestArgs).add_done_callback(resultCallBack)

        # _outResponse = tasks.result()

    except Exception as ex:
        log(f"请求异常", ex)

# 日志等级转换
def LogLevelTrans(Level):
    switch = {
        LogLevel.INFO.value : LogHelper_pb2.INFO,
        LogLevel.ERROR.value : LogHelper_pb2.ERROR,
        LogLevel.WARNING.value : LogHelper_pb2.WARNING
    }

    return switch[Level]

now = lambda : time.time()
nowTime = lambda : time.strftime('%Y-%m-%d %H:%M:%s',time.localtime())
filePath = './logClientLog.txt'

def log(title,content):
    now = nowTime()
    with open(filePath,'a+') as file:
        file.writelines(f'{now} - {title} - {content}\n')

if __name__ == '__main__':
    # _future = futures.ThreadPoolExecutor(max_workers=1)
    # _task = _future.submit(main,'测试标题','测试内容').add_done_callback(FuncCallBack)
    # main()
    start = now()
    for i in range(100):
        main('测试标题', '测试内容',LogLevel.INFO.value)
    end = now()
    # time.sleep(30)
    print(f'耗时：{end - start}s')