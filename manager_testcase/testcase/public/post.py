#!/usr/bin/python
# coding=utf-8
import requests
from public import b64
def rpost(url,data):
  r=requests.post(url,data)
  r=r.json()
  rr = r.get('code')
  try:
    da=r.get('data')
    daa=b64.b64decode(da)
    print(daa)
  except:
    print("no data")

  return rr
