import pandas as pd 
from pandas import DataFrame
import csv
data1=pd.read_csv('data.csv')
data=DataFrame(data1)
# a=data.loc[1,'star']
# print(a)
# print(data.info())
del data['number']

def traindata():
    with open('trainmodle.txt','a',encoding='utf-8') as f:
        for row in data['comments']:
            f.write(str(row)+'\n')
# df=data.sort_values(by='star',ascending=False)
traindata()
def classdata():
    pos=open('posmeituan.txt','a',encoding='utf-8')
    neg=open('negmeituan.txt','a',encoding='utf-8')
    for i in range(10000):
       
        
        
        if (int(float(data.loc[i,'star']))>0):
            k=data.loc[i,'comments']
            pos.write(k+'\n')
        if (int(float(data.loc[i,'star']))<0):
            h=data.loc[i,'comments']
            neg.write(h+'\n')
    pos.close()
    neg.close()
#classdata()
def classtestdata():
    pos=open('postest.txt','a',encoding='utf-8')
    neg=open('negtest.txt','a',encoding='utf-8')
    for i in range(1928):
        
        
        if (data.loc[i+10000,'star']>0):
            k=data.loc[i+10000,'comments']
            pos.write(k+'\n')
        if (data.loc[i+10000,'star']<0):
            h=data.loc[i+10000,'comments']
            neg.write(h+'\n')
    pos.close()
    neg.close()
classtestdata()