#!/usr/bin/python
# coding=utf-8
from public import ticketid
def url():
  url='https://mpweb.test1.fangguancha.com/'
  return url
def public(data):
  tid=ticketid.ticketid()
  trans={"deviceType":7,"userver":5,"cityId":51010000,"version":"1.0.0","utype":3,"encryMode":2,"ticketId":tid,"data":data}
  return trans
