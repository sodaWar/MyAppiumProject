from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

device = MonkeyRunner.waitForConnection()
for i in range(1, 5):

    device.startActivity(component="com.tencent.mobileqq/.activity.SplashActivity")
    device.press('KEYCODE_DPAD_DOWN', 'DOWN_AND_UP')
    MonkeyRunner.sleep(3)
    device.touch(263, 1192, "DOWN_AND_UP")  # login
    MonkeyRunner.sleep(2)

    device.touch(360, 465, 'DOWN_AND_UP')  # account
    MonkeyRunner.sleep(2)
    device.type('893026750')

    image = device.takeSnapshot()  # screenShot and match
    MonkeyRunner.sleep(2)
    image.writeToFile('D:/AndroidSkd/screenShot1.png', 'png')
    result = MonkeyRunner.loadImageFromFile('D:/AndroidSkd/qqScreenShot2.png')
    if image.sameAs(result, 0.9):
        print "match right"
    else:
        print "match wrong"

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
else:
    print('end')
