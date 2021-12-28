# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: management/ManagementCompat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Common_pb2 as common_dot_Common__pb2
from ..management import Management_pb2 as management_dot_Management__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='management/ManagementCompat.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n6org.apache.skywalking.apm.network.management.v3.compatP\001Z6skywalking.apache.org/repo/goapi/collect/management/v3\270\001\001\252\002\035SkyWalking.NetworkProtocol.V3',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!management/ManagementCompat.proto\x1a\x13\x63ommon/Common.proto\x1a\x1bmanagement/Management.proto2\xb5\x01\n\x11ManagementService\x12X\n\x18reportInstanceProperties\x12!.skywalking.v3.InstanceProperties\x1a\x17.skywalking.v3.Commands\"\x00\x12\x46\n\tkeepAlive\x12\x1e.skywalking.v3.InstancePingPkg\x1a\x17.skywalking.v3.Commands\"\x00\x42\x95\x01\n6org.apache.skywalking.apm.network.management.v3.compatP\x01Z6skywalking.apache.org/repo/goapi/collect/management/v3\xb8\x01\x01\xaa\x02\x1dSkyWalking.NetworkProtocol.V3b\x06proto3'
  ,
  dependencies=[common_dot_Common__pb2.DESCRIPTOR,management_dot_Management__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_MANAGEMENTSERVICE = _descriptor.ServiceDescriptor(
  name='ManagementService',
  full_name='ManagementService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=88,
  serialized_end=269,
  methods=[
  _descriptor.MethodDescriptor(
    name='reportInstanceProperties',
    full_name='ManagementService.reportInstanceProperties',
    index=0,
    containing_service=None,
    input_type=management_dot_Management__pb2._INSTANCEPROPERTIES,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='keepAlive',
    full_name='ManagementService.keepAlive',
    index=1,
    containing_service=None,
    input_type=management_dot_Management__pb2._INSTANCEPINGPKG,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MANAGEMENTSERVICE)

DESCRIPTOR.services_by_name['ManagementService'] = _MANAGEMENTSERVICE

# @@protoc_insertion_point(module_scope)
