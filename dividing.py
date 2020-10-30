
import re
import csv 

january=['03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
february=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','22']
bjp=['bjp4india','bjp','bjp4delhi','narendramodi','amitshah','manojtiwarimp','bjpwinningdelhi','tajinderbagga','bjp45plusindelhi','kapilmishra_ind','manojtiwari','vote4bjp','modi','jpnadda',
     'kamallagerahokejriwal','delhivotesforbjp','pmoindia','dillichalemodikesaath','amitmalviya','yobjpsopredictable','sambitswaraj','bjp_mukt_bharat','voteforbjp','bjpmuktbharat','pmmodi',
     'weloveyoumodiji','naren','modi']

inc=['incindia','congress','rahulgandhi','incdelhi','delhivotesforcongress','priyankagandhi','lambaalka','congresswalidelhi','bjp4karnataka','inc','congressmuktbharat','rahul','gandhi','indira','sonia','pappu','hath']


aap=['arvindkejriwal','aamaadmiparty','aapwinningdelhi','aap','aapketerrorists','voteforjhadu','aapkidilli','msisodia','kejriwaltsunami','vote4jhadu','kejriwalvsentirebjp','kejriwal',
     'kejriwalexposed','aapmanifesto','sanjayazadsln','atishiaap','aapdelhi','aapwithshaheenbagh','lagerahokejriwal','kejriwalphirse','raghav_chadha','manishsisodia','aapburnsdelhi','aapwithterrorists'
     ,'mufflermanreturns','kejriwalchallengesshah','delhiwithkejriwal','aapkidelhi','kejriwalatankwadihai','aapwins','aamadmiparty','aapwasted5years','yogiadityanath','admi','arvi','kejri']


for jan in january:
    write_objaap=open(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(jan)+"\\aap.csv","w",encoding='utf-8',newline='')
    csv_writeraap=csv.writer(write_objaap)
    
    write_objbjp=open(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(jan)+"\\bjp.csv","w",encoding='utf-8',newline='')
    csv_writerbjp=csv.writer(write_objbjp)
    
    write_objinc=open(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(jan)+"\\inc.csv","w",encoding='utf-8',newline='')
    csv_writerinc=csv.writer(write_objinc)
    
    write_objaapd=open(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(jan)+"\\aapd.csv","w",encoding='utf-8',newline='')
    csv_writeraapd=csv.writer(write_objaapd)
    
    write_objbjpd=open(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(jan)+"\\bjpd.csv","w",encoding='utf-8',newline='')
    csv_writerbjpd=csv.writer(write_objbjpd)
    
    write_objincd=open(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(jan)+"\\incd.csv","w",encoding='utf-8',newline='')
    csv_writerincd=csv.writer(write_objincd)
    
    write_objcount=open(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(jan)+"\\count.csv","w",encoding='utf-8',newline='')
    csv_writercount=csv.writer(write_objcount)
 
    with open( r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(jan)+"\FinalJanWithoutURL"+str(jan)+".csv", 'r',encoding="utf8") as read_obj:
        csv_reader = csv.reader(read_obj)
        aa=0
        bb=0
        ii=0
        aad=0
        bbd=0
        iid=0
        for row in csv_reader:
           a=0
           b=0
           ic=0
           text=row[2]
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
           if b==0 and ic==0:
               if a!=0:
                  row.append("arvindkejriwal")
                  aa=aa+1
                  csv_writeraap.writerow(row)
           elif a==0 and ic==0:
               if b!=0:
                  row.append("narendramodi")
                  bb=bb+1
                  csv_writerbjp.writerow(row)
           elif a==0 and b==0:
               if ic!=0:
                   row.append("rahulgandhi")
                   ii=ii+1
                   csv_writerinc.writerow(row)
           else:
               if a>=b and a>=ic:
                   row.append("arvindkejriwal")
                   aad=aad+1
                   csv_writeraapd.writerow(row)
               elif b>=a and b>=ic:
                   row.append("narendramodi")
                   bbd=bbd+1
                   csv_writerbjpd.writerow(row)
               elif ic>=a and ic>=b:
                   row.append("rahulgandhi")
                   iid=iid+1
                   csv_writerincd.writerow(row)
        csv_writercount.writerow(['aap','bjp','congress'])
        csv_writercount.writerow([aa,bb,ii])
        csv_writercount.writerow([aad,bbd,iid])
               
                
    
    read_obj.close()
    write_objincd.close()
    write_objaapd.close()
    write_objbjpd.close()
    
    write_objinc.close()
    write_objaap.close()
    write_objbjp.close()
    write_objcount.close()


    
for feb in february:
    write_objaap=open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(feb)+"\\aap.csv","w",encoding='utf-8',newline='')
    csv_writeraap=csv.writer(write_objaap)
    
    write_objbjp=open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(feb)+"\\bjp.csv","w",encoding='utf-8',newline='')
    csv_writerbjp=csv.writer(write_objbjp)
    
    write_objinc=open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(feb)+"\\inc.csv","w",encoding='utf-8',newline='')
    csv_writerinc=csv.writer(write_objinc)
    
    write_objaapd=open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(feb)+"\\aapd.csv","w",encoding='utf-8',newline='')
    csv_writeraapd=csv.writer(write_objaapd)
    
    write_objbjpd=open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(feb)+"\\bjpd.csv","w",encoding='utf-8',newline='')
    csv_writerbjpd=csv.writer(write_objbjpd)
    
    write_objincd=open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(feb)+"\\incd.csv","w",encoding='utf-8',newline='')
    csv_writerincd=csv.writer(write_objincd)
    
    write_objcount=open(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(feb)+"\\count.csv","w",encoding='utf-8',newline='')
    csv_writercount=csv.writer(write_objcount)
 
    with open( r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(feb)+"\FinalFebWithoutURL"+str(feb)+".csv", 'r',encoding="utf8") as read_obj:
        csv_reader = csv.reader(read_obj)
        aa=0
        bb=0
        ii=0
        aad=0
        bbd=0
        iid=0
        for row in csv_reader:
           a=0
           b=0
           ic=0
           text=row[2]
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
           if b==0 and ic==0:
               if a!=0:
                  row.append("arvindkejriwal")
                  aa=aa+1
                  csv_writeraap.writerow(row)
           elif a==0 and ic==0:
               if b!=0:
                  row.append("narendramodi")
                  bb=bb+1
                  csv_writerbjp.writerow(row)
           elif a==0 and b==0:
               if ic!=0:
                   row.append("rahulgandhi")
                   ii=ii+1
                   csv_writerinc.writerow(row)
           else:
               if a>=b and a>=ic:
                   row.append("arvindkejriwal")
                   aad=aad+1
                   csv_writeraapd.writerow(row)
               elif b>=a and b>=ic:
                   row.append("narendramodi")
                   bbd=bbd+1
                   csv_writerbjpd.writerow(row)
               elif ic>=a and ic>=b:
                   row.append("rahulgandhi")
                   iid=iid+1
                   csv_writerincd.writerow(row)
        csv_writercount.writerow(['aap','bjp','congress'])
        csv_writercount.writerow([aa,bb,ii])
        csv_writercount.writerow([aad,bbd,iid])
               
                
    
    read_obj.close()
    write_objincd.close()
    write_objaapd.close()
    write_objbjpd.close()
    
    write_objinc.close()
    write_objaap.close()
    write_objbjp.close()
    write_objcount.close()

        
     
        

       