# -* encoding:utf-8 *-
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException,WebDriverException
from selenium.common.exceptions import WebDriverException
from test_cm_upgrade import *
from reptile_request_get import *
from reptile_request_post import *
from receive_email import  *
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers import SchedulerNotRunningError
import unittest
import time
import requests
import json
import os
from appium.webdriver.connectiontype import ConnectionType
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select
# from appium.webdriver.common.multi_action import MultiAction
# from collections import Counter                                 #使用Counter(列表)的方法时可以需要导入该包
# import threading



class AutoTest(unittest.TestCase):
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '4.4.4',
        'deviceName': '192.168.56.101:5555',
        'app': '/Users/apple/test2.9.apk',
        'unicodeKeyboard': 'True',
        'resetKeyboard': 'True'
    }
    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

    # 卸载重新安装APP，在测试订阅球队和页面数据统计的时候用，其他页面隐藏
    # if driver.is_app_installed("com.football.supergoal"):
    #     driver.remove_app("com.football.supergoal")
    #     driver.install_app("/Users/apple/test2.9.apk")
    # else:
    #     print 'app have installed'
    # start_p = 'com.football.supergoal'
    # start_a = 'com.soka.football.home.ui.login.activity.SplashActivity'
    # driver.start_activity(start_p, start_a)

    # driver.reset()
    driver.implicitly_wait(5)

    @classmethod
    def setUpClass(cls):    #每个测试函数运行前运行，即每个test方法运行前运行一次，setUpClass（cls）是所有test运行前运行，即某个类中所有test方法运行前运行
        #如果运行一个类中的测试用例放，那么setUpClass()方法只运行一次，如果该类中有3个test方法，则setUp()方法运行3次
        print 'process is set up now'

    @classmethod
    def tearDownClass(cls):       #每个测试函数运行完后运行，tearDownClass(cls)所有test运行完后运行一次,记住setUpClass方法定义时必须加@classmethod,而tearDown()方法不用加
        print "clean the process after it down "


    #测试用例方法开始处

    #检验email是否存在，并生成一个可用的email
    def emailScreen(self):
        conn, cur = connDB()
        result = selectDBAuto(cur, 'identity', 'identity')
        email = '840@qq.com'
        # print result[0][0]
        for i in range(0, len(result)):
            a = str(i)
            if (email == result[i][0]):
                if len(email) == 10:
                    email = email[:2] + a + email[3:]
                elif len(email) == 11:
                    email = email[:2] + a + email[4:]
                elif len(email) == 12:
                    email = email[:2] + a + email[5:]
                elif len(email) == 13:
                    email = email[:2] + a + email[6:]
                else:
                    print '邮箱已到达14位了，请在循环条件中添加'
        print ("the email is availabe:") + email
        return email

    #删除文本框内容
    def editTextClear(self,text):
        driver = self.driver
        driver.keyevent(123)                                                                            #该方法将光标移到最后
        for i in range(0,len(text)):
            driver.keyevent(67)                                                                         #退格键，删除作用

    #截图
    def screenShot(self, a):
        driver = self.driver
        driver.get_screenshot_as_file('/Users/apple/AppiumTestPng/' + a)

    # 兑换礼物屏幕向上滑
    def slideUp2(self):
        time.sleep(2)
        window_size = self.driver.get_window_size()
        x = window_size['width']
        y = window_size['height']
        x1 = int(x * 0.5)
        y1 = int(y * 0.85)
        y2 = int(y * 0.21)
        self.driver.swipe(start_x=x1, start_y=y1, end_x=x1, end_y=y2, duration=500)
    #兑换礼物屏幕向下滑
    def slideDown2(self):
        time.sleep(2)
        window_size = self.driver.get_window_size()
        x = window_size['width']
        y = window_size['height']
        x1 = int(x * 0.5)
        y1 = int(y * 0.24)
        y2 = int(y * 0.77)
        self.driver.swipe(start_x=x1, start_y=y1, end_x=x1, end_y=y2, duration=500)

    #屏幕向上滑
    def slideUp(self):
        time.sleep(2)
        window_size = self.driver.get_window_size()
        x = window_size['width']
        y = window_size['height']
        x1 = int(x * 0.5)
        y1 = int(y * 0.82)
        y2 = int(y * 0.31)
        self.driver.swipe(start_x=x1, start_y=y1, end_x=x1, end_y=y2, duration=500)
    #屏幕向下滑
    def slideDown(self):
        time.sleep(2)
        window_size = self.driver.get_window_size()
        x = window_size['width']
        y = window_size['height']
        x1 = int(x * 0.5)
        y1 = int(y * 0.24)
        y2 = int(y * 0.75)
        self.driver.swipe(start_x=x1, start_y=y1, end_x=x1, end_y=y2, duration=500)
    #屏幕向右滑
    def slideRight(self):
        time.sleep(2)      #该段休眠代码很重要，不然会报错
        window_size = self.driver.get_window_size()
        x = window_size['width']
        y = window_size['height']
        x1 = int(x * 0.36)
        x2 = int(x * 0.84)
        y1 = int(y * 0.5)
        self.driver.swipe(start_x=x1,start_y=y1,end_x=x2,end_y=y1,duration=500)
    #屏幕向左滑
    def slideLeft(self):
        time.sleep(2)      #该段休眠代码很重要，不然会报错
        window_size = self.driver.get_window_size()
        x = window_size['width']
        y = window_size['height']
        x1 = int(x * 0.84)
        y1 = int(y * 0.36)
        x2 = int(x * 0.1)
        self.driver.swipe(start_x=x1, start_y=y1, end_x=x2, end_y=y1, duration=500)

    #driver.find_element_by_android_uiautomator()方式获取元素的方法简单重写
    def getElementUI(self,content):
        driver = self.driver
        # print content                                                                                     #输出传入的参数值
        driver.find_element_by_android_uiautomator('new UiSelector().text("'+content+'")').click()          #注意，将其中的引号看成两对单引号来思考

    #driver.find_element_by_xpath()方式获取元素的方法简单重写
    def getXpath(self,content):
        driver = self.driver
        driver.find_element_by_xpath('//*[(@index="'+content+'" and @class="android.widget.RelativeLayout")]').click()

    #充值页面所需要的上滑坐标
    def slideUp1(self):
        time.sleep(2)
        window_size = self.driver.get_window_size()
        x = window_size['width']
        y = window_size['height']
        x1 = int(x * 0.5)
        y1 = int(y * 0.82)
        y2 = int(y * 0.4)
        self.driver.swipe(start_x=x1, start_y=y1, end_x=x1, end_y=y2, duration=500)

    #查看Live接口返回的数据是否去除了直播10分钟无直播数据的比赛记录
    def t6(self,matchId):
        a = 0
        b = matchId
        while a == 0:
            c = match_live()
            if b not in c:
                self.screenShot('Live5.png')                            # 接口返回的数据中刚设置后的比赛了，Live页面截图查看是否还存在该比赛显示
                time.sleep(6)
                self.screenShot('Live6.png')                            # 由于live页面是每5秒请求一次接口，因此接口返回数据同预期一样时，但是前端可能还没有请求接口
                a = 1
            else:                                                       # 因此上一张截图可能该比赛还存在于live页面，这张截图是6秒后的截图,接口一定请求了，所以可以该截图为准
                print '暂未删除，继续'
                time.sleep(10)
                a = 0
        else:
            print '该比赛开始后10分钟内直播数据，已被删除'
            return 1

    # 定时打开通知栏，查看比赛开始前5分钟个推消息发送
    def t3(self):
        driver = self.driver
        a = 0
        while a == 0:
            driver.open_notifications()
            try:
                b = driver.find_element_by_android_uiautomator(
                    'new UiSelector().text("The match Everton VS Watford is about to start.Click to watch it now.")')
                self.screenShot('push5.png')                            # 用户订阅的比赛开始前5分钟的个推消息在通知栏中的截图
                b.click()
                time.sleep(1)
                self.screenShot('push6.png')                            # 用户订阅的比赛开始前5分钟的个推消息点击后跳转到Live页面的截图
                return 1
            except NoSuchElementException:
                self.slideUp()
                time.sleep(5)
                return 0

    #定时调用竞猜历史记录接口，每隔10秒调一次接口，如果结束竞猜则停止调用
    def t2(self):
        a = 0
        while a == 0:
            a = prediction_history()
            time.sleep(10)
        else:
            print '注意！竞猜记录显示已结束竞猜'
            return 1

    #setting、copyright、server页面的跳转
    def test_anotherPage(self):
        driver = self.driver
        a = driver.find_element_by_id('title_bar_iv_left')
        a.click()
        driver.find_element_by_id("tv_setting").click()                                                 #个人中心setting页面
        time.sleep(1)
        self.screenShot('anotherPage7.png')
        a.click()

        a.click()
        window_size = self.driver.get_window_size()
        x = window_size['width']                                                                        # 该模拟器的宽是480
        y = window_size['height']                                                                       # 该模拟器的长是728
        x1 = int(x * 0.24)
        y1 = int(y * 0.68)
        y2 = int(y * 0.357)
        time.sleep(1)                                                                                   #该段休眠不能去除
        self.driver.swipe(start_x=x1, start_y=y1, end_x=x1, end_y=y2, duration=1000)
        driver.find_element_by_id("tv_copyright").click()                                               #个人中心copyright页面
        time.sleep(2)
        self.screenShot('anotherPage1.png')
        a.click()

        driver.find_element_by_id("tv_service").click()                                                 #个人中心service页面
        time.sleep(1)
        self.screenShot('anotherPage8.png')
        a.click()

        driver.find_element_by_id("tv_policy").click()                                                  #个人中心privacy页面
        time.sleep(2)
        self.screenShot('anotherPage2.png')
        a.click()

        time.sleep(1)
        self.driver.swipe(start_x=x1, start_y=y2, end_x=x1, end_y=y1, duration=1000)

        driver.find_element_by_id("iv_avatar").click()
        time.sleep(1)
        driver.tap([(220,573)])                                         #登录页面中service页面，通过元素坐标点击，注意该方式点击，在tap方法内传入的position参数值必须是元组
        time.sleep(1)
        self.screenShot('anotherPage3.png')
        a.click()

        driver.tap([(366,576)])                                         #登录页面中privacy页面
        time.sleep(2)
        self.screenShot('anotherPage4.png')
        a.click()

        driver.find_element_by_id("rb_sign_up").click()
        time.sleep(1)                                                   #该段休眠不能删除
        driver.tap([(382,566)])                                         #注册页面中service页面
        time.sleep(2)
        self.screenShot('anotherPage5.png')
        a.click()

        driver.tap([(226,583)])                                         #注册页面中privacy页面
        time.sleep(2)
        self.screenShot('anotherPage6.png')
        a.click()

        print 'copyright等页面测试完毕'

    #notification页面
    def test_feedback(self):
        driver = self.driver
        b = driver.find_element_by_id("title_bar_iv_left")
        b.click()
        c = driver.find_element_by_id("tv_feedback")
        c.click()
        driver.find_element_by_id("btn_send").click()
        time.sleep(1)
        self.screenShot('feedback1.png')                                        #未输入内容时点击提交按钮系统反馈截图

        driver.find_element_by_id("et_suggest").send_keys('this is autotest')   #用户反馈功能的测试用例编写，还有部分可待之后再补
        driver.find_element_by_id("btn_send").click()
        time.sleep(2)
        self.slideUp()
        self.screenShot('feedback2.png')

        a = feedback_list()
        if a == 'this is autotest':
            print '该用户发送的消息在系统后台正确显示'
        else:
            print '系统后台第一条数据不是该用户发送的消息，很可能错误，请在系统后台核对！'

        conn, cur = connDB()
        result = feedbackAuto(cur)                                              #注意，这里content的内容写死了，之后变化需要同步进行更改
        uid = result[0][0]
        feedback_message_add(uid)                                               #系统后台回复用户消息接口调用
        b.click()
        c.click()
        time.sleep(2)
        self.screenShot('feedback3.png')

        print '用户反馈功能测试完毕'
        return uid                                                              #该代码作用是查询出刚发送消息的用户Uid

    #redeem gift页面
    def test_redeemGift(self):
        # uid = self.test_feedback()
        # print isinstance(uid,int)
        driver = self.driver
        conn, cur = connDB()
        result1 = permission(cur,241)                                           #查询出刚发送feedback的用户，是否具有积分兑换权限
        a = driver.find_element_by_id("title_bar_iv_left")
        if result1 == 0:                                                        #0代表该用户没有权限
            a.click()
            b = driver.find_element_by_id("tv_redeem")
            b.click()
            time.sleep(1)
            self.screenShot('redeem1.png')                                      #用户没有权限时页面的显示情况
            insert_permission(conn, cur, 241,'exchange')                        #新增用户兑换话费权限
            print '新增用户兑换话费权限成功'
            a.click()
            b.click()
            time.sleep(1)
            self.screenShot('redeem2.png')                                      #用户拥有兑换话费权限时页面的显示情况

            insert_permission(conn,cur,241,'redeem')                            #新增用户兑换其他商品权限
            print '新增用户兑换兑换其他商品权限成功'
            a.click()
            b.click()
            time.sleep(1)
            self.screenShot('redeem3.png')                                      #用户拥有兑换其他商品权限时页面的显示情况

        elif result1 == 1:
            a.click()
            b = driver.find_element_by_id("tv_redeem")
            b.click()
            time.sleep(1)
            self.screenShot('redeem3.png')

            delete_permission(conn, cur, 241,'redeem')                          #删除权限
            print '已删除用户兑换其他商品权限'
            a.click()
            b.click()
            time.sleep(1)
            self.screenShot('redeem2.png')

            delete_permission(conn, cur, 241,'exchange')                        #删除权限
            print '已删除用户兑换话费权限'
            a.click()
            b.click()
            time.sleep(1)
            self.screenShot('redeem1.png')

            insert_permission(conn, cur, 241,'exchange')                        #新增用户积分兑换权限
            insert_permission(conn,cur,241,'redeem')
            a.click()
            b.click()
        else:
            print '数据库中积分兑换权限的字段值发生了变化，请核对之'

        time.sleep(2)
        driver.tap([(133,258)])
        time.sleep(1)
        self.screenShot('redeem4.png')                                          # my coins按钮点击后截图
        a.click()
        e = driver.find_elements_by_id('tv_redeem')
        e[0].click()
        self.screenShot('redeem5.png')                                          #kenya兑换所需要的金钱数，查看顶部是否是KES300的截图
        c = driver.find_element_by_id('tv_country2')
        c.click()
        self.screenShot('redeem6.png')                                          #NGN1000兑换所需要的金钱数，查看顶部是否是NGN1000的截图
        driver.find_element_by_id('tv_cancel').click()
        self.screenShot('redeem7.png')                                          #检测取消按钮是否有效
        e[0].click()
        b = driver.find_element_by_id("tv_redeem")
        b.click()
        self.screenShot('redeem8.png')                                          #未填写电话号码点击redeem按钮的效果截图
        driver.find_element_by_id('et_tel').send_keys('1357578912')
        b.click()
        self.screenShot('redeem9.png')                                          # 填写电话号码位数少于11位时点击redeem按钮的效果截图
        c.click()
        b.click()
        self.screenShot('redeem10.png')                                         # 以上情况切换到Nigeria时点击redeem按钮的效果截图

        sql1 = "update user_point set point = 2999 where uid = 241"             # 将该用户的金币数量设置为2999
        cur.execute(sql1)
        conn.commit()
        delete_userSign(conn, cur, 241)
        time.sleep(1)
        driver.find_element_by_id('et_tel').send_keys('13575789124')
        b.click()
        time.sleep(1)
        self.screenShot('redeem11.png')                                                                                 # 用户金币数量不足时点击redeem按钮的效果截图
        driver.find_element_by_id('tv_getCoin').click()
        self.screenShot('redeem12.png')                                                                                 # 弹出的窗口中get coins按钮点击效果截图
        driver.find_element_by_id('tv_sign_in').click()
        driver.find_element_by_id('tv_sign_in').click()
        time.sleep(1)
        driver.tap([(216,671)])
        time.sleep(2)
        self.screenShot('redeem13.png')                                                                                 # 查看签到后的金币数量
        a.click()
        b.click()
        e[0].click()
        driver.find_element_by_id('et_tel').send_keys('13575789124')
        b.click()
        time.sleep(1)
        self.screenShot('redeem14.png')                                                                                 # 金币数量为3000时点击redeem按钮的效果截图
        d = driver.find_element_by_id('tv_ok')
        d.click()
        self.screenShot('redeem15.png')                                                                                 # 弹出的ok按钮点击效果截图

        a.click()
        self.screenShot('redeem16.png')                                                                                 # 返回个人中心页面，查看notification是否有小红点标识的截图
        driver.find_element_by_id('tv_feedback').click()
        time.sleep(1)
        self.screenShot('redeem17.png')                                                                                 # 兑换礼物后系统自动推送的文案截图
        a.click()
        self.screenShot('redeem18.png')                                                                                 # 返回个人中心页面，查看notification的小红点消失的截图
        f = driver.find_element_by_id('tv_myCoin')
        f.click()
        f.click()
        time.sleep(1)
        self.screenShot('redeem19.png')                                                                                 # 查看兑换成功后金币记录中是否有相应的记录存在截图

        a.click()
        a.click()
        b.click()
        sql2 = "update user_point set point = 3000 where uid = 241"
        cur.execute(sql2)
        conn.commit()
        e[0].click()
        c.click()                                                                                                       #测试选择Nigeria后兑换功能是否正常流程
        driver.find_element_by_id('et_tel').send_keys('13575789124')
        b.click()
        d.click()

        sql3 = "update user_point set point = 145500 where uid = 241"                                                   #兑换Samsung手机的功能是否正常流程
        cur.execute(sql3)
        conn.commit()
        e[1].click()
        b.click()
        d.click()
        self.slideUp2()

        time.sleep(1)                                                                                                   #该休眠不能缺少，否则滑动还未结束就实现点击操作了
        sql4 = "update user_point set point = 24300 where uid = 241"                                                    #兑换soccer ball的功能是否正常流程
        cur.execute(sql4)
        conn.commit()
        time.sleep(2)
        e[0].click()
        b.click()
        d.click()

        sql5 = "update user_point set point = 125700 where uid = 241"                                                   # 兑换football boots的功能是否正常流程
        cur.execute(sql5)
        conn.commit()
        e[1].click()
        b.click()
        d.click()

        sql6 = "update user_point set point = 15100 where uid = 241"                                                    # 兑换stockings的功能是否正常流程
        cur.execute(sql6)
        conn.commit()
        driver.find_elements_by_id('tv_redeem')[2].click()
        b.click()
        d.click()

        a.click()
        driver.find_element_by_id('tv_feedback').click()
        time.sleep(1)
        self.screenShot('redeem20.png')                                                                                 # 查看兑换商品成功后是否都有系统发送的文案消息
        self.slideDown2()
        time.sleep(1)
        self.screenShot('redeem21.png')                                                                                 # 总共有6条系统文案消息发送
        a.click()
        f.click()
        f.click()
        time.sleep(1)
        self.screenShot('redeem22.png')                                                                                 # 用户金币记录页面中查看是否有相应的兑换记录
        self.slideDown()
        time.sleep(1)
        self.screenShot('redeem23.png')                                                                                 # 兑换记录总共有6条

        point_goodRecord(241)                                                                                           #系统后台兑换管理接口请求，查看系统后台是否有相应的兑换记录
        print '兑换商品功能测试完毕'

    #循环注册
    def test_register1(self):
        for i in range(1000):
            driver = self.driver
            email = self.emailScreen()
            password = '123456'
            time.sleep(1)
            if i == 0:
                driver.find_element_by_id("title_bar_iv_left").click()
            else:
                driver.find_element_by_id("iv_avatar").click()
                driver.find_element_by_id("rb_sign_up").click()
                a = driver.find_element_by_id("et_email")                                                               # 输入数据库中不存在且格式正确的email
                a.click()
                a.send_keys(email)
                b = driver.find_element_by_id("et_password")                                                            # 输入格式正确的密码
                b.click()
                b.send_keys(password)                                                                                   # 输入6位数正确的密码

                c = driver.find_element_by_id("et_confirm_password")
                c.click()
                c.send_keys(password)                                                                                   # 注册的冒烟测试
                driver.find_element_by_id("btn_sign").click()
                driver.find_element_by_id("iv_avatar").click()
                driver.find_element_by_id("btn_logout").click()
                driver.find_element_by_id("btn_confirm").click()

    #转账功能
    def test_transfer(self):
        driver = self.driver
        conn,cur = connDB()
        sql1 = 'select point from user_point where uid = 241'
        cur.execute(sql1)
        d = cur.fetchall()
        if d[0][0] == 0:
            sql2 = 'update user_point set point = 100 where uid = 241'
            cur.execute(sql2)
            conn.commit()
        cur.execute(sql1)
        d = cur.fetchall()
        e = d[0][0] + 1
        f = driver.find_element_by_id("title_bar_iv_left")
        f.click()
        try:
            driver.find_element_by_id('tv_transfer').click()
        except NoSuchElementException:
            insert_permission(conn, cur, 241, 'transfer')                               # 新增用户转账权限
            s1 = "adb shell am force-stop com.football.supergoal"
            os.system(s1)
            start_p = 'com.football.supergoal'
            start_a = 'com.soka.football.home.ui.login.activity.SplashActivity'
            driver.start_activity(start_p, start_a)
            driver.find_element_by_id("title_bar_iv_left").click()
            driver.find_element_by_id('tv_transfer').click()
        time.sleep(1)
        self.screenShot('transfer1.png')       # 转账页面的截图，主要查看用户的金币数量显示是否正确
        a = driver.find_element_by_id('et_1')
        b = driver.find_element_by_id('et_2')
        driver.find_element_by_id('tv_record').click()
        time.sleep(2)
        self.screenShot('transfer2.png')       # 用户转账记录的截图
        f.click()
        a.send_keys('sdhna213')
        b.click()
        self.screenShot('transfer3.png')       #测试输入特殊字符系统的提示截图
        a.click()
        text = a.get_attribute('text')
        self.editTextClear(text)
        a.send_keys('1234591')
        b.click()
        self.screenShot('transfer4.png')       #测试输入7位数系统的提示截图

        a.click()
        text = a.get_attribute('text')
        self.editTextClear(text)
        a.send_keys('123459149')
        b.click()
        self.screenShot('transfer5.png')       # 测试输入9位数系统的提示截图
        a.click()
        text = a.get_attribute('text')
        self.editTextClear(text)
        a.send_keys('12345 32')
        b.click()
        self.screenShot('transfer6.png')       # 测试输入数字中存在空格时系统的提示截图

        c = 12345678 + 241                     # 241是uid，之后切换用户需要用uid代替
        a.click()
        text = a.get_attribute('text')
        self.editTextClear(text)
        a.send_keys(c)
        b.click()
        self.screenShot('transfer7.png')       #输入的id是自己的id时系统提示截图
        a.click()
        text = a.get_attribute('text')
        self.editTextClear(text)
        a.send_keys('99991239')
        b.send_keys('1')
        self.screenShot('transfer8.png')       # 输入的用户id不存在时，系统提示截图
        s1 = driver.find_element_by_id('tv_confirm')
        s1.click()
        s1.click()
        time.sleep(2)
        self.screenShot('transfer9.png')       # 输入的用户id不存在时，用户提交后系统提示截图

        a.click()
        text = a.get_attribute('text')
        self.editTextClear(text)
        a.send_keys('12345846')
        b.click()
        text = b.get_attribute('text')
        self.editTextClear(text)
        b.send_keys('0')
        self.screenShot('transfer10.png')       # 输入的转账金币数量为0时系统提示截图

        b.click()
        text = b.get_attribute('text')
        self.editTextClear(text)
        time.sleep(1)
        b.send_keys(e)
        self.screenShot('transfer11.png')       # 输入的转账金币数量大于用户拥有的金币数时系统提示截图
        b.click()
        text = b.get_attribute('text')
        self.editTextClear(text)
        b.send_keys(d[0][0])
        self.screenShot('transfer12.png')       # 输入的转账金币数量是用户拥有的金币数最大值时系统提示截图
        s1.click()
        time.sleep(1)
        self.screenShot('transfer13.png')       # 转账申请提交后弹出的确认窗口截图，主要核对转账的信息是否正确
        s1.click()
        time.sleep(1)
        self.screenShot('transfer14.png')       # 转账成功后的提示窗口截图
        d.click()
        driver.find_element_by_id('tv_record').click()
        time.sleep(1)
        self.screenShot('transfer15.png')       # 该用户转账成功后的转账记录页面截图
        f.click()
        f.click()
        self.screenShot('transfer16.png')       # 该用户个人中心侧栏显示的金币数截图
        s2 = driver.find_element_by_id('tv_myCoin')
        s2.click()
        s2.click()
        time.sleep(1)
        self.screenShot('transfer17.png')       # 该用户金币记录页面截图

        f.click()
        f.click()
        driver.find_element_by_id('iv_avatar').click()
        driver.find_element_by_id('et_email').send_keys('893026750@qq.com')
        driver.find_element_by_id('et_password').send_keys('123456')                    # 登录被转账的用户账号
        driver.find_element_by_id('btn_login').click()
        time.sleep(2)
        self.screenShot('transfer18.png')      # 查看是否转入金币的系统消息在notification中，有小红点标识
        driver.find_element_by_id('tv_feedback').click()
        self.screenShot('transfer19.png')      # 查看转入金币的用户收到的系统文案消息是否正确
        f.click()
        s2.click()
        s2.click()
        self.screenShot('transfer20.png')      # 查看是否有转入金币的记录截图

        f.click()
        f.click()
        driver.find_element_by_id('iv_avatar').click()
        driver.find_element_by_id('btn_logout').click()
        s1.click()                                #退出登录的用户账号
        print '转账功能测试完毕'

    #注册页面
    def test_register(self):
        driver = self.driver
        email = self.emailScreen()
        password = '123456'
        driver.find_element_by_id("title_bar_iv_left").click()
        driver.find_element_by_id("iv_avatar").click()
        driver.find_element_by_id("rb_sign_up").click()
        a = driver.find_element_by_id("et_email")                                   #输入数据库中不存在且格式正确的email
        a.click()
        a.send_keys(email)
        b = driver.find_element_by_id("et_password")                                #输入格式正确的密码
        b.click()
        b.send_keys('12345')
        c = driver.find_element_by_id("et_confirm_password")
        c.click()
        self.screenShot('register1.png')                                            #输入少于6位数的密码的截图
        b.click()
        b.send_keys('123456789012345678901')
        c.click()
        self.screenShot('register2.png')                                            #输入大于20位数的密码

        b.click()
        b.send_keys(password)                                                       #输入6位数正确的密码

        c.click()
        c.send_keys('1234567')
        driver.find_element_by_id("et_password").click()
        self.screenShot('register3.png')                                            #确认密码错误时的截图

        c.click()
        text = c.get_attribute('text')
        self.editTextClear(text)
        c.send_keys(password)
        driver.find_element_by_id("btn_sign").click()
        time.sleep(2)
        self.screenShot('register4.png')                                            # 注册的冒烟测试截图
        driver.find_element_by_id("iv_avatar").click()
        driver.find_element_by_id("btn_logout").click()
        driver.find_element_by_id("btn_confirm").click()
        time.sleep(2)
        self.screenShot('register5.png')                                            #退出新注册用户的账号截图

        print '注册功能测试完毕'

    #登录页面
    def test_login(self):
        driver = self.driver
        driver.find_element_by_id('title_bar_iv_left').click()
        driver.find_element_by_id("iv_avatar").click()
        time.sleep(2)
        a = driver.find_element_by_id("et_email")
        a.click()
        a.send_keys('abddsaqqcom')
        b = driver.find_element_by_id("et_password")
        b.click()
        self.screenShot('login1.png')                                               #邮箱只输入字母的截图

        a.click()
        a.send_keys('89302675023')
        b.click()
        self.screenShot('login2.png')                                               #邮箱只输入数字的截图

        a.click()
        a.send_keys('     893026750@163.com')
        b.click()
        self.screenShot('login3.png')                                               #邮箱输入首部为空格

        a.click()
        a.send_keys('893026750@163.com')
        for i in range(1,7):
            driver.keyevent(62)
        b.click()
        self.screenShot('login4.png')                                              #邮箱输入尾部为空格

        a.click()
        a.send_keys('893026750      @163.com')
        b.click()
        self.screenShot('login5.png')                                              #邮箱输入中间为空格

        a.click()
        a.send_keys('893026750@163com')
        b.click()
        self.screenShot('login6.png')                                              #邮箱输入没有点号

        a.click()
        a.send_keys('893026750163.com')
        b.click()
        self.screenShot('login7.png')                                              #邮箱输入没有@符号

        a.click()
        a.send_keys('h893026750@qq.com')
        b.click()
        self.screenShot('login8.png')                                              #邮箱输入格式正确

        b.send_keys('12345')
        a.click()
        self.screenShot('login9.png')                                              #密码输入格式只有5位

        b.click()
        b.send_keys('naiwu0113425hongnaiwu')
        a.click()
        self.screenShot('login10.png')                                             #密码输入格式有21位

        b.click()
        b.send_keys('aiwu0113425hongnaiwu')
        a.click()
        self.screenShot('login11.png')                                             #密码输入有20位时的截图

        b.click()
        text = b.get_attribute('text')
        self.editTextClear(text)
        b.send_keys('123456')
        a.click()                                                                  #输入6位格式正确的密码时的截图
        self.screenShot('login12.png')

        driver.find_element_by_id('btn_login').click()
        time.sleep(1)
        self.screenShot('login13.png')                                             #登录一个数据库不存在的即未注册的账号

        a.click()
        a.send_keys('893026750@qq.com')
        b.click()
        b.send_keys('12345678')
        driver.find_element_by_id('btn_login').click()
        time.sleep(1)
        self.screenShot('login14.png')                                             #登录密码错误时的截图

        b.click()
        b.send_keys('123456')
        driver.find_element_by_id('btn_login').click()
        time.sleep(2)
        self.screenShot('login15.png')                                             #登录正确的账号密码时的截图

        driver.find_element_by_id('iv_avatar').click()
        time.sleep(1)
        driver.find_element_by_id('btn_logout').click()
        driver.find_element_by_id('btn_confirm').click()
        driver.find_element_by_id('iv_avatar').click()                              #用户退出登录

        a.click()
        a.send_keys('h893026750qq.com')
        driver.find_element_by_id('tv_forget').click()
        time.sleep(1)
        self.screenShot('login16.png')                                              #邮箱格式不正确时的截图

        a.click()
        a.send_keys('h893026750@qq.com')
        driver.find_element_by_id('tv_forget').click()
        time.sleep(1)
        self.screenShot('login17.png')                                              #邮箱在数据库中不存在时的截图

        a.click()
        a.send_keys('893026750@qq.com')
        driver.find_element_by_id('tv_forget').click()
        time.sleep(1)
        self.screenShot('login18.png')                                               #邮箱正确且存在时的截图

        c = driver.find_element_by_id('et_new')
        c.click()
        c.send_keys('123456')

        d = driver.find_element_by_id('et_confirm')
        d.click()
        d.send_keys('1234567')
        e = driver.find_element_by_id('et_code')
        e.click()
        self.screenShot('login19.png')                                                #再次输入的密码错误

        d.click()
        d.send_keys('123456')
        e.send_keys('asj1')
        f = driver.find_element_by_id('btn_change')
        f.click()
        time.sleep(1)
        self.screenShot('login20.png')                                                 #验证码输入错误时的截图

        r, t = receiveEmail()
        e.click()
        text = e.get_attribute('text')
        self.editTextClear(text)
        if len(t) == 0:
            print '邮箱中没有超时验证码的邮件，请核实！'
        e.send_keys(t[0])
        f.click()
        time.sleep(1)
        self.screenShot('login21.png')                                                  #输入超时的验证码时的截图

        e.click()
        text = e.get_attribute('text')
        self.editTextClear(text)
        s = len(r)
        e.send_keys(r[s-1])
        f.click()
        time.sleep(1)
        self.screenShot('login22.png')                                                  #输入正确的验证码

        print '登录功能测试完毕'

    #完成签到任务
    def test_cplSingInTask(self):
        # uid = self.test_feedback()                  #获取用户的uid值
        # print uid
        # print isinstance(uid,int)                 #判断uid值是否是int类型
        conn, cur = connDB()
        delete_userSign(conn, cur, 241)
        print '删除用户签到记录成功'
        driver = self.driver

        driver.find_element_by_id('title_bar_iv_left').click()
        b = driver.find_element_by_id('tv_myCoin')
        b.click()
        time.sleep(1)
        self.screenShot('task29.png')      #我的金币页面
        a = driver.find_element_by_id('tv_sign_in')
        a.click()
        a.click()
        time.sleep(1)
        self.screenShot('task1.png')   #签到第一天的截图
        driver.tap([(106, 131)])
        time.sleep(1)
        self.screenShot('task2.png')  #查看第一天签到后金币是否加1的截图

        for i in range(7):                #再签到7天,查看签到后的截图
            update_userSign(conn, cur, 241)
            driver.find_element_by_id('title_bar_iv_left').click()
            b.click()
            a.click()
            a.click()
            time.sleep(2)
            if i == 0:
                self.screenShot('task3.png') #签到第二天的截图
                driver.tap([(106, 131)])
                time.sleep(1)
                self.screenShot('task4.png') #查看第二天签到后金币是否加2的截图
            elif i == 1:
                self.screenShot('task5.png') # 签到第三天的截图
                driver.tap([(106, 131)])
                time.sleep(1)
                self.screenShot('task6.png') #查看第三天签到后金币是否加3的截图
            elif i == 2:
                self.screenShot('task7.png') # 签到第四天的截图
                driver.tap([(106,131)])
                time.sleep(1)
                self.screenShot('task8.png') #查看第四天签到后金币是否加4的截图
            elif i == 3:
                self.screenShot('task9.png') # 签到第五天的截图
                driver.tap([(106,131)])
                time.sleep(1)
                self.screenShot('task10.png') #查看第五天签到后金币是否加5的截图
            elif i == 4:
                self.screenShot('task11.png') # 签到第六天的截图
                driver.tap([(106,131)])
                time.sleep(1)
                self.screenShot('task12.png') #查看第六天签到后金币是否加6的截图
            elif i == 5:
                self.screenShot('task13.png') # 签到第七天的截图
                driver.tap([(106,131)])
                time.sleep(1)
                self.screenShot('task14.png') #查看第七天签到后金币是否加7的截图
            elif i == 6:
                self.screenShot('task15.png') # 签到第八天的截图
                driver.tap([(106,131)])
                time.sleep(1)
                self.screenShot('task16.png') #查看第八天签到后金币是否只加7的截图
            else:
                print '循环出错，请查看程序'
        b.click()
        time.sleep(1)
        self.screenShot('task17.png')
        self.slideUp()
        time.sleep(1)
        self.screenShot('task18.png')

        print '签到任务测试完毕'

    #完成日常任务
    def test_dailyTask(self):
        # uid = self.test_feedback()  # 获取用户的uid值
        # print uid
        conn, cur = connDB()
        delete_userFetch(conn, cur, 241)
        delete_point_record(conn, cur, 241)
        sql2 = "delete from user_like where uid = 241"
        cur.execute(sql2)
        conn.commit()
        print '删除用户完成任务记录、观看视频文章记录以及喜欢的视频记录成功'

        driver = self.driver
        a = driver.find_element_by_id('title_bar_iv_left')
        a.click()
        b = driver.find_element_by_id('tv_myCoin')
        b.click()
        self.screenShot('task19.png')                                    #我的金币页面

        a.click()
        driver.tap([(352,320)])
        self.slideUp()
        time.sleep(2)
        driver.find_element_by_id('tv_title').click()
        time.sleep(1)
        self.screenShot('task20.png')                                    #完成日常video任务时的截图
        driver.find_element_by_id('tv_view').click()
        time.sleep(1)
        self.screenShot('task21.png')                                    #点击view按钮，查看是否正确跳转到兑换商品页面的截图

        a.click()
        driver.find_element_by_id('tv_like').click()
        time.sleep(1)
        self.screenShot('task22.png')                                    #完成日常like任务时的截图

        driver.find_element_by_id('iv_back').click()
        a.click()
        b.click()
        time.sleep(1)
        self.screenShot('task23.png')                                    #查看我的金币记录页面中任务完成情况截图

        a.click()
        driver.tap([(363,376)])
        driver.find_element_by_id('rb_news').click()                            #该方式不能成功点击
        # driver.find_element_by_xpath("//*[@text='NEWS']").click()
        time.sleep(1)
        driver.find_element_by_id('tv_views').click()
        time.sleep(1)
        self.screenShot('task24.png')                                    #完成日常news任务时的截图
        a.click()
        a.click()
        b.click()
        time.sleep(1)
        self.screenShot('task25.png')                                    #查看是否任务完成的截图

        team_A_name, team_B_name, match_id, status = select_match(cur)   # 完成日常match任务
        a.click()
        driver.tap([(352,320)])
        driver.find_element_by_xpath("//*[@text='MATCH']").click()
        try:
            driver.find_element_by_id('title_bar_tv_right')
            a.click()
        except NoSuchElementException:
            print '订阅页面不存在'
        s1 = driver.find_element_by_id('tv_left_name')
        text1 = s1.text
        s2 = driver.find_element_by_id('tv_right_name')
        text2 = s2.text
        if team_A_name == text1 and team_B_name == text2:
            if status == 2:
                s1.click()
                time.sleep(1)
                self.screenShot('task26.png')                               #比赛状态为未开始，观看该比赛时任务未完成的截图

                a.click()
                update_match(conn,cur,match_id,status)                      #更改比赛状态为直播中
                s1.click()
                time.sleep(1)
                self.screenShot('task27.png')                               #观看直播状态的比赛，任务完成的截图

                a.click()
                a.click()
                b.click()
                time.sleep(1)
                self.screenShot('task28.png')                               #观看比赛任务完成后金币页面截图

                b.click()
                time.sleep(1)
                self.screenShot('task29.png')                               #查看任务完成金币记录页面

                sql1 = "select status from `match` where match_id = '%d' " % (match_id)
                cur.execute(sql1)
                s3 = cur.fetchall()
                update_match(conn,cur,match_id,s3[0][0])

            elif status == 1:
                s1.click()
                time.sleep(1)
                self.screenShot('task27.png')      # 观看直播状态的比赛，任务完成的截图

                a.click()
                a.click()
                b.click()
                self.screenShot('task28.png')      # 观看比赛任务完成后金币页面截图

                b.click()
                self.screenShot('task29.png')      # 查看任务完成金币记录页面
            else:
                print '该比赛的数据错误，应该是手动修改的比赛状态为0，请核对'


        else:
            print '该比赛显示与数据库中查询出的结果不同，请核对检验'        #注意核对手机的时间，显示的比赛会根据手机时间来查询，所以手机时间错误可能会导致该情况发生

        print '日常任务测试完毕'
        # a = 'Huddersfield'
        # driver.find_element_by_xpath("//*[@text=a]").click()          #这种方法是通过text内容来定位元素的，但是text不能使用a变量的值，这个问题待之后处理
        # self.getElementUI("Huddersfield")      #该方法也是通过text内容定位元素的，问题与上面一样

    #完成其他任务
    def test_otherTask(self):
        email = self.emailScreen()
        password = '123456'
        driver = self.driver
        s1 = driver.find_element_by_id('title_bar_iv_left')
        s1.click()
        s2 = driver.find_element_by_id('tv_myCoin')
        s2.click()
        self.slideUp()
        time.sleep(2)
        self.screenShot('task30.png')                                                   #其他任务未完成的截图

        s1.click()
        s3 = driver.find_element_by_id('iv_avatar')
        s3.click()
        driver.find_element_by_id('rb_sign_up').click()
        a = driver.find_element_by_id('et_email')                                       #新注册一个用户然后会自动登录
        a.click()
        a.send_keys(email)
        b = driver.find_element_by_id('et_password')
        b.click()
        b.send_keys(password)
        c = driver.find_element_by_id('et_confirm_password')
        c.click()
        c.send_keys(password)
        driver.find_element_by_id('btn_sign').click()

        time.sleep(2)
        self.screenShot('task31.png')                                                   #新注册用户是否有1000金币赠送的截图,现在是根据设备号绑定，同一个设备只能送一次

        s3.click()
        driver.find_element_by_id('tv_birthday').click()
        driver.find_element_by_id('tv_cancel').click()
        self.screenShot('task32.png')                                                   #取消设置生日的截图

        driver.find_element_by_id('tv_birthday').click()
        driver.find_element_by_id('tv_confirm').click()
        time.sleep(1)
        self.screenShot('task33.png')                                                   #设置生日时的任务完成截图

        s3.click()
        driver.find_element_by_id('tv_cancel').click()
        self.screenShot('task34.png')                                                   #取消设置头像的截图

        s3.click()
        driver.find_element_by_id('tv_one').click()
        time.sleep(1)
        driver.tap([(99,225)])                #以下三个根据模拟器的坐标来实现点击的，如果换个不同手机分辨率或者手机中图片文件有更改，可能会导致寻找不到该元素
        time.sleep(2)
        driver.tap([(241,428)])
        time.sleep(2)
        driver.tap([(105,71)])
        time.sleep(8)
        self.screenShot('task35.png')                                                   #上传头像的任务完成截图，该步骤可能会很慢，导致后面元素获取不到，请注意！

        try:
            driver.find_element_by_id('tv_nickname').click()
        except NoSuchElementException:
            time.sleep(3)
            self.screenShot('task35.png')
            driver.find_element_by_id('tv_nickname').click()
        driver.tap([(202,156)])
        driver.press_keycode(32)
        driver.press_keycode(8)
        driver.press_keycode(9)
        driver.press_keycode(39)
        s1.click()
        self.screenShot('task36.png')                                                   #取消设置昵称的截图

        driver.find_element_by_id('tv_nickname').click()
        driver.tap([(202, 156)])
        driver.press_keycode(32)
        driver.press_keycode(8)
        driver.press_keycode(9)
        driver.press_keycode(39)
        driver.find_element_by_id('title_bar_tv_right').click()
        time.sleep(2)
        self.screenShot('task37.png')                                                   #设置昵称任务完成的截图

        s1.click()
        s2.click()
        time.sleep(2)
        self.slideUp()
        time.sleep(1)
        self.screenShot('task38.png')                                                   #其他任务都完成的任务页面展示
        self.slideDown()
        s2.click()
        time.sleep(1)
        self.screenShot('task39.png')                                                   #任务完成后金币记录页面展示

        print '其他任务测试完毕'
        #资讯页面

    #充值功能，国家汇率变动时查看用户此时充值时是否有提示
    def test_recharge(self):
        # uid = self.test_feedback()  # 获取用户的uid值
        # print uid
        # conn,cur = connDB()
        driver = self.driver
        #
        # driver.find_element_by_id('title_bar_iv_left').click()
        # driver.tap([(352,320)])
        driver.find_element_by_id('rb_prediction').click()
        # time.sleep(3)
        # self.screenShot('recharge1.png')       #用户没有充值权限的截图
        #
        # a = select_recharge(cur, uid)
        # update_recharge(conn,cur,uid,a)
        # self.slideDown()
        # time.sleep(3)
        # self.screenShot('recharge2.png')       #增加用户充值权限的截图
        #
        # driver.find_element_by_id('tv_recharge').click()
        # contexts = driver.contexts              #context是代表两个不同的环境，driver.contexts获取native和webview页面环境，返回数列值
        # # souce = driver.page_source            #获取当前页面的源代码
        # # f = open("page_source.txt",'wb')      #打开一个文件，没有就新建一个，w是新建（会覆盖原有文件），b是二进制文件，a的话就是在末尾追加
        # # f.write(souce+'\n')                   #wb就是以二进制写模式打开
        # # f.close()                             #写入的内容格式会自动换行，但是不能根据元素换行，即不能显示于网站形式一样，这个问题待之后研究
        # driver.switch_to.context(contexts[1])   #切换到webview环境,切换回native环境按以上步骤再次操作即可
        # now = driver.current_context
        # print now
        # # WebDriverWait(driver, 5).until(lambda driver: driver.find_elements_by_class_name('wrapper')[1],message='该元素检测超时，查看网络情况')
        # driver.find_element_by_class_name('records').click()
        # time.sleep(3)
        # driver.switch_to.context("NATIVE_APP")          #切换到原生环境，不然不能够使用下一行截图的代码
        # self.screenShot('recharge3.png')       #无充值记录时的页面显示
        # driver.find_element_by_id('title_bar_iv_left').click()
        #
        # driver.switch_to.context(contexts[1])
        # for i in range(8):
        #     time.sleep(2)
        #     driver.switch_to.context(contexts[1])
        #     driver.find_element_by_class_name('countrySelect').click()
        #     g = Select(driver.find_element_by_class_name('countrySelect'))
        #     if i == 0 or i == 1 or i == 2 or i == 3:
        #         g.select_by_value('Kenya')                        #点击下拉框中值的方法！！使用select_by_value()方法，以及之前还需要实例化Select为g哦！
        #     else:
        #         g.select_by_value('Nigeria')                          #注意该方式点击有一个特点，就是相当于只是选择了下拉框中的值，但是并没有点击的效果，只是选中的效果！！
        #     driver.switch_to.context(contexts[0])
        #     driver.tap([(237,495)])                                 #点击屏幕的任意一处回到未弹出下拉框之前的屏幕，且下拉框中的值是选中后的值，相当于点击的效果分为两步，一步是选中，一步是点击
        #     driver.switch_to.context(contexts[1])                   #而select_by_value()方法只是选中，没有点击，所以需要再次点击一次屏幕
        #     time.sleep(1)                                             #该代码不能删，不然金额元素获取不到
        #     x = driver.find_elements_by_class_name('wrapper')  # 第一个默认金额的元素
        #     time.sleep(2)       #该段休眠也最好加上，不然也可能会出现运行速度过快，还未获取总的x元素后就再次点击的情况，导致IndexError的错误
        #     print len(x)        #该段代码不能删，不然会报IndexError异常，超出数列极限,且不能跟上面print len(x)换位置
        #     print i             #该原因待之后查询
        #     if i == 4:
        #         x[0].click()
        #     elif i == 5:
        #         x[1].click()
        #     elif i == 6:
        #         x[2].click()
        #     elif i == 7:
        #         x[3].click()
        #     else:
        #         x[i].click()
        #     driver.switch_to.context(contexts[0])
        #     self.slideUp()
        #     # driver.find_element_by_class_name('recharge').click()           #该代码会报‘不允许使用复合类名称’的错误，但实际看源码并不是复合类，该问题待之后查找
        #     # driver.switch_to.context(contexts[1])                           该方法能够获取到button的元素，并且也正常点击了，但是点击的效果显示是一个div框架，并没有真正点击到按钮
        #     # driver.find_element_by_xpath("//*[@id='postBtn' and @class='recharge']").click()      #因此没有正确跳转页面，这种情况和select_by_value()方法所显示的效果有差别,该情况与下拉框所出现的情况比较特殊，待之后有机会查找
        #     time.sleep(1)
        #     driver.tap([(243,523)])                                 #238,433;243,520这个按钮有毒，这种点击也能偶尔显示成一个div框架，没有真正点击跳转到下一个页面，已解决，以下捕获异常中的代码即解决方式
        #     time.sleep(2)
        #     if i == 0:
        #         self.screenShot('recharge4.png')   #充值流程的第一个页面截图
        #     elif i == 1:
        #         self.screenShot('recharge9.png')
        #     elif i == 2:
        #         self.screenShot('recharge14.png')
        #     elif i == 3:
        #         self.screenShot('recharge19.png')
        #     elif i == 4:
        #         self.screenShot('recharge40.png')
        #     elif i == 5:
        #         self.screenShot('recharge41.png')
        #     elif i ==6:
        #         self.screenShot('recharge42.png')
        #     elif i == 7:
        #         self.screenShot('recharge43.png')
        #     else:
        #         print '第一个页面截图时，出现程序异常，请注意'
        #
        #     try:
        #         driver.switch_to.context(contexts[1])
        #         x = driver.find_element_by_class_name('em-ico')       #元素不唯一，可以用复数定位，把所有的相同元素定位出来，按下标取第几个就行
        #         ActionChains(driver).click(x).perform()
        #     except NoSuchElementException:
        #         driver.switch_to.context(contexts[0])
        #         driver.tap([(415,355)])
        #         time.sleep(1)
        #         driver.tap([(238, 460)])
        #         print '异常捕获'
        #         time.sleep(2)
        #         if i == 0:
        #             self.screenShot('recharge4.png')  # 充值流程的第一个页面截图
        #         elif i == 1:
        #             self.screenShot('recharge9.png')
        #         elif i == 2:
        #             self.screenShot('recharge14.png')
        #         elif i == 3:
        #             self.screenShot('recharge19.png')
        #         elif i == 4:
        #             self.screenShot('recharge40.png')
        #         elif i == 5:
        #             self.screenShot('recharge41.png')
        #         elif i == 6:
        #             self.screenShot('recharge42.png')
        #         elif i == 7:
        #             self.screenShot('recharge43.png')
        #         else:
        #             print '第一个页面截图时，出现程序异常，请注意'
        #         driver.switch_to.context(contexts[1])
        #         x = driver.find_element_by_class_name('em-ico')  # 元素不唯一，可以用复数定位，把所有的相同元素定位出来，按下标取第几个就行
        #         ActionChains(driver).click(x).perform()
        #
        #     if i == 0 or i == 1 or i == 2 or i == 3:
        #         time.sleep(2)
        #         k = driver.find_element_by_class_name('lipa_payment_title')
        #         ActionChains(driver).click(k).perform()
        #         z = driver.find_element_by_id('lipaBtnBox')
        #         ActionChains(driver).click(z).perform()
        #         driver.switch_to.context(contexts[0])
        #         self.screenShot('recharge44.png')              #Kes国家充值的第二个页面
        #         driver.switch_to.context(contexts[1])
        #         driver.find_element_by_class_name('payment_half_btn').click()
        #         time.sleep(2)
        #         driver.switch_to.context(contexts[0])
        #         self.screenShot('recharge45.png')              # Kes国家充值的第三个页面
        #         driver.switch_to.context(contexts[1])
        #         n = driver.find_element_by_class_name('payment_result_btn')
        #         ActionChains(driver).click(n).perform()
        #         time.sleep(2)
        #         driver.switch_to.context(contexts[0])
        #         self.screenShot('recharge46.png')              # Kes国家充值的第四个页面
        #         driver.switch_to.context(contexts[1])
        #
        #     elif i == 4 or i == 5 or i == 6 or i == 7:
        #         time.sleep(2)
        #         f = driver.find_element_by_id('lipaPayKindTxt')           #该元素能够获取到但是会报‘element is not clickable’错误，即元素不能点击,以后出现该情况需要考虑用ActionsChains类中的click()方法来实现
        #         ActionChains(driver).click(f).perform()
        #         # b = driver.find_element_by_class_name('lipa_input_box')   #注意，该元素虽然可以被选中，但是不能被点击，会报'ElementNotVisibleException'异常，即元素不可点击
        #         b = driver.find_element_by_id('inputEmail')                #以上不能点击的问题通过ActionChains这个类来解决，该类基本满足所有对鼠标操作的需求
        #         ActionChains(driver).click(b).perform()
        #         b.clear()
        #         ActionChains(driver).send_keys('893026750@qq.com').perform()
        #         c = driver.find_element_by_id('lipaBtnBox')
        #         ActionChains(driver).click(c).perform()
        #         driver.switch_to.context(contexts[0])
        #         if i == 4:
        #             self.screenShot('recharge5.png')        #充值流程的第二个页面的截图
        #         elif i == 5:
        #             self.screenShot('recharge10.png')
        #         elif i == 6:
        #             self.screenShot('recharge15.png')
        #         elif i == 7:
        #             self.screenShot('recharge20.png')
        #         else:
        #             print '第二个页面截图时，出现程序异常，请注意'
        #         time.sleep(8)
        #
        #         driver.switch_to.context(contexts[1])
        #         driver.find_element_by_xpath("//*[@placeholder='0000 0000 0000 0000']").send_keys('4084084084084081')
        #         driver.find_element_by_xpath("//*[@placeholder='MM / YY']").send_keys('0120')
        #         driver.find_element_by_xpath("//*[@placeholder='123']").send_keys('408')
        #         driver.find_element_by_id('pay-btn').click()
        #         driver.switch_to.context(contexts[0])
        #         time.sleep(3)
        #         if i == 4:
        #             self.screenShot('recharge6.png')    #充值流程的第三个页面截图
        #         elif i == 5:
        #             self.screenShot('recharge11.png')
        #         elif i == 6:
        #             self.screenShot('recharge16.png')
        #         elif i == 7:
        #             self.screenShot('recharge21.png')
        #         else:
        #             print '第三个页面截图时，出现程序异常，请注意'
        #         time.sleep(3)
        #         if i == 4:
        #             self.screenShot('recharge7.png')    #充值流程的第四个页面，充值流程结束页面
        #         elif i == 5:
        #             self.screenShot('recharge12.png')
        #         elif i == 6:
        #             self.screenShot('recharge17.png')
        #         elif i == 7:
        #             self.screenShot('recharge22.png')
        #         else:
        #             print '第四个页面截图时，出现程序异常，请注意'
        #         driver.switch_to.context(contexts[1])
        #         h = driver.find_element_by_class_name('payment_continue_btn')
        #         ActionChains(driver).click(h).perform()
        #         driver.switch_to.context(contexts[0])
        #         # driver.find_element_by_css_selector('a')     #该异常是由于python selenium包的一个错误，可以通过降级版本来解决，将版本降级到Appium-Python-Client == 0.14和Selenium == 2.45.0
        #         # driver.find_element_by_tag_name('a')         #该定位方式以及by_css、by_link_text等方式时会报不支持该会话，错误的定位器策略异常
        #         time.sleep(2)
        #         if i == 4:
        #             self.screenShot('recharge8.png')          #充值完成后跳转回充值页面的截图，第五个截图
        #         elif i == 5:
        #             self.screenShot('recharge13.png')
        #         elif i == 6:
        #             self.screenShot('recharge18.png')
        #         elif i == 7:
        #             self.screenShot('recharge23.png')
        #         else:
        #             print '第五个页面截图时，出现程序异常，请注意'
        #
        #     else:
        #         print '循环出错，请核实'
        #
        # driver.switch_to.context(contexts[1])
        # time.sleep(3)
        # driver.find_element_by_class_name('records').click()
        # time.sleep(3)
        # driver.switch_to.context(contexts[0])
        # self.screenShot('recharge24.png')       #用户充值后查看充值记录
        #
        # driver.find_element_by_id('title_bar_iv_left').click()
        # driver.switch_to.context(contexts[1])
        # # y = driver.find_element_by_xpath("//*[@placeholder='point']")
        # y = driver.find_element_by_css_selector("[placeholder='point']")
        # y.send_keys('0')
        # driver.switch_to.context(contexts[0])
        # self.slideUp()
        # driver.tap([(238,500)])
        # time.sleep(2)
        # self.screenShot('recharge25.png')      #输入的金币数量为0
        #
        # driver.switch_to.context(contexts[1])
        # y.clear()
        # y.send_keys('9.9')
        # driver.switch_to.context(contexts[0])
        # driver.tap([(238,500)])
        # time.sleep(2)
        # self.screenShot('recharge26.png')      #输入的金币数量为小数
        #
        # driver.switch_to.context(contexts[1])
        # y.clear()
        # y.send_keys('9@qq')
        # driver.switch_to.context(contexts[0])
        # driver.tap([(238,500)])
        # time.sleep(2)
        # self.screenShot('recharge27.png')      #输入的金币数量为特殊字符
        #
        # driver.switch_to.context(contexts[1])
        # y.clear()
        # y.send_keys('9')
        # driver.switch_to.context(contexts[0])
        # driver.tap([(238,500)])
        # time.sleep(2)
        # self.screenShot('recharge28.png')      #输入的金币数量值小于10
        #
        # driver.switch_to.context(contexts[1])
        # current_window1 = driver.window_handles[0]
        # print current_window1                                                #充值流程第一个页面的窗口
        # y.clear()
        # y.send_keys('10')
        # driver.switch_to.context(contexts[0])
        # self.screenShot('recharge29.png')      #输入的金币数量值为10,未点击之前截图
        # driver.tap([(238,500)])
        # time.sleep(5)
        # self.screenShot('recharge30.png')      #输入的金币数量值为10，点击后截图
        #
        # driver.find_element_by_id('title_bar_iv_left').click()
        # driver.press_keycode(4)                                 #按手机上的返回键
        # driver.find_element_by_id('tv_recharge').click()
        # time.sleep(3)
        # driver.tap([(177,693)])
        # time.sleep(1)
        # driver.press_keycode(8)
        # time.sleep(1)                                           #注意这段休眠很重要，不然可能输入的结果只有1，而不是11.
        # driver.press_keycode(8)
        # self.slideUp()
        # self.screenShot('recharge31.png')  # 输入的金币数量值为11,未点击之前截图
        # driver.tap([(238, 500)])
        # time.sleep(3)
        # self.screenShot('recharge32.png')  # 输入的金币数量值为11，点击后截图
        #
        # driver.press_keycode(4)
        # driver.find_element_by_id('tv_recharge').click()
        # time.sleep(3)
        # driver.tap([(177,693)])
        # time.sleep(2)
        # driver.press_keycode(8)
        # driver.press_keycode(7)
        # driver.press_keycode(7)
        # driver.press_keycode(8)
        # self.slideUp()
        # self.screenShot('recharge33.png')  # 输入的金币数量值为1001,未点击之前截图
        # driver.tap([(238, 500)])
        # time.sleep(3)
        # self.screenShot('recharge34.png')  # 输入的金币数量值为1001，点击后截图
        #
        # driver.press_keycode(4)                                 #按手机上的返回键
        driver.find_element_by_id('tv_recharge').click()
        time.sleep(3)
        driver.tap([(177,693)])
        time.sleep(2)
        driver.press_keycode(9)
        time.sleep(2)
        driver.press_keycode(12)
        self.slideUp()
        self.screenShot('recharge35.png')  # 输入的金币数量值为25正常值,未点击之前截图
        time.sleep(3)
        driver.tap([(238, 500)])
        self.screenShot('recharge36.png')  # 输入的金币数量值为25正常值，点击后截图
        time.sleep(3)
        driver.tap([(414, 481)])
        time.sleep(2)
        driver.tap([(157, 483)])
        time.sleep(2)
        driver.tap([(255, 541)])
        time.sleep(2)
        driver.keyevent(123)             # 该方法将光标移到最后
        for i in range(0, 20):
            driver.keyevent(67)
        s1 = "adb shell input text '893026750'"
        s2 = "adb shell input keyevent KEYCODE_AT"
        s3 = "adb shell input text 'qq.com'"
        os.system(s1)
        os.system(s2)
        os.system(s3)
        driver.tap([(231,641)])
        time.sleep(15)
        self.screenShot('recharge37.png')
        driver.tap([(157,368)])
        s4 = "adb shell input text '4084084084084081'"
        os.system(s4)
        time.sleep(3)
        driver.tap([(112,468)])
        s5 = "adb shell input text '0120'"
        os.system(s5)
        driver.tap([(325,463)])
        s6 = "adb shell input text '408'"
        os.system(s6)
        driver.tap([(229,558)])
        time.sleep(8)
        self.screenShot('recharge38.png')
        driver.tap([(235,440)])
        time.sleep(2)
        self.screenShot('recharge39.png')

        driver.press_keycode(4)
        driver.find_element_by_id('title_bar_iv_left').click()
        driver.find_element_by_id('tv_feedback').click()
        time.sleep(2)
        self.screenShot('recharge47.png')                  #用户充值后系统app内发送消息到notification中的截图
        driver.open_notifications()
        self.screenShot('recharge48.png')                  #打开系统通知栏，用户充值后无个推消息推送的截图
        self.slideUp()
        mn = driver.find_elements_by_android_uiautomator('new UiSelector().text("click here >")')
        mn[len(mn)-1].click()
        time.sleep(1)
        self.screenShot('recharge49.png')                  #app发送的消息点击跳转到myCoins页面的截图
        driver.find_element_by_id('tv_myCoin').click()
        time.sleep(1)
        self.screenShot('recharge50.png')                  #充值的金额在myCoins的金币记录页面显示的截图
        driver.find_element_by_id('title_bar_iv_left').click()
        driver.find_element_by_id('title_bar_iv_left').click()
        print '充值功能测试完成'

        #adb shell命令，待之后可用
        # package_name = "adb shell pm list package"
        # terminal_back = os.popen(package_name)  # 查询出android设备中已经安装的所有应用包名（包括系统应用和用户应用），并获得返回值（返回值是一个文件对象，格式为fd）
        # terminal_result = str(terminal_back.read())  # 读取所返回的文件对象内容，并转换为string类型
        # print terminal_result
        # f_result = terminal_result.find("com.football.supergoal")  # find函数找不到时返回-1，找到了则返回查找到字符串的第一个出现的位置
        # print f_result
        # os.system("adb shell am force-stop com.football.supergoal")    #杀掉该进程，再启动APP

        #以下代码待之后解决，这个noSuchWindowException异常需研究怎么解决
        # all_windows = driver.window_handles
        # current_window2 = all_windows[0]
        # print current_window2
        # for i in all_windows:
        #     if current_window2 != i:
        #         print 'y'
        #         driver.switch_to.window(current_window2)          该行代码执行时会报没有这个窗口的异常，研究从这里开始
        #         print 'y'
        #         y.send_keys('11')
        #         print 'y'
        #     else:
        #         driver = driver.switch_to.window(current_window2)
        # y.send_keys('11')
        # print 'y'
        # driver.switch_to.context(contexts[0])
        # self.slideUp()
        # self.screenShot('recharge31.png')  # 输入的金币数量值为11,未点击之前截图
        # driver.tap([(235, 408)])
        # time.sleep(3)
        # self.screenShot('recharge32.png')  # 输入的金币数量值为11，点击后截图
        #
        # driver.find_element_by_id('title_bar_iv_left').click()
        # driver.find_element_by_id('tv_recharge').click()
        # driver.switch_to.context(contexts[1])
        # y.send_keys('1001')
        # driver.switch_to.context(contexts[0])
        # self.slideUp()
        # self.screenShot('recharge33.png')  # 输入的金币数量值为1001,未点击之前截图
        # driver.tap([(235, 408)])
        # time.sleep(3)
        # self.screenShot('recharge34.png')  # 输入的金币数量值为1001，点击后截图

    #竞猜功能
    def test_prediction(self):
        driver = self.driver
        # uid = self.test_feedback()
        m1 = driver.find_element_by_id("title_bar_iv_left")
        m1.click()
        time.sleep(2)
        driver.tap([(352, 320)])
        time.sleep(1)
        s2 = driver.find_element_by_id('rb_prediction')
        s2.click()
        time.sleep(1)
        s3 = driver.find_element_by_id('tv_prediction_records')
        s3.click()
        time.sleep(1)
        self.screenShot('prediction1.png')
        m1.click()

        conn, cur = connDB()
        b = select_match_prediction(
            cur)        # 数据库返回的数据,注意接口返回的数据中，是要求比赛状态处于2即未开始状态，在之后的操作中会有改变比赛状态的操作，所以中途调试时需要手动改第一条EPL比赛的状态为2
        a = match_prediction()                                                                              # 接口返回的数据
        print b[0]
        if a.sort() == b.sort():                                                                            # sort是将数列排序
            print '数据库返回与接口返回数据相同，正确'
        else:
            print '注意！数据不相同，请核对'
        b = select_match_prediction(cur)
        sql1 = "SELECT * FROM `match` WHERE match_id = '%d' " % (b[0])
        cur.execute(sql1)
        cur.fetchall()

        v1 = 1
        while v1:
            try:
                self.getElementUI("EPL")
                v1 = 0
            except NoSuchElementException:
                self.slideUp1()
                v1 = 1

        # try:
        #     self.getElementUI("EPL")
        # except NoSuchElementException:
        #     self.slideUp1()                         # 注意，可能出现上拉的时候，第一个EPL比赛正好元素被覆盖了一半，就会点击到第二个比赛，之后如果有问题可通过改变上滑的距离来解决
        #     try:
        #         self.getElementUI("EPL")
        #     except NoSuchElementException:
        #         self.slideUp1()
        #         try:
        #             self.getElementUI("EPL")
        #         except NoSuchElementException:
        #             print '后台手动添加的比赛有点多，需要多几次上拉刷新操作，请核实'
        # else:
        #     print '发生非NosuchElement异常，请注意！'

        time.sleep(2)
        self.screenShot('prediction2.png')                                                           # prediction页面截图
        self.getElementUI("Overview")
        time.sleep(1)
        self.screenShot('prediction3.png')                                                           # overview页面截图
        self.getElementUI("Line-up")
        time.sleep(3)
        self.screenShot('prediction4.png')                                                           # Line-up页面截图
        self.getElementUI("Highlights")
        time.sleep(1)
        self.screenShot('prediction5.png')                                                           # Highlights页面
        self.getElementUI("Prediction")
        self.getElementUI("Live")
        time.sleep(1)
        self.screenShot('prediction6.png')                                                           # Live页面截图
        m1.click()

        # driver.set_network_connection(ConnectionType.NO_CONNECTION)                                  #该方法突然无效，原因暂时未知
        driver.set_network_connection(ConnectionType.AIRPLANE_MODE)                                  # 设置网络为飞行模式
        self.getElementUI("EPL")
        time.sleep(2)
        self.screenShot('prediction7.png')                                                           # 无网络时prediction页面截图
        self.getElementUI("Overview")
        time.sleep(1)
        self.screenShot('prediction8.png')                                                           # 无网络时overview页面截图
        self.getElementUI("Line-up")
        time.sleep(3)
        self.screenShot('prediction9.png')                                                           # 无网络时Line-up页面截图
        self.getElementUI("Highlights")
        time.sleep(1)
        self.screenShot('prediction10.png')                                                          # 无网络时Highlights页面
        self.getElementUI("Prediction")
        self.getElementUI("Live")
        time.sleep(1)
        self.screenShot('prediction11.png')                                                          # 无网络时Live页面截图
        driver.find_element_by_id("title_bar_iv_left").click()
        driver.set_network_connection(ConnectionType.WIFI_ONLY)                 # 0是未设置网络类型，1是飞行模式，2是仅打开wifi，4是仅打开数据流量，6是wifi和数据流量都打开

        sql2 = "update match_prediction set status = 3 WHERE id = '%d' " % (b[0])
        sql3 = "update `match` set status = 1 WHERE match_id = '%d' " % (b[0])
        cur.execute(sql2)
        cur.execute(sql3)
        conn.commit()
        self.getElementUI("EPL")
        time.sleep(2)
        self.screenShot('prediction12.png')                                                          # 竞猜关闭时prediction页面截图
        self.getElementUI("Overview")
        time.sleep(1)
        self.screenShot('prediction13.png')                                                          # 比赛直播状态但没有数据时overview页面截图
        self.getElementUI("Line-up")
        time.sleep(3)
        self.screenShot('prediction14.png')                                                          # 比赛直播状态但没数据时Line-up页面截图
        self.getElementUI("Highlights")
        time.sleep(1)
        self.screenShot('prediction15.png')                                                          # 比赛直播状态但没数据时Highlights页面
        self.getElementUI("Prediction")
        self.getElementUI("Live")
        time.sleep(1)
        self.screenShot('prediction16.png')                                                          # 比赛直播状态但没数据时Live页面截图
        m1 = driver.find_element_by_id("title_bar_iv_left")
        m1.click()
        self.screenShot('prediction29.png')                                                          # 比赛直播状态竞猜关闭状态时prediction页面显示

        print b[0]
        sql4 = "update match_person set match_id = '%d' WHERE  id = 1" % (b[0])
        cur.execute(sql4)
        conn.commit()
        self.getElementUI("EPL")
        self.getElementUI("Line-up")
        time.sleep(3)
        self.screenShot('prediction17.png')                                                          # 比赛直播状态且有数据时Line-up页面截图
        m1.click()
        sql5 = "update match_person set match_id = '%d' WHERE  id = 2" % (b[0])
        cur.execute(sql5)
        conn.commit()
        self.getElementUI("EPL")
        self.getElementUI("Line-up")
        time.sleep(3)
        self.screenShot('prediction18.png')                                                          # 比赛直播状态且再增加一条数据时Line-up页面截图
        driver.find_element_by_id("title_bar_iv_left").click()

        sql6 = "update match_event set match_id = '%d' WHERE id = 1" % (b[0])
        cur.execute(sql6)
        conn.commit()
        self.getElementUI("EPL")
        self.getElementUI("Overview")
        time.sleep(1)
        self.screenShot('prediction19.png')                                                          # 比赛直播状态且有数据时Overview页面截图
        driver.find_element_by_id("title_bar_iv_left").click()
        sql7 = "update match_event set match_id = '%d' WHERE id = 2" % (b[0])
        cur.execute(sql7)
        conn.commit()
        self.getElementUI("EPL")
        self.getElementUI("Overview")
        time.sleep(1)
        self.screenShot('prediction20.png')                                                          # 比赛直播状态且再增加一条数据时Overview页面截图
        driver.find_element_by_id("title_bar_iv_left").click()
        sql8 = "update match_stat set match_id = '%d' WHERE id = 1" % (b[0])
        cur.execute(sql8)
        conn.commit()
        self.getElementUI("EPL")
        self.getElementUI("Overview")
        self.slideUp()
        time.sleep(2)
        self.screenShot('prediction21.png')                                                          # 比赛直播状态且有数据时statistics页面（现合并在overview页面中）截图
        driver.find_element_by_id("title_bar_iv_left").click()
        sql9 = "update match_stat set match_id = '%d' WHERE id = 2" % (b[0])
        cur.execute(sql9)
        conn.commit()
        self.getElementUI("EPL")
        self.getElementUI("Overview")
        self.slideUp()
        time.sleep(2)
        self.screenShot('prediction22.png')                                                          # 比赛直播状态且再增加一条数据时statistics页面截图
        m1.click()

        sql10 = "update video set match_id = '%d' WHERE id = 5200" % (b[0])
        cur.execute(sql10)
        conn.commit()
        self.getElementUI("EPL")
        self.getElementUI("Highlights")
        time.sleep(1)
        self.screenShot('prediction23.png')                                                         # 比赛直播状态且有highlights数据时highlights页面截图
        driver.find_element_by_xpath("//*[@class='android.widget.LinearLayout' and @index='0']").click()
        time.sleep(2)
        self.screenShot('prediction24.png')                                                         # highlights视频点击后跳转到的页面截图
        driver.find_element_by_id('tv_cancel').click()
        driver.find_element_by_id('iv_play').click()
        time.sleep(2)
        self.screenShot('prediction25.png')                                                         # highlights视频点击播放的页面截图
        m1.click()
        driver.find_element_by_id('iv_back').click()
        m1.click()

        sql11 = "update video set match_id = '%d' WHERE id = 5201" % (b[0])
        cur.execute(sql11)
        conn.commit()
        self.getElementUI("EPL")
        self.getElementUI("Highlights")
        time.sleep(1)
        self.screenShot('prediction26.png')                                                         # 比赛直播状态且再增加highlights数据时highlights页面截图
        self.slideUp()
        driver.find_element_by_xpath("//*[@class='android.widget.LinearLayout' and @index='1']").click()
        time.sleep(2)
        self.screenShot('prediction27.png')                                                         # 新增的highlights视频点击后跳转到的页面截图
        driver.find_element_by_id('iv_play').click()
        time.sleep(2)
        self.screenShot('prediction28.png')                                                         # 新增的highlights视频点击播放的页面截图
        driver.find_element_by_id("title_bar_iv_left").click()
        driver.find_element_by_id('iv_back').click()
        driver.find_element_by_id("title_bar_iv_left").click()

        sql12 = "update match_phrase set match_id = '%d' WHERE id = 1" % (b[0])
        cur.execute(sql12)
        conn.commit()
        self.getElementUI("EPL")
        self.getElementUI("Live")
        time.sleep(2)
        self.screenShot('prediction30.png')                                                         # 比赛直播状态且有live数据时的Live页面截图
        sql13 = "update match_phrase set match_id = '%d' WHERE id = 2" % (b[0])
        sql14 = "update match_phrase set match_id = '%d' WHERE id = 3" % (b[0])
        sql15 = "update match_phrase set match_id = '%d' WHERE id = 4" % (b[0])
        cur.execute(sql13)
        cur.execute(sql14)
        cur.execute(sql15)
        conn.commit()
        time.sleep(30)                                                                              # Live页面是每20s请求一次接口数据
        self.screenShot('prediction31.png')                                                         # 比赛直播状态且新增live数据时的Live页面截图
        m1.click()

        sql16 = "update match_phrase set match_id = 50834870 WHERE id = 1"
        sql17 = "update match_phrase set match_id = 50834870 WHERE id = 2"
        sql18 = "update match_phrase set match_id = 50834870 WHERE id = 3"
        sql19 = "update match_phrase set match_id = 50834870 WHERE id = 4"
        sql20 = "update `match` set status = 0 WHERE match_id = '%d' " % (b[0])
        cur.execute(sql16)
        cur.execute(sql17)
        cur.execute(sql18)
        cur.execute(sql19)
        cur.execute(sql20)
        conn.commit()
        self.slideDown()
        time.sleep(2)
        self.screenShot('prediction32.png')                                                         # 该比赛结束后在tab_prediction页面的截图
        driver.find_element_by_id('rb_match').click()
        time.sleep(1)
        # driver.find_element_by_android_uiautomator('new UiSelector().text("EPL R15")').click()      #该text内容需要变化，之后查看怎么修改
        self.getElementUI("0 - 0")                                                                    # 该text内容需要变化，之后查看怎么修改
        time.sleep(1)
        self.screenShot('prediction33.png')                                                           # 比赛结束状态且无live数据时的Live页面截图
        self.getElementUI("Prediction")
        time.sleep(1)
        self.screenShot('prediction34.png')                                                           # 比赛结束状态时的prediction页面截图
        driver.find_element_by_id("title_bar_iv_left").click()

        sql21 = "update match_person set match_id = 50834870 WHERE  id = 1"
        sql22 = "update match_person set match_id = 50834870 WHERE  id = 2"
        sql23 = "update match_event set match_id = 50834870 WHERE  id = 1"
        sql24 = "update match_event set match_id = 50834870 WHERE  id = 2"
        sql25 = "update match_stat set match_id = 50834870 WHERE id = 1"
        sql26 = "update match_stat set match_id = 50834870 WHERE id = 2"
        sql27 = "update video set match_id = 0 WHERE id = 5200"
        sql28 = "update video set match_id = 0 WHERE id = 5201"
        cur.execute(sql21)
        cur.execute(sql22)
        cur.execute(sql23)
        cur.execute(sql24)
        cur.execute(sql25)
        cur.execute(sql26)
        cur.execute(sql27)
        cur.execute(sql28)
        conn.commit()
        self.getElementUI("EPL R13")
        self.getElementUI("Overview")
        time.sleep(1)
        self.screenShot('prediction35.png')                                                         # 比赛结束状态且无overview数据时的overview页面截图
        self.getElementUI("Line-up")
        time.sleep(3)
        self.screenShot('prediction36.png')                                                         # 比赛结束状态且无line-up数据时的Line-up页面截图
        self.getElementUI("Highlights")
        time.sleep(1)
        self.screenShot('prediction37.png')                                                         # 比赛结束状态且无highlights数据时的Highlights页面截图
        m1.click()
        sql29 = "update `match` set status = 2 WHERE match_id = '%d' " % (b[0])
        sql30 = "update match_prediction set status = 2 WHERE id = '%d' " % (b[0])
        cur.execute(sql29)
        cur.execute(sql30)
        conn.commit()

        s2.click()
        self.getElementUI("EPL")
        self.getElementUI("50")
        time.sleep(1)
        self.screenShot('prediction38.png')                                                         # 未选择预测结果直接点击下注金额按钮后的页面效果截图
        self.getElementUI("100")                                                                    # 系统提示未截取到，该问题之后解决
        time.sleep(1)
        self.screenShot('prediction39.png')
        self.getElementUI("200")
        time.sleep(1)
        self.screenShot('prediction40.png')
        driver.find_element_by_id('et_bet_coins').send_keys('100')
        s10 = driver.find_element_by_id('btn_bet')
        s10.click()
        self.screenShot('prediction41.png')                                                         # 输入金额后点击提交按钮后的页面截图

        driver.find_element_by_id('tv_win_a').click()
        d = driver.find_element_by_id('et_bet_coins')
        d.clear()
        d.send_keys('2.@#$%&*+-qsd')
        self.screenShot('prediction41.png')                                                         # 输入金额为特殊字符的页面截图
        d.clear()
        d.send_keys('0')
        s10.click()
        self.screenShot('prediction42.png')                                                         # 输入金额为0并点击提交按钮后的页面截图
        d.clear()
        d.send_keys('10000000')
        s10.click()
        self.screenShot('prediction43.png')                                                         # 输入金额特别大并点击提交按钮后的页面截图
        s11 = driver.find_element_by_id('btn_right')
        s11.click()
        time.sleep(1)
        self.screenShot('prediction44.png')                                                         # 点击getCoins按钮后跳转到页面截图
        driver.find_element_by_id("title_bar_iv_left").click()

        sql31 = "SELECT * FROM user_point WHERE uid = '%d' " % (241)
        cur.execute(sql31)
        result2 = cur.fetchall()
        userGolds = result2[0][2]
        d.clear()
        d.send_keys(userGolds + 1)
        s10.click()
        self.screenShot('prediction45.png')                                                         # 输入用户金币数+1的数量，点击提交按钮后的截图
        s12 = driver.find_element_by_id('btn_left')
        s12.click()

        d.clear()
        d.send_keys('20')
        s10.click()
        s11.click()
        s11.click()
        time.sleep(1)
        self.screenShot('prediction46.png')                                                         # 正常竞猜后跳转到竞猜记录后的页面截图

        driver.find_element_by_id("title_bar_iv_left").click()
        self.screenShot('prediction47.png')                                                         # 返回竞猜页面后查看页面内容是否被清空的页面截图
        self.getElementUI("50")
        s10.click()
        self.screenShot('prediction48.png')                                                         # 返回竞猜页面后确认是否能够继续竞猜的页面截图（未选择预测结果）

        # e = driver.find_element_by_android_uiautomator('new UiSelector().text("No")')             #注意！！is_enable()必须要通过text来判断，即class_name方式来获取元素，才能使用该方法
        print s12.is_displayed()                                                                    # is_displayed()方法不能通过class_name方式获取元素，需要通过id来获取元素，才能使用该方法
        if s12.is_displayed() == True:
            s12.click()
            d.click()
        else:
            d.click()
        d.send_keys(userGolds)
        s10.click()
        time.sleep(1)
        self.screenShot('prediction49.png')                                                         # 输入金额为用户所拥有的金额数量，点击提交按钮后的页面截图
        s12.click()

        driver.find_element_by_id("title_bar_iv_left").click()
        driver.find_element_by_id("title_bar_iv_left").click()
        driver.find_element_by_id('tv_feedback').click()
        self.screenShot('prediction49.png')                                                         # 用户竞猜20金币后，系统在APP内发送消息的页面截图

        f = driver.find_elements_by_android_uiautomator('new UiSelector().text("click here >")')
        f[len(f) - 1].click()
        time.sleep(2)
        self.screenShot('prediction50.png')                                                         # APP发送的消息点击跳转到竞猜记录页面的截图
        driver.open_notifications()                                                                 # 打开手机的下拉菜单
        time.sleep(2)
        self.screenShot('prediction51.png')                                                         # 系统通知栏截图，查看是否有个推消息发送，预期是没有
        self.slideUp()
        m1.click()
        m1.click()
        driver.find_element_by_id('tv_myCoin').click()
        driver.find_element_by_id('tv_myCoin').click()
        time.sleep(1)
        self.screenShot('prediction52.png')                                                         # 用户竞猜20金币后在myCoins页面显示的金币记录截图
        driver.find_element_by_id("title_bar_iv_left").click()
        driver.find_element_by_id("title_bar_iv_left").click()
        driver.tap([(352, 320)])
        s2.click()
        try:
            s3.click()
        except NoSuchElementException:
            self.slideDown()
            try:
                s3.click()
            except NoSuchElementException:
                self.slideDown()
                s3.click()
            else:
                print '后台手动添加的比赛有点多，需要多几次下拉刷新操作，请核实'
        time.sleep(2)
        self.screenShot('prediction53.png')                                                         # 用户竞猜20金币后，从prediction records按钮进入竞猜页面的截图
        driver.find_element_by_xpath("//*[@index='0' and @class='android.widget.LinearLayout']").click()
        time.sleep(2)
        self.screenShot('prediction54.png')                                                         # 竞猜记录能够点击跳转到相应的竞猜页面截图
        m1.click()
        m1.click()

        try:
            self.getElementUI("EPL")
        except NoSuchElementException:
            self.slideUp()
            try:
                self.getElementUI("EPL")
            except NoSuchElementException:
                self.slideUp()
                self.getElementUI("EPL")
            else:
                print '后台手动添加的比赛有点多，需要多几次上拉刷新操作，请核实'
        d = driver.find_element_by_id('et_bet_coins')
        driver.find_element_by_id('tv_win_a').click()
        d.clear()
        d.send_keys('120')
        s10.click()
        s11.click()
        s12.click()
        self.screenShot('prediction55.png')                                                     # 用户下注金额后每种竞猜的赔率变化、查看是否增加了真实的下注金额和次数截图
        driver.find_element_by_id('tv_draw').click()
        d.send_keys('250')
        s10.click()
        s11.click()
        s12.click()
        driver.find_element_by_id('tv_win_b').click()
        d.send_keys('180')
        s10.click()
        s11.click()
        s12.click()
        self.screenShot('prediction56.png')             # 用户下注金额后每种竞猜的赔率变化以及虚拟金币数量和下注次数是否增加截图，注意查看用户拥有的金币数量是否减少了下注金币数

        sql32 = "select * from match_prediction WHERE id = '%d' " % (b[0])
        cur.execute(sql32)
        result3 = cur.fetchall()
        winAmount = result3[0][1]
        tieAmount = result3[0][2]
        lossAmount = result3[0][3]
        allAmount = winAmount + tieAmount + lossAmount
        winOdds = allAmount * 0.8 / winAmount
        tieOdds = allAmount * 0.8 / tieAmount
        lossOdds = allAmount * 0.8 / lossAmount
        print '主队胜的赔率是：' + str(winOdds) + '    两队平的赔率是：' + str(tieOdds) + '    客队赢的赔率是：' + str(lossOdds)
        print '请注意核对赔率是否与界面显示相同！'
        #
        sql33 = "update `match` set status = 0,fs_a = 2,fs_b = 1 WHERE match_id = '%d' " % (b[0])
        cur.execute(sql33)
        conn.commit()
        # t = threading.Thread(target=self.t2())                  #新建一个子线程，每隔10秒运行一次t2函数，查看竞猜记录是否已结束竞猜;但是该方法会在运行之后的代码时，抛出异常TypeError
        # t.start()
        sched = BlockingScheduler()      # 该方式效果与上面相同，不同的是不会抛出异常，该方式是通过APScheduler这个定时任务框架来实现的，在运行完后可以关闭调度器，而不会杀掉进程
        if self.t2() == 1:
            try:
                sched.shutdown(wait=False)  # 关闭调度器
            except SchedulerNotRunningError:
                print '调度任务已结束'
        else:
            sched.add_job(self.t2(), 'interval')                                                # 新增作业，job管理是APScheduler的核心
            sched.start()
        try:
            driver.open_notifications()
        except KeyError:
            print 'app被莫名退出'                                                                # 该退出原因可能是app的bug，更有可能是运行环境导致的问题，待研究
            s1 = "adb shell am force-stop com.football.supergoal"  # 该杀掉进程重新启动APP的方法有效性待实际验证
            os.system(s1)
            start_p = 'com.football.supergoal'
            start_a = 'com.soka.football.home.ui.login.activity.SplashActivity'
            driver.start_activity(start_p, start_a)
            time.sleep(2)
            s2.click()
            driver.open_notifications()
        time.sleep(2)
        self.screenShot('prediction57.png')                                                     # 系统通知栏截图，竞猜比赛结束后发送个推消息，可点击
        self.getElementUI("Prediction result")
        time.sleep(2)
        self.screenShot('prediction58.png')                                                     # 竞猜结果个推消息点击跳转到竞猜记录页面的截图
        driver.find_element_by_id("title_bar_iv_left").click()
        try:
            s3.click()                                                                          # 利用子线程的方法不能点击该按钮，原因未知
        except NoSuchElementException:
            self.slideDown()
            try:
                s3.click()
            except NoSuchElementException:
                self.slideDown()
                s3.click()
            else:
                print '后台手动添加的比赛有点多，需要多几次下拉刷新操作，请核实'
        time.sleep(1)
        self.screenShot('prediction59.png')                                                     # 竞猜结束后竞猜记录截图，注意核对相关信息
        driver.find_element_by_id("title_bar_iv_left").click()
        driver.find_element_by_id("title_bar_iv_left").click()
        driver.find_element_by_id('tv_myCoin').click()
        time.sleep(1)
        driver.find_element_by_id('tv_myCoin').click()
        time.sleep(1)
        self.screenShot('prediction60.png')             # 竞猜结束后金币变化数量截图，特别注意竞猜赢了是否有金币增加的记录，上面已有竞猜后金币减少的截图，所以这里注意另外赢得情况

        sql34 = "update `match` set status = 2,fs_a = 0,fs_b = 0 WHERE match_id = '%d' " % (b[0])
        sql35 = "update match_prediction set status = 2 WHERE id = '%d' " % (b[0])
        cur.execute(sql34)
        cur.execute(sql35)
        conn.commit()
        print '竞猜测试结束'

    #系统推送功能
    def test_push(self):
        driver = self.driver
        conn,cur = connDB()
        s1 = driver.find_element_by_id('title_bar_iv_left')
        s1.click()
        s3 = driver.find_element_by_id('tv_redeem')
        s3.click()
        s3.click()
        sql7 = 'select point from user_point where uid = 241'
        sql8 = 'update user_point set point = 10000 where uid = 241'
        cur.execute(sql7)
        c = cur.fetchall()
        if c[0][0] < 3000 :
            cur.execute(sql8)
            conn.commit()

        driver.find_element_by_id('et_tel').send_keys('13575789124')
        s3.click()
        time.sleep(1)
        self.screenShot('push1.png')                                                        #用户兑换礼物成功后的系统提示截图
        driver.find_element_by_id('tv_ok').click()
        s1.click()
        driver.open_notifications()
        time.sleep(1)
        self.screenShot('push2.png')                                                        #用户兑换礼物成功后无个推消息，打开通知栏查看的截图
        self.slideUp()
        driver.find_element_by_id('tv_feedback').click()
        time.sleep(1)
        self.screenShot('push3.png')                                                        #用户兑换礼物成功后app内发送消息到notification中的截图，且不能点击
        s1.click()
        driver.find_element_by_id('tv_myCoin').click()
        driver.find_element_by_id('tv_myCoin').click()
        time.sleep(1)
        self.screenShot('push4.png')                                                        #用户兑换礼物成功金币变化在myCoins的记录页面
        s1.click()
        s1.click()

        sql3 = "select team_id from user_team_subscription where uid = 241"                 #检查用户是否订阅了进行测试的比赛其中一支球队
        cur.execute(sql3)
        result1 = cur.fetchall()
        c = []
        for i in range(len(result1)):
            c.append(result1[i][0])
        if 674 in c or 696 in c:
            print '该用户已关注其中一支球队'
        else:
            driver.find_element_by_id('tv_subscribed').click()
            driver.find_element_by_id('title_bar_tv_right').click()
            time.sleep(1)
            self.getElementUI("Everton")                                                 #注意！该方式抓取元素时，外面用单引号，里面用双引号，不然可能会报错，原因待查询
            driver.find_element_by_id('title_bar_tv_right').click()
            s1.click()

        driver.tap([(352,320)])
        now1 = datetime.datetime.now()
        setTime1 = now1 + datetime.timedelta(minutes=8) - datetime.timedelta(hours=8)               #用户订阅的比赛开始前5分钟的个推消息
        sql1 = "update `match` set status=2,fs_a=0,fs_b=0,start_play='%s' WHERE match_id = '50762648' "% (setTime1)
        sql5 = "delete from match_phrase_push where match_id = '50762648' "
        sql6 = "delete from match_subscribe_push_history where match_id = '50762648' "
        cur.execute(sql1)
        cur.execute(sql5)
        cur.execute(sql6)
        print '该比赛推送表已删除相关数据'
        conn.commit()

        driver.find_element_by_id('rb_live').click()
        self.screenShot('push9.png')                                            #比赛开始前5分钟在Live页面显示的截图,主要查看是否比赛显示是否倒计时，以及相关比赛信息是否正确
        a1 = 0
        while a1 == 0:
            driver.open_notifications()
            try:
                b = driver.find_element_by_android_uiautomator(
                    'new UiSelector().text("The match Everton VS Watford is about to start.Click to watch it now.")')
                self.screenShot('push5.png')                                    # 用户订阅的比赛开始前5分钟的个推消息在通知栏中的截图
                b.click()
                time.sleep(1)
                self.screenShot('push6.png')                                    # 用户订阅的比赛开始前5分钟的个推消息点击后跳转到Live页面的截图
                a1 = 1
            except NoSuchElementException:
                self.slideUp()
                time.sleep(5)
                a1 = 0
        else:
            print '比赛开始前5分钟的个推消息已收到'

        # try:
        #     sched = BlockingScheduler()                                                       #这种异常突然出现，之后再修改
        #     if self.t3() == 1:
        #         try:
        #             sched.shutdown(wait=False)                                                # 关闭调度器
        #         except SchedulerNotRunningError:
        #             print '调度任务已结束'
        #     else:
        #         sched.add_job(self.t3(), 'interval', seconds = 2)                             # 新增作业，job管理是APScheduler的核心
        #         sched.start()
        # except TypeError:
        #     print 'no'
        #     sched = BlockingScheduler()
        #     if self.t3() == 1:
        #         try:
        #             sched.shutdown(wait=False)  # 关闭调度器
        #         except SchedulerNotRunningError:
        #             print '调度任务已结束'
        #     else:
        #         sched.add_job(self.t3(), 'interval', seconds=2)                               # 新增作业，job管理是APScheduler的核心
        #         sched.start()

        s1.click()
        self.screenShot('push10.png')                                               #个推消息点击返回后，查看在live页面比赛的倒计时时间显示是否变化，主要验证该功能是否有效


        now2 = datetime.datetime.now() - datetime.timedelta(hours=8)                                #用户订阅的比赛开始时发送的个推消息
        sql2 = "update `match` set start_play='%s',status=1 WHERE match_id = '50762648' "% (now2)
        cur.execute(sql2)
        conn.commit()

        a2 = 0
        while a2 == 0:
            driver.open_notifications()
            try:
                b = driver.find_element_by_android_uiautomator(
                    'new UiSelector().text("The match Everton VS Watford has started.Click here to watch live text.")')
                self.screenShot('push7.png')                                                  # 用户订阅的比赛开始时的个推消息在通知栏中的截图
                b.click()
                time.sleep(1)
                self.screenShot('push8.png')                                                  # 用户订阅的比赛开始时个推消息点击后跳转到Live页面的截图
                a2 = 1
            except NoSuchElementException:
                self.slideUp()
                time.sleep(5)
                a2 = 0
        else:
            print '比赛开始时的个推消息已收到'

        s1.click()
        self.screenShot('push11.png')                                                        #比赛开始时，查看Live页面比赛的滚动直播显示提示语是否是系统提示语的截图
        self.getElementUI("Everton")
        time.sleep(2)
        self.screenShot('push12.png')                                                        #比赛开始时，查看直播比赛详情页面中的是否有显示系统的提示语截图
        s1.click()

        match_push_phrase()                                                                 #进球推送的接口调用
        a3 = 0
        while a3 == 0:
            driver.open_notifications()
            try:
                b = driver.find_element_by_android_uiautomator(
                    'new UiSelector().text("Everton vs Watford :check it now")')
                self.screenShot('push13.png')                                               # 用户订阅的比赛进球后的个推消息在通知栏中的截图
                b.click()
                time.sleep(1)
                self.screenShot('push14.png')                                               # 用户订阅的比赛进球后的个推消息点击后跳转到Live页面的截图
                a3 = 1
            except NoSuchElementException:
                self.slideUp()
                time.sleep(5)
                a3 = 0
        else:
            print '用户订阅的比赛进球时发送的个推消息已收到'

        s1.click()

        sql4 = "update `match` set status = 0,fs_a = 0,fs_b = 0,start_play = '2017-11-20 01:30:00' WHERE match_id = '50762648' "
        cur.execute(sql4)                                                                   #个推测试完毕后将该比赛已更改的信息还原
        conn.commit()
        print '个推消息推送测试完毕'

    #直播页面
    def test_live(self):
        driver = self.driver                                                    #live页面比赛倒计时的时间是根据接口返回的时间减去手机系统设置的时间来显示的
        conn,cur = connDB()
        a = select_live_match(cur)                                              #数据库返回的live页面数据
        b = match_live()                                                        #Live页面的match/live/available接口请求的数据
        if a.sort() == b.sort():
            print 'Live页面数据核对完成且正确'
        else:
            print '请注意！数据库与接口返回的数据不同，请核实'
        b = match_live()

        driver.find_element_by_id('rb_live').click()
        if len(b) <= 3:
            time.sleep(2)
            self.screenShot('live1.png')
        elif 3 < len(b) <= 6:
            time.sleep(2)
            self.screenShot('live1.png')                                        #live页面直播比赛的android端截图，查看该页面中显示的比赛数量是否与数据库或接口相同
            self.slideUp()
            time.sleep(1)
            self.screenShot('live2.png')
        elif 6 < len(b) <= 9:
            time.sleep(2)
            self.screenShot('live1.png')
            self.slideUp()
            time.sleep(1)
            self.screenShot('live2.png')
            self.slideUp()
            time.sleep(1)
            self.screenShot('live3.png')
        elif len(b) > 9:
            print '直播比赛超过9场，请手动查看'
        else:
            print '出现异常，请注意！'

        print b[0]
        sql1 = "select * from `match` WHERE match_id = '%d' "% (b[0])
        cur.execute(sql1)
        result1 = cur.fetchall()
        print 'Live页面显示的第一场比赛的信息如下，请核对相关信息:'
        # print result1
        print '比赛ID：' + str(result1[0][1]) + '   主队队名：' + str(result1[0][3]) + '   客队队名：' + str(result1[0][6]) + '   联盟名称：' + str(result1[0][9]) + '   比赛时间:' + str(result1[0][20])
        if len(b) <= 3:
            driver.find_element_by_id('tv_leg_name').click()
        elif 3 < len(b) <= 6:
            self.slideDown()
            driver.find_element_by_id('tv_leg_name').click()
        elif 6 < len(b) <= 9:
            self.slideDown()
            self.slideDown()
            driver.find_element_by_id('tv_leg_name').click()
        elif len(b) > 9:
            print '直播比赛超过9场，请手动查看'
            driver.find_element_by_id('tv_leg_name').click()
        else:
            print '出现异常，请注意！'
        time.sleep(2)
        self.screenShot('live4.png')                                                        #Live页面显示的第一场比赛的详情页面截图，查看页面是否显示比赛倒计时及比赛相关信息
        driver.find_element_by_id('title_bar_iv_left').click()

        now = datetime.datetime.now()
        now1 = now.strftime('%Y-%m-%d %H:%M:%S')
        now2 = datetime.datetime.strptime(now1,'%Y-%m-%d %H:%M:%S')
        rs_time = now2 - datetime.timedelta(minutes=11) - datetime.timedelta(hours=8)
        sql2 = "update `match` set  status = 1,start_play = '%s' WHERE match_id = '%d' "% (rs_time,b[0])    #将第一场比赛的状态改为直播中，并且开始比赛时间已经距离现在时间11分钟
        cur.execute(sql2)
        conn.commit()

        # sched = BlockingScheduler()
        # if self.t6(b[0]) == 1:                                #该方法需要利用调度器来定时，但是与下面的代码效果一样，区别在哪还不知道，待研究
        #     try:                                              #该方法与下面的代码比较，另外加了一层调度器，所以更复杂了点，但是作用是什么还未知
        #         sched.shutdown(wait=False)
        #     except SchedulerNotRunningError:
        #         print '调度任务已结束'
        # else:
        #     sched.add_job(self.t6(b[0]), 'interval')
        #     sched.start()
        a = 0
        while a == 0:
            c = match_live()
            if b[0] not in c:
                self.screenShot('live5.png')                                                    # 接口返回的数据中刚设置后的比赛了，Live页面截图查看是否还存在该比赛显示
                time.sleep(6)
                self.screenShot('live6.png')                                    # 由于live页面是每5秒请求一次接口，因此接口返回数据同预期一样时，但是前端可能还没有请求接口
                a = 1
            else:                                                       # 因此上一张截图可能该比赛还存在于live页面，这张截图是6秒后的截图,接口一定请求了，所以可以该截图为准
                print '暂未删除，继续'
                time.sleep(5)
                a = 0
        else:
            print '该比赛开始后10分钟内直播数据，已被删除'

        sql3 = "update `match` set  status = 1,start_play = now(),minute = 5 WHERE match_id = '%d' "% (b[0])       #将第一场比赛改为直播中，比赛已进行到第5分钟
        cur.execute(sql3)
        conn.commit()
        self.screenShot('live7.png')                                    #Live页面显示的第一场比赛截图，主要查看页面比赛进行时间显示（可能未显示为更改后的时间，可用做后面对比）
        time.sleep(5)
        self.screenShot('live8.png')                                    #Live页面显示的第一场比赛截图，查看页面比赛进行时间显示
        driver.find_element_by_id('tv_leg_name').click()
        time.sleep(2)
        self.screenShot('live9.png')                                    #Live页面显示的第一场比赛详情页面截图，查看比赛进行的时间显示

        sql4 = "update match_phrase  set match_id = '%d' WHERE id = 3"% (b[0])              #增加比赛的文字直播信息
        cur.execute(sql4)
        conn.commit()
        time.sleep(10)                                                                      #直播详情页面每10秒调一次接口，所以需等待10秒
        self.screenShot('live10.png')                                                       #新增的文字直播内容查看是否显示在Live详情页面中的截图
        driver.find_element_by_id('title_bar_iv_left').click()
        self.screenShot('live11.png')                                                       #新增的文字直播内容查看是否显示在Live页面中的截图，验证滚动的文字直播功能
        time.sleep(20)
        self.screenShot('live12.png')                   #由于live页面与live详情页面不是同步的，所以文字直播最新增加的内容在这两个页面不会同步，要显示新增的必须等待接口调用时间

        sql5 = "update `match` set  status = 2,start_play = '%s',minute = 0 WHERE match_id = '%d' "% (result1[0][20],b[0])      #将该测试的第一场比赛所有修改的内容都更新回原来的状态
        sql6 = "update match_phrase  set match_id = 50834870 WHERE id = 3"
        cur.execute(sql5)
        cur.execute(sql6)
        conn.commit()
        print 'live功能测试完毕'

    #订阅功能
    def test_subscribe(self):
        driver = self.driver
        # uid = self.test_feedback()
        conn,cur = connDB()
        delete_subscription(conn,cur,241)
        x1 = driver.find_element_by_id('title_bar_iv_left')
        x1.click()
        driver.tap([(339,571)])
        for i in range(2):
            driver.find_element_by_id('rb_match').click()
            time.sleep(2)
            s1 = "adb shell am force-stop com.football.supergoal"
            os.system(s1)
            start_p = 'com.football.supergoal'
            start_a = 'com.soka.football.home.ui.login.activity.SplashActivity'
            driver.start_activity(start_p, start_a)
        driver.find_element_by_id('rb_match').click()
        time.sleep(2)
        self.screenShot('subscribe1.png')                                           #用户第一次打开match页面时展示subscribe页面的截图

        self.getXpath('6')
        self.getXpath('11')
        driver.find_element_by_xpath("//*[(@text='La Liga')]").click()
        time.sleep(1)
        self.getXpath('2')
        self.getXpath('8')
        x2 = driver.find_element_by_id('title_bar_tv_right')
        x2.click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[(@index='0' and @text='Subscribe')]").click()
        time.sleep(1)
        self.screenShot('subscribe2.png')                                           #用户从match页面进入然后再订阅球队

        result = select_subscribption(cur, 241)                                         #从数据库中查看该用户订阅球队的比赛总共有多少个（比赛开始时间大于现在的）
        if result == 0:
            print '暂停线程5秒，等待数据插入数据库'
            time.sleep(3)
        e = len(result)
        s1 = []
        b = []
        for i in range(e):
            s2 = result[i][0]
            s1.append(s2)
        print s1

        for m in range(len(s1)):                                                                 #循环出每个用户订阅的球队
            a = select_match_subcribption(cur, s1[m])
            for n in range(len(a)):                                                              #循环出每个球队的比赛
                b.append(a[n][1])                                                                #将每个比赛的matchId添加到一个列表中
        # d =Counter(a1)                                                                         #显示出列表中所有元素重复的次数，返回值是一个字典，注意要导入Counter包
        c = list(set(b))                                                                         # 去除列表中重复的元素
        s3 = len(c)
        print s3
        s4 = match_reptile()                                                                     #接口返回的用户订阅球队比赛数量
        if s4 == s3:
            print '接口返回的数据与数据库查询出的结果相同，用户订阅球队比赛显示的数量没有问题'
        else:
            print '注意!数据不同，请核对'

        #刷新与定位到当前日期比赛的按钮测试
        for i in range(5):
            driver.find_element_by_id('iv_locate').click()
            time.sleep(1)
            if i == 0:
                self.screenShot('subscribe3.png')                                                #点击定位按钮后截图
            elif i == 1:
                self.screenShot('subscribe4.png')
            elif i == 2:
                self.screenShot('subscribe5.png')
            elif i == 3:
                self.screenShot('subscribe6.png')
            elif i == 4:
                self.screenShot('subscribe7.png')
            else:
                print '循环出错，请核对之'
        for i in range(5):
            self.slideDown()
            time.sleep(2)
            if i == 0:
                self.screenShot('subscribe8.png')                                               #下拉刷新拉出所订阅的球队历史比赛的截图
            elif i == 1:
                self.screenShot('subscribe9.png')
            elif i == 2:
                self.screenShot('subscribe10.png')
            elif i == 3:
                self.screenShot('subscribe11.png')
            elif i == 4:
                self.screenShot('subscribe12.png')
            else:
                print '循环出错，请核对之'


        delete_subscription(conn,cur,241)
        x1.click()
        driver.find_element_by_id('tv_subscribed').click()
        time.sleep(1)
        self.screenShot('subscribe13.png')                                                      #用户未订阅时的订阅页面显示截图
        # driver.find_element_by_id('tv_subscribe').click()
        # time.sleep(2)
        # self.screenShot('subscribe14.png')     #由subscribe按钮进入订阅比赛页面
        # driver.find_element_by_id('title_bar_iv_left').click()
        x2.click()
        time.sleep(2)
        self.screenShot('subscribe15.png')                                                      #由add more按钮进入订阅比赛页面
        self.getXpath('5')
        self.getXpath('10')
        self.screenShot('subscribe16.png')                                                      #用户订阅EPL球队的截图

        driver.find_element_by_xpath("//*[(@text='La Liga')]").click()
        time.sleep(1)
        self.getXpath('3')
        self.getXpath('11')
        self.screenShot('subscribe17.png')                                                      #用户订阅LaLiga球队的截图

        driver.find_element_by_xpath("//*[(@text='Bundesliga')]").click()
        # time.sleep(1)
        self.slideUp()
        time.sleep(1)
        self.getXpath('9')
        self.getXpath('13')
        self.screenShot('subscribe18.png')                                                      # 用户订阅Bundesliga球队的截图

        driver.find_element_by_xpath("//*[(@text='Ligue 1')]").click()
        time.sleep(1)
        self.getXpath('0')
        self.getXpath('15')
        self.screenShot('subscribe19.png')      #用户订阅Ligue 1球队的截图

        driver.find_element_by_xpath("//*[(@text='serie A')]").click()
        time.sleep(1)
        self.getXpath('14')
        self.getXpath('6')
        self.screenShot('subscribe20.png')      # 用户订阅serie A球队的截图
        x2.click()
        time.sleep(2)
        self.screenShot('subscribe21.png')      # 用户订阅球队后的截图
        self.slideUp()
        self.screenShot('subscribe22.png')      #滑动屏幕后查看是否总共有10个球队

        a = driver.find_elements_by_id('tv_subscribed')
        a[6].click()
        time.sleep(1)
        self.screenShot('subscribe23.png')      #由subscribed按钮取消订阅球队的截图
        driver.find_element_by_id('tv_cancel').click()
        time.sleep(1)
        self.screenShot('subscribe24.png')      #操作取消后的页面截图
        a[6].click()
        driver.find_element_by_id('tv_unsub').click()
        time.sleep(2)
        self.screenShot('subscribe25.png')      #取消订阅某个球队后的页面截图

        # 由add more按钮取消订阅球队
        x2.click()
        driver.find_element_by_xpath("//*[(@text='La Liga')]").click()
        time.sleep(1)
        self.getXpath('3')
        self.getXpath('11')
        driver.find_element_by_xpath("//*[(@text='Bundesliga')]").click()
        # time.sleep(1)
        self.slideUp()
        time.sleep(1)
        self.getXpath('9')
        self.getXpath('13')
        driver.find_element_by_xpath("//*[(@text='Ligue 1')]").click()
        time.sleep(1)
        self.getXpath('0')
        self.getXpath('15')
        x2.click()
        time.sleep(2)
        self.screenShot('subscribe26.png')    #由add more按钮取消订阅球队后的截图,只留下LPL和serie A的球队

        x1.click()
        time.sleep(1)
        driver.tap([(339,571)])
        driver.find_element_by_id('rb_match').click()
        driver.find_element_by_xpath("//*[(@index='0' and @text='Subscribe')]").click()
        time.sleep(1)
        self.screenShot('subscribe27.png')    #通过match进入subscribe页面，显示用户取消订阅球队是否成功的截图

        result = select_subscribption(cur, 241)  # 从数据库中查看该用户订阅球队的比赛总共有多少个（比赛开始时间大于现在的）
        e = len(result)
        s5 = []
        b = []
        for i in range(e):
            s6 = result[i][0]
            s5.append(s6)
        print s5

        for m in range(len(s5)):  # 循环出每个用户订阅的球队
            a = select_match_subcribption(cur, s5[m])
            for n in range(len(a)):  # 循环出每个球队的比赛
                b.append(a[n][1])  # 将每个比赛的matchId添加到一个列表中
        # d =Counter(a1)                                        #显示出列表中所有元素重复的次数，返回值是一个字典，注意要导入Counter包
        c = list(set(b))  # 去除列表中重复的元素
        s7 = len(c)
        print s7
        s8 = match_reptile()  # 接口返回的用户订阅球队比赛数量
        if s8 == s7:
            print '接口返回的数据与数据库查询出的结果相同，用户订阅球队比赛显示的数量没有问题'
        else:
            print '注意!数据不同，请核对'
        print '订阅功能测试结束'

    #新闻页面
    def test_new(self):
        driver = self.driver
        conn,cur = connDB()
        driver.find_element_by_id("rb_news").click()
        s2 = driver.find_elements_by_id("tv_title")
        s2[3].click()
        time.sleep(2)
        self.screenShot('news1.png')                                                                #正常点击文章的截图
        driver.find_element_by_id("tv_cancel").click()
        s1 = driver.find_element_by_id("title_bar_iv_left")
        s1.click()

        self.slideDown()
        time.sleep(1)
        self.screenShot('news2.png')                                                                #无新数据插入时下拉刷新
        sql1 = "insert into article(title,content,small_cover,url,type,create_time,update_time,is_priority)" \
               " VALUES ('test article','this is test article','9322f75abfa67802c63bbce530be0e59.jpg','https://www.zhihu.com/explore',1,now(),now(),0)"
        sql2 = "DELETE FROM article WHERE title = 'test article' "
        cur.execute(sql1)
        conn.commit()
        self.slideDown()
        time.sleep(2)
        self.screenShot('news3.png')                                                                #有新数据插入时下拉刷新
        s2[0].click()
        time.sleep(2)
        self.screenShot('news4.png')                                                                #新增的文章点击后的页面
        s1.click()
        cur.execute(sql2)
        conn.commit()
        self.slideDown()

        self.slideUp()
        time.sleep(2)
        self.screenShot('news5.png')                                                                #屏幕向上滑
        time.sleep(1)
        s2[3].click()
        time.sleep(2)
        self.screenShot('news6.png')                                                                #滑动后点击
        s1.click()

        for i in range(4):
            self.slideUp()
            time.sleep(1)
        time.sleep(2)
        self.screenShot('news7.png')                                                                #上拉刷新
        s2[3].click()
        time.sleep(2)
        self.screenShot('news8.png')                                                                #上拉刷新后点击

        a = article_list()                                                                          #接口返回的数据
        conn, cur = connDB()
        b = selectArticle(cur)                                                                      #数据库返回的值
        for i in a:
            if a.count(i) > 1:
                print '有数据重复，请注意'
        print '接口返回的数据无重复，正常'
        if a == b:
            print '数据库返回与接口返回相同'
        else:
            print '请注意！接口与数据库返回的数据不相同'

    #video页面之banner区域
    def test_videoBanner(self):
        driver = self.driver
        try:
            self.getElementUI("article1")
            # self.test2("\"article1\"")                                                      #注意！斜杠是转义字符，将双引号作为参数
        except NoSuchElementException:
            self.slideLeft()
            try:
                self.getElementUI("article1")
            except NoSuchElementException:
                self.slideLeft()
                try:
                    self.getElementUI("article1")
                except NoSuchElementException:
                    print 'banner区域超过3个上线banner'
        time.sleep(1)
        self.screenShot('banner1.png')                                                                        #banner文章点击后的截图
        driver.find_element_by_id("tv_cancel").click()
        s1 = driver.find_element_by_id("title_bar_iv_left")
        s1.click()

        try:
            self.getElementUI("match1")
        except NoSuchElementException:
            self.slideLeft()
            try:
                self.getElementUI("match1")
            except NoSuchElementException:
                self.slideLeft()
                try:
                    self.getElementUI("match1")
                except NoSuchElementException:
                    print 'banner区域超过3个上线banner'

        time.sleep(1)
        self.screenShot('banner2.png')                                                                      #banner比赛点击后的截图
        s1.click()

        try:
            self.getElementUI("video")
        except NoSuchElementException:
            self.slideLeft()
            try:
                self.getElementUI("video")
            except NoSuchElementException:
                self.slideLeft()
                try:
                    self.getElementUI("video")
                except NoSuchElementException:
                    print 'banner区域超过3个上线banner'
        time.sleep(1)
        self.screenShot('banner3.png')                                                                      #banner视频点击后的截图
        driver.find_element_by_id("iv_back").click()

        # 新增一个banner文章
        delivery_url = "http://api.admin.test.sokafootball.com/admin/banner/update"
        values = {"id": 33, "status": 0}
        delivery_data = json.dumps(values)
        delivery_headers = {"Content-Type": "application/json"}
        requests.post(url=delivery_url, data=delivery_data, headers=delivery_headers)                        #调用缓存post接口
        print ("新增文章接口调用成功")
        self.slideDown()
        time.sleep(2)
        self.screenShot('banner4.png')                                                                       #新增一个banner文章
        try:
            self.getElementUI("article2")
        except NoSuchElementException:
            self.slideLeft()
            try:
                self.getElementUI("article2")
            except NoSuchElementException:
                self.slideLeft()
                try:
                    self.getElementUI("article2")
                except NoSuchElementException:
                    self.slideLeft()
                    try:
                        self.getElementUI("article2")
                    except NoSuchElementException:
                        print 'banner区域超过4个上线banner'
        time.sleep(1)
        self.screenShot('banner5.png')                                                                      #新增的banner文章点击后的截图
        s1.click()

        # 新增一个banner比赛，新增的比赛，是否正确点击到所新增的比赛

        delivery_url = "http://api.admin.test.sokafootball.com/admin/banner/update"
        values = {"id": 36, "status": 0}
        delivery_data = json.dumps(values)
        delivery_headers = {"Content-Type": "application/json"}
        requests.post(url=delivery_url, data=delivery_data, headers=delivery_headers)
        print ("新增比赛接口调用成功")
        self.slideDown()
        time.sleep(2)
        self.screenShot('banner6.png')                                                                      #新增banner比赛后的截图
        try:
            self.getElementUI("match2")
        except NoSuchElementException:
            self.slideLeft()
            try:
                self.getElementUI("match2")
            except NoSuchElementException:
                self.slideLeft()
                try:
                    self.getElementUI("match2")
                except NoSuchElementException:
                    self.slideLeft()
                    try:
                        self.getElementUI("match2")
                    except NoSuchElementException:
                        self.slideLeft()
                        try:
                            self.getElementUI("match2")
                        except NoSuchElementException:
                            print 'banner区域超过5个上线banner'
        time.sleep(1)
        self.screenShot('banner7.png')                                                                      #新增的比赛banner点击后的截图
        s1.click()

        #下线banner
        delivery_url = "http://api.admin.test.sokafootball.com/admin/banner/update"
        values_list = [36,33,34,40,39]
        for id in values_list:
            try:
                values = {"id": id, "status": 1}
                delivery_data = json.dumps(values)
                delivery_headers = {"Content-Type": "application/json"}
                requests.post(url=delivery_url, data=delivery_data, headers=delivery_headers)

                self.slideDown()
                time.sleep(3)
                if id == 36:
                    self.screenShot('banner8.png')                                                          #依次下线banner后的截图
                elif id == 33:
                    self.screenShot('banner9.png')
                elif id == 34:
                    self.screenShot('banner10.png')
                elif id == 40:
                    self.screenShot('banner11.png')
                elif id == 39:
                    self.screenShot('banner12.png')
                else:
                    print ("banner list异常，请查看之")
            except IndentationError,e:
                traceback.print_exc()
                print "所要下线的banner中有某个已下线，请查看之"
            else:
                print ("下线" + str(id) + "号banner成功")

        #上线banner
        delivery_url = "http://api.admin.test.sokafootball.com/admin/banner/update"
        values_list = [34, 40, 39]
        for id in values_list:
            try:
                values = {"id": id, "status": 0}
                delivery_data = json.dumps(values)
                delivery_headers = {"Content-Type": "application/json"}
                requests.post(url=delivery_url, data=delivery_data, headers=delivery_headers)
                self.slideDown()
                time.sleep(3)
                if id == 34:
                    self.screenShot('banner13.png')                                                         #依次上线banner主要是还原之前的设置环境
                elif id == 40:
                    self.screenShot('banner14.png')
                elif id == 39:
                    self.screenShot('banner15.png')
                else:
                    print ("banner list异常，请查看之")
            except IndentationError:
                traceback.print_exc()
                print "所要上线的banner中有某个已上线，请查看之"
            else:
                print ("上线" + str(id) + "号banner成功")

        print 'banner区域测试完毕'

        # update_banner1(conn, cur, 33,1)  # 需要在控制台弹出来这个1，弹出框怎么显示需要学习下

    #video页面之match区域
    def test_videoMatch(self):
        driver = self.driver
        conn, cur = connDB()
        r = show_matchIndex(cur)
        match_mes = r[0]
        print 'A队名称:', match_mes[0], '   B队名称:', match_mes[1], '   联盟名称:', match_mes[2], '   比赛开始时间:', match_mes[3]
        status = r[1]
        if status == 1:
            time.sleep(4)
            self.screenShot('matchLive16.png')

            #注意：这里只是一部分，之后还需要根据比赛状态来进行点击查看。如这里只是一场比赛还未开始时的页面显示情况，
            # 还有比赛结束后（有数据和无数据）、比赛过程中等情况的页面显示情况
            driver.find_element_by_id("tv_time").click()    #主页显示的比赛详细信息，其页面显示情况。
            time.sleep(1)
            self.screenShot('matchLive1.png')

            self.getElementUI("Prediction")
            time.sleep(1)
            self.screenShot('matchLive2.png')

            self.getElementUI("Overview")
            time.sleep(1)
            self.screenShot('matchLive3.png')

            self.getElementUI("Line-up")
            time.sleep(1)
            self.screenShot('matchLive4.png')

            self.getElementUI("Statistics")
            time.sleep(1)
            self.screenShot('matchLive5.png')

            self.getElementUI("Live")
            time.sleep(1)
            self.screenShot('matchLive6.png')
            driver.find_element_by_id("title_bar_iv_left")

            #更改主页显示比赛的状态

            update_matchIndex(conn, cur, status)
            time.sleep(2)

            self.slideDown()
            time.sleep(2)
            self.screenShot('matchLive7.png')
            print ("截图完毕，请查看之")

        elif status == 0:
            time.sleep(2)
            self.screenShot('matchLive8.png')

            # 更改主页显示比赛的状态
            update_matchIndex(conn, cur, status)
            time.sleep(2)

            self.slideDown()
            time.sleep(2)
            self.screenShot('matchLive9.png')

            driver.find_element_by_id("tv_time").click()
            time.sleep(2)
            self.screenShot('matchLive10.png')

            self.getElementUI("Prediction")
            time.sleep(2)
            self.screenShot('matchLive11.png')

            self.getElementUI("Overview")
            time.sleep(2)
            self.screenShot('matchLive12.png')

            self.getElementUI("Line-up")
            time.sleep(2)
            self.screenShot('matchLive13.png')

            self.getElementUI("Statistics")
            time.sleep(2)
            self.screenShot('matchLive14.png')

            self.getElementUI("Live")
            time.sleep(2)
            self.screenShot('matchLive15.png')
            driver.find_element_by_id("title_bar_iv_left")
            print ("截图完毕，请查看之")

    #友盟数据测试
    def test_youmeng(self):
        for i in range(300):
            driver = self.driver
            time.sleep(3)
            try:
                self.getElementUI("article")                                                                #banner1点击
            except NoSuchElementException:                                                                  #注意，该异常需要导入相应的异常包才能够被捕获,且是selenium的包
                try:
                    self.slideLeft()
                    self.getElementUI("article")
                except NoSuchElementException:
                    try:
                        self.slideLeft()
                        self.getElementUI("article")
                    except NoSuchElementException:
                        print 'banner区域发生变化，请后台查看banner修改以及修改程序'
            time.sleep(1)
            if i == 0:
                driver.find_element_by_id("tv_cancel").click()
                driver.find_element_by_id('title_bar_iv_left').click()
            else:
                driver.find_element_by_id('title_bar_iv_left').click()

            time.sleep(2)
            try:
                self.getElementUI("match")                                                                   #banner2点击
            except NoSuchElementException:
                try:
                    self.slideLeft()
                    self.getElementUI("match")
                except NoSuchElementException:
                    try:
                        self.slideLeft()
                        self.getElementUI("match")
                    except NoSuchElementException:
                        print 'banner区域发生变化，请后台查看banner修改以及修改程序'
            time.sleep(1)
            x1 = driver.find_element_by_id('title_bar_iv_left')
            x1.click()

            time.sleep(2)
            try:
                self.getElementUI("video")                                                                    #banner3点击
            except NoSuchElementException:
                try:
                    self.slideLeft()
                    self.getElementUI("video")
                except NoSuchElementException:
                    try:
                        self.slideLeft()
                        self.getElementUI("video")
                    except NoSuchElementException:
                        print 'banner区域发生变化，请后台查看banner修改以及修改程序'
            driver.find_element_by_id('iv_back').click()

            driver.find_element_by_id('rb_prediction').click()                                          #tab_prediction点击
            driver.find_element_by_id('rb_news').click()                                                #tab_news点击
            driver.find_element_by_id('rb_video').click()                                               #tab_video点击
            self.getElementUI("0 - 0")                                                                  #banner_match点击
            x1.click()
            driver.find_element_by_id('rb_match').click()                                               #tab_match
            time.sleep(2)
            self.getElementUI("La Liga")                                                                #tab_La点击
            self.getElementUI("Bundesliga")                                                             #tab_Bundesliga点击
            self.getElementUI("Ligue 1")                                                                #tab_Ligue点击
            self.getElementUI("Champions League")                                                       #tab_Champions点击
            self.getElementUI("Bundesliga")
            self.getElementUI("EPL")                                                                    #tab_EPL
            self.getElementUI("Subscribe")                                                              #subscribe点击

            driver.find_element_by_xpath("//*[@index='1' and @class='android.widget.RelativeLayout']").click()
            time.sleep(2)
            self.getElementUI("Prediction")                                                             #match_tab_prediction点击

            self.getElementUI("Overview")                                                               #match_tab_overview点击
            self.getElementUI("Line-up")                                                                #match_tab_line_up点击
            self.getElementUI("Highlights")                                                             #match_tab_highlights点击
            self.getElementUI("Live")                                                                   #match_tab_text点击
            x1.click()

            time.sleep(1)
            driver.find_element_by_id('rb_prediction').click()
            driver.find_element_by_xpath("//*[@index='1' and @class='android.widget.RelativeLayout']").click()
            time.sleep(1)
            self.getElementUI("Live")                                                                   #match_tab_text点击
            self.getElementUI("Prediction")           #match_tab_prediction点击
            x1.click()

            conn,cur = connDB()
            sql = "TRUNCATE table user_fetch"
            cur.execute(sql)
            print '清除用户观看视频记录成功'
            driver.find_element_by_id('rb_video').click()                               #tab_video点击
            self.slideUp()
            driver.find_element_by_xpath("//*[@index='1' and @class='android.widget.RelativeLayout']").click()              #count_normal数量，未使用youtube
            time.sleep(1)
            driver.find_element_by_id('iv_play').click()                                        #count_youtube数量
            time.sleep(2)
            x1.click()
            driver.find_element_by_id('iv_back').click()

            x1.click()
            driver.find_element_by_id('tv_subscribed').click()
            driver.find_element_by_id('title_bar_tv_right').click()                             #add_team点击

            time.sleep(2)
            s1 = "adb shell am force-stop com.football.supergoal"                               #重新启动APP
            os.system(s1)
            start_p = 'com.football.supergoal'
            start_a = 'com.soka.football.home.ui.login.activity.SplashActivity'
            try:
                driver.start_activity(start_p, start_a)
            except WebDriverException:
                driver.start_activity(start_p, start_a)
            finally:
                driver.start_activity(start_p, start_a)

