#!/usr/bin/python
# coding=utf-8
import unittest
import json
import requests
from public import base
from public import b64
import base64
from public import ticketid

class MyfirstTestCase(unittest.TestCase):
  def setUp(self):
    self.url=base.get_host('/users/docollect')
    tid=ticketid.ticketid()
    print(tid)
    data={"contentHId": "1135229672691335168","contentType": 0,"lat":30.265656,"lng":104.5658995498,"collectType": 0}
    print(data)
    data=b64.b64(data)
    self.trans=base.get_trans(data)
  def test_sample(self):
    r=requests.post(self.url,data=self.trans)
    r=r.json()
    da=r.get("code")
    self.assertEqual(da, 0)
    #da=b64.b64decode(da)
    print (r)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
