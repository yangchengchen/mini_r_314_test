#!/usr/bin/python
# coding=utf-8
import unittest
import json
import requests
from public import base
from public import b64
import base64

class MyfirstTestCase(unittest.TestCase):
  '''首页模块 / 首页广告'''
  def setUp(self):
    self.url=base.get_host('users/docollect')
    self.data={"contentHId": "1","contentType": 1,"lat": 30.265656,"lng": 104.5658995498,"collectType": 1}
    self.data=b64.b64(self.data)
    self.trans=base.get_trans(self.data)
  def test_sample(self):
    r=requests.post(self.url,data=self.trans)
    r=r.json()
    print(r)
    da=r.get('code')
    self.assertEqual(da,0)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
