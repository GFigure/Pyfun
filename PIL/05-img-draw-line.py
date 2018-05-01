# -*- coding:utf-8 -*-
__author__ = "東飛"
__date__ = "2018-5-1"

from PIL import Image, ImageDraw

im = Image.open('./img/avatar.jpg')
drawAvatar = ImageDraw.Draw(im)
xSize, ySize = im.size
# 三等分位置
drawAvatar.line([0, 0.33 * ySize, xSize, 0.33 * ySize], fill=(255, 100, 0), width=3)

# 左下角到中心点，右下角到中心点
drawAvatar.line([(0, ySize), (0.5 * xSize, 0.5 * ySize), (xSize, ySize)], fill=(255, 0, 0), width=3)
im.save('./img/avatar_line.jpg')

drawAvatar.arc([10,20,100,300],0,270,fill=(255,0,0))
im.save('./img/avatar_arc.jpg')

drawAvatar.text([0.95 * xSize,0.05 * ySize], "那小子真帅", fill = (255,0,0))
im.save('./img/avatar_text.jpg')