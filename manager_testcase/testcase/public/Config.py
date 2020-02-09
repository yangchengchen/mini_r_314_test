#!/usr/bin/python
# coding=utf-8
from public import ticketid
import time
def url():
  url='https://api.test.chuangjialive.com/bj-web-mini/'
  return url
def public(data):
  tid=ticketid.ticketid()
  trans = {"deviceType": 7, "userver": 5, "cityId": 51010000, "version": "1.0.0", "utype": 3, "encryMode": 2,"ticketId":tid, "data": data,"ipAddress":"123.0.0.1","deviceNo":"sfjjks","timestamp":str(time.time()).replace('.', '')}
  #trans={"deviceType":7,"userver":5,"cityId":51010000,"version":"1.0.0","utype":3,"encryMode":2,"ticketId":tid,"data":data}
  return trans
