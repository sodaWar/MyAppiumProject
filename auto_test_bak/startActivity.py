# -*- coding:utf-8 -*-
import traceback
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as de
from com.android.monkeyrunner import MonkeyImage as mi
import sys

device = mr.waitForConnection()

try:
    for i in range(10):
        if i == 3:
            #	sys.exit(0)   作用是退出程序引发SystemExit异常, 可以捕获异常执行些清理工作. n默认值为0, 表示正常退出. 其他都是非正常退出.
            continue
        device.startActivity(component="com.tencent.mobileqq/.activity.SplashActivity")
        mr.alert('prepare to reboot')
        print i

except Exception, e:
    traceback.print_exc()
else:
    print('the end!!!')
    # device.reboot()    #设备重启
