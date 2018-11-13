# -*- coding: utf-8 -*-

import grpc
import sys
sys.path.append('..')
from GRPCConsul import GrpcConsul_pb2,GrpcConsul_pb2_grpc
from ConsulConf import consul_resolver,ConsulHelper

def main():
    # ip, port = ConsulHelper.GetIpPort("TestConsul_server")
    channel = grpc.insecure_channel(f"127.0.0.1:8108")
    client = GrpcConsul_pb2_grpc.GrpcConsulHelperStub(channel)
    result = client.Test(GrpcConsul_pb2.Request(inString="gRPC Request"))
    print(result.outString)

if __name__ == '__main__':
    main()