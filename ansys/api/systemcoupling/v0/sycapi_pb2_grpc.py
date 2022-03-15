# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ansys.api.systemcoupling.v0.sycapi_pb2 as sycapi__pb2


class SycApiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
                '/syc.SycApi/Ping',
                request_serializer=sycapi__pb2.PingRequest.SerializeToString,
                response_deserializer=sycapi__pb2.PingResponse.FromString,
                )
        self.InvokeCommand = channel.unary_unary(
                '/syc.SycApi/InvokeCommand',
                request_serializer=sycapi__pb2.CommandRequest.SerializeToString,
                response_deserializer=sycapi__pb2.CommandResponse.FromString,
                )
        self.Quit = channel.unary_unary(
                '/syc.SycApi/Quit',
                request_serializer=sycapi__pb2.QuitRequest.SerializeToString,
                response_deserializer=sycapi__pb2.QuitResponse.FromString,
                )


class SycApiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InvokeCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Quit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SycApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=sycapi__pb2.PingRequest.FromString,
                    response_serializer=sycapi__pb2.PingResponse.SerializeToString,
            ),
            'InvokeCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.InvokeCommand,
                    request_deserializer=sycapi__pb2.CommandRequest.FromString,
                    response_serializer=sycapi__pb2.CommandResponse.SerializeToString,
            ),
            'Quit': grpc.unary_unary_rpc_method_handler(
                    servicer.Quit,
                    request_deserializer=sycapi__pb2.QuitRequest.FromString,
                    response_serializer=sycapi__pb2.QuitResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'syc.SycApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SycApi(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/syc.SycApi/Ping',
            sycapi__pb2.PingRequest.SerializeToString,
            sycapi__pb2.PingResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InvokeCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/syc.SycApi/InvokeCommand',
            sycapi__pb2.CommandRequest.SerializeToString,
            sycapi__pb2.CommandResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Quit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/syc.SycApi/Quit',
            sycapi__pb2.QuitRequest.SerializeToString,
            sycapi__pb2.QuitResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
