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
    self.url=base.get_host('ugccontent/pagelist?page=true')
    data={"typeId":"1","pageSize":20,"curPage":1,"lng":104.2659898,"lat":40.659898}
    data=b64.b64(data)
    self.trans=base.get_trans(data)
  def test_sample(self):
    r=requests.post(self.url,data=self.trans)
    r=r.json()
    da=r.get("data")
    da=b64.b64decode(da)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
