# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: post.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'post.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\npost.proto\x12\x05posts\"\x94\x01\n\x04Post\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x12\n\ncreator_id\x18\x04 \x01(\t\x12\x12\n\ncreated_at\x18\x05 \x01(\t\x12\x12\n\nupdated_at\x18\x06 \x01(\t\x12\x12\n\nis_private\x18\x07 \x01(\x08\x12\x0c\n\x04tags\x18\x08 \x03(\t\"m\n\x11\x43reatePostRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x12\n\ncreator_id\x18\x03 \x01(\t\x12\x12\n\nis_private\x18\x04 \x01(\x08\x12\x0c\n\x04tags\x18\x05 \x03(\t\"2\n\x0eGetPostRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0crequester_id\x18\x02 \x01(\t\"{\n\x11UpdatePostRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x12\n\nis_private\x18\x04 \x01(\x08\x12\x0c\n\x04tags\x18\x05 \x03(\t\x12\x14\n\x0crequester_id\x18\x06 \x01(\t\"5\n\x11\x44\x65letePostRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0crequester_id\x18\x02 \x01(\t\"I\n\x10ListPostsRequest\x12\x14\n\x0crequester_id\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x11\n\tpage_size\x18\x03 \x01(\x05\")\n\x0cPostResponse\x12\x19\n\x04post\x18\x01 \x01(\x0b\x32\x0b.posts.Post\"/\n\x11ListPostsResponse\x12\x1a\n\x05posts\x18\x01 \x03(\x0b\x32\x0b.posts.Post\"\x07\n\x05\x45mpty2\xb4\x02\n\x0bPostService\x12;\n\nCreatePost\x12\x18.posts.CreatePostRequest\x1a\x13.posts.PostResponse\x12\x35\n\x07GetPost\x12\x15.posts.GetPostRequest\x1a\x13.posts.PostResponse\x12;\n\nUpdatePost\x12\x18.posts.UpdatePostRequest\x1a\x13.posts.PostResponse\x12\x34\n\nDeletePost\x12\x18.posts.DeletePostRequest\x1a\x0c.posts.Empty\x12>\n\tListPosts\x12\x17.posts.ListPostsRequest\x1a\x18.posts.ListPostsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'post_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_POST']._serialized_start=22
  _globals['_POST']._serialized_end=170
  _globals['_CREATEPOSTREQUEST']._serialized_start=172
  _globals['_CREATEPOSTREQUEST']._serialized_end=281
  _globals['_GETPOSTREQUEST']._serialized_start=283
  _globals['_GETPOSTREQUEST']._serialized_end=333
  _globals['_UPDATEPOSTREQUEST']._serialized_start=335
  _globals['_UPDATEPOSTREQUEST']._serialized_end=458
  _globals['_DELETEPOSTREQUEST']._serialized_start=460
  _globals['_DELETEPOSTREQUEST']._serialized_end=513
  _globals['_LISTPOSTSREQUEST']._serialized_start=515
  _globals['_LISTPOSTSREQUEST']._serialized_end=588
  _globals['_POSTRESPONSE']._serialized_start=590
  _globals['_POSTRESPONSE']._serialized_end=631
  _globals['_LISTPOSTSRESPONSE']._serialized_start=633
  _globals['_LISTPOSTSRESPONSE']._serialized_end=680
  _globals['_EMPTY']._serialized_start=682
  _globals['_EMPTY']._serialized_end=689
  _globals['_POSTSERVICE']._serialized_start=692
  _globals['_POSTSERVICE']._serialized_end=1000
# @@protoc_insertion_point(module_scope)
