def forward_max_match(sentence, dictionary, max_word_length):
    sentence_length = len(sentence)
    i = 0
    result = []

    while i < sentence_length:
        # 设置初始窗口长度，尽量匹配最长的词
        end = min(i + max_word_length, sentence_length)

        # 尝试匹配最长的词
        while i < end:
            word = sentence[i:end]
            if word in dictionary:
                result.append(word)
                break
            end -= 1

        # 如果没有匹配的词，将单个字符作为词
        if i == end:
            result.append(sentence[i])
            end = i + 1

        i = end

    return result


# 示例词典
dictionary = {"清华大学", "清华", "北京", "我", "来到"}
max_word_length = max(len(word) for word in dictionary)  # 词典中最长词的长度

# 测试句子
sentence = "我来到北京清华大学"
print(forward_max_match(sentence, dictionary, max_word_length))