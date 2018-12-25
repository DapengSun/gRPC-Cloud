# -*- coding: utf-8 -*-
import json
import sys
sys.path.append('..')
import grpc
import threading
from Common.FlaskHelper import tool,responseStatus
from Log import LogHelper_Client
import time
from flask import Flask, request, Blueprint, jsonify
from concurrent import futures
from Log import LogHelper_pb2,LogHelper_pb2_grpc
from ConsulConf import addr_ip
from EnumType.CommonEnum import LogLevel

logModule = Blueprint('logModule',__name__)

nowTime = lambda : time.strftime('%Y-%m-%d %H:%M:%s',time.localtime())

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

@logModule.route('/write',methods=['GET','POST'])
def Log():
    try:
        data = request.get_data()
        if data == None:
            raise Exception('参数为空')
        jsonData = json.loads(data)

        # 获取参数
        title = jsonData.get('Title',None)
        content = jsonData.get('Content',None)
        logLevel = jsonData.get('LogLevel',None)
        if not (title and content and logLevel):
            raise Exception('参数有误')

        ip = port = None
        if ip == None and port == None:
            ip = addr_ip
            port = 8111
        _channel = grpc.insecure_channel(f'{ip}:{port}')
        _client = LogHelper_pb2_grpc.LogHelperStub(_channel)
        _hostName = 'MyPC'
        _ipAddr = f'{ip}:{port}'

        # 判断logLevel是否在范围内
        logLevel = int(logLevel)
        levelList = [0, 1, 2]
        isLogLevel = lambda x: x in levelList
        if(isLogLevel(logLevel)):
            requestArgs = {'IpAddr': _ipAddr, 'CDate': nowTime(), 'Level': LogLevelTrans(logLevel), 'Title': title,
                           'Content': content}
            pool = futures.ThreadPoolExecutor(max_workers=5)
            pool.submit(writeLog, _client, **requestArgs).add_done_callback(resultCallBack)
            return tool.jsonResult(responseStatus.Ok, '日志记录成功！', '')
        else:
            return tool.jsonResult(responseStatus.Error,'日志等级异常！','')
    except Exception as ex:
        log('异常记录', ex)
        return tool.jsonResult(responseStatus.Error,ex, '')


@logModule.route('/',methods=['GET'])
def Test():
    """
    @@@
    #### example
        import requests
        url='http://127.0.0.1:5000/api/get_something'
        try:
            print requests.get(url).text
        except:
            pass
    @@@
    """
    # log('测试主题','测试内容')
    return jsonify({'platform': 'get something'})

filePath = './Log.txt'
def log(title,content):
    '''
    本地日志记录
    :param title:标题
    :param content:内容
    :return:
    '''
    now = nowTime()
    with open(filePath,'a+') as file:
        file.writelines(f'{now} - {title} - {content}\n')

def LogLevelTrans(Level):
    '''
    日志等级转换
    :param Level:
    :return:
    '''
    switch = {
        LogLevel.INFO.value : LogHelper_pb2.INFO,
        LogLevel.ERROR.value : LogHelper_pb2.ERROR,
        LogLevel.WARNING.value : LogHelper_pb2.WARNING
    }

    return switch[Level]
