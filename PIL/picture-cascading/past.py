# coding: utf-8
#
# @note: 这里两张照片层叠选择的方法是：
#   假设两张照片的同一点的像素分别为 A，B，则层叠之后该点得像素为( alpha 取值在 0 和 1 之间)：
#       A * alpha + B * (1-alpha)
#

import os
import time
import numpy
import random
import numexpr
from PIL import Image, ImageFont, ImageDraw

STAG = time.time()

root = ""       # 脚本的根目录
W_num = 15      # 一行放多少张照片
H_num = 15      # 一列放多少张照片
W_size = 320    # 照片宽为多少
H_size = 180    # 照片高为多少

alpha = 0.5 # 图片透明度
aval = []   # 存放所有照片的路径


# name: getAllPhotos
# todo: 获得所有照片的路径
def getAllPhotos():
    print("正在获取图片路径...")
    STA = time.time()
    root = os.getcwd() + "/"
    src = root + "/photos/"
    for i in os.listdir(src):
        if os.path.splitext(src + i)[-1] == ".jpg" or os.path.splitext(src + i)[-1] == ".png":
            aval.append(src + i)
    print("getAllPhotos Func Time %s" % (time.time() - STA))


# name: transfer
# todo: 将照片转为一样的大小
def transfer(img_path, dst_width, dst_height):
    print("正在重置图片大小...")
    STA = time.time()
    im = Image.open(img_path)
    if im.mode != "RGBA":
        im = im.convert("RGBA")
    resized_img = im.resize((dst_width, dst_height), Image.ANTIALIAS)
    resized_img = resized_img.crop((0, 0, dst_width, dst_height))
    print("transfer Func Time %s" % (time.time() - STA))

    return resized_img


# name: createNevImg
# todo: 创建一张新的照片并保存
def createNevImg():
    # 正在创建一张新的照片并保存...

    iW_size = W_num * W_size
    iH_size = H_num * H_size
    I = numpy.array(transfer(root + "lyf.jpg", iW_size, iH_size))
    I = numexpr.evaluate("""I*(1-alpha)""")

    for i in range(W_num):
        for j in range(H_num):
            SH = I[(j * H_size):((j + 1) * H_size), (i * W_size):((i + 1) * W_size)]
            STA = time.time()
            DA = transfer(random.choice(aval), W_size, H_size)
            print("Cal Func Time %s" % (time.time() - STA))
            res = numexpr.evaluate("""SH+DA*alpha""")
            I[(j * H_size):((j + 1) * H_size), (i * W_size):((i + 1) * W_size)] = res

    img = Image.fromarray(I.astype(numpy.uint8))
    img = img.convert("RGB")
    img.save("createNevImg_%s_past3_1.jpg" % alpha)


# name: newRotateImage
# todo: 将createnevimg中得到的照片旋转，粘贴到另外一张照片中
def newRotateImage():
    imName = "createNevImg_%s_past3_1.jpg" % alpha
    print("正在将图片旋转中...")
    STA = time.time()
    im = Image.open(imName)
    im2 = Image.new("RGB", (W_size * int(W_num + 1), H_size * (H_num + 4)))
    im2.paste(im, (int(0.5 * W_size), int(0.8 * H_size)))
    im2 = im2.rotate(359)
    im2.save("newRotateImage_%s_past3.jpg" % alpha)

    print("newRotateImage Func Time %s" % (time.time() - STA))


# name: writetoimage
# todo: 在图片中写祝福语
def writeToImage():
    print("正在向图片中添加祝福语...")
    STA = time.time()
    img = Image.open("newRotateImage_%s_past3.jpg" % alpha)
    # 字体库，字体大小
    font = ImageFont.truetype('xindexingcao57.ttf', 300)
    draw = ImageDraw.Draw(img)
    draw.ink = 21 + 118 * 256 + 65 * 256 * 256

    # draw.text((0,H_size * 6),unicode("happy every day",'utf-8'),(0,0,0),font=font)

    tHeight = H_num + 1
    draw.text((W_size * 0.5, H_size * tHeight), "happy life written by python", font=font)

    img.save("final_%s_past3.jpg" % alpha)
    # rgb_im = img.convert('RGB')
    # rgb_im.save('final_past.jpg')

    print("writeToImage Func Time %s" % (time.time() - STA))


# name:
# todo: 入口函数
if __name__ == "__main__":
    getAllPhotos()
    createNevImg()
    newRotateImage()
    writeToImage()
    # print("Total Time %s" % (time.time() - STAG))
