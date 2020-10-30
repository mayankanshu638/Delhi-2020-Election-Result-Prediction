# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:24:16 2020

@author: Mayank$AGGARWAL
"""

aap=['aap','kejri','muffler','aam','admi','arvi','jhadu','jhado']
bjp=['bjp','modi','naren','bharat','janta','lotus','kamal','pm','prime','chowkidar','kml']
inc=['congress','rahul','gandhi','indira','sonia','pappu','hath','inc','national']

# Python3 code to demonstrate working of 
# Frequency of substring in string  
# Using count() 
import os
import re
a=0
b=0
ic=0
text="mmmodi999modi 99modi99m narendra mayank aap modi modiiii mmodi narendramodi gandhiaaaaaaa"
for i in aap:
    res=text.count(str(i))
    if res > 0:
       text=re.sub('[0-9|a-z]*'+i+'[a-z|0-9]*', '',text)
       a=a+res
for i in bjp:
    res=text.count(str(i))
    if res > 0:
       text=re.sub('[0-9|a-z]*'+i+'[a-z|0-9]*', '',text)
       b=b+res
for i in inc:
     res=text.count(str(i))
     if res > 0:
        text=re.sub('[0-9|a-z]*'+i+'[a-z|0-9]*', '',text)
        ic=ic+res
if a==0 and ic==0:
    print("aap")
    
    
m=100
n=12
if m==100 or n==121:
    print("HEllo")
    
os.mkdir(r"C:\Users\hp\Desktop\Election\mayank")


"""for i in mention:
    print(i[1:])"""
    
import re  
import csv 
m = []
h = []
with open('EnglishTextWithoutURLinLowerCase.csv', 'r',encoding="utf8") as read_obj:
    csv_reader = csv.reader(read_obj)
    for row in csv_reader:
        t1=[]
        t2=[]
        t1=re.findall(r'[@]\w+', row[1])
        m=m+t1
        t2=re.findall(r'[#]\w+', row[1])
        h=h+t2
        print(row[0],t1,t2)

read_obj.close()

mention = []
hashtag =[]
for i in m:
    mention.append(i[1:])
for i in h:
    hashtag.append(i[1:])
mh=mention+hashtag
fmention=list(set(mention))
fhashtag=list(set(hashtag))
mhf=list(set(mh))


write_obj=open("Keywords.csv","w",encoding='utf-8',newline='')
csv_writer=csv.writer(write_obj)
csv_writer.writerow(["Sno","Keywords","Frequency"])
counter=0
for i in mhf:
    counter=counter+1
    t=[]
    t.append(counter)
    t.append(i)
    t.append(mh.count(i))
    csv_writer.writerow(t)
    
write_obj.close()



import pandas as pd 
  
#making data frame from csv file 
data=pd.read_csv("Keywords.csv") 
  
#sorting data frame by Team and then By names 
data.sort_values(["Frequency"], axis=0,
                 ascending=False, inplace=True) 
data.drop(["Sno"], axis = 1, inplace = True)
  
#display 
data.to_csv("KeywordsAccFrequency.csv", index= False) 


dat=pd.read_csv("Keywords.csv") 
  
#sorting data frame by Team and then By names 
qdat.sort_values(["Keywords"], axis=0,
                 ascending=True, inplace=True) 
dat.drop(["Sno"], axis = 1, inplace = True)
  
#display 
dat.to_csv("KeywordsAccKeywords.csv", index= False) 




















