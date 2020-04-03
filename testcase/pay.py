#!/usr/bin/python
# coding=utf-8
import base64
import requests
import json
from testcase.public import ticketid
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def dingdan():
  url1='http://192.168.10.88:8087/order/placeorder'
  url = 'https://api.test.chuangjialive.com/bj-web-mini/order/placeorder'
  #data={"logisticsId":"1161952222670487552","contactMobile":"18888888000","goodsParams":[{"goodsId":"1179668728925567100","distributorId":"1036536328113618944","quantity":"2"}]}
  data={'logisticsId': '1161952222670487552','goodsParams': [{'goodsId': '1179668728925567100','quantity': '2','activityId': '','goodsType': 1}],'contactMobile': '18888888000','contactName': 'test','picksiteId': '1195236636804251648'}
  data = str(data).encode()
  data = base64.b64encode(data)
  tid = ticketid.ticketid()
  trans = {"deviceType": 7, "userver": 5, "cityId": 51010000, "version": "1.0.0", "utype": 3, "encryMode": 2,"ticketId":tid, "data": data,"ipAddress":"123.0.0.1","deviceNo":"sfjjks","timestamp":str(time.time()).replace('.', '')}
  #print(trans)
  s=requests.session()
  #try:
  r=s.post(url,data=trans,verify=False)
  print(r)
  da=r.json()
  print(da)
  #except:
    #print("error")
  da=da.get("data")
  da=base64.b64decode(da)
  da = json.loads(da)
  print(da)
  da=da['id']
  zhifu(s,tid, da)

def zhifu(a,b,c):
  url='http://10.10.0.184:80/order/payment'
  ord=c
  ti=b
  data={"orderId":ord,"ticketId":ti}
  print(data)
  data = str(data).encode()
  data = base64.b64encode(data)
  tid = ticketid.ticketid()
  print(tid)
  trans = {"deviceType": 7, "userver": 5, "cityId": 51010000, "version": "1.0.0", "utype": 3, "encryMode": 2,"ticketId": tid, "data": data,"ipAddress":"123.0.0.1","deviceNo":"sfjjks","timestamp":str(time.time()).replace('.', '')}
  print(trans)
  r = requests.post(url, data=trans)
  r = r.json()
  print(r)


if __name__ =='__main__':
  #for i in range(0,9000):
    #time.sleep(2)
  dingdan()
