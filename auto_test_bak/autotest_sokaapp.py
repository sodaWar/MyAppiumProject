# -* encoding:utf-8 *-
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
from com.android.monkeyrunner.easy import EasyMonkeyDevice as emd
from com.android.monkeyrunner.easy import By
from test_cm_upgrade import *
import os
import traceback

device = mr.waitForConnection(5,'127.0.0.1:62001')
def isAppExit():
    package_name = "adb shell pm list package"
    cmdback = os.popen(package_name)
    cmdresult = str(cmdback.read())
    f_result= cmdresult.find("com.soka.football")
    print f_result
    if not f_result == -1:
        print "app is exit"
        return 1
    else:
        print "app not exit"
        return 0

def isProcessExit():
    process = os.popen("adb shell dumpsys meminfo")
    cmdback = str(process)
    result = cmdback.find("com.soka.football")
    print result
    if not result == -1:
        print "Soka Football app is run"
        return 1
    else:
        print "Soka Football app is not run"
        return 0


def startActivity(time = [0]):
    if isProcessExit() == 1:
        os.system("adb shell am force-stop com.soka.football")
        print ('kill the progress success')
    else:
        package_name = "com.soka.football"
        activity = ".home.ui.login.activity.SplashActivity"
        comment_name = package_name + '/' + activity
        device.startActivity(component=comment_name)

        new_time = time[0] + 1
        time[0] = new_time
        auto_teach(new_time)

        return new_time


def auto_teach(i):
    easy_device = emd(device)
    device.press('KEYCODE_DPAD_DOWN', 'DOWN_AND_UP')
    mr.sleep(2)
    if i == 1:
        easy_device.touch(By.id('id/tv_standard'), md.DOWN_AND_UP)         # (第一次下载APP后打开APP需要这个代码)
        easy_device.touch(By.id('id/title_bar_iv_left'), md.DOWN_AND_UP)
        easy_device.touch(By.id('id/tv_myCoin'), md.DOWN_AND_UP)
        easy_device.touch(By.id('id/tv_sign_in'), md.DOWN_AND_UP)
        easy_device.touch(By.id(''),md.DOWN_AND_UP)
    else:
        easy_device.touch(By.id('id/title_bar_iv_left'), md.DOWN_AND_UP)
        easy_device.touch(By.id('id/tv_myCoin'), md.DOWN_AND_UP)
        easy_device.touch(By.id('id/tv_sign_in'), md.DOWN_AND_UP)
        easy_device.touch(By.id(''),md.DOWN_AND_UP)

