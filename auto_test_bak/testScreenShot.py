from com.android.monkeyrunner import MonkeyRunner as mr

from com.android.monkeyrunner import MonkeyDevice as md

device=mr.waitForConnection()

package='com.dq.zombieskater.main'

activity='.MainActivity'

runComponent=package+'/'+activity

device.startActivity(component=runComponent)

mr.sleep(9)

result=device.takeSnapshot()

mr.sleep(2)#This step is very important!

result.writeToFile('E:/monkeyrunner/apk/status_update1.png','png')

device.press('KEYCODE_BACK','DOWN_AND_UP')

print("Image success!!")

#more image

num=10

for i in range(1,num):

         result2=device.takeSnapshot()

         result2.writeToFile('E:/monkeyrunner/apk/'+str(i)+'.png','png')

         mr.sleep(2)

else:

         print("end")

