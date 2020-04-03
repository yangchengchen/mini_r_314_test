#!/usr/bin/python
# coding=utf-8
import unittest
import json
import requests
from testcase.public import base
from testcase.public import b64
import base64
from testcase.public import ticketid
from testcase.public import sql

class MyfirstTestCase(unittest.TestCase):
  def setUp(self):
    self.url=base.get_host('/focaltopic/listbyradiustype')
    id = sql.bjqsql()
    data={"radiusTypeId":id}
    #print(data)
    data=b64.b64(data)
    self.trans=base.get_trans(data)
  def test_sample(self):
    r=requests.post(self.url,data=self.trans)
    r=r.json()
    da=r.get("code")
    self.assertEqual(da, 0)
    print (r)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
