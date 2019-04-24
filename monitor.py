# coding:utf-8
'''
@create: yiquriyue(yiquriyue@outlook.com)
@datetime: 2019-04-10
@description: The function is to down load all CPA data ,And write to CSV file.
'''
import requests
import sys,os
import urllib2
import json
import re
import codecs
import csv
import chardet
import datetime
from bs4 import BeautifulSoup
reload(sys)
sys.setdefaultencoding( "utf-8" )
link = 'http://cmispub.cicpa.org.cn/cicpa2_web/PersonIndexAction.do'

class Spiker():
    def __init__(self,url):
        self.url = url
    def get(self,str):
        out = codecs.open("return.csv",'a+','utf-8')
        csv_write = csv.writer(out)
        if os.path.getsize("return.csv") == 0:
            hand = [u'姓名',u'性别',u'所内职务',u'是否党员',u'学历',u'学位',u'专业',u'毕业学校',u'资格获取方式',u'考核批准文号',u'批准时间',u'注册会计师证书编号',u'是否合伙人（股东）',u'批准注册文件号',u'批准注册时间',u'所在事务所',u'本年度应完成学时',u'本年度已完成学时',u'处罚/惩戒信息',u'参加公益活动']
            csv_write.writerow(hand)
        url= 'http://cmispub.cicpa.org.cn/cicpa2_web/07/{}.shtml'.format(str)
        r = requests.get(url)
        r.encoding = 'GB18030'
        soup = BeautifulSoup(r.text, 'html.parser')
        list = []
        for k in soup.find_all('td',class_='data_tb_content'):
            new = k.get_text()
            new = new.strip()
            new = new.encode("utf-8")
            list.append(new)
        csv_write.writerow(list)
        return None
    
    def post(self,text):
        # print r.text
        while True: 
            try:
                # Only success can jump out of the loop, so when you find that there is no data for a long time,
                # it is very likely that all the data has been downloaded, and of course,
                # the network problem on your machine is not ruled out.
                r = requests.post(self.url,data=text)
                soup = BeautifulSoup(r.text, 'html.parser')
                for k in soup.find_all('tr', class_='rsTr'):
                    for a in k.find_all('a'):
                        new = str(a)[32:64]
                        self.get(new)
                break
            except Exception,e:
                print e,'error'
    def my_encode(self,str):
        new_str = str.encode(encoding='gbk',errors='strict')
        new_str = new_str.replace('\\x','%')
        new_str = new_str.upper()
        return new_str
if __name__ == '__main__':
    start_time = datetime.datetime.now()
    spiker = Spiker(link)
    for i in range(1,10000):
        # Download 15 pieces of data from page 1
        text = {'method':'indexQuery','queryType':'2','isStock':'00','pageSize':15,'pageNum':i,'ascGuid':'','offName':'','perCode':'','perName':''}
        spiker.post(text)
    # spiker.geat('AF082116FCF899E07A7D9CE45A51D940')
    end_time = dtetime.datetime.now()
    print end_time-start_time