#! /usr/bin/python
#　-*- coding: utf-8 -*-

import os
import sys
import signal


def kill(pid):

	try:
        a = os.kill(pid, signal.SIGKILL)
        # a = os.kill(pid, signal.9) #　与上等效
        print 'kill haved successed'
       # print 'having kill the process and pid is %s,　the return:%s' % (pid, a)
    #except(OSError,e):
        print 'have no this process!!!'

if __name__ == '__main__':
    kill(2648)