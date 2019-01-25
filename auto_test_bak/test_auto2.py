# -* encoding:utf-8 *-
# from com.android.monkeyrunner import MonkeyRunner as mr
# from com.android.monkeyrunner import MonkeyDevice as md
# from com.android.monkeyrunner import MonkeyImage as mi
# from com.android.monkeyrunner.easy import EasyMonkeyDevice as emd
# from com.android.monkeyrunner.easy import By
#from test_cm_upgrade import *
import commands
import os
import re
import traceback
#import MySQLdb

print "我是"
#print MySQLdb.__file__
print os.__file__






#from pymysql import *

#from pymysql import __init__

#
# def connectdb():
#     print("正在连接服务器.....")
#     db = pymysql.connect(
#         host="34.235.86.20",
#         port=3306,
#         user="sokamgrdev",
#         password="sokamgr@Pwd",
#         charset="utf8mb4",
#         db="sokadb"
#      #   cursorclass=pymysql.cursors.DictCursor
#     )
#     print("连接服务器成功")
# #     return db



# values = os.system("adb shell pm list packages |grep com.soka.football")       判断一个字符串是否包含另一个字符串
# print values
# akl = str(values)
# print akl
# a = "com.soka.football"
# if a in akl:
#     print "is here"
# else:
#     print "not found"




# a = "adb shell pm list packages |grep com.soka.football"
# (status, b) = commands.getstatusoutput(a)
# print  status
# print b

# print commands.getoutput("adb shell pm list packages")


#
# string = 'asdf32323313a1sd3213sad1f3d'
# pattern = re.compile('.{1,1}')
# print(' '.join(pattern.findall(string)))

# print u'\u0020\u0020\u0020 893026750@163.com!'
# print 'HelloWorld !'
# a = u'\u0020\u0020\u0020 893026750@163.com!'
# print len(a)
# if a == "":
#     print "empty"
# else:
#     print "is not"

# def emailScreen():
#     conn, cur = connDB()
#     result = selectDBAuto(cur)
#     a = '893026751@qq.com'
#     print len(result)
#     for i in range(0, len(result)):
#         if (a == result[i][0]):
#             print "the email have existed:" + a
#             a = a[:8] + str(i + 1) + a[9:]
#     print ("the email is availabe:") + a
#     return a
#
#
# if __name__ == "__main__":
#     emailScreen()


#
# def auto_register():
#     device = mr.waitForConnection()
#     easy_device = emd(device)
#     package_name = "com.football.soccerbook"
#     activity = "com.soka.football.home.ui.login.activity.SplashActivity"
#     comment_name = package_name + '/' + activity
#     device.startActivity(component=comment_name)
#
#     mr.sleep(2)
#     device.press('KEYCODE_DPAD_DOWN', 'DOWN_AND_UP')
#     mr.sleep(2)
#     easy_device.touch(By.id('id/title_bar_iv_left'), md.DOWN_AND_UP)
#
#     email = "893026750@qq.com"
#     password = "12345"
#
#     easy_device.touch(By.id('id/iv_avatar'), md.DOWN_AND_UP)
#     mr.sleep(1)
#     device.drag((1272, 1002), (249, 1105), 3, 10)
#     mr.sleep(1)
#     easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
#     device.type(email)
#     mr.sleep(3)
#     device.touch(136, 594, 'DOWN_AND_UP')
#     device.type(password)
#     mr.sleep(1)
#     easy_device.touch(By.id('id/et_confirm_password'), md.DOWN_AND_UP)
#     device.type(password)
#     mr.sleep(2)
#     easy_device.touch(By.id('id/btn_sign'), md.DOWN_AND_UP)
#     mr.sleep(1)
#
#     image = device.takeSnapshot()
#     mr.sleep(2)
#     image.writeToFile('/Users/apple/auto_test/AutoImage/RegisterN1.png', 'png')
#     result = mr.loadImageFromFile('/Users/apple/auto_test/AutoImage/test1.png', 'png')
#     if image.sameAs(result, 1):
#         print ("register user is  match right")
#     else:
#         print ("the register function have problem!!")
#
# if __name__ == "__main__":
#     auto_register()
        # a = '893026751@qq.com'
        # result = ['893026751@qq.com','893026752@qq.com','893026753@qq.com','893026754@qq.com','893026755@qq.com']
        # for i in range(0, 5):
        #     if a == result[i]:
        #         print "the mail have existed"
        #         b = i+2
        #         print str(b)
        #         a = a[:8] + str(b) + a[9:]
        #         print a



        # a = u'893026750@qq.com'
        # b = '893026750@qq.com'
        # if a == b:
        #     print "the same"
        # else:
        #     print "not the same"

        # a = '893026750@qq.com'
        # b = unicode(a)
