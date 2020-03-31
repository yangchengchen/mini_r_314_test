#!/usr/bin/python
# coding=utf-8
import unittest
import json
import requests
from public import base
from public import b64
from public import post
import base64
from public import ticketid
from public import sql

class MyfirstTestCase(unittest.TestCase):
  '''订单模块（2.1） / 收货地址列表（根据下订单用户Id）'''
  def setUp(self):
    self.url=base.get_host('/order/logisticslistbyuserid')
    data={"pageSize": 10,"curPage": 1}
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