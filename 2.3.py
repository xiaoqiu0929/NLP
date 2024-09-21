class TransitionBasedParser:
    def __init__(self, sentence):
        # 初始化句子和依存关系存储
        self.sentence = sentence.split()  # 将句子按空格分割为单词
        self.stack = []  # 栈
        self.buffer = self.sentence.copy()  # 缓冲区，初始时为整个句子
        self.dependencies = []  # 存储依存关系

    def parse(self):
        # 解析句子的主函数
        while self.buffer or len(self.stack) > 1:
            if len(self.stack) >= 2 and self.can_reduce():
                if self.is_right_arc():
                    self.right_arc()
                elif self.is_left_arc():
                    self.left_arc()
            else:
                self.shift()
        return self.dependencies

    def shift(self):
        # 将缓冲区第一个词推入栈
        if self.buffer:
            word = self.buffer.pop(0)
            self.stack.append(word)
            print(f"SHIFT: 将 '{word}' 推入栈")

    def left_arc(self):
        # 左弧：栈顶词作为依存词，栈第二个词作为中心词
        dep = self.stack.pop(-2)
        head = self.stack[-1]
        self.dependencies.append((head, 'dep', dep))
        print(f"LEFT-ARC: {head} <- {dep}")

    def right_arc(self):
        # 右弧：栈顶词作为中心词，栈第二个词作为依存词
        head = self.stack[-2]
        dep = self.stack.pop(-1)
        self.dependencies.append((head, 'dep', dep))
        print(f"RIGHT-ARC: {head} -> {dep}")

    def can_reduce(self):
        # 简单判断是否可以进行弧操作（根据实际场景可以更加复杂）
        return len(self.stack) >= 2

    def is_left_arc(self):
        # 假设简单规则：如果栈第二个词是主语，则进行LEFT-ARC（可更复杂化）
        return self.stack[-2] == 'I'

    def is_right_arc(self):
        # 假设简单规则：其他情况进行RIGHT-ARC（可更复杂化）
        return True


# 示例句子：I love NLP
sentence = "I love NLP"
parser = TransitionBasedParser(sentence)
dependencies = parser.parse()

# 输出依存关系
print("依存关系：")
for dep in dependencies:
    print(f"{dep[0]} -[{dep[1]}]-> {dep[2]}")
