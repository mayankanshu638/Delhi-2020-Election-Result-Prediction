# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:21:05 2020

@author: Mayank$AGGARWAL
"""


import csv
import os
import glob

mycsvdir ='\January'
#mycsvdir = '\February'
csvfiles = glob.glob(os.path.join(r'C:\Users\hp\Desktop\Election'+str(mycsvdir),'*csv'))
for csvfile in csvfiles:
    temp = list(csvfile)
    mypath=r"C:\Users\hp\Desktop\Election\Datewise"+str(mycsvdir)+temp[36]+temp[37]+temp[38]+temp[39]+temp[40]+temp[41]
    os.mkdir(mypath)
    csvpath=temp[36]+temp[37]+temp[38]+temp[39]+temp[40]+temp[41]+".csv"
    write_obj=open(str(mypath)+str(csvpath),"w",encoding='utf-8',newline='')
    csv_writer=csv.writer(write_obj)
    with open(csvfile, 'r',encoding="utf8") as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            if row[15]=='or_language':
                  csv_writer.writerow(row)
            if row[15]=='en':
                csv_writer.writerow(row)
            
        
read_obj.close()
write_obj.close()
