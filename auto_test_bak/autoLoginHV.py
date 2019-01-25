from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By

device = MonkeyRunner.waitForConnection()

device.startActivity(component="com.tencent.mobileqq/.activity.SplashActivity")

easy_device = EasyMonkeyDevice(device)

device.press('KEYCODE_DPAD_DOWN','DOWN_AND_UP')

MonkeyRunner.sleep(3)    # (this is very import)

easy_device.touch(By.id('id/btn_login'), MonkeyDevice.DOWN_AND_UP)

device.touch(120,397,'DOWN_AND_UP')

device.type('893026750')

# easy_device.touch(By.id('id/password'), MonkeyDevice.DOWN_AND_UP)
#
# device.type('hongnaiwu3425')
#
# easy_device.touch(By.id('id/login'), MonkeyDevice.DOWN_AND_UP)
#
# device.press('KEYCODE_BACK','DOWN_AND_UP')
