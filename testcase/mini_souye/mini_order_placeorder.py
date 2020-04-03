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
from testcase.public import post
class MyfirstTestCase(unittest.TestCase):
  '''订单模块（2.1） / 订单下单'''
  def setUp(self):
    self.url=base.get_host('/order/placeorder')
    data={'logisticsId': '','picksiteId': '','contactMobile': '15928009661','contactName': '杨程晨','goodsParams': [{'goodsId': '1179668728925567117','quantity': 1,'activityId': '1204246392755716096','goodsType': 2}],'trace_uid': '1036536328113618944'}
    #print(data)
    data=b64.b64(data)
    self.trans=base.get_trans(data)
  def test_sample(self):
    r = post.rpost(self.url, data=self.trans)
    # da=r.get('code')
    self.assertEqual(r, 0)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
