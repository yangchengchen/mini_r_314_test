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
import sys
sys.path.append('/var/jenkins_home/workspace/test/manager_testcase/testcase/public')

class MyfirstTestCase(unittest.TestCase):
  '''文章模块 / 文章详情'''
  def setUp(self):
    self.url=base.get_host('/article/detail')
    id = sql.bjqsql()
    data={"id":id}
    print(data)
    data=b64.b64(data)
    self.trans=base.get_trans(data)
  def test_sample(self):
    r=requests.post(self.url,data=self.trans)
    print(r)
    r=r.json()
    da=r.get("code")
    self.assertEqual(da, 0)
    print (r)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
