import sys
import random,time
from datetime import datetime
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage 

def getlanchtime(screenshot,startActivity):
	device=MonkeyRunner.waitForConnection()
	result = MonkeyRunner.loadImageFromFile(screenshot)
	device.shell('am force-stop %s' % startActivity.split('/')[0])
	device.startActivity(component= startActivity)
	device.press('KEYCODE_DPAD_DOWN','DOWN_AND_UP')
	MonkeyRunner.sleep(3)
	device.touch(263,1192,"DOWN_AND_UP")    #login	
	MonkeyRunner.sleep(2)
    
	start_time = float(time.time())
	print (start_time)
	s_timeArray = time.localtime(start_time)
	s_time = time.strftime("%Y-%m-%d %H:%M:%S", s_timeArray)
	print (s_time)

	while 1:
		current_time = float(time.time())
		print (current_time)
		c_timeArray = time.localtime(current_time)
		c_time = time.strftime("%Y-%m-%d %H:%M:%S",c_timeArray)
		print (c_time)


		loginPageImage = device.takeSnapshot()
		MonkeyRunner.sleep(2)
		loginPageImage.writeToFile('D:/adt-bundle-windows-x86-20130917/loginPageImage.png','png')
		
		if(result.sameAs(loginPageImage,0.6)):
			lanch_time = current_time - start_time
			print (lanch_time)

			break
		else:
			print('the result is unlike')
			break

if __name__ == "__main__":
	getlanchtime(sys.argv[1],sys.argv[2])
