# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc
import sys
sys.path.append('..')
from SSO import SSOVerifyUrl_pb2 as SSOVerifyUrl__pb2


class SSOVerifyUrlStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.VerifyUrl = channel.unary_unary(
        '/SSOVerifyUrl/VerifyUrl',
        request_serializer=SSOVerifyUrl__pb2.VerifyInRequest.SerializeToString,
        response_deserializer=SSOVerifyUrl__pb2.VerifyOutResponse.FromString,
        )


class SSOVerifyUrlServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def VerifyUrl(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SSOVerifyUrlServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'VerifyUrl': grpc.unary_unary_rpc_method_handler(
          servicer.VerifyUrl,
          request_deserializer=SSOVerifyUrl__pb2.VerifyInRequest.FromString,
          response_serializer=SSOVerifyUrl__pb2.VerifyOutResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'SSOVerifyUrl', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
