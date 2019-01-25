from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
import os
import sys
import signal

device = MonkeyRunner.waitForConnection()


def kill_tenor(pid):
    try:
        a = os.kill(pid, signal.SIGKILL)
        print'you have kill the pid %s tenor,the return is:%s' % (pid, a)
    except OSError, e:
        print'no have this tenor!!'


for i in range(1, 5):

    device.startActivity(component="com.tencent.mobileqq/.activity.SplashActivity")
    device.press('KEYCODE_DPAD_DOWN', 'DOWN_AND_UP')
    MonkeyRunner.sleep(3)
    device.touch(263, 1192, "DOWN_AND_UP")  # login
    MonkeyRunner.sleep(2)

    device.touch(360, 465, 'DOWN_AND_UP')  # account
    MonkeyRunner.sleep(2)
    device.type('893026750')

    device.touch(146, 322, "DOWN_AND_UP")  # password
    MonkeyRunner.sleep(2)
    device.type('hongnaiwu3425')

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
