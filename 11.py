import numpy as np

class GraphBasedDependencyParser:
    def __init__(self, sentence, weights):
        """
        :param sentence: 输入句子
        :param weights: 权重矩阵，表示依存关系边的权重
        """
        self.sentence = ['ROOT'] + sentence.split()  # 在句子前面添加 ROOT 节点
        self.n = len(self.sentence)
        self.weights = weights  # 依存关系权重矩阵
        self.tree = []  # 最终的依存树，保存依存关系（父节点, 子节点）

    def parse(self):
        """
        使用 Chu-Liu/Edmonds 算法解析句子，寻找最大生成树
        """
        # 使用 Chu-Liu/Edmonds 算法找到最大生成树
        mst = self.chu_liu_edmonds()
        return mst

    def chu_liu_edmonds(self):
        """
        Chu-Liu/Edmonds 算法实现，寻找依存图的最大生成树
        """
        parent = [-1] * self.n  # 保存每个节点的父节点
        for i in range(1, self.n):
            max_weight = -float('inf')
            max_parent = -1
            for j in range(self.n):
                if i != j and self.weights[j][i] > max_weight:  # 找到最大权重的边
                    max_weight = self.weights[j][i]
                    max_parent = j
            parent[i] = max_parent  # 记录父节点
            self.tree.append((self.sentence[max_parent], self.sentence[i]))

        return self.tree

# 示例句子
sentence = "I love NLP"
# 权重矩阵（示例），表示句子中每对词的依存关系权重
weights = np.array([
    [0, 5, 2, 1],  # ROOT 对句中其他词的依存权重
    [0, 0, 3, 2],  # "I" 对句中其他词的依存权重
    [0, 3, 0, 4],  # "love" 对句中其他词的依存权重
    [0, 2, 1, 0]   # "NLP" 对句中其他词的依存权重
])

parser = GraphBasedDependencyParser(sentence, weights)
mst = parser.parse()

# 输出依存树
print("依存树：")
for dep in mst:
    print(f"{dep[0]} -> {dep[1]}")
