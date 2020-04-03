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
  '''商品模块（2.1） / SKU列表（我的小店-根据分销商Id）'''
  def setUp(self):
    self.url=base.get_host('/productsku/skulistbydistributorid')
    self.data={"pageSize": 10,"curPage": 1,"goodsName":"鸡"}
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
