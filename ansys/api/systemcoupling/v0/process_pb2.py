# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: process.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='process.proto',
  package='ansys.api.systemcoupling.v0',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rprocess.proto\x12\x1b\x61nsys.api.systemcoupling.v0\"\r\n\x0bPingRequest\"\x0e\n\x0cPingResponse\"\r\n\x0bQuitRequest\"\x0e\n\x0cQuitResponse2\xc7\x01\n\x07Process\x12]\n\x04Ping\x12(.ansys.api.systemcoupling.v0.PingRequest\x1a).ansys.api.systemcoupling.v0.PingResponse\"\x00\x12]\n\x04Quit\x12(.ansys.api.systemcoupling.v0.QuitRequest\x1a).ansys.api.systemcoupling.v0.QuitResponse\"\x00\x62\x06proto3'
)




_PINGREQUEST = _descriptor.Descriptor(
  name='PingRequest',
  full_name='ansys.api.systemcoupling.v0.PingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=46,
  serialized_end=59,
)


_PINGRESPONSE = _descriptor.Descriptor(
  name='PingResponse',
  full_name='ansys.api.systemcoupling.v0.PingResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=75,
)


_QUITREQUEST = _descriptor.Descriptor(
  name='QuitRequest',
  full_name='ansys.api.systemcoupling.v0.QuitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=90,
)


_QUITRESPONSE = _descriptor.Descriptor(
  name='QuitResponse',
  full_name='ansys.api.systemcoupling.v0.QuitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=106,
)

DESCRIPTOR.message_types_by_name['PingRequest'] = _PINGREQUEST
DESCRIPTOR.message_types_by_name['PingResponse'] = _PINGRESPONSE
DESCRIPTOR.message_types_by_name['QuitRequest'] = _QUITREQUEST
DESCRIPTOR.message_types_by_name['QuitResponse'] = _QUITRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PingRequest = _reflection.GeneratedProtocolMessageType('PingRequest', (_message.Message,), {
  'DESCRIPTOR' : _PINGREQUEST,
  '__module__' : 'process_pb2'
  # @@protoc_insertion_point(class_scope:ansys.api.systemcoupling.v0.PingRequest)
  })
_sym_db.RegisterMessage(PingRequest)

PingResponse = _reflection.GeneratedProtocolMessageType('PingResponse', (_message.Message,), {
  'DESCRIPTOR' : _PINGRESPONSE,
  '__module__' : 'process_pb2'
  # @@protoc_insertion_point(class_scope:ansys.api.systemcoupling.v0.PingResponse)
  })
_sym_db.RegisterMessage(PingResponse)

QuitRequest = _reflection.GeneratedProtocolMessageType('QuitRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUITREQUEST,
  '__module__' : 'process_pb2'
  # @@protoc_insertion_point(class_scope:ansys.api.systemcoupling.v0.QuitRequest)
  })
_sym_db.RegisterMessage(QuitRequest)

QuitResponse = _reflection.GeneratedProtocolMessageType('QuitResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUITRESPONSE,
  '__module__' : 'process_pb2'
  # @@protoc_insertion_point(class_scope:ansys.api.systemcoupling.v0.QuitResponse)
  })
_sym_db.RegisterMessage(QuitResponse)



_PROCESS = _descriptor.ServiceDescriptor(
  name='Process',
  full_name='ansys.api.systemcoupling.v0.Process',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=109,
  serialized_end=308,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='ansys.api.systemcoupling.v0.Process.Ping',
    index=0,
    containing_service=None,
    input_type=_PINGREQUEST,
    output_type=_PINGRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Quit',
    full_name='ansys.api.systemcoupling.v0.Process.Quit',
    index=1,
    containing_service=None,
    input_type=_QUITREQUEST,
    output_type=_QUITRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROCESS)

DESCRIPTOR.services_by_name['Process'] = _PROCESS

# @@protoc_insertion_point(module_scope)
