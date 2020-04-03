#!/usr/bin/python
# coding=utf-8
import unittest
import json
import requests
from testcase.public import base
from testcase.public import b64
from testcase.public import post
import base64

class MyfirstTestCase(unittest.TestCase):
  '''订单模块（2.1） / 我的订单列表（根据用户Id-我买到的）'''
  def setUp(self):
    self.url=base.get_host('/order/buyorderlistbyuserid')
    data={"pageSize": 10,"curPage": 1,"orderStatus":0}
    #print(data)
    data=b64.b64(data)
    self.trans=base.get_trans(data)
  def test_sample(self):
    r=post.rpost(self.url,data=self.trans)
    #da=r.get('code')
    self.assertEqual(r,0)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
