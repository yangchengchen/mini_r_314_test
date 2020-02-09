#!/usr/bin/python
# coding=utf-8
import unittest
import json
import requests
from public import base
from public import b64
from public import post
import base64
class MyfirstTestCase(unittest.TestCase):
  '''我的模块/关注/取消关注用户'''
  def setUp(self):
    self.url=base.get_host('/users/focus')
    self.data={"curPage": 1,"pageSize": 20}
    self.data=b64.b64(self.data)
    self.trans=base.get_trans(self.data)
  def test_sample(self):
    r=post.rpost(self.url,data=self.trans)
    self.assertEqual(r,0)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
