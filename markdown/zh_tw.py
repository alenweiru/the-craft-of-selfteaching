from langconv import *
import os
import glob
import ntpath
def Simplified2Traditional(sentence):
    '''
    将sentence中的简体字转为繁体字
    :param sentence: 待转换的句子
    :return: 将句子中简体字转换为繁体字之后的句子
    '''
    sentence = Converter('zh-hant').convert(sentence)
    return sentence
def creatdir():
    root = os.getcwd()
    zh_tw = os.path.join(root,"zh_tw")
    if not os.path.exists(zh_tw):
        os.mkdir(zh_tw)
    return root,zh_tw
if __name__=="__main__":
    root,zh_tw = creatdir()
    md_file = glob.glob(root+'/*.md')
    for file in md_file:
        f = open(file, "r",encoding='UTF-8')
        traditional_sentence = Simplified2Traditional(f.read())
        dest = os.path.join(zh_tw,ntpath.basename(file))
        with open(dest,'a',encoding='UTF-8') as f:
            f.write(traditional_sentence)
        