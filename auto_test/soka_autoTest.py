# -* encoding:utf-8 *-
from appium import webdriver
from appium.webdriver.connectiontype import ConnectionType
from collections import Counter
from test_cm_upgrade import *
from reptile_request_get import *
from reptile_request_post import *
from receive_email import *
from Tkinter import *
import tkMessageBox
import time
import os
import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers import SchedulerNotRunningError
import threading
from appium import webdriver


# class Bird(object):
#     have_feather = True
#     way_of_reproduction = "egg"
#     def move(self,dx,dy):
#         position = [0,0]
#         position[0] = position[0] + dx
#         position[1] = position[1] + dy
#         return position
# class Chicken(Bird):
#     way_of_reproduction = 'walk'
#     possible_in_kfc = True
# class Oriole(Bird):
#     way_of_reproduction = 'fly'
#     possible_in_kfc = False
# qike = Chicken()
# print Chicken.way_of_reproduction
# print(qike.move(10,3))



# conn,cur = connDB()
# youtube_url = youtube_video(cur)
# print youtube_url


# List=[1,2,2,2,2,3,3,3,4,4,4,4]                                #返回一个列表中某个重复元素的个数数量{2:4,3:3,4:4}
# a = List.count(1)

# a = {}
# for i in List:
#     if List.count(i)>1:
#         a[i] = List.count(i)
#         print a[i]
# print (a)


# s1 = "cd ../.."                                               #通过命令行打开系统的应用程序，先切换到应用程序的当前目录才能打开
# s2 = "open /Applications/Jietu.app"
#
# os.system(s1)
# os.system(s2)
# conn,cur = connDB()
# sql1 = "START TRANSACTION"
# sql2 = "update tag set status_flag = 1"
# sql3 = "update tag set status_flag = 1 WHERE id = 2"
# sql4 = "update tag set status_flag = 1 WHERE id = 3"
# sql5 = "update tag set status_flag = 1 WHERE id = 4"
# sql6 = "ROLLBACK"
# sql7 = "select * from tag WHERE id = 1"
#
# a = [sql1,sql2,sql3,sql4,sql5,sql6,sql7]                                            #判断没有根据
# for i in range(len(a)):
#     cur.execute(a[i])
#     if a[i].lower().find('update') != -1 and a[i].lower().find('where') != -1:      #lower()方法是将字符串变成小写，大写的方法是upper()
#         conn.commit()
#     elif a[i].lower().find('update') != -1 and a[i].lower().find('where') == -1:
#         cur.execute(sql6)
#         conn.commit()
#         print '该SQL语句有问题！sql' + str(i + 1)
#     elif i == 6:
#         result = cur.fetchall()
#         print result
#     else:
#         print '无更新操作'
#         conn.commit()
#
# a = select_live_match(cur)
# print a
# a = 0
# if a == 0:
#     print (time.time())
#     a = thd.Timer(3, prediction_history()).start()
# else:
#     print 'y'

# 每隔10秒钟执行

# def t2():
#     a = 0
#     while a == 0:
#         a = prediction_history()
#         time.sleep(3)
#     else:
#         try:
#             print '注意！竞猜记录显示已结束竞猜'
#             return 1
#         except  TypeError:
#             print 'n'

# sched =BlockingScheduler()
# if t2() == 1:
#     try:
#         sched.shutdown(wait=False)
#     except SchedulerNotRunningError:
#         print '调度任务已结束'
# else:
#     sched.add_job(t2, 'interval')
#     sched.start()

#
# if __name__ == '__main__':
#     t = threading.Thread(target=t2)
#     t.start()
# #
#     # 主进程要处理的事情
#     t.join()


# conn,cur = connDB()
# b = select__match_prediction(cur)               #数据库返回的数据
# a = match_prediction()                          #接口返回的数据
# print a
# print b
# if a.sort() == b.sort():
#     print 'yes'
# else:
#     print 'no'


# conn,cur = connDB()
# result = select_subscribption(cur,241)
# e = len(result)
# s1 = []
# b = []
# for i in range(e):
#     s2 = result[i][0]
#     s1.append(s2)
# print s1
#
# for m in range(len(s1)):
#     a = select_match_subcribption(cur, s1[m])
#     for n in range(len(a)):
#         b.append(a[n][1])
#         print b
#     print a1
# c =Counter(a1)                                          #显示出列表中所有元素重复的次数，返回值是一个字典，注意要导入Counter包
# s3 = list(set(b))                                       #去除列表中重复的元素
# print len(s3)
    # s3 = s3 + a
    # print s3

#
# def a():
#     conn, cur = connDB()
#     result = selectDBAuto(cur, 'identity', 'identity')
#     email = '830@qq.com'
#     # print result[0][0]
#     for i in range(0, len(result)):
#         a = str(i)
#         if (email == result[i][0]):
#             print "the email have existed:" + email
#             if len(email) == 10:
#                 email = email[:2] + a + email[3:]
#                 print email
#             elif len(email) == 11:
#                 email = email[:2] + a + email[4:]
#                 print email
#             elif len(email) == 12:
#                 email = email[:2] + a + email[5]
#                 print email
#     print ("the email is availabe:") + email
#     return email
# # print email
# b = a()
# print b

