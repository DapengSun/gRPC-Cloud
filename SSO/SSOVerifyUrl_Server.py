# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
import grpc
import time
from SSO import SSOVerifyUrl_pb2,SSOVerifyUrl_pb2_grpc,cursor
from concurrent import futures
from SSO import Config
from ConsulConf.ConsulHelper import Register,Unregister
from ConsulConf import addr_ip

class SSOVerifyUrl(SSOVerifyUrl_pb2_grpc.SSOVerifyUrlServicer):
    def VerifyUrl(self, request, context):
        try:
            _responseUrl = str.join('',[Config.VerifyLoginUrl, '?requesturl=', request.RequestUrl])
            if request.TicketId is not None and request.TicketId != '':
                _sql = "Select * from TicketInfo Where TicketId = '%s'" % (request.TicketId)
                cursor.execute(_sql)
                _tickinfo = cursor.fetchone()

                if _tickinfo is not None:
                    return SSOVerifyUrl_pb2.VerifyOutResponse(Code=200, Message="验证成功", Content=request.TicketId)
                else:
                    return SSOVerifyUrl_pb2.VerifyOutResponse(Code=500, Message="验证失败", Content=_responseUrl)
            else:
                return SSOVerifyUrl_pb2.VerifyOutResponse(Code=500,Message="验证失败",Content=_responseUrl)
        except Exception as ex:
            return SSOVerifyUrl_pb2.VerifyOutResponse(Code=500,Message="验证异常",Content=_responseUrl)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    service = SSOVerifyUrl()
    SSOVerifyUrl_pb2_grpc.add_SSOVerifyUrlServicer_to_server(service,server)
    server.add_insecure_port(f"{addr_ip}:8105")
    Register('VerifyUrl_Server',f'{addr_ip}',8105,"3")
    server.start()

    try:
        # time.sleep(10)
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        Unregister("VerifyUrl_Server", f"{addr_ip}", 8105)
        server.stop(0)

if __name__ == '__main__':
    main()