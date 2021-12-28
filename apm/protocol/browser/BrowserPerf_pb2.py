# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: browser/BrowserPerf.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Common_pb2 as common_dot_Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='browser/BrowserPerf.proto',
  package='skywalking.v3',
  syntax='proto3',
  serialized_options=b'\n3org.apache.skywalking.apm.network.language.agent.v3P\001Z:skywalking.apache.org/repo/goapi/collect/language/agent/v3\252\002\035SkyWalking.NetworkProtocol.V3',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19\x62rowser/BrowserPerf.proto\x12\rskywalking.v3\x1a\x13\x63ommon/Common.proto\"\xe8\x02\n\x0f\x42rowserPerfData\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x16\n\x0eserviceVersion\x18\x02 \x01(\t\x12\x0c\n\x04time\x18\x03 \x01(\x03\x12\x10\n\x08pagePath\x18\x04 \x01(\t\x12\x14\n\x0credirectTime\x18\x05 \x01(\x05\x12\x0f\n\x07\x64nsTime\x18\x06 \x01(\x05\x12\x10\n\x08ttfbTime\x18\x07 \x01(\x05\x12\x0f\n\x07tcpTime\x18\x08 \x01(\x05\x12\x11\n\ttransTime\x18\t \x01(\x05\x12\x17\n\x0f\x64omAnalysisTime\x18\n \x01(\x05\x12\x0f\n\x07\x66ptTime\x18\x0b \x01(\x05\x12\x14\n\x0c\x64omReadyTime\x18\x0c \x01(\x05\x12\x14\n\x0cloadPageTime\x18\r \x01(\x05\x12\x0f\n\x07resTime\x18\x0e \x01(\x05\x12\x0f\n\x07sslTime\x18\x0f \x01(\x05\x12\x0f\n\x07ttlTime\x18\x10 \x01(\x05\x12\x15\n\rfirstPackTime\x18\x11 \x01(\x05\x12\x0f\n\x07\x66mpTime\x18\x12 \x01(\x05\"\x94\x02\n\x0f\x42rowserErrorLog\x12\x10\n\x08uniqueId\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x16\n\x0eserviceVersion\x18\x03 \x01(\t\x12\x0c\n\x04time\x18\x04 \x01(\x03\x12\x10\n\x08pagePath\x18\x05 \x01(\t\x12.\n\x08\x63\x61tegory\x18\x06 \x01(\x0e\x32\x1c.skywalking.v3.ErrorCategory\x12\r\n\x05grade\x18\x07 \x01(\t\x12\x0f\n\x07message\x18\x08 \x01(\t\x12\x0c\n\x04line\x18\t \x01(\x05\x12\x0b\n\x03\x63ol\x18\n \x01(\x05\x12\r\n\x05stack\x18\x0b \x01(\t\x12\x10\n\x08\x65rrorUrl\x18\x0c \x01(\t\x12\x1a\n\x12\x66irstReportedError\x18\r \x01(\x08*R\n\rErrorCategory\x12\x08\n\x04\x61jax\x10\x00\x12\x0c\n\x08resource\x10\x01\x12\x07\n\x03vue\x10\x02\x12\x0b\n\x07promise\x10\x03\x12\x06\n\x02js\x10\x04\x12\x0b\n\x07unknown\x10\x05\x32\xb3\x01\n\x12\x42rowserPerfService\x12L\n\x0f\x63ollectPerfData\x12\x1e.skywalking.v3.BrowserPerfData\x1a\x17.skywalking.v3.Commands\"\x00\x12O\n\x10\x63ollectErrorLogs\x12\x1e.skywalking.v3.BrowserErrorLog\x1a\x17.skywalking.v3.Commands\"\x00(\x01\x42\x93\x01\n3org.apache.skywalking.apm.network.language.agent.v3P\x01Z:skywalking.apache.org/repo/goapi/collect/language/agent/v3\xaa\x02\x1dSkyWalking.NetworkProtocol.V3b\x06proto3'
  ,
  dependencies=[common_dot_Common__pb2.DESCRIPTOR,])

_ERRORCATEGORY = _descriptor.EnumDescriptor(
  name='ErrorCategory',
  full_name='skywalking.v3.ErrorCategory',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ajax', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='resource', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='vue', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='promise', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='js', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='unknown', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=707,
  serialized_end=789,
)
_sym_db.RegisterEnumDescriptor(_ERRORCATEGORY)

ErrorCategory = enum_type_wrapper.EnumTypeWrapper(_ERRORCATEGORY)
ajax = 0
resource = 1
vue = 2
promise = 3
js = 4
unknown = 5



