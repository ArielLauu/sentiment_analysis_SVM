#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import os
import re
import sys
import warnings
import logging
from gensim import corpora
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')


#jieba.load_userdict(r"Data\基因.txt")


def process_txt(filePath, path):
    # 从html中提取text
    # filePath = r"Data\Gene_text"
    # path = r"G:\知识服务\Zhihu-master\Data\Gene"
    temp = ''
    i = 0
    # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    with open(filePath, 'w', encoding="GBK") as Writer:
        for parent, dirnames, filenames in os.walk(path):
            for filename in filenames:
                subPath=path + '\\' + filename
                with open(subPath,'r+', encoding='gb18030',errors='ignore') as Reader:
                     content=Reader.readlines()
                     print(type(content))
                     Writer.write(str(content)+"\n")
                     i = i + 1




if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])  # 得到文件名
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)

    # 输入文件目录
    inp = r'data\ChnSentiCorp_htl_ba_2000'
    folders = ['neg', 'pos']
    for foldername in folders:
        logger.info("running " + foldername + " files.")
        # 输入文件
        path = inp + '\\' + foldername
        # 输出文件
        filePath = '2000_' + foldername + '.txt'
        process_txt(filePath, path)
        with open(filePath, "r", encoding='gb18030',errors='ignore') as Reader:
            texts = [line.strip() for line in Reader.readlines()]
            #pro_process_cn = pre_process_cn(texts)
            #save_dict(pro_process_cn, 'cn')

    pass

