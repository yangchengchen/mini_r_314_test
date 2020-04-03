#!/usr/bin/python
# coding=utf-8
from locust import HttpLocust, TaskSet, task
import base64
import requests
import json
from testcase.public import ticketid
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json

class UserBehavior(TaskSet):
    #@task
    #def fgclogin(self):
        #data={"type":1,"account":"yangchengchen","password":"yCC@5216029"}
        #r=self.client.post("/api/account/login",json=data).text
        #rr=json.loads(r)
        #assert rr['code']==0
    def on_start(self):
      data = {"account": "", "password": "", "verifyCode": "", "openid": "oPynN4ogKhaxnZPtas3IjImsX6Gk",
              "unionid": "owpHew38EZjAsnAPZtzd0h3_W6rw", "nickname": "", "headImg": "", "userInfo": ""}
      da = str(data).encode()
      data = base64.b64encode(da)
      payload = {"deviceType": 7, "userver": 5, "cityId": 51010000, "version": "1.0.0", "utype": 3, "encryMode": 2,
                 "data": data}
      # print('payload', payload)
      r = requests.post("http://uiap.test1.maifangma.com/login", data=payload, verify=False)
      # print(r.content)
      r = r.json()
      r = r.get("data")
      r = str(r).encode()
      r = base64.b64decode(r)
      print(type(r))
      # r=str(r, encoding='gbk')
      print(type(r))
      r = json.loads(r)
      # print(r)
      # r=r.json()
      self.r = r["ticketId"]

    @task
    def dingdan(self):
      #url = 'https://mpweb.test1.fangguancha.com/order/placeorder'
      data = {"logisticsId": "1157184376623071232", "contactMobile": "15928009661", "goodsParams": [{"goodsId": "1179668728925567101", "distributorId": "1036536328113618944", "quantity": "2"}]}
      data = str(data).encode()
      data = base64.b64encode(data)
      #tid = ticketid.ticketid()
      trans = {"deviceType": 7, "userver": 5, "cityId": 51010000, "version": "1.0.0", "utype": 3, "encryMode": 2,"ticketId": self.r, "data": data}
      # print(trans)
      r=self.client.post("/order/placeorder",data=trans)
      # try:
      rr = r.json()
      assert rr['code'] == 0
      print(rr)
      # except:


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0
