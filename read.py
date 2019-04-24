# -*- coding: utf-8 -*-
'''
@create: yiquriyue(yiquriyue@outlook.com)
@datetime: 2019-04-10
@description: This function will read the name of the accountant in your CSV file and the information of all
              transactions, and find the corresponding data in the monitor. If found, write the information into it,
              otherwise only write the data you provide.
'''
import csv
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf8') 
csvFile = open('return.csv','r')
reader = csv.reader(csvFile)
data = {}
for item in reader:
    if item and item[0]:
        name = item[0]
        data[name] = []
        data[name].append(item)
def read_csv(file_path):
    csvFile = open(file_path, "r")
    reader = csv.reader(csvFile)
    out = codecs.open("{}_new.csv".format(file_path),'w+','utf-8')
    csv_write = csv.writer(out)
    data_a = []
    a = 0
    b = 0
    for item in reader:
        new_item = []
        for i in item :
            # try:
                # i = i.decode('gb2312').encode('utf-8')
            # except:
                # pass
            new_item.append(i)
        if new_item and new_item[0]:
            name = new_item[0]
            office = new_item[7]
            count,old_list = find(name,office)
        else:
            count = 0
            old_list = []
        # count,old_list = find(name,office)
        list = []
        if old_list:
            child_list = []
            for i in old_list[0]:
                try:
                    i = i.decode('ascii').encode('utf-8')
                except:
                    pass
                child_list.append(i)
            list.append(child_list)
        if count!=1:
            a = a + 1
            csv_write.writerow(new_item)
        else:
            b = b + 1
            try:
                newlist = [new_item[0],new_item[1],new_item[2],new_item[3],new_item[4],new_item[5],new_item[6],new_item[7],new_item[8],new_item[9],new_item[10],new_item[11],new_item[12],list[0][1],list[0][2],list[0][3],list[0][4],list[0][5],list[0][6],list[0][7],list[0][8],list[0][10],list[0][12],list[0][14],list[0][15]]
                csv_write.writerow(newlist)
            except:
                csv_write.writerow(new_item)
                print newlist
    print a,b
    csvFile.close()

def find(name,office):
    # Here, I define a rule, first of all, the matching name, if there is only one then return the data, if not,
    # then return 0, if there are more than one matching firm, this return, if there is only one then return the data,
    # if not, return 0, if there are more than one number of returns. When choosing, in order to be cautious,
    # the data returned to 1 is selected and the rest is discarded.
    if data.has_key(name):
        if len(data[name])==1:
            return 1,data[name]
        else:
            i=0
            result = []
            for a in data[name]:
                if a[15] == office:
                    i = i + 1
                    result.append(a)
                else:
                    pass
            return i,result
                
    else:
        return 0,False
if __name__ == '__main__':
    # you file
    read_csv('bb.csv')
    