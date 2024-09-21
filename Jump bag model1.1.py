import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import skipgrams
from tensorflow.keras.layers import Input, Embedding, Dot, Reshape, Dense
from tensorflow.keras.models import Model
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# 1. 数据预处理：准备语料
corpus = ['I love programming with Python', 'Python is great for machine learning',
          'I use Python to build neural networks', 'Deep learning is a powerful tool']
tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
vocab_size = len(tokenizer.word_index) + 1
word_index = tokenizer.word_index

# 2. 创建Skip-Gram数据
sequences = tokenizer.texts_to_sequences(corpus)
pairs, labels = skipgrams(sequences[0], vocabulary_size=vocab_size, window_size=2)

# 3. 定义Skip-Gram模型
embedding_dim = 100
input_target = Input((1,))
input_context = Input((1,))

embedding = Embedding(vocab_size, embedding_dim, input_length=1, name='embedding')
target_embedding = embedding(input_target)
context_embedding = embedding(input_context)

# 计算两个嵌入向量的点积
dot_product = Dot(axes=-1)([target_embedding, context_embedding])
dot_product = Reshape((1,))(dot_product)
output = Dense(1, activation='sigmoid')(dot_product)

model = Model(inputs=[input_target, input_context], outputs=output)
model.compile(optimizer='adam', loss='binary_crossentropy')
model.summary()

# 4. 训练模型
pairs = np.array(pairs)
labels = np.array(labels)
model.fit([pairs[:, 0], pairs[:, 1]], labels, epochs=100, batch_size=64)

# 5. 获取词嵌入
word_embeddings = model.get_layer('embedding').get_weights()[0]

# 6. 可视化词嵌入
def plot_word_embeddings(embeddings, word_index):
    words = list(word_index.keys())
    word_vectors = np.array([embeddings[word_index[word]] for word in words])

    # 使用PCA降维到2D
    pca = PCA(n_components=2)
    reduced_word_vectors = pca.fit_transform(word_vectors)

    # 绘制
    plt.figure(figsize=(10, 10))
    for word, (x, y) in zip(words, reduced_word_vectors):
        plt.scatter(x, y)
        plt.text(x + 0.01, y + 0.01, word, fontsize=12)
    plt.show()

# 可视化词向量
plot_word_embeddings(word_embeddings, word_index)
