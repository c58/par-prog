# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: movie.protobuf

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
  name='movie.protobuf',
  package='',
  serialized_pb=_b('\n\x0emovie.protobuf\"}\n\x05Movie\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1b\n\x05genre\x18\x02 \x02(\x0e\x32\x0c.Movie.Genre\x12\x0c\n\x04year\x18\x04 \x02(\x05\x12\x0e\n\x06\x61\x63tors\x18\x03 \x03(\t\"+\n\x05Genre\x12\x08\n\x04\x44RAM\x10\x00\x12\x0b\n\x07SHOOTER\x10\x01\x12\x0b\n\x07\x46\x41NTASY\x10\x02')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_MOVIE_GENRE = _descriptor.EnumDescriptor(
  name='Genre',
  full_name='Movie.Genre',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DRAM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOOTER', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FANTASY', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=100,
  serialized_end=143,
)
_sym_db.RegisterEnumDescriptor(_MOVIE_GENRE)


_MOVIE = _descriptor.Descriptor(
  name='Movie',
  full_name='Movie',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Movie.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='genre', full_name='Movie.genre', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='year', full_name='Movie.year', index=2,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='actors', full_name='Movie.actors', index=3,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MOVIE_GENRE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=143,
)

_MOVIE.fields_by_name['genre'].enum_type = _MOVIE_GENRE
_MOVIE_GENRE.containing_type = _MOVIE
DESCRIPTOR.message_types_by_name['Movie'] = _MOVIE

Movie = _reflection.GeneratedProtocolMessageType('Movie', (_message.Message,), dict(
  DESCRIPTOR = _MOVIE,
  __module__ = 'movie.protobuf_pb2'
  # @@protoc_insertion_point(class_scope:Movie)
  ))
_sym_db.RegisterMessage(Movie)


# @@protoc_insertion_point(module_scope)
