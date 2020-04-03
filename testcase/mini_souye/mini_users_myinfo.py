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

class MyfirstTestCase(unittest.TestCase):
  '''我的模块／我的信息模块'''
  def setUp(self):
    self.url=base.get_host('/users/myinfo')
    #tid = ticketid.ticketid()
    data={}
    #print(data)
    data=b64.b64(data)
    self.trans=base.get_trans(data)
  def test_sample(self):
    r=post.rpost(self.url,data=self.trans)
    self.assertEqual(r,0)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
