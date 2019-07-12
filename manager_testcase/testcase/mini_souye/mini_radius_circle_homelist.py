#!/usr/bin/python
# coding=utf-8
import unittest
import json
import requests
from public import base
from public import b64
import base64

class MyfirstTestCase(unittest.TestCase):
  def setUp(self):
    self.url=base.get_host('radius/circle/homelist?page=true')
    self.data={"curPage": 1,"pageSize": 20}
    self.data=b64.b64(self.data)
    self.trans=base.get_trans(self.data)
  def test_sample(self):
    r=requests.post(self.url,data=self.trans)
    r=r.json()
    print(r)
    dd=r.get('data')
    d=b64.b64decode(dd)
    print(d)
    da=r.get('code')
    self.assertEqual(da,0)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
