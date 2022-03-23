# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ansys.api.systemcoupling.v0.command_pb2 as command__pb2


class CommandStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InvokeCommand = channel.unary_unary(
                '/syc.Command/InvokeCommand',
                request_serializer=command__pb2.CommandRequest.SerializeToString,
                response_deserializer=command__pb2.CommandResponse.FromString,
                )


class CommandServicer(object):
    """Missing associated documentation comment in .proto file."""

    def InvokeCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CommandServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'InvokeCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.InvokeCommand,
                    request_deserializer=command__pb2.CommandRequest.FromString,
                    response_serializer=command__pb2.CommandResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'syc.Command', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Command(object):
    """Missing associated documentation comment in .proto file."""

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
        return grpc.experimental.unary_unary(request, target, '/syc.Command/InvokeCommand',
            command__pb2.CommandRequest.SerializeToString,
            command__pb2.CommandResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
