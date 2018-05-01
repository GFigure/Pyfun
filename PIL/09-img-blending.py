# -*- coding:utf-8 -*-
__author__ = "東飛"
__date__ = "2018-5-1"

from PIL import Image


# 1、使用 Image.blend() 接口
# 两幅图像进行合并时，按公式：blended_img = img1 * (1 – alpha) + img2* alpha 进行。
# 两张图片的大小必须一致
def blend_two_images():
    img1 = Image.open("./img/img-blending-05.jfif")
    img1.convert('RGBA')
    img1 = img1.resize((600, 400), Image.ANTIALIAS)

    img2 = Image.open("./img/img-blending-04.jpg")
    img2.convert('RGBA')
    img2 = img2.resize((600, 400), Image.ANTIALIAS)

    img = Image.blend(img1, img2, 0.3)
    img.show()
    # img.save("./img/img-blending.png")

    return


# 2、使用Image.composite()接口
# 该接口使用掩码（mask）的形式对两幅图像进行合并。
def blend_two_images2():
    img1 = Image.open("./img/img-blending-04.jpg")
    img1 = img1.convert('RGBA')

    img2 = Image.open("./img/img-blending-06.jfif")
    img2 = img2.convert('RGBA')

    r, g, b, alpha = img2.split()
    alpha = alpha.point(lambda i: i > 0 and 204)

    img = Image.composite(img2, img1, alpha)

    img.show()

    return


if __name__ == '__main__':
    # blend_two_images()
    blend_two_images2()
