# -*- coding: utf-8 -*-

import grpc
import sys
sys.path.append('..')
from GRPCConsul import GrpcConsul_pb2,GrpcConsul_pb2_grpc
from concurrent import futures
import time
from ConsulConf import addr_ip
from ConsulConf.ConsulHelper import Register,Unregister

class GrpcConsulHelper(GrpcConsul_pb2_grpc.GrpcConsulHelperServicer):
    def Test(self, request, context):
        return GrpcConsul_pb2.Response(outString="gRPC Server Response!")

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    service = GrpcConsulHelper()
    GrpcConsul_pb2_grpc.add_GrpcConsulHelperServicer_to_server(service,server)
    server.add_insecure_port(f'192.168.0.192:8108')
    Register('TestConsul_server',f'192.168.0.192',8108,"1")
    server.start()

    try:
        time.sleep(60)
    except KeyboardInterrupt:
        Unregister("TestConsul_server", f'192.168.0.192', 8108)
        server.stop()

if __name__ == "__main__":
    main()