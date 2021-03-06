# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app.proto',
  package='tutorial',
  serialized_pb=_b('\n\tapp.proto\x12\x08tutorial\"X\n\x0f\x45\x64\x64ystoneBeacon\x12\x0b\n\x03URL\x18\x01 \x01(\t\x12\x15\n\rUID_namespace\x18\x02 \x01(\t\x12\x14\n\x0cUID_instance\x18\x03 \x01(\t\x12\x0b\n\x03TLM\x18\x04 \x01(\t\"\x93\x03\n\x06WebApp\x12\x0e\n\x02id\x18\x01 \x01(\x05:\x02-1\x12\x16\n\x05\x61ppId\x18\x02 \x01(\t:\x07<no-id>\x12\x1a\n\x07\x61ppName\x18\x03 \x01(\t:\t<Unnamed>\x12\x17\n\x0bversionCode\x18\x04 \x01(\x05:\x02-1\x12\x18\n\x0bversionName\x18\x05 \x01(\t:\x03\x30.0\x12\x0b\n\x03lat\x18\x06 \x01(\t\x12\x0c\n\x04long\x18\x07 \x01(\t\x12)\n\x06\x62\x65\x61\x63on\x18\x08 \x01(\x0b\x32\x19.tutorial.EddystoneBeacon\x12\x1f\n\tindexFile\x18\t \x01(\t:\x0cindex.bundle\x12.\n\x10indexFileAndroid\x18\n \x01(\t:\x14index.android.bundle\x12&\n\x0cindexFileIos\x18\x0b \x01(\t:\x10index.ios.bundle\x12\x17\n\tMainClass\x18\x0c \x01(\t:\x04main\x12\x1e\n\x10MainAndroidClass\x18\r \x01(\t:\x04main\x12\x1a\n\x0cMainIosClass\x18\x0e \x01(\t:\x04main\"(\n\x07\x41ppList\x12\x1d\n\x03\x61pp\x18\x01 \x03(\x0b\x32\x10.tutorial.WebApp')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EDDYSTONEBEACON = _descriptor.Descriptor(
  name='EddystoneBeacon',
  full_name='tutorial.EddystoneBeacon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='URL', full_name='tutorial.EddystoneBeacon.URL', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='UID_namespace', full_name='tutorial.EddystoneBeacon.UID_namespace', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='UID_instance', full_name='tutorial.EddystoneBeacon.UID_instance', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='TLM', full_name='tutorial.EddystoneBeacon.TLM', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=111,
)


_WEBAPP = _descriptor.Descriptor(
  name='WebApp',
  full_name='tutorial.WebApp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tutorial.WebApp.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appId', full_name='tutorial.WebApp.appId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("<no-id>").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='appName', full_name='tutorial.WebApp.appName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("<Unnamed>").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='versionCode', full_name='tutorial.WebApp.versionCode', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='versionName', full_name='tutorial.WebApp.versionName', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("0.0").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lat', full_name='tutorial.WebApp.lat', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='long', full_name='tutorial.WebApp.long', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='beacon', full_name='tutorial.WebApp.beacon', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='indexFile', full_name='tutorial.WebApp.indexFile', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("index.bundle").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='indexFileAndroid', full_name='tutorial.WebApp.indexFileAndroid', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("index.android.bundle").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='indexFileIos', full_name='tutorial.WebApp.indexFileIos', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("index.ios.bundle").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MainClass', full_name='tutorial.WebApp.MainClass', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("main").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MainAndroidClass', full_name='tutorial.WebApp.MainAndroidClass', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("main").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MainIosClass', full_name='tutorial.WebApp.MainIosClass', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("main").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=517,
)


_APPLIST = _descriptor.Descriptor(
  name='AppList',
  full_name='tutorial.AppList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app', full_name='tutorial.AppList.app', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=519,
  serialized_end=559,
)

_WEBAPP.fields_by_name['beacon'].message_type = _EDDYSTONEBEACON
_APPLIST.fields_by_name['app'].message_type = _WEBAPP
DESCRIPTOR.message_types_by_name['EddystoneBeacon'] = _EDDYSTONEBEACON
DESCRIPTOR.message_types_by_name['WebApp'] = _WEBAPP
DESCRIPTOR.message_types_by_name['AppList'] = _APPLIST

EddystoneBeacon = _reflection.GeneratedProtocolMessageType('EddystoneBeacon', (_message.Message,), dict(
  DESCRIPTOR = _EDDYSTONEBEACON,
  __module__ = 'app_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.EddystoneBeacon)
  ))
_sym_db.RegisterMessage(EddystoneBeacon)

WebApp = _reflection.GeneratedProtocolMessageType('WebApp', (_message.Message,), dict(
  DESCRIPTOR = _WEBAPP,
  __module__ = 'app_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.WebApp)
  ))
_sym_db.RegisterMessage(WebApp)

AppList = _reflection.GeneratedProtocolMessageType('AppList', (_message.Message,), dict(
  DESCRIPTOR = _APPLIST,
  __module__ = 'app_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.AppList)
  ))
_sym_db.RegisterMessage(AppList)


# @@protoc_insertion_point(module_scope)
