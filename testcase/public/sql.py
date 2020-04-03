import pymysql
from testcase.public import sqlconnect
def bjqsql():
  cur=sqlconnect.sqlconnect()
  sql="select id from dims_radius_type WHERE status=1"
  cur.execute(sql)
  u,=cur.fetchone()
  print(u)
  return u
def htsql():
  conn = pymysql.connect(host='10.254.33.50', user='test', password='N2W6BNg8BOwWDCy2', db='bj_wechat_content', charset='utf8')
  cur=conn.cursor()
  sql="select id from focal_topic WHERE status=1"
  cur.execute(sql)
  u,=cur.fetchone()
  print(u)
  return u
def plsql():
  conn = pymysql.connect(host='10.254.33.50', user='test', password='N2W6BNg8BOwWDCy2', db='bj_wechat_content', charset='utf8')
  cur=conn.cursor()
  sql="select content_h_id from content_comment WHERE status=1 AND content_type=0 AND is_reply=0"
  cur.execute(sql)
  u,=cur.fetchone()
  print(u)
  return u
def dtxqsql():
  '''动态详情表查询动态id'''
  cur = sqlconnect.sqlconnect()
  sql = "select content_h_id from ugc_content_d WHERE status=1 "
  cur.execute(sql)
  u, = cur.fetchone()
  print(u)
  return u

