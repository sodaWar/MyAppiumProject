import os
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

device = MonkeyRunner.waitForConnection()


def isProcessExit():
    process = os.popen("adb shell dumpsys meminfo ")
    terminal_back = process.read()
    print (str(terminal_back))
    p = str(terminal_back).find('com.tencent.mobileqq')
    print p

    if not p == -1:
        print ('QQ is run')
        return True
    else:
        print ('QQ is not run')
        return False


for i in range(1, 5):
    isProcessExit()
    device.startActivity(component="com.tencent.mobileqq/.activity.SplashActivity")
    device.press('KEYCODE_DPAD_DOWN', 'DOWN_AND_UP')
    MonkeyRunner.sleep(3)
    device.touch(263, 1192, "DOWN_AND_UP")  # login
    MonkeyRunner.sleep(2)

    device.touch(360, 465, 'DOWN_AND_UP')  # account
    MonkeyRunner.sleep(2)
    device.type('893026750')

    result = device.takeSnapshot()  # screenShot
    MonkeyRunner.sleep(2)
    result.writeToFile('/Users/apple/auto_test/screenShot1.png', 'png')

    device.touch(146, 322, "DOWN_AND_UP")  # password
    MonkeyRunner.sleep(2)
    device.type('hongnaiwu3425')

    #	result = device.takeSnapshot()         #screenShot
    #	MonkeyRunner.sleep(2)
    #	result.writeToFile('D:/adt-bundle-windows-x86-20130917/screenShot2.png','png')

    device.touch(342, 408, "DOWN_AND_UP")  # enter button
    MonkeyRunner.sleep(3)

    device.press('KEYCODE_BACK', 'DOWN_AND_UP')  # back up
    MonkeyRunner.sleep(2)

    device.press('KEYCODE_HOME', 'DOWN_AND_UP')  # back  home
    MonkeyRunner.sleep(2)

    print i
    MonkeyRunner.sleep(2)
    os.system("adb shell am force-stop com.tencent.mobileqq")
    print ('kill the progress success')
else:
    print('end')
