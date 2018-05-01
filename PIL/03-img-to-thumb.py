# -*- coding:utf-8 -*-
__author__ = "東飛"
__date__ = "2018-5-1"

import os, sys
from PIL import Image

print(sys.argv[1:])
for infile in sys.argv[1:]:
    print(infile)
    outfile = os.path.splitext(infile)[0] + ".thumbnail"  # 缩略图文件名+后缀
    if infile != outfile:
        try:
            im = Image.open(infile)  # 打开图像
            x, y = im.size  # 获取原图像的大小（width、height）
            im.thumbnail((x // 2, y // 2))  # 缩略图大小
            im.save('./img/' + outfile, "JPEG")  # 保存为 JPEG 格式
        except IOError:
            print("cannot create thumbnail for", infile)
