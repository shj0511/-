#
# from bs4 import BeautifulSoup
# import requests
#
# with requests.session() as s:
#     url = 'https://club.jd.com/comment/productPageComments.action'
#     data = {
#         'productId':'3888284',
#         'score':0,
#         'sortType':5,
#         'pageSize':10,
#         'isShadowSku':0,
#         'page':0
#     }
#     r = s.get(url, params = data)
#     print(r.json())
#
#
#
# import pynlpir as pl
# pl.open()
# outstr=''
# with open("pos_test.txt",'r',encoding='utf-8') as file:
#     for line in file:
#         line=pl.segment(line,pos_tagging=False)
#
#         for i in range(len(line)):
#             outstr+=str(line[i])
#             outstr+=' '
#     print(outstr)
# import requests as re
# import json
# from bs4 import BeautifulSoup
# def getid(tag,start):
#
#         ur="https://movie.douban.com/j/search_subjects?type=movie&tag={0}&sort=recommend&page_limit=20&page_start={1}".format(tag,start)
#         result=re.get(ur).text
#         data=json.loads(result)
#         for j in range(20):
#                 try:
#                         print (data['subjects'][j]['id'])
#
# # print(data['subjects'][j]['id'],' | ',data['subjects'][j]['title'],' | ',data['subjects'][j]['rate'])
#                 except:
#                         continue
# list=['爱情',['科幻'],['动作'],['悬疑'],['恐怖'],['成长'],['喜剧']]
# for i in range (10):
#         try:
#                 getid('科幻',i*20)
#                 # with open('id.txt','a',encoding='utf8') as file:
#                 #         file.writelines(moveid)
#         except:
#                continue
# import requests as re
# from bs4 import BeautifulSoup
# url="https://movie.douban.com/subject/26647117/comments?start=0&limit=20&sort=new_score&status=P&percent_type=h"
# result=re.get(url=url)
#
# soup=BeautifulSoup(result.text,'html.parser')
# print(soup)
# y=soup.select('.comment-item')[0].p.text
# print(y)

# import nltk
# text=open('negout.txt','r',encoding='utf-8').read()
# postext=open('posout.txt','r',encoding='utf-8').read()
# # print(len(text)/len(set(text)))
# # print(text.count(''),postext.count(''))
# print(sorted(set(text[:10])))
# print(sorted(set(postext[:100])))
# fdist=nltk.FreqDist(text)
# fdist.plot(30,cumulative=True)
import  jieba
import matplotlib.pyplot as plt
import pickle
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
word_lst=[]
word_lst2=[]
word_dict = {}
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

with open('posout.txt','r',encoding='utf-8') as wf, open("poskehuan.csv", 'w',encoding='utf-8') as wf2:

    word_lst=jieba.cut(wf.read().strip())
    stopwords=stopwordslist('stopwords.txt')
    for word in word_lst:
        if word not in stopwords:
            word_lst2.append(word)
    # for i in word_lst:
    #     print(i)


    for item in word_lst2:

        if item not in word_dict:

            word_dict[item] = 1
        else:
            word_dict[item] += 1

    for key in word_dict:
        print(key, word_dict[key])
        wf2.write(key + ',' + str(word_dict[key]) + '\n')
import codecs



# 第一次运行程序时将分好的词存入文件
text = ''
with open('poskehuan.txt','r',encoding='utf-8') as fin:
    for line in fin.readlines():
        line = line.strip('\n')
        # text += ' '.join(jieba.cut(line))
        text += ' '
fout = open('poskehuan.txt','wb',encoding='utf-8')
pickle.dump(text,fout)
fout.close()
fr = open('poskehuan.txt','rb',encoding='utf-8')
text = pickle.load(fr)

backgroud_Image = plt.imread('girl.jpg')
wc = WordCloud( background_color = 'white',    # 设置背景颜色
                mask = backgroud_Image,        # 设置背景图片
                max_words = 2000,            # 设置最大现实的字数
                stopwords = STOPWORDS,        # 设置停用词
                font_path = 'C:/Users/Windows/fonts/msyh.ttf',# 设置字体格式，如不设置显示不了中文
                max_font_size = 50,            # 设置字体最大值
                random_state = 30,            # 设置有多少种随机生成状态，即有多少种配色方案
                )
wc.generate(text)
image_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func = image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()