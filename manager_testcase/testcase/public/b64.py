#!/usr/bin/python
# coding=utf-8
import base64
def b64(data):
  data=str(data).encode()
  data=base64.b64encode(data)
  return data
def b64decode(data):
  data=base64.b64decode(data)
  return data