def auto_login(i,account,password):
    runStartApp()

    easy_device.touch(By.id('id/iv_avatar'),md.DOWN_AND_UP)
    mr.sleep(1)

    if i == 0:
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type(account)
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapShot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/OnlyLetter1.png','png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/OnlyLetter.png','png')
        if image.sameAs(result,1):
            print ("input only letter match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 1:
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type(account)
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapShot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/OnlyNumber1.png','png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/OnlyNumber.png','png')
        if image.sameAs(result,1):
            print ("input only number match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 2:
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type(account)
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapShot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/PreludeNull1.png','png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/PreludeNull.png','png')
        if image.sameAs(result,1):
            print ("input prelude null match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 3:
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type(account)
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapShot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/MiddleNull1.png','png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/MiddleNull.png','png')
        if image.sameAs(result,1):
            print ("input middle null match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 4:
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type(account)
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapShot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/TailNull1.png','png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/TailNull.png','png')
        if image.sameAs(result,1):
            print ("input tail null match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 5:
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type(account)
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapShot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/NoDot1.png','png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/NoDot.png','png')
        if image.sameAs(result,1):
            print ("input no dot match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 6:
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type(account)
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapShot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/No@1.png','png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/No@.png','png')
        if image.sameAs(result,1):
            print ("input no @ match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 7:
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type(password)
        mr.sleep(1)
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)

        image = device.takeSnapShot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/FiveNumberPs1.png', 'png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/FiveNumberPs@.png', 'png')
        if image.sameAs(result, 1):
            print ("input five number password  match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 8:
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type(password)
        mr.sleep(1)
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)

        image = device.takeSnapShot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/TwentyOnePs1.png', 'png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/TwentyOnePs@.png', 'png')
        if image.sameAs(result, 1):
            print ("input twenty one password  match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))


    easy_device.touch(By.id('id/btn_login'),md.DOWN_AND_UP)
    easy_device.touch(By.id('id/tv_forget'), md.DOWN_AND_UP)

def serverPolicy():
    runStartApp()

    easy_device.touch(By.id('id/iv_avatar'),md.DOWN_AND_UP)
    mr.sleep(1)
    device.touch(258,666,'DOWN_AND_UP')
    mr.sleep(1)

    image = device.takeSnapShot()
    mr.sleep(2)
    image.writeToFile('D:/AndroidSdk/AutoImage/TeamServer1.png', 'png')
    result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/TeamServer.png', 'png')
    if image.sameAs(result, 1):
        print ("the team server page  match right")
    else:
        print ("there is a problem here,please check , and the number is:" + "the team server page")

    easy_device.touch(By.id('id/title_bar_iv_left'), md.DOWN_AND_UP)
    device.touch(456,664,'DOWN_AND_UP')

    image = device.takeSnapShot()
    mr.sleep(2)
    image.writeToFile('D:/AndroidSdk/AutoImage/PrivacyPolicy1.png', 'png')
    result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/PrivacyPolicy.png', 'png')
    if image.sameAs(result, 1):
        print ("the privacy policy page  match right")
    else:
        print ("there is a problem here,please check , and the number is:" + "the privacy policy page")


def runStartApp():
    if isAppExit() == 0:
        device.installPackage('D:\\SOKA1.1.0.apk')
        startActivity()
    else:
        startActivity()

def runServerPage():
    serverPolicy()


def runLogin():
    for i in range(10):
        if i == 0:
            account = raw_input("请输入账号：")
            mr.sleep(1)
            device.type('abddsaqqcom')
            password = input("请输入密码：")
            device.type(u'\u0020\u0020\u0020\u0020')
            auto_login(i,account,password)

        elif i == 1:
            account = raw_input("请输入账号：")
            mr.sleep(1)
            device.type('89302675023')
            password = input("请输入密码：")
            device.type(u'\u0020\u0020\u0020\u0020')
            auto_login(i,account,password)

        elif i == 2:
            account = raw_input("请输入账号：")
            mr.sleep(1)
            device.type(u'\u0020\u0020\u0020\u0020 893026750@163.com')
            password = input("请输入密码：")
            device.type(u'\u0020\u0020\u0020\u0020')
            auto_login(i,account,password)

        elif i == 3:
            account = raw_input("请输入账号：")
            mr.sleep(1)
            device.type(u'893026750\u0020\u0020\u0020\u0020@163.com')
            password = input("请输入密码：")
            device.type(u'\u0020\u0020\u0020\u0020')
            auto_login(i,account,password)

        elif i == 4:
            account = raw_input("请输入账号：")
            mr.sleep(1)
            device.type(u'893026750@163.com\u0020\u0020\u0020\u0020')
            password = input("请输入密码：")
            device.type(u'\u0020\u0020\u0020\u0020')
            auto_login(i,account,password)

        elif i == 5:
            account = raw_input("请输入账号：")
            mr.sleep(1)
            device.type('893026750@163com')
            password = input("请输入密码：")
            device.type(u'\u0020\u0020\u0020\u0020')
            auto_login(i,account,password)

        elif i == 6:
            account = raw_input("请输入账号：")
            mr.sleep(1)
            device.type('893026750163.com')
            password = input("请输入密码：")
            device.type(u'\u0020\u0020\u0020\u0020')
            auto_login(i,account,password)

        elif i == 7:
            password = input("请输入密码：")
            mr.sleep(1)
            device.type('abcde')
            account = raw_input("请输入账号：")
            device.type(u'\u0020\u0020\u0020\u0020')
            auto_login(i,account,password)

        elif i == 8:
            password = input("请输入密码：")
            mr.sleep(1)
            device.type('abcdejhsas32328976jsm')
            account = raw_input("请输入账号：")
            device.type(u'\u0020\u0020\u0020\u0020')
            auto_login(i,account,password)



def main():
    result = True
    print ("请选择需要自动化测试的功能：")
    print ("1.教学引导功能")
    print ("2.登录功能")
    print ("3.忘记密码")
    print ("4.政策与服务页面")
    print ("按Q退出程序")
    number = raw_input()
    while (result):
        if (number == 'q' or number == 'Q'):
            print ("程序退出中....")
            mr.sleep(3)
            break

        elif (int(number) == 1):
            try:
                print ("教学页面自动化测试开始...")
                runStartApp()
            except Exception as e:
                traceback.print_exc()
            finally:
                print ("测试结束")

        elif (int(number) == 2):
            try:
                print ("登录页面测试开始")
                runLogin()
            except Exception as e:
                traceback.print_exc()
            finally:
                print ("测试结束")

        elif (int(number) == 3):
            try:
                print ("忘记密码功能测试开始")

            except Exception as e:
                traceback.print_exc()

        elif (int(number) == 4):
            try:
                print ("政策与服务页面测试开始")

            except Exception as e:
                traceback.print_exc()

        else:
            print ("输入非法，将结束进程")
            break

        print ("请选择以上四个操作：1、教学引导 2、登录页面 3、忘记密码 4、政策与服务.(按Q退出程序)")
        number = raw_input("请选择操作")




if __name__ == "__main__":
    main()