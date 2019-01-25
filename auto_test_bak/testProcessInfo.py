import psutil
import re
import sys
import os


def processinfo(x):
    p = psutil.get_process_list()
    for r in p:
        aa = str(r)
        f = re.compile(x, re.I)
        if f.search(aa):
            # print aa.split('pid=')[1].split(',')[0]
            print(aa.split('pid=', 2))


processinfo(sys.argv[1])

print ('process %s' % os.getpid())

pid = 7044
os.popen('taskkill.exe /pid:' + str(pid))

for p in psutil.process_iter():
    if p.name == SERVER_NAME:
        p.kill()
