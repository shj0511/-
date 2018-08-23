import logging
from  gensim.models  import word2vec
from gensim.models.word2vec import  Word2Vec
from  gensim.models.word2vec import  LineSentence
logging.basicConfig(format = '%(asctime)s : %(levelname)s : %(message)s', level = logging.INFO)
# sentcens=word2vec.Text8Corpus('allpos.txt')
model = Word2Vec(LineSentence('trainmodle1.txt'),sg=1,size=300,min_count=3,window=8, hs=1,min_alpha=0.15,)
model.save('meituan.model')
