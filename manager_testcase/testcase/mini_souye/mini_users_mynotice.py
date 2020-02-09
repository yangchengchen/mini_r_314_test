#!/usr/bin/python
# coding=utf-8
import unittest
import json
import requests
from public import base
from public import b64
import base64
from public import ticketid
from public import sql
from public import post

class MyfirstTestCase(unittest.TestCase):
  '''我的模块／我的小红点'''
  def setUp(self):
    self.url=base.get_host('/users/mynotice')
    data={}
    print(data)
    data=b64.b64(data)
    self.trans=base.get_trans(data)
  def test_sample(self):
    r=post.rpost(self.url,data=self.trans)
    self.assertEqual(r,0)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
