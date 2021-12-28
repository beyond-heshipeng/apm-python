# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service-mesh-probe/service-mesh-compat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..service_mesh_probe import service_mesh_pb2 as service__mesh__probe_dot_service__mesh__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='service-mesh-probe/service-mesh-compat.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n7org.apache.skywalking.apm.network.servicemesh.v3.compatP\001Z7skywalking.apache.org/repo/goapi/collect/servicemesh/v3\270\001\001\252\002\035SkyWalking.NetworkProtocol.V3',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n,service-mesh-probe/service-mesh-compat.proto\x1a%service-mesh-probe/service-mesh.proto2o\n\x18ServiceMeshMetricService\x12S\n\x07\x63ollect\x12 .skywalking.v3.ServiceMeshMetric\x1a\".skywalking.v3.MeshProbeDownstream\"\x00(\x01\x42\x97\x01\n7org.apache.skywalking.apm.network.servicemesh.v3.compatP\x01Z7skywalking.apache.org/repo/goapi/collect/servicemesh/v3\xb8\x01\x01\xaa\x02\x1dSkyWalking.NetworkProtocol.V3b\x06proto3'
  ,
  dependencies=[service__mesh__probe_dot_service__mesh__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_SERVICEMESHMETRICSERVICE = _descriptor.ServiceDescriptor(
  name='ServiceMeshMetricService',
  full_name='ServiceMeshMetricService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=87,
  serialized_end=198,
  methods=[
  _descriptor.MethodDescriptor(
    name='collect',
    full_name='ServiceMeshMetricService.collect',
    index=0,
    containing_service=None,
    input_type=service__mesh__probe_dot_service__mesh__pb2._SERVICEMESHMETRIC,
    output_type=service__mesh__probe_dot_service__mesh__pb2._MESHPROBEDOWNSTREAM,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICEMESHMETRICSERVICE)

DESCRIPTOR.services_by_name['ServiceMeshMetricService'] = _SERVICEMESHMETRICSERVICE

# @@protoc_insertion_point(module_scope)
