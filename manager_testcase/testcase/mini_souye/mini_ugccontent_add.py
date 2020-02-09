#!/usr/bin/python
# coding=utf-8
import unittest
import json
import requests
from public import base
from public import b64
import base64
from public import post

class MyfirstTestCase(unittest.TestCase):
  '''动态模块／新增动态'''
  def setUp(self):
    self.url=base.get_host('/ugccontent/add')
    self.data={"unionid":"owpHew38EZjAsnAPZtzd0h3_W6rw","ip":"192.168.10.235","contentBriefTxt":"ceshi","contentBriefPics":["https://wechatmsg.fangguancha.com/head/1036536328113618944/2019/11/28/fc8ca945091846caa9a294a20453cfae.jpg"],"radiusTypeId":"51010000005","ocalTopicId":"1186178774413082624","ipAddress":{"address":"四川省成都市武侯区锦晖东街","lng":104.06971322324222,"title":"成都银泰中心in99(成都市武侯区)","lat":30.585799977248566},"goodsId":"1179668728925567130"}
    self.data=b64.b64(self.data)
    self.trans=base.get_trans(self.data)
  def test_sample(self):
    r=post.rpost(self.url,data=self.trans)
    self.assertEqual(r,0)
  def tearDown(self):
    print ("succese")
if __name__ =='__main__':
  unittest.main()
