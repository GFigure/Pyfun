# -*- coding:utf-8 -*-
__author__ = "東飛"
__date__ = "2018-5-1"

from PIL import Image
def roll(image, delta):
    "Roll an image sideways"
    xsize, ysize = image.size
    delta = delta % xsize  # 翻卷多少像素
    if delta == 0: return image   # 不翻卷图形
    part1 = image.crop((0, 0, delta, ysize))  # 左边矩形选区
    part2 = image.crop((delta, 0, xsize, ysize))  # 右边矩形选区
    part1.load()
    part2.load()
    image.paste(part2, (0, 0, xsize-delta, ysize)) # 原右边图形贴到左边
    image.paste(part1, (xsize-delta, 0, xsize, ysize))  # 原左边图形贴到右边
    return image

img = Image.open('./img/avatar.jpg')
print(img.size)
roll(img,100).save('./img/avatar_roll.jpg','JPEG')