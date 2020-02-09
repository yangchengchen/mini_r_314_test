#!/usr/bin/python
# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os
import sys
#sys.path.append('./testcase')
#=============定义发送邮件====================
def send_mail(file_new):
  f=open(file_new,'rb')
  mail_body=f.read()
  f.close()
  msg=MIMEText(mail_body,'html','utf-8')
  msg['Subject']=Header("半径314自动化测试报告",'utf-8')

  smtp=smtplib.SMTP()
  smtp.connect("smtp.qq.com")
  smtp.login("277642429@qq.com","cwycivhpidiwbjgc")
  smtp.sendmail("277642429@qq.com","277642429@qq.com",msg.as_string())
  smtp.quit()
  print('email has send out')

#================查找报告目录，找到最新生成的测试报告文件=================
def new_report(testreport):
  lists=os.listdir(testreport)#返回指定路径下的文件夹或者文件
  lists.sort(key=lambda fn:os.path.getatime(testreport+ "/" +fn))
  file_new=os.path.join(testreport,lists[-1])
  print (file_new)
  return file_new

if __name__=='__main__':
  test_dir='./testcase/mini_souye'
  test_report='./report'
  discover=unittest.defaultTestLoader.discover(test_dir,pattern='mini_*.py')
  now=time.strftime("%Y-%m-%d_%H_%M_%S")
  filename='./report/'+now+'result.html'
  fp=open(filename,'wb')
  runner=HTMLTestRunner(stream=fp,title='测试报告',description='用例执行情况：',verbosity=2)
  runner.run(discover)
  fp.close()
  new_report=new_report(test_report)
  send_mail(new_report)
