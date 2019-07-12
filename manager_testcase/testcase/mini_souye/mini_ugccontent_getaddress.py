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
    self.url=base.get_host('/ugccontent/getaddress?page=true')
    self.data={"lat": 30.605708,"lng": 104.068680,"curPage": 1,"pageSize": 20}
    self.data=b64.b64(self.data)
    self.trans=base.get_trans(self.data)
  def test_sample(self):
    r=requests.post(self.url,data=self.trans)
    print(r)
    r=r.json()
    rr = r.get('code')
    r=r.get('data')
    r=json.loads(r)
    print(type(r))
    r=b64.b64decode(r)
    print(r)
    #da=r.get('code')
    self.assertEqual(rr,0)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
