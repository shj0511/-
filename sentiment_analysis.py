# -*- coding: utf-8 -*-
import jieba
from sklearn.naive_bayes import  MultinomialNB,GaussianNB

from gensim.models.word2vec import Word2Vec
from gensim.models import word2vec
import logging
import os
import re
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
from sklearn.svm import  SVC

#导入训练模型

model=word2vec.Word2Vec.load('meituan.model')

def getword(wordlist):
    vecs=[]
    for word in wordlist:
        word=word.replace('\n','')
        try:
            vecs.append(model[word])
        except:
            continue

    return np.array(vecs,dtype='float')


def buidwordvec(filename):
    posinput=[]
    file= open(filename,'r',encoding='utf-8') .readlines()

    for line in file:
        resultlist=getword(line)

        if len(resultlist)!=0:
            resultarray=sum(np.array(resultlist))/len(resultlist)

 
            posinput.append(resultarray)
#    print(posinput)
    return posinput
def sentiment_a(file1,file2):
    posinput=buidwordvec(file1)

    neginput=buidwordvec(file2)

    y=np.concatenate((np.ones(len(posinput)),np.zeros(len(neginput))))



    X=posinput[:]
    for neg in neginput:
        X.append(neg)
    X=np.array(X)
    # # X=scale(X)
    # pca=PCA.fit(X)
    # plt.figure(1, figsize=(4, 3))
    # plt.clf()
    # plt.axes([.2, .2, .7, .7])
    # plt.plot(pca.explained_variance_, linewidth=2)
    # plt.axis('tight')
    # plt.xlabel('n_components')
    # plt.ylabel('explained_variance_')
    # X= PCA(n_components = 200).fit_transform(X)


    # for i in range(20):
    clf=SVC(kernel='rbf',C=3, decision_function_shape='ovr')
    # clf=GaussianNB()

    clf.fit(X,y)

    pos_test=buidwordvec('pos_test_cut.txt')
    neg_test=buidwordvec('neg_test_cut.txt')
    pos_test=np.array(pos_test)
    neg_test=np.array(neg_test)
    x_test=np.concatenate((pos_test,neg_test))
    # x_test=PCA(n_components = 200).fit_transform(x_test)
    y_test=np.concatenate((np.ones(len(pos_test)),np.zeros(len(neg_test))))
    # print(clf.predict(x_test))
    # print(len(y_test))
    s=clf.score(x_test,y_test)
    print(str(s))
    return(s)
sentiment_a('posout.txt','negout.txt')














# r=model.similarity('肯尼迪','巴顿')
# print("肯尼迪 巴顿 相似度  ："+str(r))
#
# r1=model.doesnt_match("肯尼迪  巴顿  美国  德国".split())
# print("肯尼迪  巴顿  美国  德国 中不合群的词  ："+r1)
#
# r2=model.most_similar("新鲜",topn=8)
# print(r2)
#print(model.most_similar("将军",topn=5))
# print(model["美国"])
# def getwordvecs(wordlist):
#     vec=[]
#     for word in wordlist:
#         word=word.replace('\n',' ')
#         try:
#             vec.append(model[word].shape(1,300))
#         except KeyError:
#             continue
#     return np.array(vec,dtype=float)

# with open("posfile",'r',encoding='utf-8') as file:
#     posword=file.readlines()
# with open("negfile",'r',encoding='utf-8') as file:
#     negword=file.readlines()
#
# pos_vecs=getwordvecs(posword)
# neg_vecs=getwordvecs(negword)
