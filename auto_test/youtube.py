# -* encoding:utf-8 *-
from test_cm_upgrade import *
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
import time

# conn,cur = connDB()
# youtube_url = youtube_video(cur)

driver = webdriver.Chrome()
driver.maximize_window()                # 最大化浏览器
driver.implicitly_wait(5)               # 设置隐式时间等待

# b =[]
# for i in range(len(youtube_url)):
#     r_url = youtube_url[i]
#     driver.get(r_url)
#     time.sleep(2)
#     try:
#         driver.find_element_by_class_name('ytp-size-button').click()
#     except ElementNotVisibleException:
#         sql1 = "select id from video where url = '%s'" %(youtube_url[i])
#         sql2 = "update video set status = 2 where url = '%s'" %(youtube_url[i])
#         cur.execute(sql1)
#         id = cur.fetchall()
#         print '该视频不能播放,视频id是' + str(id[0][0]) + '，请核对'
#         b.append(id[0][0])
#         cur.execute(sql2)
#         conn.commit()
# print b
# driver.quit()