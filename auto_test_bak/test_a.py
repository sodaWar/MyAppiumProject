from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi
from com.android.monkeyrunner.easy import EasyMonkeyDevice as emd
from com.android.monkeyrunner.easy import By
import traceback

# # if __name__ == '__main__':
# #     number = raw_input()
# #     if number == 1:
# #         print "yes"
# #     else:
# #         print "no"
#
def start():
    print "abc"

if __name__ == '__main__':
    result = True
    print ("please change a operate:")
    print ("1.tech page function")
    print ("2.login function")
    print ("3.forget password")
    print ("4.server and privacy")
    print ("input Q and ending the procedure")

    while (result):

        number = mr.input("enter you number:")
        if number is None:
            print "please input Q and ending the procedure"
        elif  not number:
            print "please input number or input Q  to  ending the procedure"
        else:
            try:
                nm_first = int(number)
                print nm_first
            except ValueError:
                nm_first = str(number)
                print nm_first
            else:
                print "input have problem"

            if (nm_first == 'q' or nm_first == 'Q'):
                print ("procedure is ending....")
                mr.sleep(3)
                break

            elif (nm_first.isspace() == True):
                print ("input is can not be null and input again")

            elif (int(nm_first) == 1):
                try:
                    print ("tech page is begin start...")
                    start()
                except Exception:
                    traceback.print_exc()
                finally:
                    print ("test is end")

            elif (int(nm_first) == 2):
                try:
                    print ("login page is begin start")
                    #runLogin()
                except Exception:
                    traceback.print_exc()
                finally:
                    print ("test is end")

            elif (int(nm_first) == 3):
                try:
                    print ("forget password function is begin")

                except Exception:
                    traceback.print_exc()

            elif (int(nm_first) == 4):
                try:
                    print ("server page is begin....")

                except Exception:
                    traceback.print_exc()

            else:
                print ("input is invalid")
                mr.sleep(2)
                break

            mr.sleep(3)
            print ("please change a operate:")
            print ("1.tech page function")
            print ("2.login function")
            print ("3.forget password")
            print ("4.server and privacy")
            print ("input Q and ending the procedure")



# number = mr.input("enter you number:")
# try:
#     nm_first = int(number)
#     print nm_first
# except ValueError:
#     nm_first = str(number)
#     print nm_first
# else:
#     print "input have problem"
#
# while(1):
#     if (nm_first == 'q' or nm_first == 'Q'):
#         print "yes"
#     else:
#         print "no"