# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: language-agent/Meter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ..common import Common_pb2 as common_dot_Common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='language-agent/Meter.proto',
  package='skywalking.v3',
  syntax='proto3',
  serialized_options=b'\n3org.apache.skywalking.apm.network.language.agent.v3P\001Z:skywalking.apache.org/repo/goapi/collect/language/agent/v3',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1alanguage-agent/Meter.proto\x12\rskywalking.v3\x1a\x13\x63ommon/Common.proto\"$\n\x05Label\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"M\n\x10MeterBucketValue\x12\x0e\n\x06\x62ucket\x18\x01 \x01(\x01\x12\r\n\x05\x63ount\x18\x02 \x01(\x03\x12\x1a\n\x12isNegativeInfinity\x18\x03 \x01(\x08\"U\n\x10MeterSingleValue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\x06labels\x18\x02 \x03(\x0b\x32\x14.skywalking.v3.Label\x12\r\n\x05value\x18\x03 \x01(\x01\"u\n\x0eMeterHistogram\x12\x0c\n\x04name\x18\x01 \x01(\t\x12$\n\x06labels\x18\x02 \x03(\x0b\x32\x14.skywalking.v3.Label\x12/\n\x06values\x18\x03 \x03(\x0b\x32\x1f.skywalking.v3.MeterBucketValue\"\xbe\x01\n\tMeterData\x12\x36\n\x0bsingleValue\x18\x01 \x01(\x0b\x32\x1f.skywalking.v3.MeterSingleValueH\x00\x12\x32\n\thistogram\x18\x02 \x01(\x0b\x32\x1d.skywalking.v3.MeterHistogramH\x00\x12\x0f\n\x07service\x18\x03 \x01(\t\x12\x17\n\x0fserviceInstance\x18\x04 \x01(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\x03\x42\x08\n\x06metric\"B\n\x13MeterDataCollection\x12+\n\tmeterData\x18\x01 \x03(\x0b\x32\x18.skywalking.v3.MeterData2\xa7\x01\n\x12MeterReportService\x12@\n\x07\x63ollect\x12\x18.skywalking.v3.MeterData\x1a\x17.skywalking.v3.Commands\"\x00(\x01\x12O\n\x0c\x63ollectBatch\x12\".skywalking.v3.MeterDataCollection\x1a\x17.skywalking.v3.Commands\"\x00(\x01\x42s\n3org.apache.skywalking.apm.network.language.agent.v3P\x01Z:skywalking.apache.org/repo/goapi/collect/language/agent/v3b\x06proto3'
  ,
  dependencies=[common_dot_Common__pb2.DESCRIPTOR,])




_LABEL = _descriptor.Descriptor(
  name='Label',
  full_name='skywalking.v3.Label',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='skywalking.v3.Label.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='skywalking.v3.Label.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_end=102,
)


_METERBUCKETVALUE = _descriptor.Descriptor(
  name='MeterBucketValue',
  full_name='skywalking.v3.MeterBucketValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bucket', full_name='skywalking.v3.MeterBucketValue.bucket', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='count', full_name='skywalking.v3.MeterBucketValue.count', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='isNegativeInfinity', full_name='skywalking.v3.MeterBucketValue.isNegativeInfinity', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=104,
  serialized_end=181,
)


_METERSINGLEVALUE = _descriptor.Descriptor(
  name='MeterSingleValue',
  full_name='skywalking.v3.MeterSingleValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='skywalking.v3.MeterSingleValue.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='skywalking.v3.MeterSingleValue.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='skywalking.v3.MeterSingleValue.value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=183,
  serialized_end=268,
)


_METERHISTOGRAM = _descriptor.Descriptor(
  name='MeterHistogram',
  full_name='skywalking.v3.MeterHistogram',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='skywalking.v3.MeterHistogram.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='labels', full_name='skywalking.v3.MeterHistogram.labels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='skywalking.v3.MeterHistogram.values', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=270,
  serialized_end=387,
)


_METERDATA = _descriptor.Descriptor(
  name='MeterData',
  full_name='skywalking.v3.MeterData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='singleValue', full_name='skywalking.v3.MeterData.singleValue', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='histogram', full_name='skywalking.v3.MeterData.histogram', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='service', full_name='skywalking.v3.MeterData.service', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serviceInstance', full_name='skywalking.v3.MeterData.serviceInstance', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='skywalking.v3.MeterData.timestamp', index=4,
      number=5, type=3, cpp_type=2, label=1,
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
    _descriptor.OneofDescriptor(
      name='metric', full_name='skywalking.v3.MeterData.metric',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=390,
  serialized_end=580,
)


_METERDATACOLLECTION = _descriptor.Descriptor(
  name='MeterDataCollection',
  full_name='skywalking.v3.MeterDataCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='meterData', full_name='skywalking.v3.MeterDataCollection.meterData', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=582,
  serialized_end=648,
)

_METERSINGLEVALUE.fields_by_name['labels'].message_type = _LABEL
_METERHISTOGRAM.fields_by_name['labels'].message_type = _LABEL
_METERHISTOGRAM.fields_by_name['values'].message_type = _METERBUCKETVALUE
_METERDATA.fields_by_name['singleValue'].message_type = _METERSINGLEVALUE
_METERDATA.fields_by_name['histogram'].message_type = _METERHISTOGRAM
_METERDATA.oneofs_by_name['metric'].fields.append(
  _METERDATA.fields_by_name['singleValue'])
_METERDATA.fields_by_name['singleValue'].containing_oneof = _METERDATA.oneofs_by_name['metric']
_METERDATA.oneofs_by_name['metric'].fields.append(
  _METERDATA.fields_by_name['histogram'])
_METERDATA.fields_by_name['histogram'].containing_oneof = _METERDATA.oneofs_by_name['metric']
_METERDATACOLLECTION.fields_by_name['meterData'].message_type = _METERDATA
DESCRIPTOR.message_types_by_name['Label'] = _LABEL
DESCRIPTOR.message_types_by_name['MeterBucketValue'] = _METERBUCKETVALUE
DESCRIPTOR.message_types_by_name['MeterSingleValue'] = _METERSINGLEVALUE
DESCRIPTOR.message_types_by_name['MeterHistogram'] = _METERHISTOGRAM
DESCRIPTOR.message_types_by_name['MeterData'] = _METERDATA
DESCRIPTOR.message_types_by_name['MeterDataCollection'] = _METERDATACOLLECTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Label = _reflection.GeneratedProtocolMessageType('Label', (_message.Message,), {
  'DESCRIPTOR' : _LABEL,
  '__module__' : 'language_agent.Meter_pb2'
  # @@protoc_insertion_point(class_scope:skywalking.v3.Label)
  })
_sym_db.RegisterMessage(Label)

MeterBucketValue = _reflection.GeneratedProtocolMessageType('MeterBucketValue', (_message.Message,), {
  'DESCRIPTOR' : _METERBUCKETVALUE,
  '__module__' : 'language_agent.Meter_pb2'
  # @@protoc_insertion_point(class_scope:skywalking.v3.MeterBucketValue)
  })
_sym_db.RegisterMessage(MeterBucketValue)

MeterSingleValue = _reflection.GeneratedProtocolMessageType('MeterSingleValue', (_message.Message,), {
  'DESCRIPTOR' : _METERSINGLEVALUE,
  '__module__' : 'language_agent.Meter_pb2'
  # @@protoc_insertion_point(class_scope:skywalking.v3.MeterSingleValue)
  })
_sym_db.RegisterMessage(MeterSingleValue)

MeterHistogram = _reflection.GeneratedProtocolMessageType('MeterHistogram', (_message.Message,), {
  'DESCRIPTOR' : _METERHISTOGRAM,
  '__module__' : 'language_agent.Meter_pb2'
  # @@protoc_insertion_point(class_scope:skywalking.v3.MeterHistogram)
  })
_sym_db.RegisterMessage(MeterHistogram)

MeterData = _reflection.GeneratedProtocolMessageType('MeterData', (_message.Message,), {
  'DESCRIPTOR' : _METERDATA,
  '__module__' : 'language_agent.Meter_pb2'
  # @@protoc_insertion_point(class_scope:skywalking.v3.MeterData)
  })
_sym_db.RegisterMessage(MeterData)

MeterDataCollection = _reflection.GeneratedProtocolMessageType('MeterDataCollection', (_message.Message,), {
  'DESCRIPTOR' : _METERDATACOLLECTION,
  '__module__' : 'language_agent.Meter_pb2'
  # @@protoc_insertion_point(class_scope:skywalking.v3.MeterDataCollection)
  })
_sym_db.RegisterMessage(MeterDataCollection)


DESCRIPTOR._options = None

_METERREPORTSERVICE = _descriptor.ServiceDescriptor(
  name='MeterReportService',
  full_name='skywalking.v3.MeterReportService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=651,
  serialized_end=818,
  methods=[
  _descriptor.MethodDescriptor(
    name='collect',
    full_name='skywalking.v3.MeterReportService.collect',
    index=0,
    containing_service=None,
    input_type=_METERDATA,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='collectBatch',
    full_name='skywalking.v3.MeterReportService.collectBatch',
    index=1,
    containing_service=None,
    input_type=_METERDATACOLLECTION,
    output_type=common_dot_Common__pb2._COMMANDS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_METERREPORTSERVICE)

DESCRIPTOR.services_by_name['MeterReportService'] = _METERREPORTSERVICE

# @@protoc_insertion_point(module_scope)
