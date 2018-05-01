# -*- coding:utf-8 -*-
__author__ = "東飛"
__date__ = "2018-5-1"

from PIL import Image
import time
import os
import math

img_dir = "./img/sample/"
dst_width = 640
dst_height = 640
numPic = 100


# name: transfer
# todo: 重置图片大小 640 X 640
def processImg(img_dir, dst_width, dst_height):
    index = 1
    STA = time.time()
    img_paths = os.listdir(img_dir)
    print("正在重置图片大小...")
    for img_path in img_paths:
        im = Image.open(img_dir + img_path)
        if im.mode != "RGBA":
            im = im.convert("RGBA")
        # im.resize((dst_width, dst_height), Image.ANTIALIAS)
        # im.thumbnail((dst_width, dst_height))
        # im.save("./img/thumb/{0}.png".format(index))

        resized_img = im.resize((dst_width, dst_height), Image.ANTIALIAS)
        resized_img = resized_img.crop((0, 0, dst_width, dst_height))
        resized_img.save("./img/thumb/{0}.png".format(index))
        index += 1
        # return

    print("transfer Func Time %s" % (time.time() - STA))


def mergeImg():
    STA = time.time()
    img_paths = os.listdir(img_dir)
    eachsize = int(math.sqrt(float(640 * 640) / numPic))
    print(eachsize)

    numline = int(640 / eachsize)
    print(numline)

    toImage = Image.new('RGB', (640, 640))
    x = 0
    y = 0
    for i in img_paths:
        try:
            # 打开图片
            img = Image.open(img_dir + "/" + i)
        except IOError:
            print("Error: 没有找到文件或读取文件失败")
        else:
            # 缩小图片
            img = img.resize((eachsize, eachsize), Image.ANTIALIAS)
            # 拼接图片
            toImage.paste(img, (x * eachsize, y * eachsize))
            x += 1
            if x == numline:
                x = 0
                y += 1

    toImage.save('./img/merged.jpg')
    print("Merged Func Time %s" % (time.time() - STA))

if __name__ == '__main__':
    # processImg(img_dir, dst_width, dst_height)
    # print(os.listdir(img_dir))
    mergeImg()

