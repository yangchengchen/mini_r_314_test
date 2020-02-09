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
  '''订订单模块（2.1） / 收货地址编辑'''
  def setUp(self):
    self.url=base.get_host('/order/logisticsedit')
    self.data={ "id": "","name": "ycc","address": "111","mobile": "15777777777","hasDefault": 1,"area": "双流区","oprType": 1,"regionId": "510104000000","city": "","province": ""}
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
