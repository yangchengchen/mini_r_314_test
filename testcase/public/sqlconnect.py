import pymysql
def sqlconnect():
  con=pymysql.connect(host='192.168.10.221', user='root', password='$%XP4HEdvq5CQUcP', db='bj_wechat_content', charset='utf8')
  cur=con.cursor()
  return cur
