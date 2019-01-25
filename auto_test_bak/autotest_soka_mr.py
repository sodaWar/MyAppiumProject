# -* encoding:utf-8 *-
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
from com.android.monkeyrunner.easy import EasyMonkeyDevice as emd
from com.android.monkeyrunner.easy import By
from test_cm_upgrade import *
import os
import traceback

device = mr.waitForConnection()
easy_device = emd(device)

def isAppExit():
    package_name = "adb shell pm list package"
    cmdback = os.popen(package_name)
    cmdresult = str(cmdback.read())
    f_result = cmdresult.find("com.soka.football")
    print f_result
    if not f_result == -1:
        print "app is exit"
        return 1
    else:
        print "app not exit"
        return 0


def isProcessExit():
    process_name = "adb shell dumpsys meminfo"
    cmdback = os.popen(process_name)
    cmdresult = str(cmdback.read())
    f_result = cmdresult.find("com.soka.football")
    print f_result
    if not f_result == -1:
        print "Soka Football app is run"
        return 1
    else:
        print "Soka Football app is not run"
        return 0


def startActivity(time=[0]):
    package_name = "com.soka.football"
    activity = ".home.ui.login.activity.SplashActivity"
    comment_name = package_name + '/' + activity
    device.startActivity(component=comment_name)

    new_time = time[0] + 1
    time[0] = new_time
    print time[0]
    mr.sleep(1)
    auto_teach(new_time)

    return new_time


