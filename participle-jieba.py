import jieba
import jieba.posseg as pseg
seg_list = jieba. cut("我来到北京清华大学", cut_all= True )
print("Full Mode: " + "/ ". join(seg_list)) # 全模式
seg_list = jieba. cut("我来到北京清华大学", cut_all= False )
print("Default Mode: " + "/ ". join(seg_list)) # 精确模式
seg_list = jieba. cut("他来到了网易杭研大厦") # 默认是精确模式
print(", ". join(seg_list))
seg_list = jieba. cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")
print(", ". join(seg_list))

seg_list = jieba.cut("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
import jieba.posseg as pseg
words = pseg.cut("工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作")
for word, flag in words:
    print('%s %s' % (word, flag))