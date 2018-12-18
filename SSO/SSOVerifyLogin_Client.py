# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
import grpc
from SSO import SSOVerifyLogin_pb2,SSOVerifyLogin_pb2_grpc
from CeleryConf import app

@app.task
def main(UserName,PassWord):
    _channel = grpc.insecure_channel('192.168.7.151:8106')
    _client = SSOVerifyLogin_pb2_grpc.SSOVerifyLoginStub(_channel)
    _outResponse = _client.VerifyLogin(SSOVerifyLogin_pb2.VerifyLoginRequest(UserName=UserName,PassWord=''))
    return {"Code": _outResponse.Code, "Message": _outResponse.Message, "Content": _outResponse.Content}

if __name__ == '__main__':
    print(main('13520387252','123456'))