# -*- coding:utf-8 -*-
__author__ = "東飛"
__date__ = "2018-5-2"
import requests

""" http://ai.baidu.com/docs#/OCR-Python-SDK/top """

from aip import AipOcr

""" APPID AK SK """
APP_ID = '11179096'
API_KEY = '9SOU6XS1yANpLs4OtjjMp8UW'
SECRET_KEY = 'skT2qgdckzuaB4RUX4xHyzMPpvzLncFG'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# """ 读取图片 """
# def get_file_content(filePath):
#     with open(filePath, 'rb') as fp:
#         return fp.read()
#
# image = get_file_content('1.jpg')
#
# """ 调用通用文字识别, 图片参数为本地图片 """
# client.basicGeneral(image);
#
# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "ENG"
# # options["detect_direction"] = "true"
# # options["detect_language"] = "true"
# # options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为本地图片 """
# result = client.basicGeneral(image, options)
# print(result)


def get_img(url):
    r = requests.get(url)
    with open('2.jpg', 'wb') as fp:
        fp.write(r.content)

url = "https://authcode.jd.com/verify/image?a=1&acid=52ff043e-db1e-4f39-91d6-36b525d3b93e&uid=52ff043e-db1e-4f39-91d6-36b525d3b93e&yys=1525234026089"
r = requests.get(url,allow_redirects=False)
print(r.content)



# """ 调用通用文字识别, 图片参数为远程url图片 """
# client.basicGeneralUrl(url);
#
# """ 如果有可选参数 """
# options = {}
# options["language_type"] = "ENG"
# # options["detect_direction"] = "true"
# # options["detect_language"] = "true"
# # options["probability"] = "true"
#
# """ 带参数调用通用文字识别, 图片参数为远程url图片 """
# result = client.basicGeneralUrl(url, options)
# print(result)







# """ 调用通用文字识别（高精度版） """
# client.basicAccurate(image);
#
# """ 如果有可选参数 """
# options = {}
# options["detect_direction"] = "true"
# options["probability"] = "true"
#
# """ 带参数调用通用文字识别（高精度版） """
# client.basicAccurate(image, options)