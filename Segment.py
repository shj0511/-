import jieba
jieba.load_userdict("mydict.txt")
import pynlpir as pl
pl.open()

def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def sent2word(sentence):
    # seglist=pl.segment(sentence.strip(),pos_tagging=False)
    # print(seglist)
    seglist=jieba.cut(sentence.strip())
    stopwords=stopwordslist('stopwords.txt')
    outstr=''
    # for word in range(len(seglist)):
    for word in seglist:
        # word=seglist[i]
        if word not  in stopwords:
            if word!='\t':
                outstr += word
                outstr += ' '
    return outstr
def seg(filein,fileout):


    inputs=open(filein,'r',encoding='utf-8')

    outputs=open(fileout,'w',encoding='utf-8')

    for line in inputs:
        line=sent2word(line)
        outputs.write(line+'\n')



    outputs.close()
    inputs.close()

seg('posmeituan.txt','posout.txt')
seg('negmeituan.txt','negout.txt')
# seg('trainmodle.txt','trainmodle1.txt')
# seg('negtest.txt','neg_test_cut.txt')
# seg('postest.txt','pos_test_cut.txt')