# import json
#
# values = {"id": 33,"status" : 0}
# delivery_data = json.dumps(values)
# delivery_url = "http://api.admin.test.sokafootball.com/admin/banner/update"
# delivery_headers = {"Content-Type" : "application/json"}
# r = requests.post(url = delivery_url,data = delivery_data,headers=delivery_headers)





# def printentry():            #弹出输入框并获取其值
#     print var.get()
# from Tkinter import *
# root=Tk()
# var=StringVar()
# Entry(root,textvariable=var).pack() #设置输入框对应的文本变量为var
# Button(root,text="print entry",command=printentry).pack()
# root.mainloop()

#
# from Tkinter import *
#
# from tkMessageBox import *
#
#
# def answer():
#     showerror("Answer", "Sorry, no answer available")       #弹出对话框的一种方式，用python内置函数Tkinter库来实现
#
#
# def callback():
#     if askyesno('Verify', 'Really quit?'):
#
#         showwarning('Yes', 'Not yet implemented')
#
#     else:
#
#         showinfo('No', 'Quit has been cancelled')
#
#
# Button(text='Quit', command=callback).pack(fill=X)
#
# Button(text='Answer', command=answer).pack(fill=X)
#
# mainloop()

# import easygui                 #弹出对话框的一种方式，用python第三方库来实现
# Yes_or_No = easygui.buttonbox("Yes of No?", choices = ['Yes','No'])
# print Yes_or_No




# def installApp(self):
#     if self.driver.is_app_installed("com.football.soccerbook") == 'True':
#         self.driver.remove_app("com.football.soccerbook")
#         self.driver.install_app("/Users/apple/sokafootball2.1.2.apk")
#     else:
#         self.driver.install_app("/Users/apple/sokafootball2.1.2.apk")
#
# desired_caps = {
#     'platformName': 'Android',
#     'deviceName': '192.168.56.101:5555',
#     'platformVersion': '4.4.4',
#     'app' : '/Users/apple/sokafootball2.1.2.apk',
#     # 'appPackage': 'com.football.soccerbook',
#     # 'appActivity': 'com.soka.football.home.ui.login.activity.SplashActivity',
#     'unicodeKeyboard': 'True',
#     'resetKeyboard': 'True'
# }
#
#
# driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
# driver.start_activity("com.football.soccerbook","com.soka.football.home.ui.login.activity.SplashActivity")
# time.sleep(3)
#
# if driver.is_app_installed("com.football.soccerbook"):
#     driver.remove_app("com.football.soccerbook")
#     driver.install_app("/Users/apple/sokafootball2.1.2.apk")

#
# conn, cur = connDB()
# r = show_matchIndex(cur)
# status = r[1]
# match_mes = r[0]
# print 'A队名称:',match_mes[0],'   B队名称:',match_mes[1],'   联盟名称:',match_mes[2],'   比赛开始时间:',match_mes[3]
#
#
# def emailScreen(self):
#     conn, cur = connDB()
#     result = selectDBAuto(cur, 'identity', 'identity')
#     email = '893026750@qq.com'
#     print len(result)
#     for i in range(0, len(result)):
#         if (email == result[i][0]):
#             print "the email have existed:" + email
#             email = email[:8] + str(i + 1) + email[9:]
#     print ("the email is availabe:") + email
#     return email
# update_matchIndex(conn,cur,status)

# print isinstance(result1,int)
# uid = result1+1
#
# result2 = insert_permission(conn,cur,uid)
# print result2


# content = '893026751@qq.com'
# print len(result)
# for i in range(0, len(result)):
#     if (email == result[i][0]):
#         print "the email have existed:" + email
#         email = email[:8] + str(i + 1) + email[9:]
# print ("the email is availabe:") + email


# else:
#     driver.install_app("/Users/apple/sokafootball2.1.2.apk")


# print driver.is_app_installed("com.football.soccerbook")
# if driver.is_app_installed("com.football.soccerbook") == 'True':
    # driver.remove_app("com.football.soccerbook")
# else:
#


# driver.implicitly_wait(2)
# time.sleep(2000)

# driver.find_element_by_id("tv_standard").click()
# driver.find_element_by_id("title_bar_iv_left").click()
# driver.find_element_by_id("tv_myCoin").click()
# driver.find_element_by_id("tv_sign_in").click()
# driver.find_element_by_id("tv_task_name").click()
# driver.find_element_by_id("rb_match").click()
#
#
# time.sleep(3)
# # driver.swipe(240, 600, 240, 230,3000)
#
#
#
#
# window_size = driver.get_window_size()
# x = window_size['width']
# y = window_size['height']
# x1 = int(x * 0.5)
# y1 = int(y * 0.82)
# y2 = int(y * 0.31)
# driver.swipe(start_x = x1,start_y = y1,end_x = x1,end_y = y2,duration = 2000)
#
#
#
#
#查看并使用该代码的用法:
# WebDriverWait(dr, 30).until(lambda the_driver: the_driver.find_element_by_id('qsbk.app:id/tabPanel').is_displayed())