# -*- coding: utf-8 -*-

import grpc
import time
import sys
sys.path.append("..")
from concurrent import futures
from Log import LogHelper_pb2,LogHelper_pb2_grpc
from RedisOper import oper
from Common.CommonHelper import Tool
from ConsulConf.ConsulHelper import Register,Unregister
from ConsulConf import addr_ip

class LogHelper(LogHelper_pb2_grpc.LogHelperServicer):
    def WriteLog(self, request, context):
        try:
            _ip = request.IpAddr
            _cDate = request.CDate
            _level = LogHelper_pb2.LogLevel.keys()[request.Level]
            _title = request.Title
            _content = request.Content
            _logId = Tool.GetGuid()
            oper.hashHmset(_logId,{"IpAddr":_ip,"CDate":_cDate,"Level":_level,"Title":_title,"Content":_content})
            return LogHelper_pb2.OutResponse(Code=200,Message="日志记录成功",Content="")
        except Exception as ex:
            return LogHelper_pb2.OutResponse(Code=500,Message="日志记录异常",Content="")

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    service = LogHelper()
    LogHelper_pb2_grpc.add_LogHelperServicer_to_server(service,server)
    server.add_insecure_port(f'{addr_ip}:8111')
    # 192.168.0.192
    Register('Log_Server',f'{addr_ip}',8111,"1")
    server.start()

    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        Unregister("Log_Server", f"{addr_ip}", 8111)
        server.stop(0)

if __name__ == '__main__':
    main()