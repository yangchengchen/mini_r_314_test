#!/usr/bin/python
# coding=utf-8
import unittest
import json
import requests
from testcase.public import base
from testcase.public import b64
import base64
from testcase.public import ticketid
import re

class MyfirstTestCase(unittest.TestCase):
  def setUp(self):
    self.url=base.get_host('/radius/circle/list?page=true')
    tid = ticketid.ticketid()
    data={"curPage": 1,"pageSize": 20}
    #print(data)
    data=b64.b64(data)
    self.trans=base.get_trans(data)
  def test_sample(self):
    r=requests.post(self.url,data=self.trans)
    r=r.json()
    da=r.get("data")
    #self.assertEqual(da, 0)
    da=b64.b64decode(da)
    da=json.loads(da)
    lis=da["list"]
    lis=str(lis)
    print(lis)
    li=re.search(r"'id':(.*?),",lis)
    print (li.group(1))
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
