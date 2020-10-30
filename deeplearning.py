from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
import pandas as pd
import matplotlib.pyplot as plt
import os 
import numpy as np
pipeline = Pipeline(
            [
                ('vect', CountVectorizer()),
                ('tfidf', TfidfTransformer()),
                ('clf', SGDClassifier(
                    loss='hinge',
                    penalty='l2',
                    alpha=1e-3,
                    random_state=42,
                    max_iter=100,
                    learning_rate='optimal',
                    tol=None,
                )),
            ]
        )

df = pd.read_csv(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb01\aap.csv", header=None, usecols=[2])
train_df=pd.read_csv(r"C:\Users\hp\Desktop\Election\Datewise\Dataset\training.csv")
learner = pipeline.fit(train_df['text'],train_df['truth'])
'''
Training the model
'''

test_df = pd.read_csv(r"C:\Users\hp\Desktop\Election\Datewise\Dataset\test.csv")
df['pred'] = learner.predict(df[2])
test_df.to_csv(r"C:\Users\hp\Desktop\Election\Datewise\Dataset\prediction_of_svm.csv",index = False)

pop=0

january=['03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
february=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','22']
jaapv=list()
jbjpv=list()
jincv=list()
faapv=list()
fbjpv=list()
fincv=list()
for i in january:
    count =0
    if os.stat(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\\cleanaap.csv").st_size != 0:
        dfa=pd.read_csv(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\\cleanaap.csv", header=None, usecols=[2])
        dfa['pred'] = learner.predict(dfa[2])
        for j in dfa['pred']:
            pop+=1
            if j==1:
                count+=1
        jaapv.append(count)       
    else:
        jaapv.append(count)
    count =0
    if os.stat(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\\cleanbjp.csv").st_size != 0:
        dfa=pd.read_csv(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\\cleanbjp.csv", header=None, usecols=[2])
        dfa['pred'] = learner.predict(dfa[2])
        for j in dfa['pred']:
            pop+=1
            if j==1:
                count+=1
        jbjpv.append(count)       
    else:
        jbjpv.append(count)
    count =0
    if os.stat(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\\cleaninc.csv").st_size != 0:
        dfa=pd.read_csv(r"C:\Users\hp\Desktop\Election\Datewise\January\Jan"+str(i)+"\\cleaninc.csv", header=None, usecols=[2])
        dfa['pred'] = learner.predict(dfa[2])
        for j in dfa['pred']:
            pop+=1
            if j==1:
                count+=1
        jincv.append(count)       
    else:
        jincv.append(count)
   
    
for i in february:
    count =0
    if os.stat(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\\cleanaap.csv").st_size != 0:
        dfa=pd.read_csv(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\\cleanaap.csv", header=None, usecols=[2])
        dfa['pred'] = learner.predict(dfa[2])
        for j in dfa['pred']:
            pop+=1
            if j==1:
                count+=1
        faapv.append(count)       
    else:
        faapv.append(count)
    count =0
    if os.stat(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\\cleanbjp.csv").st_size != 0:
        dfa=pd.read_csv(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\\cleanbjp.csv", header=None, usecols=[2])
        dfa['pred'] = learner.predict(dfa[2])
        for j in dfa['pred']:
            pop+=1
            if j==1:
                count+=1
        fbjpv.append(count)       
    else:
        fbjpv.append(count)
    count =0
    if os.stat(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\\cleaninc.csv").st_size != 0:
        dfa=pd.read_csv(r"C:\Users\hp\Desktop\Election\Datewise\February\Feb"+str(i)+"\\cleaninc.csv", header=None, usecols=[2])
        dfa['pred'] = learner.predict(dfa[2])
        for j in dfa['pred']:
            pop+=1
            if j==1:
                count+=1
        fincv.append(count)       
    else:
        fincv.append(count)
index = np.arange(len(january))
jaapv=3*np.array(jaapv)
jbjpv=8*np.array(jbjpv)
jincv=10*np.array(jincv)
plt.bar(index+0.25,jaapv/max(jaapv),color = 'g', width = .25)
plt.bar(index+0.50,jbjpv/max(jbjpv),color = 'r', width = .25)
plt.bar(index+0.75,jincv/max(jincv),color = 'b', width = .25)
plt.xlabel('Dates', fontsize=10)
plt.ylabel('No of Votes', fontsize=10)
plt.xticks(index, january, fontsize=8, rotation=00)
plt.title('January')
plt.show()
index = np.arange(len(february))
faapv=3*np.array(faapv)
fbjpv=70*np.array(fbjpv)
fincv=70*np.array(fincv)
plt.bar(index+0.25,faapv/max(faapv),color = 'g', width = .25)
plt.bar(index+0.50,fbjpv/max(fbjpv),color = 'r', width = .25)
plt.bar(index+0.75,fincv/max(fincv),color = 'b', width = .25)
plt.xlabel('Dates', fontsize=10)
plt.ylabel('No of votes', fontsize=10)
plt.xticks(index, february, fontsize=10, rotation=00)
plt.title('February')
plt.show()

import numpy as np
index = np.arange(len(january))
jaapv=3*np.array(jaapv)
jbjpv=8*np.array(jbjpv)
jincv=10*np.array(jincv)
plt.plot(january,jaapv/max(jaapv) , color='g')
plt.plot(january,jbjpv/max(jbjpv), color='r')
plt.plot(january,jincv/max(jincv), color='b')
plt.xlabel('Dates', fontsize=10)
plt.ylabel('No of Votes', fontsize=10)
plt.xticks(index, january, fontsize=8, rotation=00)
plt.title('January')
plt.show()
index = np.arange(len(february))
faapv=3*np.array(faapv)
fbjpv=70*np.array(fbjpv)
fincv=70*np.array(fincv)
plt.plot(february,faapv/max(faapv) , color='g')
plt.plot(february,fbjpv/max(fbjpv), color='r')
plt.plot(february,fincv/max(fincv), color='b')
plt.xlabel('Dates', fontsize=10)
plt.ylabel('No of votes', fontsize=10)
plt.xticks(index, february, fontsize=10, rotation=00)
plt.title('February')
plt.show()











