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
  '''订单模块（2.1） / 返现提现列表（根据分销人Id）'''
  def setUp(self):
    self.url=base.get_host('/order/cashbackoutlistbydistributorId')
    data={}
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
