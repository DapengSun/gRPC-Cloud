# -*- coding: utf-8 -*-

import grpc
import sys
sys.path.append('..')
from SSO import SSOVerifyUrl_pb2,SSOVerifyUrl_pb2_grpc
from CeleryConf import app

@app.task
def main(RequestUrl,TicketId):
    _channel = grpc.insecure_channel('127.0.0.1:8105')
    _client = SSOVerifyUrl_pb2_grpc.SSOVerifyUrlStub(_channel)
    _outResponse = _client.VerifyUrl(SSOVerifyUrl_pb2.VerifyInRequest(RequestUrl=RequestUrl, TicketId=TicketId))
    return {"Code":_outResponse.Code,"Message":_outResponse.Message,"Content":_outResponse.Content}

if __name__ == '__main__':
    # print(main('https://www.qq.com','adf84108d85211e89864559b0a5fbe9b'))
    print(main('https://www.qq.com', 'adf84108d85211e89864559b0a5fbe9b'))