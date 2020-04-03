#!/usr/bin/python
# coding=utf-8
import unittest
import json
import requests
from testcase.public import base
from testcase.public import b64
import base64
from testcase.public import post

class MyfirstTestCase(unittest.TestCase):
  '''搜索模块／搜索结果'''
  def setUp(self):
    self.url=base.get_host('/search/firstpage/list')
    self.data={"searchTxt": "测试"}
    self.data=b64.b64(self.data)
    self.trans=base.get_trans(self.data)
  def test_sample(self):
    r=post.rpost(self.url,data=self.trans)
    self.assertEqual(r,0)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
