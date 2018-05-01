# -*- coding:utf-8 -*-
__author__ = "東飛"
__date__ = "2018-5-1"

from PIL import Image, ImageDraw, ImageFont


# 需要传入参数：字符串，字体颜色
def drawText(text, color, imageName, new_imageName):
    avatar = Image.open(imageName)
    drawAvatar = ImageDraw.Draw(avatar)
    xSize, ySize = avatar.size
    # 指定字体大小
    fontSize = min(xSize, ySize) // 12
    # 引用本地TrueType格式的字体文件，创建一个ImageFont实例
    myFont = ImageFont.truetype('consola.ttf', fontSize)
    # 在图片上写字，y轴位置根据字体大小变化，fill参数指定字的颜色，font参数必须是ImageFont实例的值
    drawAvatar.text([0.9 * xSize, 0.1 * ySize - fontSize], text, fill=color, font=myFont)
    avatar.save(new_imageName)


if __name__ == '__main__':
    color = (255, 0, 0)
    drawText('9', color, './img/avatar.jpg', './img/avatar_new.jpg')
