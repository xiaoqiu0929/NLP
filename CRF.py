import pycrfsuite

# 准备特征函数
def word2features(sent, i):
    word = sent[i][0]
    features = [
        'bias',
        f'word={word}',
        f'word[-1]={word[-1]}',
    ]

    if i > 0:
        prev_word = sent[i - 1][0]
        features.append(f'prev_word={prev_word}')
    else:
        features.append('BOS')

    if i < len(sent) - 1:
        next_word = sent[i + 1][0]
        features.append(f'next_word={next_word}')
    else:
        features.append('EOS')

    return features

# 生成句子的特征
def sent2features(sent):
    return [word2features(sent, i) for i in range(len(sent))]

# 生成句子的标签
def sent2labels(sent):
    return [label for _, label in sent]

# 训练数据
train_sents = [
    [('我', 'B'), ('喜欢', 'S'), ('吃', 'B'), ('苹果', 'E')],
    [('你', 'B'), ('喝', 'B'), ('茶', 'S')],
]

X_train = [sent2features(s) for s in train_sents]
y_train = [sent2labels(s) for s in train_sents]

# 训练 CRF 模型
trainer = pycrfsuite.Trainer()
for xseq, yseq in zip(X_train, y_train):
    trainer.append(xseq, yseq)

# 设置参数
trainer.set_params({
    'c1': 1.0,  # L1正则化
    'c2': 0.1,  # L2正则化
    'max_iterations': 100,  # 最大迭代次数
    'feature.possible_transitions': True
})

trainer.train('crf_model.crfsuite')

# 加载模型并进行预测
tagger = pycrfsuite.Tagger()
tagger.open('crf_model.crfsuite')

# 新的测试句子
test_sent = [('我',), ('想',), ('吃',), ('苹果',)]
X_test = sent2features(test_sent)
y_pred = tagger.tag(X_test)

# 输出分词结果（中文）
print("预测的标签：", y_pred)
