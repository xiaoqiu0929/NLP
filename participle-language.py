import nltk

sentence = """At eight o'clock on Thursday morning
Arthur didn't feel very good. New York is a well-kown city"""
tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
tagged

