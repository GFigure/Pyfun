# -*- coding:utf-8 -*-
__author__ = "東飛"
__date__ = "2018-5-2"

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(executable_path="D:/Program Files/BrowserDriver/geckodriver-0.20.1.exe")
# driver.get("http://www.baidu.com")
driver.get("https://www.huohu123.com/view?app_id=183")

# 鼠标移动至图片上 右键保存图片
# elem_pic = driver.find_element_by_xpath("//div[@id='lg']/img")
elem_pic = driver.find_element_by_xpath("//div[@class='detail-top']/img")
print(elem_pic.get_attribute("src"))
action = ActionChains(driver).move_to_element(elem_pic)
action.context_click(elem_pic)

# 重点:当右键鼠标点击键盘光标向下则移动至右键菜单第一个选项
action.send_keys(Keys.ARROW_DOWN)
action.send_keys()
action.send_keys('v')  # 另存为
action.perform()

# 获取另存为对话框(失败)
# action.switch_to_alert()
# action.accept()
