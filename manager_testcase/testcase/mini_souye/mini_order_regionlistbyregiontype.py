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
  '''订单模块（2.1） / 区域列表（通过省市区类型）'''
  def setUp(self):
    self.url=base.get_host('/order/regionlistbyregiontype')
    self.data={"regionType": 1}
    self.data=b64.b64(self.data)
    self.trans=base.get_trans(self.data)
  def test_sample(self):
    r=post.rpost(self.url,data=self.trans)
    #da=r.get('code')
    self.assertEqual(r,0)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
