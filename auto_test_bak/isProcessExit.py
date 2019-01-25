import os


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


isProcessExit()
