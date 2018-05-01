# -*- coding:utf-8 -*-
__author__ = "東飛"
__date__ = "2018-5-1"

from PIL import Image
img = Image.open('./img/avatar.jpg')

# Image实例有5个属性，如下：
# format : 返回图像的格式(PNG,JPG,None等)。如果图像不是从文件读取的，它的值就是None
# mode : 返回图像的模式。常用模式有 L (luminance) 表示灰度图像, RGB 表示真彩色图像, and CMYK 表示出版图像。官方说明-图像模式完整列表
# size : 是一个二元tuple，包含width和height（宽度和高度，单位都是px）
# palette : 仅当 mode 为 P 时有效，返回 ImagePalette 实例
# info : 以字典的形式返回实例的信息

print(img.format)
print(img.mode)
print(img.size)
print(img.palette)
print(img.info)
img.show()