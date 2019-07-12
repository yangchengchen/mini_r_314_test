#!/usr/bin/python
# coding=utf-8
import base64
import requests
import json
def ticketid():
  data = {"account": "", "password": "", "verifyCode": "", "openid": "oPynN4ogKhaxnZPtas3IjImsX6Gk","unionid": "8EZjAsnAPZtzd0h3_W6rw", "nickname": "", "headImg": "", "userInfo": ""}
  da = str(data).encode()
  data = base64.b64encode(da)
  payload = {"deviceType": 7, "userver": 5, "cityId": 51010000, "version": "1.0.0", "utype": 3, "encryMode": 2,"data": data}
  #print('payload', payload)
  r = requests.post("https://uiap.test1.maifangma.com/login", data=payload)
  print(r)
  r = r.json()
  r = r.get("data")
  r = base64.b64decode(r)
  r=json.loads(r)
  r=r["ticketId"]
  print(r)
  return r

if __name__=='__main__':
  ticketid()