_BROWSERPERFDATA = _descriptor.Descriptor(
  name='BrowserPerfData',
  full_name='skywalking.v3.BrowserPerfData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='skywalking.v3.BrowserPerfData.service', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceVersion', full_name='skywalking.v3.BrowserPerfData.serviceVersion', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='skywalking.v3.BrowserPerfData.time', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagePath', full_name='skywalking.v3.BrowserPerfData.pagePath', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='redirectTime', full_name='skywalking.v3.BrowserPerfData.redirectTime', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dnsTime', full_name='skywalking.v3.BrowserPerfData.dnsTime', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ttfbTime', full_name='skywalking.v3.BrowserPerfData.ttfbTime', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tcpTime', full_name='skywalking.v3.BrowserPerfData.tcpTime', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transTime', full_name='skywalking.v3.BrowserPerfData.transTime', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domAnalysisTime', full_name='skywalking.v3.BrowserPerfData.domAnalysisTime', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fptTime', full_name='skywalking.v3.BrowserPerfData.fptTime', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domReadyTime', full_name='skywalking.v3.BrowserPerfData.domReadyTime', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='loadPageTime', full_name='skywalking.v3.BrowserPerfData.loadPageTime', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='resTime', full_name='skywalking.v3.BrowserPerfData.resTime', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sslTime', full_name='skywalking.v3.BrowserPerfData.sslTime', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ttlTime', full_name='skywalking.v3.BrowserPerfData.ttlTime', index=15,
      number=16, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='firstPackTime', full_name='skywalking.v3.BrowserPerfData.firstPackTime', index=16,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fmpTime', full_name='skywalking.v3.BrowserPerfData.fmpTime', index=17,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=66,
  serialized_end=426,
)


_BROWSERERRORLOG = _descriptor.Descriptor(
  name='BrowserErrorLog',
  full_name='skywalking.v3.BrowserErrorLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='uniqueId', full_name='skywalking.v3.BrowserErrorLog.uniqueId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service', full_name='skywalking.v3.BrowserErrorLog.service', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceVersion', full_name='skywalking.v3.BrowserErrorLog.serviceVersion', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='skywalking.v3.BrowserErrorLog.time', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pagePath', full_name='skywalking.v3.BrowserErrorLog.pagePath', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='category', full_name='skywalking.v3.BrowserErrorLog.category', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grade', full_name='skywalking.v3.BrowserErrorLog.grade', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='skywalking.v3.BrowserErrorLog.message', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line', full_name='skywalking.v3.BrowserErrorLog.line', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='col', full_name='skywalking.v3.BrowserErrorLog.col', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stack', full_name='skywalking.v3.BrowserErrorLog.stack', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errorUrl', full_name='skywalking.v3.BrowserErrorLog.errorUrl', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='firstReportedError', full_name='skywalking.v3.BrowserErrorLog.firstReportedError', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=429,
  serialized_end=705,
)

_BROWSERERRORLOG.fields_by_name['category'].enum_type = _ERRORCATEGORY
DESCRIPTOR.message_types_by_name['BrowserPerfData'] = _BROWSERPERFDATA
DESCRIPTOR.message_types_by_name['BrowserErrorLog'] = _BROWSERERRORLOG
DESCRIPTOR.enum_types_by_name['ErrorCategory'] = _ERRORCATEGORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BrowserPerfData = _reflection.GeneratedProtocolMessageType('BrowserPerfData', (_message.Message,), {
  'DESCRIPTOR' : _BROWSERPERFDATA,
  '__module__' : 'browser.BrowserPerf_pb2'
  # @@protoc_insertion_point(class_scope:skywalking.v3.BrowserPerfData)
  })
_sym_db.RegisterMessage(BrowserPerfData)

BrowserErrorLog = _reflection.GeneratedProtocolMessageType('BrowserErrorLog', (_message.Message,), {
  'DESCRIPTOR' : _BROWSERERRORLOG,
  '__module__' : 'browser.BrowserPerf_pb2'
  # @@protoc_insertion_point(class_scope:skywalking.v3.BrowserErrorLog)
  })
_sym_db.RegisterMessage(BrowserErrorLog)


DESCRIPTOR._options = None

_BROWSERPERFSERVICE = _descriptor.ServiceDescriptor(
  name='BrowserPerfService',
  full_name='skywalking.v3.BrowserPerfService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=792,
  serialized_end=971,
  methods=[
  _descriptor.MethodDescriptor(
    name='collectPerfData',
    full_name='skywalking.v3.BrowserPerfService.collectPerfData',
    index=0,
    containing_service=None,
    input_type=_BROWSERPERFDATA,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='collectErrorLogs',
    full_name='skywalking.v3.BrowserPerfService.collectErrorLogs',
    index=1,
    containing_service=None,
    input_type=_BROWSERERRORLOG,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BROWSERPERFSERVICE)

DESCRIPTOR.services_by_name['BrowserPerfService'] = _BROWSERPERFSERVICE

# @@protoc_insertion_point(module_scope)
