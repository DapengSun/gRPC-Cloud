# -*- coding: utf-8 -*-

import grpc
import sys
sys.path.append('..')
from SSO import SSOVerifyLogin_pb2,SSOVerifyLogin_pb2_grpc,cursor
from concurrent import futures
import time

class SSOVerifyLogin(SSOVerifyLogin_pb2_grpc.SSOVerifyLoginServicer):
    def VerifyLogin(self, request, context):
        try:
            _userName = request.UserName
            _passWord = request.PassWord

            _sql = "Select * from AccountInfo Where LoginName = '%s' and PassWord = '%s'" % (_userName,_passWord)
            cursor.execute(_sql)
            _result = cursor.fetchone()

            if _result:
                return SSOVerifyLogin_pb2.VerifyLoginResponse(Code=SSOVerifyLogin_pb2.OK, Message="登录成功", Content='')
            else:
                return SSOVerifyLogin_pb2.VerifyLoginResponse(Code=SSOVerifyLogin_pb2.Failed, Message="登录失败", Content='')
        except Exception as ee:
            return SSOVerifyLogin_pb2.VerifyLoginResponse(Code=SSOVerifyLogin_pb2.Failed, Message="登录失败", Content=ee)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    service = SSOVerifyLogin()
    SSOVerifyLogin_pb2_grpc.add_SSOVerifyLoginServicer_to_server(service,server)
    server.add_insecure_port('127.0.0.1:8102')
    server.start()

    try:
        time.sleep(10)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    main()