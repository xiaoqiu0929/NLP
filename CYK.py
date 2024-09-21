def convert_to_cnf(grammar):
    # 辅助函数：将上下文无关文法转换为Chomsky范式（如有必要）
    # 在这里假设输入的文法已经是CNF形式
    return grammar


# CYK算法实现
def cyk_parse(sentence, grammar):
    # 将句子分割为单词
    words = sentence.split()  # 例如: "the cat chased the dog" -> ["the", "cat", "chased", "the", "dog"]
    n = len(words)  # 句子中单词的数量

    # 初始化一个二维解析表P，P[i][j]存储从words[i]到words[j]能生成的非终结符集合
    P = [[set() for _ in range(n)] for _ in range(n)]

    # 将文法转换为Chomsky范式（如果文法不是CNF形式）
    grammar = convert_to_cnf(grammar)

    # 步骤1：初始化表格，每个单词对应的非终结符
    for i, word in enumerate(words):
        for lhs, rhs in grammar:
            if rhs == [word]:  # 如果文法规则A -> word，表示A可以生成这个单词
                P[i][i].add(lhs)  # 将A放入P[i][i]，表示A可以生成words[i]

    # 步骤2：通过动态规划填充表格，处理跨度为2到n的子串
    for length in range(2, n + 1):  # 从跨度2开始，遍历每个子句的长度
        for i in range(n - length + 1):  # 子串的起始位置
            j = i + length - 1  # 子串的结束位置
            for k in range(i, j):  # 尝试所有可能的分割点k
                for lhs, rhs in grammar:
                    if len(rhs) == 2:  # 确保文法规则是二元规则A -> BC
                        B, C = rhs  # 右侧的两个非终结符
                        # 如果P[i][k]包含B，且P[k+1][j]包含C，则A可以生成words[i:j]
                        if B in P[i][k] and C in P[k + 1][j]:
                            P[i][j].add(lhs)  # 将A加入P[i][j]

    # 步骤3：检查表格的最后一格P[0][n-1]是否包含起始符号'S'
    return 'S' in P[0][n - 1]  # 如果包含S，则说明句子符合文法


# 示例文法（已为Chomsky范式）
grammar = [
    ('S', ['NP', 'VP']),  # S -> NP VP
    ('NP', ['Det', 'N']),  # NP -> Det N
    ('VP', ['V', 'NP']),  # VP -> V NP
    ('Det', ['the']),  # Det -> 'the'
    ('N', ['cat']),  # N -> 'cat'
    ('N', ['dog']),  # N -> 'dog'
    ('V', ['chased'])  # V -> 'chased'
]

# 示例句子
sentence = "the cat chased the dog"

# 调用CYK算法解析句子
if cyk_parse(sentence, grammar):
    print("该句子符合文法！")
else:
    print("该句子不符合文法。")
