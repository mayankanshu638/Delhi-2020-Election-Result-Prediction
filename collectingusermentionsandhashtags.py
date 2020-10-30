import csv
import re
import pandas as pd 
january=['03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
february=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','22']
for i in january:
    m = []
    h = []
    with open(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\FinalJanWithoutURL"+str(i)+".csv", 'r',encoding="utf8") as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            t1=[]
            t2=[]
            t1=re.findall(r'[@]\w+', row[2])
            m=m+t1
            t2=re.findall(r'[#]\w+', row[2])
            h=h+t2
            print(row[2],t1,t2)
    read_obj.close()
    mention = []
    hashtag =[]
    for j in m:
        mention.append(j[1:])
    for j in h:
        hashtag.append(j[1:])
    mh=mention+hashtag
    fmention=list(set(mention))
    fhashtag=list(set(hashtag))
    mhf=list(set(mh))
    
    
    write_obj=open(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\Keywords.csv","w",encoding='utf-8',newline='')
    csv_writer=csv.writer(write_obj)
    csv_writer.writerow(["Sno","Keywords","Frequency"])
    counter=0
    for j in mhf:
        counter=counter+1
        t=[]
        t.append(counter)
        t.append(j)
        t.append(mh.count(j))
        csv_writer.writerow(t)      
    write_obj.close()
    data=pd.read_csv(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\Keywords.csv")  
    data.sort_values(["Frequency"], axis=0,
                     ascending=False, inplace=True) 
    data.drop(["Sno"], axis = 1, inplace = True)
    data.to_csv(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\KeywordsAccToFrequency.csv", index= False) 
    
for i in february:
    m = []
    h = []
    with open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\FinalFebWithoutURL"+str(i)+".csv", 'r',encoding="utf8") as read_obj:
        csv_reader = csv.reader(read_obj)
        for row in csv_reader:
            t1=[]
            t2=[]
            t1=re.findall(r'[@]\w+', row[2])
            m=m+t1
            t2=re.findall(r'[#]\w+', row[2])
            h=h+t2
            print(row[2],t1,t2)
    read_obj.close()
    mention = []
    hashtag =[]
    for j in m:
        mention.append(j[1:])
    for j in h:
        hashtag.append(j[1:])
    mh=mention+hashtag
    fmention=list(set(mention))
    fhashtag=list(set(hashtag))
    mhf=list(set(mh))
    
    
    write_obj=open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\Keywords.csv","w",encoding='utf-8',newline='')
    csv_writer=csv.writer(write_obj)
    csv_writer.writerow(["Sno","Keywords","Frequency"])
    counter=0
    for j in mhf:
        counter=counter+1
        t=[]
        t.append(counter)
        t.append(j)
        t.append(mh.count(j))
        csv_writer.writerow(t)      
    write_obj.close()
    data=pd.read_csv(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\Keywords.csv")  
    data.sort_values(["Frequency"], axis=0,
                     ascending=False, inplace=True) 
    data.drop(["Sno"], axis = 1, inplace = True)
    data.to_csv(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\KeywordsAccToFrequency.csv", index= False) 
    
    

