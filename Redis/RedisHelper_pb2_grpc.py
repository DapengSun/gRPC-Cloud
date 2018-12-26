# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
import sys
sys.path.append('..')
from Redis import RedisHelper_pb2 as RedisHelper__pb2

class RedisHelperStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RedisCacheStr = channel.unary_unary(
        '/RedisHelper/RedisCacheStr',
        request_serializer=RedisHelper__pb2.RedisCacheRequest.SerializeToString,
        response_deserializer=RedisHelper__pb2.RedisCacheResponse.FromString,
        )
    self.RedisCacheList = channel.unary_unary(
        '/RedisHelper/RedisCacheList',
        request_serializer=RedisHelper__pb2.RedisCacheRequest.SerializeToString,
        response_deserializer=RedisHelper__pb2.RedisCacheResponse.FromString,
        )
    self.RedisCacheHash = channel.unary_unary(
        '/RedisHelper/RedisCacheHash',
        request_serializer=RedisHelper__pb2.RedisCacheHashRequest.SerializeToString,
        response_deserializer=RedisHelper__pb2.RedisCacheResponse.FromString,
        )
    self.RedisCacheHashMapping = channel.unary_unary(
        '/RedisHelper/RedisCacheHashMapping',
        request_serializer=RedisHelper__pb2.RedisCacheHashMappingRequest.SerializeToString,
        response_deserializer=RedisHelper__pb2.RedisCacheResponse.FromString,
        )
    self.GetSqlValue = channel.unary_unary(
        '/RedisHelper/GetSqlValue',
        request_serializer=RedisHelper__pb2.RedisCacheSQLRequest.SerializeToString,
        response_deserializer=RedisHelper__pb2.RedisCacheResponse.FromString,
        )


class RedisHelperServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RedisCacheStr(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RedisCacheList(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RedisCacheHash(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RedisCacheHashMapping(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetSqlValue(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_RedisHelperServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RedisCacheStr': grpc.unary_unary_rpc_method_handler(
          servicer.RedisCacheStr,
          request_deserializer=RedisHelper__pb2.RedisCacheRequest.FromString,
          response_serializer=RedisHelper__pb2.RedisCacheResponse.SerializeToString,
      ),
      'RedisCacheList': grpc.unary_unary_rpc_method_handler(
          servicer.RedisCacheList,
          request_deserializer=RedisHelper__pb2.RedisCacheRequest.FromString,
          response_serializer=RedisHelper__pb2.RedisCacheResponse.SerializeToString,
      ),
      'RedisCacheHash': grpc.unary_unary_rpc_method_handler(
          servicer.RedisCacheHash,
          request_deserializer=RedisHelper__pb2.RedisCacheHashRequest.FromString,
          response_serializer=RedisHelper__pb2.RedisCacheResponse.SerializeToString,
      ),
      'RedisCacheHashMapping': grpc.unary_unary_rpc_method_handler(
          servicer.RedisCacheHashMapping,
          request_deserializer=RedisHelper__pb2.RedisCacheHashMappingRequest.FromString,
          response_serializer=RedisHelper__pb2.RedisCacheResponse.SerializeToString,
      ),
      'GetSqlValue': grpc.unary_unary_rpc_method_handler(
          servicer.GetSqlValue,
          request_deserializer=RedisHelper__pb2.RedisCacheSQLRequest.FromString,
          response_serializer=RedisHelper__pb2.RedisCacheResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'RedisHelper', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