#banner1、banner2、banner3、banner_match、tab_news、tab_La、tab_Ligue、tab_Champions、subscribe、tab_EPL、match_tab_overview、match_tab_line_up、match_tab_highlights、count_youtube、add_team、count_normal分别1次；
#tab_match、tab_Bundesliga、match_tab_prediction、match_tab_text点击2次；tab_video7次；tab_prediction3次

    def test_bigTarge(self):
        conn,cur = connDB()
        sql1 = "delete from  turn_table_record where uid = 241"
        cur.execute(sql1)
        conn.commit()

        driver = self.driver
        driver.find_element_by_id("tv_skip").click()
        driver.find_element_by_id("rb_prediction").click()
        driver.find_element_by_xpath("//*[(@text='Lucky wheel')]").click()
        for m in range(300):
            try:
                driver.find_element_by_id("tv_whell_start").click()
                time.sleep(5)
            except NoSuchElementException:
                continue

        a = []
        for m in range(6):
            sql2 = "select count(*) from turn_table_record where uid = 241 and result = %d" % (m)
            cur.execute(sql2)
            b = cur.fetchall()
            a.append(b)
        n = a[0] + a[1] + a[2] + a[3] + a[4] + a[5]
        print "nothing总共有" + str(a[0]) + "次" + "    " + "free次数有" + str(a[2]) + "次" + "    " + "中得10金币有" + str(a[1]) + "次"
        print "中得50金币总共有" + str(a[3]) + "次" + "    " + "中得100金币有" + str(a[4]) + "次" + "    " + "中得1000金币有" + str(a[5]) + "次"
        c = 10 * a[1] + 50 * a[3] + 100 * a[4] + 1000 * a[5]
        d = 20 * (n - a[2])
        e = (n - a[0]) / n
        print "总返奖" + str(c)
        print "总消耗金币" + str(d)
        print "返奖率" + str(e)

        driver.find_element_by_id("title_bar_iv_left").click()
        driver.find_element_by_xpath("//*[(@text='Lucky slot')]").click()
        for i in range(300):
            try:
                driver.find_element_by_id("btn_spin").click()
                time.sleep(5)
            except NoSuchElementException:
                continue



    #测试用例方法结束处


    def test_tearDown(self):
        self.driver.close_app()   #关闭当前的app应用窗口
        self.driver.quit()        #不仅关闭了当前的app应用窗口还彻底的退出WedDriver,释放了Driver与Server之间的链接，quit会更好的释放资源



    @unittest.skipIf(True,"I don't want to run this case ,and skip it")
    #unittest.skip是无条件跳过某个case的执行，该方法是condition为True时跳过，unittest.skipUnless是condition为False时跳过
    def test_skipFunction(self):
        print "hello python"


if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    #可以将TestSuite看成是包含所有测试用例的一个容器
    testCase = [AutoTest("test_bigTarge")]
    # testCase = [AutoTest("test_prediction"),AutoTest("test_tearDown"),AutoTest("test_skipFunction")]   #可以将TestCase看成是对特定类进行测试的方法的集合
    suite.addTests(testCase)                                                                           #将测试用例添加到TestSuite这个容器中

    unittest.TextTestRunner(verbosity=2).run(suite)  #TextTestRunner是用来执行测试用例的
    #其中的run(test)会执行TestSuite/TestCase中的run(result)方法，也就是说TestCase有个内置函数也叫run()方法

    # suite1 = unittest.TestLoader.loadTestsFromTestCase(AutoTest)
    #TestLoader是用来加载TestCase到TestSuite
    #loadTestsFromTestCase方法是从代码中每个地方去寻找TestCase，并创建它们的实例,将TestCase的实例add到TestSuiter中，再返回一个TestSuiter实例


