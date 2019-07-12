#!/usr/bin/python
# coding=utf-8
import manager_testcase.testcase.public.Config as Config
def get_host(EndPoint):
  host=Config.url()
  endpoint=EndPoint
  url=''.join([host,endpoint])
  return url
def get_trans(Data):
  data=Config.public(Data)
  return data
