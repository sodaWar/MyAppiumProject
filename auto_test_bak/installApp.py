from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage
import time 

device = MonkeyRunner.waitForConnection()

r_start = time.clock()
device.removePackage('com.tencent.mobileqq')
r_end = time.clock()
r_time = r_end - r_start
print ('remove the app use:',r_time)
MonkeyRunner.sleep(3)

i_start = time.clock()
device.installPackage('/Users/apple/mobileqq_android.apk')
i_end = time.clock()
i_time = i_end - i_start
print('install the app use:',i_time)


