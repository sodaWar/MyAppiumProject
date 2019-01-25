import sys
import random, time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage


def getlanchtime(screenshot, startActivity):
    device = MonkeyRunner.waitForConnection()
    result = MonkeyRunner.loadImageFromFile(screenshot)
    device.shell('am force-stop %s' % startActivity.split('/')[0])
    device.startActivity(component=startActivity)

    start_time = time.time()
    print (start_time)
    while 1:
        current_time = time.time()
        print (current_time)
        mainPageImage = device.takeSnapshot()
        MonkeyRunner.sleep(2)
        mainPageImage.writeToFile('D:/adt-bundle-windows-x86-20130917/mainPageImage.png', 'png')
        if (result.sameAs(mainPageImage, 0.6)):
            launch_time = current_time - start_time
            print launch_time
            break
        else:
            print('the result is unlike')
            break


if __name__ == "__main__":
    getlanchtime(sys.argv[1], sys.argv[2])
