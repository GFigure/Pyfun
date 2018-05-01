# -*- coding:utf-8 -*-
__author__ = "東飛"
__date__ = "2018-5-1"

from PIL import Image
import os
import sys

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)  # f 变量是除扩展名以外的文件名，e 变量是扩展名
    outfile = f + ".png"  # 拼凑输出文件名
    if infile != outfile:  # 保存的图像格式跟原图像格式不一样
        try:
            # img = Image.open(infile)
            Image.open(infile).convert("RGBA").save('./img/' + outfile)  # 转换图像格式
        except IOError:
            print("Cannot convert", infile)  # 图像无法打开，则处理异常