def auto_login(i):
    runStartApp()

    easy_device.touch(By.id('id/iv_avatar'), md.DOWN_AND_UP)
    mr.sleep(1)

    if i == 0:
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type('abddsaqqcom')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/OnlyLetter1.png', 'png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/OnlyLetter.png', 'png')
        if image.sameAs(result, 1):
            print ("input only letter match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 1:
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type('89302675023')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/OnlyNumber1.png', 'png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/OnlyNumber.png', 'png')
        if image.sameAs(result, 1):
            print ("input only number match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 2:
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type(u'\u0020\u0020\u0020\u0020 893026750@163.com')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/PreludeNull1.png', 'png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/PreludeNull.png', 'png')
        if image.sameAs(result, 1):
            print ("input prelude null match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 3:
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type(u'893026750\u0020\u0020\u0020\u0020@163.com')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/MiddleNull1.png', 'png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/MiddleNull.png', 'png')
        if image.sameAs(result, 1):
            print ("input middle null match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 4:
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type(u'893026750@163.com\u0020\u0020\u0020\u0020')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/TailNull1.png', 'png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/TailNull.png', 'png')
        if image.sameAs(result, 1):
            print ("input tail null match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 5:
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type('893026750@163com')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/NoDot1.png', 'png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/NoDot.png', 'png')
        if image.sameAs(result, 1):
            print ("input no dot match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 6:
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type('893026750163.com')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/No@1.png', 'png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/No@.png', 'png')
        if image.sameAs(result, 1):
            print ("input no @ match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))

    elif i == 7:
        easy_device.touch(By.id('id/et_password'), md.DOWN_AND_UP)
        mr.sleep(1)
        device.type('abcde')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
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
        device.type('abcdejhsas32328976jsm')
        mr.sleep(1)
        easy_device.touch(By.id('id/et_email'), md.DOWN_AND_UP)

        image = device.takeSnapshot()
        mr.sleep(2)
        image.writeToFile('D:/AndroidSdk/AutoImage/TwentyOnePs1.png', 'png')
        result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/TwentyOnePs@.png', 'png')
        if image.sameAs(result, 1):
            print ("input twenty one password  match right")
        else:
            print ("there is a problem here,please check , and the number is:" + str(i))


def serverPolicy():
    runStartApp()

    mr.sleep(2)
    easy_device.touch(By.id('id/iv_avatar'), md.DOWN_AND_UP)
    mr.sleep(1)
    device.touch(348, 880, 'DOWN_AND_UP')
    mr.sleep(5)

    image = device.takeSnapshot()
    mr.sleep(2)
    image.writeToFile('D:/AndroidSdk/AutoImage/TeamServer1.png', 'png')
    result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/TeamServer.png', 'png')
    if image.sameAs(result, 1):
        print ("the team server page  match right")
    else:
        print ("there is a problem here,please check , and the number is: the team server page" )

    mr.sleep(2)
    easy_device.touch(By.id('id/title_bar_iv_left'), md.DOWN_AND_UP)
    mr.sleep(1)
    device.touch(571, 880, 'DOWN_AND_UP')
    mr.sleep(5)

    image = device.takeSnapshot()
    mr.sleep(2)
    image.writeToFile('D:/AndroidSdk/AutoImage/PrivacyPolicy1.png', 'png')
    result = mr.loadImageFromFile('D:/AndroidSdk/AutoImage/PrivacyPolicy.png', 'png')
    if image.sameAs(result, 1):
        print ("the privacy policy page  match right")
    else:
        print ("there is a problem here,please check , and the number is: the privacy policy page")


def auto_teach(i):
    device.press('KEYCODE_DPAD_DOWN', 'DOWN_AND_UP')
    mr.sleep(2)
    if i == 0:  # 第一次打开APP时
        easy_device.touch(By.id('id/tv_standard'), md.DOWN_AND_UP)
        mr.sleep(1)
        easy_device.touch(By.id('id/title_bar_iv_left'), md.DOWN_AND_UP)
        mr.sleep(1)
        easy_device.touch(By.id('id/tv_myCoin'), md.DOWN_AND_UP)
        mr.sleep(1)
        easy_device.touch(By.id('id/tv_sign_in'), md.DOWN_AND_UP)
        mr.sleep(1)
        easy_device.touch(By.id('id/iv_hint'), md.DOWN_AND_UP)
    else:
        easy_device.touch(By.id('id/title_bar_iv_left'), md.DOWN_AND_UP)
        print "you have complete the teach"


def runStartApp():
    if isAppExit() == 0:
        device.installPackage('D:\\SOKA1.1.0.apk')
        startActivity()
    elif isAppExit() == 1 and isProcessExit() == 1:
        os.system("adb shell am force-stop com.soka.football")
        print ('kill the progress success')
        startActivity()
    else:
        startActivity()


def runLogin():
    for i in range(9):
        auto_login(i)
        # print "执行+ %d +测试用例完毕" + i
        print "execute case and NO:" + str(i)


def main():
    result = True
    print ("please chage a operate:")
    print ("1.tech page function")
    print ("2.login function")
    print ("3.forget password")
    print ("4.server and privacy")
    print ("input Q and ending the procedure")

    while (result):

        number = mr.input("enter you number:")
        if number is None:
            print "please input Q and ending the procedure"
        elif not number:
            print "please input number or input Q  to  ending the procedure"
        else:
            try:
                nm_first = int(number)
                print nm_first
            except ValueError:
                nm_first = str(number)
                print nm_first
            else:
                print "input have problem"

            if (nm_first == 'q' or nm_first == 'Q'):
                print ("procedure is ending....")
                mr.sleep(3)
                break

            elif (nm_first.isspace() == True):
                print ("input is can not be null and input again")

            elif (int(nm_first) == 1):
                try:
                    print ("tech page is begin start...")
                    runStartApp()
                except Exception:
                    traceback.print_exc()
                finally:
                    print ("test is end")

            elif (int(nm_first) == 2):
                try:
                    print ("login page is begin start")
                    runLogin()
                except Exception:
                    traceback.print_exc()
                finally:
                    print ("test is end")

            elif (int(nm_first) == 3):
                try:
                    print ("forget password function is begin")

                except Exception:
                    traceback.print_exc()

            elif (int(nm_first) == 4):
                try:
                    print ("server page is begin....")

                except Exception:
                    traceback.print_exc()

            else:
                print ("input is invalid")
                mr.sleep(2)
                break

            mr.sleep(2)
            print ("please chage a operate:")
            print ("1.tech page function")
            print ("2.login function")
            print ("3.forget password")
            print ("4.server and privacy")
            print ("input Q and ending the procedure")



if __name__ == "__main__":
    main()

