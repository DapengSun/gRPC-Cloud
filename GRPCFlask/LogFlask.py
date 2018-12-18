# -*- coding: utf-8 -*-
import json
import sys
import threading

sys.path.append('..')
from Common.FlaskHelper import tool,responseStatus
from Log import LogHelper_Client
import time
from flask import Flask, request, Blueprint, jsonify
from concurrent import futures

logModule = Blueprint('logModule',__name__)

@logModule.route('/write',methods=['GET','POST'])
def Log():
    try:
        data = request.get_data()
        if data == None:
            raise Exception('参数为空')
        jsonData = json.loads(data)

        title = jsonData.get('Title',None)
        content = jsonData.get('Content',None)
        logLevel = jsonData.get('LogLevel',None)
        if not (title and content and logLevel):
            raise Exception('参数有误')
        logLevel = int(logLevel)

        levelList = [0, 1, 2]
        isLogLevel = lambda x: x in levelList
        if(isLogLevel(logLevel)):
            threadPool = futures.ThreadPoolExecutor(max_workers=5)
            task = threadPool.submit(LogHelper_Client.main,title,content,logLevel)
            logResult = task.result()
            if (logResult['Code'] == 200):
                return tool.jsonResult(responseStatus.Ok, '日志记录成功！', '')
            else:
                return tool.jsonResult(responseStatus.Error, '日志记录失败！', logResult['Message'])
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

nowTime = lambda : time.strftime('%Y-%m-%d %H:%M:%s',time.localtime())
filePath = './Log.txt'

def log(title,content):
    now = nowTime()
    with open(filePath,'a+') as file:
        file.writelines(f'{now} - {title} - {content}\n')

# if __name__ == '__main__':
#     app.run()