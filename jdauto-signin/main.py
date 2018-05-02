# -*- coding:utf-8 -*-
__author__ = "東飛"
__date__ = "2018-5-2"

import os
import time
from aip import AipOcr
from selenium import webdriver
from scrapy.selector import Selector
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# set profile，保存验证码
fp = webdriver.FirefoxProfile()
fp.set_preference("driver.download.folderList", 2)
fp.set_preference("driver.download.manager.showWhenStarting", False)
fp.set_preference("driver.download.dir", os.getcwd())
fp.set_preference("driver.helperApps.neverAsk.saveToDisk", "image/jpeg")

# driver = webdriver.Chrome(executable_path="D:/Program Files/BrowserDriver/chromedriver-2.38.exe")
# driver = webdriver.PhantomJS(executable_path="D:/Program Files/phantomjs-2.1.1-windows/bin/phantomjs.exe")
driver = webdriver.Firefox(firefox_profile=fp, executable_path="D:/Program Files/BrowserDriver/geckodriver.exe")

driver.get("https://passport.jd.com/new/login.aspx")
# 设置窗口
# driver.set_window_size(1200, 800)


# response = driver.page_source
# t_selector = Selector(text=response)

# 账户登录
driver.find_element_by_css_selector(".login-tab.login-tab-r a").click()
# # 输入框写入值
# driver.find_element_by_css_selector(".item.item-fore1 input[name='loginname']").send_keys("18860873453")
# driver.find_element_by_css_selector(".item.item-fore2 input[name='nloginpwd']").send_keys("jd@465125")
driver.find_element_by_id('loginname').send_keys("18860873453")
driver.find_element_by_id('nloginpwd').send_keys("jd@465125")

# 鼠标移动至验证码上 右键保存
# img_url = driver.find_element_by_css_selector("img#JD_Verification1").get_attribute('src')
img_elem = driver.find_element_by_id("JD_Verification1")
img_url = img_elem.get_attribute('src')
print(img_url)

action = ActionChains(driver).move_to_element(img_elem)
action.context_click(img_elem)
time.sleep(3)
action.send_keys(Keys.ARROW_DOWN)
action.send_keys('v')
action.perform()



# 点击提交
driver.find_element_by_css_selector("a#loginsubmit").click()
# time.sleep(20)
# driver.quit()




# 处理cookies
# driver.get(img_url)
# for k, v in cookies.iteritems():
#     cookie_dict = {'name': k, 'value': v}
#     driver.add_cookie(cookie_dict)
# driver.get(img_url)
# cookies = driver.get_cookies()
