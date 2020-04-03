#!/usr/bin/python
# coding=utf-8
import base64
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import time
def ticketid():
  url1='http://192.168.10.238:9900/login'
  url='http://uiap.test.chuangjialive.com/login'
  #urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
  #urllib3.disable_warnings()
  #logging.captureWarnings(True)
  data = {"account": "", "password": "", "verifyCode": "", "openid": "oPynN4ogKhaxnZPtas3IjImsX6Gk","unionid": "owpHew38EZjAsnAPZtzd0h3_W6rw", "nickname": "ycc", "headImg": "", "userInfo": ""}
  da = str(data).encode()
  data = base64.b64encode(da)
  payload = {"deviceNo":"sfjjks","timestamp":str(time.time()).replace('.', ''),"deviceType": 7, "userver": 5, "cityId": 51010000, "version": "1.0.0", "utype": 3, "encryMode": 2,"data": data,"ipAddress":"123.0.0.1"}
  #print('payload', payload)
  r = requests.post(url, data=payload,verify=False)
  #print(r.content)
  r = r.json()
  #print(r)
  r = r.get("data")
  r= str(r).encode()
  r = base64.b64decode(r)
  #print(r)
  #r=str(r, encoding='gbk')
  r=json.loads(r)
  r=r["ticketId"]
  #print(r)
  return r

if __name__=='__main__':
  ticketid()
