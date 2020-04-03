#!/usr/bin/python
# coding=utf-8
import unittest
import json
import requests
from testcase.public import base
from testcase.public import b64
import base64
from testcase.public import ticketid
from testcase.public import post
from testcase.public import sql

class MyfirstTestCase(unittest.TestCase):
  def setUp(self):
    '''动态模块／动态信息'''
    self.url=base.get_host('/ugccontent/detail')
    id = sql.dtxqsql()
    tid=ticketid.ticketid()
    data = {"id":"1176777395743490048"}
    print(data)
    data=b64.b64(data)
    self.trans=base.get_trans(data)
  def test_sample(self):
    r=post.rpost(self.url,data=self.trans)
    #da=r.get("code")
    #self.assertEqual(da, 0)
    #da=b64.b64decode(da)
    self.assertEqual(r, 0)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
