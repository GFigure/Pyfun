# -*- coding:utf-8 -*-
__author__ = "東飛"
__date__ = "2018-5-1"

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机字母（大写）:
def rndChar():
    return chr(random.randint(65, 90))


# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 图片大小：240 x 60
width = 60 * 4
height = 60
# 创建Image对象，背景为白色
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 创建Font对象，字体为“Arial.ttf”
font = ImageFont.truetype('consola.ttf', 36)
# 用随机颜色填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

# 输出4个字母，字母颜色随机
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

# 对图像模糊
image = image.filter(ImageFilter.BLUR)
image.save('./img/code.jpg', 'jpeg')
