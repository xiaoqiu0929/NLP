from gensim.models import word2vec
from multiprocessing import cpu_count

# 加载文本数据
dataset = word2vec.Text8Corpus('text8')
data = [d for d in dataset]

# 使用前1000个句子作为训练数据
data_part1 = data[:1000]

# 构建word2vec模型
model = word2vec.Word2Vec(data_part1, min_count=0, workers=cpu_count())

# 保存模型
model.save('word2vec_model')

# 加载模型
model = word2vec.Word2Vec.load('word2vec_model')

# 查看与某个词相似的词
similar_words = model.wv.most_similar('word')
print(similar_words)